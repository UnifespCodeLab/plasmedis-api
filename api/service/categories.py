from api import db
from api.model.database.categories import Categoria
from api.model.database.posts import Postagem
from sqlalchemy import func

def PostCategorias(data):
    new_categoria = Categoria(nome=data['nome'])

    db.session.add(new_categoria)
    db.session.commit()

    return {"message": f"Categoria criado com sucesso"}

def GetCategorias():
    categorias = Categoria.query.outerjoin(Postagem).add_columns(func.count(Postagem.id).label('postagens')).group_by(Categoria.id).all()
    results = [
        {
            "nome": categoria.Categoria.nome,
            "id": categoria.Categoria.id,
            "postagens": categoria.postagens
        } for categoria in categorias]

    return {"count": len(results), "Categorias": results, "message": "success"}

def deleteCategorias(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()

    return  {"message": f"Categoria deletada com sucesso"}
