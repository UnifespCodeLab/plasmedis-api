from flask_cors import cross_origin
from api.util.decorators import required
from api.service.posts import PostCategorias, GetCategorias
from api import api
from flask_restx import Resource
import api.model.request.posts as request
import api.model.response.posts as response
import api.model.response.default as default


categories = api.namespace('categories', description="Categories namespace")

@categories.route("/")
class Forms(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def post(self, data):
        return PostCategorias(data)
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def get(self):
        return GetCategorias()