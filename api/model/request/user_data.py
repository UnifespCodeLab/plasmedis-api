from flask_restx import fields

from api import api

user_data_request = api.model("User Data Created", {
    "settings_id": fields.Integer(),
    "user_data": fields.Nested({})
})
