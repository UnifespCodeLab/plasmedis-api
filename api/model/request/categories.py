from api import api
from flask_restx import fields

category = api.model("Create Category", {
    "nome": fields.String("nome", required=True)
})