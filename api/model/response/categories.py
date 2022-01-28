from api import api
from flask_restx import fields

category = api.model("Category", {
    "id": fields.Integer(),
    "nome": fields.String("nome")
})

category_list = api.model("Category List", {
    "count": fields.Integer(),
    "Categorias": fields.List(fields.Nested(category)),
    "message": fields.String()
})