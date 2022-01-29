from api import api
from flask_restx import fields

comment = api.model("Comment", {
    "texto": fields.String(),
    "criador": fields.Integer(),
    "postagem": fields.Integer(),
    "resposta": fields.Integer(),
    "data": fields.String()
})

comment_list = api.model("Comment List", {
    "count": fields.Integer(),
    "comments": fields.List(fields.Nested(comment)),
    "message": fields.String()
})

creator = api.model("Comment Creator", {
    "id": fields.Integer(),
    "name": fields.String()
})

comment_creator = api.model("Comment With Creator", {
    "id": fields.Integer(),
    "texto": fields.String(),
    "criador": fields.Nested(creator),
    "resposta": fields.Integer(),
    "data": fields.String()
})

comment_creator_list = api.model("Comment With Creator List",{
    "count": fields.Integer(),
    "comments": fields.List(fields.Nested(comment_creator)),
    "message": fields.String()
})