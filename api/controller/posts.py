from flask_cors import cross_origin
from api.util.decorators import required, token_required
from api.service.posts import Categorias, Selo, GetPostagens, PostPostagens, Recomendados, Filtros, PostagensId, ListaPostagens
from flask import Blueprint
from api import api
from flask_restx import Resource
import api.model.request.auth as request
import api.model.response.auth as response
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
    def put(self):
        return Selo(id)

@posts.route("/")
class Posts(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def get(self):
        return GetPostagens()

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=False)
    def post(self, data):
        return PostPostagens(data)

#TODO: criar controller para recomendados?
@app.route('/recomendados', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def recomendados():
    return Recomendados()

@app.route('/postagens/categorias/<id_categoria>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def filtros(id_categoria):
    return Filtros(id_categoria)

@app.route('/postagens/<id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def postagensId(id):
    return PostagensId(id)

#TODO: padronizar nome?
@app.route('/lista_postagens/<id>', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@token_required
def lista_postagens(id):
    return ListaPostagens(id)