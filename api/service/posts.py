from flask import request
from api import db
from api.model.database.posts import Postagem
from api.model.database.categories import Categoria
from api.model.database.users import Usuario
from api.service.comments import ComentariosPostagem

def PutSelo(id):
    postagem = Postagem.query.get_or_404(id)
    postagem.selo = True

    db.session.add(postagem)
    db.session.commit()

    return {"message": f"Selo emitido!"}

def PostPostagens(data):
    new_post = Postagem(texto=data['texto'], criador=data['criador'], titulo=data['titulo'], categoria=data['categoria'])

    db.session.add(new_post)
    db.session.commit()

    return {"message": f"Postagem criada"}

def GetPostagens():
    postagensWithCriador = Postagem.query.join(Usuario, Postagem.criador == Usuario.id, isouter=True).add_columns(Usuario.real_name, Usuario.bairro)

    # filtros gerais
    bairro = request.args.get('bairro', None)
    categoria = request.args.get('categoria', None)

    if categoria is not None:
        postagensWithCriador = postagensWithCriador.filter(Postagem.categoria.in_(map(int, categoria.split(','))))

    if bairro is not None:
        postagensWithCriador = postagensWithCriador.filter(Usuario.bairro.in_(map(int, bairro.split(','))))

    postagens = postagensWithCriador.all()
    results = []
    for post in postagens:
        results.append({"id": post.Postagem.id, "titulo": post.Postagem.titulo,"texto": post.Postagem.texto,"criador": post.real_name,"bairro": post.bairro,"selo":post.Postagem.selo,"categoria":post.Postagem.categoria,"data":post.Postagem.data})

    return {"count": len(results), "post": results, "message": "success"}

def GetRecomendados():
    postagens = Postagem.query.filter_by(selo=True).all()
    results = []
    for post in postagens:
        user = Usuario.query.get_or_404(post.criador)
        results.append({"id": post.id, "titulo": post.titulo,"texto": post.texto,"criador": user.real_name,"selo":post.selo,"categoria":post.categoria})

    return {"count": len(results), "post": results, "message": "success"}

def GetFiltros(id_categoria):
    postagens = Postagem.query.join(Categoria, id_categoria == Postagem.categoria)
    results = []
    for post in postagens:
        user = Usuario.query.get_or_404(post.criador)
        results.append({"id": post.id, "titulo": post.titulo,"texto": post.texto,"criador": user.real_name,"selo":post.selo,"categoria":post.categoria, "data": post.data})

    return {"count": len(results), "post": results, "message": "success"}

def GetPostagensId(id):
    post = Postagem.query.filter_by(id=id).first()
    comments = ComentariosPostagem(post.id)
    post_user = Usuario.query.get_or_404(id)
    result = {
        "id": post.id,
        "titulo": post.titulo,
        "texto": post.texto,
        "criador": {
            "id": post_user.id,
            "name": post_user.real_name
        },
        "selo":post.selo,
        "categoria":post.categoria,
        "data": post.data,
        "comentarios": comments['comments']
    }
    return result

def GetListaPostagens(id):
    try :
        postagens = Postagem.query.all()
        user = Usuario.query.get_or_404(id)
        results = []
        for post in postagens:
            if post.criador == user.id:
                results.append({"titulo": post.titulo,"texto": post.texto,"criador": user.real_name})

        return {"count": len(results), "post": results, "message": "success"}
    except:
        return {"error": 404, "message": "Usuário não encontrado"}