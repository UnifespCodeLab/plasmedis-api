from flask_cors import cross_origin
from api.util.decorators import required, token_required
from api.service.posts import Categorias, PutSelo, GetPostagens, PostPostagens, GetRecomendados, GetFiltros, GetPostagensId, GetListaPostagens
from flask import Blueprint
from api import api
from flask_restx import Resource
import api.model.request.posts as request
import api.model.response.posts as response
import api.model.response.default as default


#TODO: adicionar prefixo para as chamadas
app = Blueprint('posts', __name__, url_prefix='')

posts = api.namespace('posts', description="Posts namespace")

#TODO: criar controller para categorias?
#TODO: separar POST e GET
#TODO: adicionar json_required POST
@app.route('/categorias', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def categorias():
    return Categorias()

@posts.route("/<int:id>/stamp")
class Stamp(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def put(self, id):
        return PutSelo(id)

@posts.route("")
class Posts(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_full_list, token=False)
    def get(self):
        return GetPostagens()

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.post_create, token=False)
    def post(self, data):
        return PostPostagens(data)

@posts.route("/recommended")
class Recomended(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_full_list, token=False)
    def get(self):
        return GetRecomendados()

@posts.route("/category/<int:id>")
class Filter(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_full_list, token=False)
    def get(self, id):
        return GetFiltros(id)

@posts.route("/<int:id>")
class PostsId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_comments, token=False)
    def get(self, id):
        return GetPostagensId(id)

@posts.route("/user/<int:id>")
class UserPosts(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_list, token=False)
    def get(self, id):
        return GetListaPostagens(id)