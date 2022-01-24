from flask_cors import cross_origin
from api.util.decorators import required
from api.service.forms import PostFormSocio, GetFormSocio, PostFormSocioGetByUser, GetFormSocioGetByUser
from api import api
from flask_restx import Resource
import api.model.request.forms as request
import api.model.response.forms as response
import api.model.response.default as default

forms = api.namespace('forms', description="Forms namespace")

@forms.route("/")
class Forms(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.form_socio, token=False)
    def post(self, data):
        return PostFormSocio(data)


@forms.route("/<int:id>")
class FormsId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.form_socio_list, token=False)
    def get(self, id):
        return GetFormSocio(id)
    
@forms.route("/user/<int:id>")
class FormsUser(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.form_socio_message, token=False)
    def get(self, id):
        return GetFormSocioGetByUser(id)

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.status_message, request=response.form_socio, token=False)
    def post(self, data, id):
        return PostFormSocioGetByUser(data, id)

