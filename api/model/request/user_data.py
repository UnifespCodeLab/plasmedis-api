from api import api
from flask_restx import fields

user_data = api.model('user_data', {})

user_data_request = api.model("User Data Created", {
    "settings_id": fields.Integer(),
    "user_data": fields.Nested(user_data)
})
