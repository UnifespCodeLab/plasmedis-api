from flask_cors import cross_origin
from flask_restx import Resource

from api import api

from api.util.decorators import required
from api.util.auth import get_authorized_user
from api.util.request import get_path_without_pagination_args, get_pagination_arg
from api.util.response import get_paginated_list

from api.service.notifications import All, Create, UpdateRead

import api.model.request.notifications as request
import api.model.response.notifications as response
import api.model.response.default as default
from api.util.errors import MessagedError

notifications = api.namespace('notifications', description="Notifications namespace")

@notifications.route("")
class Notifications(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.notifications_list, token=True)
    def get(self):
        results = All()

        page, limit = get_pagination_arg()
        path = get_path_without_pagination_args()
        notifications_page = get_paginated_list("notifications", results, path, page, limit)

        if 'notifications' in notifications_page:
            return notifications_page, 200
        return notifications_page, 400
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(request=request.notification_create, response=default.message, token=True)
    def post(self, data):
        try:
            id = Create(data)
        except MessagedError as e:
            return {"message": e.message}, 500
        
        return {"message": f"Notificacao {id} criada"}, 200
    

@notifications.route("/<int:id>/read")
class MarkAsRead(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def put(self, id):
        try:
            UpdateRead(id, True)
        except MessagedError as e:
            return {"message": e.message}, 500
        
        return {"message": f"Notificacao {id} marcada como lida"}, 200
    

@notifications.route("/bulk-read")
class BulkMarkAsRead(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(request=request.notifications_bulk_read, response=default.message, token=True)
    def post(self, data):
        try:
            for id in data['ids']:
                UpdateRead(id, True)
        except MessagedError as e:
            for id in data['ids']:
                UpdateRead(id, False)
            return {"message": f"Houve algum erro ao marcar uma ou mais notificacoes como lida. Mensagem de erro: {e.message}"}, 500
        
        return {"message": f"Notificacoes marcadas como lidas"}, 200