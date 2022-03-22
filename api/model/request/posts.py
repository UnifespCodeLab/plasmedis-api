from api import api
from flask_restx import fields

post_create = api.model("Post Create",
{
    "titulo": fields.String(),
    "texto": fields.String(),
    "criador": fields.Integer(),
    "categoria": fields.Integer()
})

post_update = api.model("Post Update", {
    "titulo": fields.String(),
    "texto": fields.String(),
    "categoria": fields.Integer(),
    "selo": fields.Boolean()
})