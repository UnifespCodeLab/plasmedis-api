from api import db
from api.model.database.categories import Categoria

def PostCategorias(data):
    new_categoria = Categoria(nome=data['nome'])

    db.session.add(new_categoria)
    db.session.commit()

    return {"message": f"Categoria criado com sucesso"}

def GetCategorias():
    categorias = Categoria.query.all()
    results = [
        {
            "nome": categoria.nome,
            "id": categoria.id
        } for categoria in categorias]

    return {"count": len(results), "Categorias": results, "message": "success"}