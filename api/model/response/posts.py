from api import api
from flask_restx import fields

post = api.model("Post",
{
    "titulo": fields.String(),
    "texto": fields.String(),
    "criador": fields.String()
})

post_list = api.model("Post List", {
    "count": fields.Integer(),
    "post": fields.List(fields.Nested(post)),
    "message": fields.String()
})

creator = api.model("Creator", {
    "id": fields.Integer(),
    "name": fields.String()
})

comment = api.model("Post Comment", {
    "texto": fields.String(),
    "criador": fields.Nested(creator),
    "resposta": fields.Integer(),
    "data": fields.String()
})

post_comments = api.model("Post With Comments",
{
    "id": fields.Integer(),
    "titulo": fields.String(),
    "texto": fields.String(),
    "criador": fields.Nested(creator),
    "selo": fields.Boolean(),
    "categoria": fields.Integer(),
    "data": fields.String(),
    "comentarios": fields.List(fields.Nested(comment))
})

post_full = api.model("Post Full",
{
    "id": fields.Integer(),
    "titulo": fields.String(),
    "texto": fields.String(),
    "criador": fields.String(),
    "id_criador": fields.Integer(),
    "bairro": fields.Integer(),
    "selo": fields.Boolean(),
    "categoria": fields.Integer(),
    "comentarios": fields.Integer(),
    "data": fields.String()
})

post_full_list = api.model("Post Full List", {
    "count": fields.Integer(),
    "post": fields.List(fields.Nested(post_full)),
    "message": fields.String()
})