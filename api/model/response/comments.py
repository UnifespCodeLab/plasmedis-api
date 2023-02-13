from api import api
from flask_restx import fields

from api.model.metadata import created

comment = api.model("Comment", {
    "id": fields.Integer(),
    "texto": fields.String(),
    "postagem": fields.Integer(),
    "resposta": fields.Integer(),
    # metadata
    "created": fields.Nested(created)
})

comment_list = api.model("Comment List", {
    "count": fields.Integer(),
    "current": fields.Integer(),
    "limit": fields.Integer(),
    "previous": fields.String(),
    "next": fields.String(),
    "comments": fields.List(fields.Nested(comment)),
})
