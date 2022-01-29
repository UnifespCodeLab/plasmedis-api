from flask_cors import cross_origin
from api.util.decorators import required
from api.service.comments import PostComentarios, GetComentarios, GetComentariosPostagem
from api import api
from flask_restx import Resource
import api.model.request.categories as request
import api.model.response.categories as response
import api.model.response.default as default

comments = api.namespace('comments', description="Comments namespace")

@comments.route("/")
class Comments(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def post(self, data):
        return PostComentarios(data)
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def get(self):
        return GetComentarios()

@comments.route("/post/<int:id>")
class CommentsPost(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def get(self, id):
        return GetComentariosPostagem(id)