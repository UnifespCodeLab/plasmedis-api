from api import api
from flask_restx import fields

privileges = api.model("Privileges", {
    "id": fields.Integer,
    "name": fields.String
})

privileges_list = api.model("Privileges List", {
    "count": fields.Integer,
    "current": fields.Integer(),
    "limit": fields.Integer(),
    "previous": fields.String(),
    "next": fields.String(),
    "privileges": fields.List(fields.Nested(privileges)),
})
