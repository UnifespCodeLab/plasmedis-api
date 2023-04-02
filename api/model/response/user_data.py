from api import api
from flask_restx import fields

info = api.model('user_data', {
    "person_info":{
        "name": fields.String(),
        "age":fields.Integer()
    },
    "technical": {
        "ip_adress": fields.String(),
        "browser": fields.String()
    }
    })

user_data = api.model("User Data Response", {
    "message": fields.String(),
    "user_data": fields.Nested(info)
})