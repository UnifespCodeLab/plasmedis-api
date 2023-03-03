from api import api
from flask_restx import fields

from api.model.metadata import created

post = api.model("Post", {
    "titulo": fields.String(),
    "texto": fields.String(),
    # metadata
    "created": fields.Nested(created)
})

post_list = api.model("Post List", {
    "count": fields.Integer(),
    "post": fields.List(fields.Nested(post)),
    "message": fields.String()
})

post_complete = api.model("Post Complete", {
    "id": fields.Integer(),
    "categoria": fields.Integer(),
    "titulo": fields.String(),
    "texto": fields.String(),
    "selo": fields.Boolean(),
    "comments_count": fields.Integer(),
    # metadata
    "created": fields.Nested(created),
})

comment = api.model("Post Comment", {
    "id": fields.Integer(),
    "texto": fields.String(),
    "resposta": fields.Integer(),
    # metadata
    "created": fields.Nested(created)
})

post_complete_list = api.model("Post Complete List", {
    "count": fields.Integer(),
    "current": fields.Integer(),
    "limit": fields.Integer(),
    "previous": fields.String(),
    "next": fields.String(),
    "posts": fields.List(fields.Nested(post_complete))
})
