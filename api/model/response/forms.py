from api import api
from flask_restx import fields

form_socio = api.model("Form Socio",
{    
    "nome_rep_familia": fields.String(),
    "qtd_pessoas_familia": fields.Integer(),
    "pessoa_amamenta": fields.Boolean(),
    "qtd_criancas": fields.Integer(),
    "gestante": fields.Boolean(),
    "qtd_amamentando": fields.Integer(),
    "qtd_criancas_deficiencia": fields.Integer(),
    "qtd_gestantes": fields.Integer()
})

form_socio_message = api.model("Form Socio Message",
{
    "message": fields.String(), 
    "form": fields.Nested(form_socio)
})

form_socio_item = api.model("Form Socio Item",
{    
    "preenchido": fields.Boolean(),
    "nome_rep": fields.String(),
    "qtd_pessoas": fields.Integer(),
    "qtd_criancas": fields.Integer(),
    "gestante": fields.Boolean(),
    "qtd_amamentando": fields.Integer(),
    "qtd_criancas_deficiencia": fields.Integer(),
    "pessoa_amamenta": fields.Boolean(),
    "qtd_gestantes": fields.Integer()
})

form_socio_list = api.model("Form Socio List", {
    "count": fields.Integer(),
    "users": fields.List(fields.Nested(form_socio_item)),
})