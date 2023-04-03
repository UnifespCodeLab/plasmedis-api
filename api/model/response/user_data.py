from flask_restx import fields

from api import api

generic_model = api.model('Generic', {
    "message": fields.String(),
    'user_data': fields.Raw(description='Data')
})
