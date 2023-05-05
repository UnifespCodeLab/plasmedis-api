from api import api
from flask_restx import fields

user = api.model("User", {
    "id": fields.Integer,
    "type": fields.Integer,
    "active": fields.Boolean,
    "email": fields.String,
    "username": fields.String,
    "name": fields.String,
    "has_data": fields.Boolean,
    "has_accepted_terms": fields.Boolean
})

user_data = api.model("User Data", {
    'genero': fields.String,
    'nascimento': fields.Date,
    'area_atuacao': fields.String,
    'instituicao': fields.String,
    'campus': fields.String,
    'setor': fields.String,
    'deficiencia': fields.Boolean,
    'parente_com_tea': fields.Boolean,
    'freq_convivio_tea': fields.String,
    'qtd_alunos_tea': fields.Integer,
    'tempo_trabalho_tea': fields.Integer,
    'qtd_pacientes_tea_ano': fields.Integer,
})

user_with_data = api.inherit("User with Data", user, {
    "data": fields.Nested(user_data, allow_null=True)
})

user_complete = api.model("User Complete", {
    "user": fields.Nested(user_with_data)
})

users_list = api.model("Users List", {
    "count": fields.Integer(),
    "current": fields.Integer(),
    "limit": fields.Integer(),
    "previous": fields.String(),
    "next": fields.String(),
    "users": fields.List(fields.Nested(user))
})

user_create_message = api.model("User Create Message", {
    "message": fields.String(),
    "user": fields.Integer()
})
