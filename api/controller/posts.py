from flask_cors import cross_origin
from api.util.decorators import required
from api.service.posts import PutSelo, GetPostagens, PostPostagens, GetRecomendados, GetFiltros, GetPostagensId, \
    GetListaPostagens, UpdatePostagem
from api import api
from flask_restx import Resource
import api.model.request.posts as request
import api.model.response.posts as response
import api.model.response.default as default

posts = api.namespace('posts', description="Posts namespace")

@posts.route("/<int:id>/stamp")
class Stamp(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def put(self, id):
        return PutSelo(id)

@posts.route("")
class Posts(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_full_list, token=True)
    def get(self):
        return GetPostagens()

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.post_create, token=True)
    def post(self, data):
        return PostPostagens(data)

@posts.route("/recommended")
class Recomended(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_full_list, token=True)
    def get(self):
        return GetRecomendados()

@posts.route("/category/<int:id>")
class Filter(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_full_list, token=True)
    def get(self, id):
        return GetFiltros(id)

@posts.route("/<int:id>")
class PostsId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_comments, token=True)
    def get(self, id):
        return GetPostagensId(id)

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.post_update, token=True)
    def put(self, id, data):
        return UpdatePostagem(id, data)

@posts.route("/user/<int:id>")
class UserPosts(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_list, token=True)
    def get(self, id):
        return GetListaPostagens(id)