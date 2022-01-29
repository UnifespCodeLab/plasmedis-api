from api import api
from flask_restx import fields

comment = api.model("Comment Create",
{
    "texto": fields.String(),
    "criador": fields.Integer(),
    "resposta": fields.Integer(),
    "postagem": fields.Integer()
})
