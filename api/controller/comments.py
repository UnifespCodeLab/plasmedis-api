from flask_cors import cross_origin
from flask_restx import Resource

from api import api, app
from api.util.decorators import required
from api.util.auth import get_authorized_user
from api.util.request import get_path_without_pagination_args, get_pagination_arg
from api.util.response import get_paginated_list
from api.service.comments import All, ByPost, Create, Remove, Edit
import api.model.request.comments as request
import api.model.response.comments as response
import api.model.response.default as default
from api.util.errors import ForbiddenError, MessagedError

comments = api.namespace('comments', description="Comments namespace")

@comments.route("")
class Comments(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @api.doc(summary='POST Comment', description='This endpoint handles a POST request that posts a comment')
    @required(response=default.message, request=request.comment, token=True)
    def post(self, data):
        id = Create(data, get_authorized_user())
        return {"message": f"Comentário {id} registrado"}, 200

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @api.doc(summary='GET Comments', description='This endpoint handles a GET request and returns the list of comments')
    @required(response=response.comment_list, token=True)
    def get(self):
        results = All()
        page, limit = get_pagination_arg()
        path = get_path_without_pagination_args()
        comments_page = get_paginated_list("comments", results, path, page, limit)
        if 'comments' in comments_page:
            return comments_page, 200
        return comments_page, 400

@comments.route("/post/<int:id>")
class CommentsPost(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @api.doc(summary='GET Comment by ID', description='This endpoint handles a GET request and returns a specific comment by ID')
    @required(response=response.comment_list, token=True)
    def get(self, id):
        results = ByPost(id)
        page, limit = get_pagination_arg()
        path = get_path_without_pagination_args()
        comments_page = get_paginated_list("comments", results, path, page, limit)
        if 'comments' in comments_page:
            return comments_page, 200
        return comments_page, 400

@comments.route("/<int:id>", methods=["DELETE", "PATCH", "OPTIONS"])
class CommentsId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @api.doc(summary='DELETE Comment by ID', description='This endpoint handles a DELETE request that deletes a comment by ID')
    @required(response=default.message, token=True)
    def delete(self, id):
        try:
            Remove(id, get_authorized_user())
            return {"message": f"Comentário {id} removido com sucesso"}, 200
        except MessagedError as e:
            return {"message": e.message}, 500

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @api.doc(summary='PATCH Comment by ID', description='This endpoint atualiza um comentário específico por ID')
    @required(response=default.message, request=request.comment, token=True)
    def patch(self, id):
        data = api.payload  # Captura o corpo da requisição (JSON)
        try:
            updated_comment = Edit(id, data, get_authorized_user())
            return {"message": "Comentário atualizado com sucesso", "comment": updated_comment}, 200
        except ForbiddenError as e:
            return {"message": e.message}, 403
        except Exception as e:
            return {"message": "Erro ao atualizar o comentário"}, 500

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    def options(self):
        response = app.make_response('')
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        return response
