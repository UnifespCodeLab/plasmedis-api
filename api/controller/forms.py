from flask_cors import cross_origin
from api.util.decorators import required
from api.service.forms import FormSocio, FormSocioGetByUser
from api import api
from flask_restx import Resource
import api.model.request.posts as request
import api.model.response.posts as response
import api.model.response.default as default

forms = api.namespace('forms', description="Forms namespace")

@forms.route("/<int:id>")
class Forms(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def get(self, id):
        return FormSocio(id)
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def post(self, id):
        return FormSocio(id)

@forms.route("/user/<int:id>")
class FormsUser(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def get(self, id):
        return FormSocioGetByUser(id)

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def post(self, id):
        return FormSocioGetByUser(id)

