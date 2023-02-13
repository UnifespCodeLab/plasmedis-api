from flask import request as req
from flask_cors import cross_origin
from flask_restx import Resource

import json

from api import api

from api.util.decorators import required
from api.util.auth import get_authorized_user
from api.util.request import get_path_without_pagination_args, get_pagination_arg
from api.util.response import get_paginated_list

from api.service.categories import All, ById, Create, Remove

import api.model.request.categories as request
import api.model.response.categories as response
import api.model.response.default as default

from api.util.errors import MessagedError

categories = api.namespace('categories', description="Categories namespace")


@categories.route("")
class Forms(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.category, token=True)
    def post(self, data):
        id = Create(data, get_authorized_user())

        return {"message": f"Categoria {id} criada com sucesso"}, 200
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.category_list, token=True)
    def get(self):
        categorias = All()

        page, limit = get_pagination_arg()
        path = get_path_without_pagination_args()
        categories_page = get_paginated_list("categories", categorias, path, page, limit)

        if 'categories' in categories_page:
            return categories_page, 200
        return categories_page, 400


@categories.route("/<int:id>")
class CategoriesId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def delete(self, id):
        data = None
        if req.data.read():
            data = json.loads(req.data.decode('utf-8'))

        try:
            replacement = None
            if data is not None and "replace_id" in data:
                replacement = data["replace_id"]

            category = Remove(id, replacement, get_authorized_user())

            if replacement is None:
                return {"message": f"Categoria \"{category['name']}\" ({id}) removida com sucesso"}, 200
            else:
                replacementCategory = ById(replacement)
                return {"message": f"Categoria \"{category['name']}\" ({id}) removida com sucesso (e substituida por \"{replacementCategory['name']}\")"}, 200
        except MessagedError as e:
            # erro geral, que possui alguma mensagem especifica
            # nesse caso, informar a mensagem ed erro pro usuario E um status code 500 INTERNAL SERVER ERROR
            return {"message": e.message}, 500
