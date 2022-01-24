from api import api
from flask_restx import fields

form_socio = api.model("Form Socio With Id",
{
    "nome_rep_familia": fields.String(),
    "pessoa": fields.Integer(),
    "qtd_pessoas_familia": fields.Integer(),
    "pessoa_amamenta": fields.Boolean(),
    "qtd_criancas": fields.Integer(),
    "gestante": fields.Boolean(),
    "qtd_amamentando": fields.Integer(),
    "qtd_criancas_deficiencia": fields.Integer(),
    "qtd_gestantes": fields.Integer()
})