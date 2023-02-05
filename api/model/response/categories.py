from api import api
from flask_restx import fields

category = api.model("Category", {
    "id": fields.Integer(),
    "name": fields.String("name"),
    "posts": fields.Integer()
})

category_list = api.model("Category List", {
    "count": fields.Integer(),
    "current": fields.Integer(),
    "limit": fields.Integer(),
    "previous": fields.String(),
    "next": fields.String(),
    "categories": fields.List(fields.Nested(category))
})
