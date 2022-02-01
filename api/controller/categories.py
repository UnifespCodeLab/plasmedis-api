from flask_cors import cross_origin
from api.util.decorators import required
from api.service.categories import PostCategorias, GetCategorias, deleteCategorias
from api import api
from flask_restx import Resource
import api.model.request.categories as request
import api.model.response.categories as response
import api.model.response.default as default


categories = api.namespace('categories', description="Categories namespace")

@categories.route("/")
class Categorias(Resource):

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.category, token=True)
    def post(self, data):
        return PostCategorias(data)
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.category_list, token=True)
    def get(self):
        return GetCategorias()

@categories.route("/<int:id>")
class CategoriasId(Resource):

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def delete(self, id):
        return deleteCategorias(id)
