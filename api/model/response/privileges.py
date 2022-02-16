from api import api
from flask_restx import fields

privileges = api.model("Privileges", {
    "user_type": fields.String
})

privileges_list = api.model("Privileges List",{
    "count": fields.Integer,
    "Privileges": fields.Nested(privileges),
    "message": fields.String
})
