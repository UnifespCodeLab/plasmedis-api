from flask_cors import cross_origin
from flask_restx import Resource

from api import api

from api.util.decorators import required
from api.util.errors import MessagedError
from api.util.request import get_integer_list_arg, get_boolean_arg, get_path_without_pagination_args, get_pagination_arg
from api.util.response import get_paginated_list
from api.util.auth import get_authorized_user

from api.service.posts import All, ById, Create, UpdateStamp, Remove

import api.model.request.posts as request
import api.model.response.posts as response
import api.model.response.default as default

posts = api.namespace('posts', description="Posts namespace")


@posts.route("")
class Posts(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_complete_list, token=True)
    def get(self):
        results = All(recommended=get_boolean_arg('recommended', None),
                      categories=get_integer_list_arg('category'),
                      creators=get_integer_list_arg('creator'))

        page, limit = get_pagination_arg()
        path = get_path_without_pagination_args()
        posts_page = get_paginated_list("posts", results, path, page, limit)

        if 'posts' in posts_page:
            return posts_page, 200
        return posts_page, 400

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.post_create, token=True)
    def post(self, data):
        id = Create(data, get_authorized_user())

        return {"message": f"Postagem {id} criada"}, 200


@posts.route("/<int:id>")
class PostsId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_complete, token=True)
    def get(self, id):
        return ById(id), 200

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def delete(self, id):
        try:
            Remove(id, get_authorized_user())

            return {"message": f"Postagem {id} removida com sucesso"}, 200
        except MessagedError as e:
            # erro geral, que possui alguma mensagem especifica
            # nesse caso, informar a mensagem ed erro pro usuario E um status code 500 INTERNAL SERVER ERROR
            return {"message": e.message}, 500


@posts.route("/<int:id>/stamp")
class Stamp(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def put(self, id):
        UpdateStamp(id, True, get_authorized_user())

        return {"message": f"Selo emitido!"}, 200

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def delete(self, id):
        UpdateStamp(id, False, get_authorized_user())

        return {"message": f"Selo removido!"}, 200


@posts.route("/category/<int:id>")
class Filter(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_complete_list, token=True)
    def get(self, id):
        results = All(categories=[id])

        page, limit = get_pagination_arg()
        path = get_path_without_pagination_args()
        posts_page = get_paginated_list("posts", results, path, page, limit)

        if 'posts' in posts_page:
            return posts_page, 200
        return posts_page, 400


@posts.route("/user/<int:id>")
class UserPosts(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.post_complete_list, token=True)
    def get(self, id):
        results = All(creators=[id])

        page, limit = get_pagination_arg()
        path = get_path_without_pagination_args()
        posts_page = get_paginated_list("posts", results, path, page, limit)

        if 'posts' in posts_page:
            return posts_page, 200
        return posts_page, 400
    