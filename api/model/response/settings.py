from api import api
from flask_restx import fields


visible = api.model("Visibility", {
    "/categorias": fields.Boolean()
})

settings = api.model("Settings", {
    "id": fields.Integer(),
    "visible": fields.Nested(visible)
})

settings_response = api.model("Settings Response", {
    "message": fields.String(),
    "settings": fields.Nested(settings)
})
