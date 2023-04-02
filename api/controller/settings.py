from flask import request as req
from flask_cors import cross_origin
from flask_restx import Resource

from api import api, AUTH_VERSION

from api.util.decorators import required, token_required
from api.util.auth import get_authorized_user
from api.util.errors import EntryNotFoundError, MessagedError, NotFoundError
from api.util.request import get_boolean_arg
import api.model.request.user_data as request

from api.service.settings import *

import api.model.response.settings as response
import api.model.response.user_data as user_data_response
import api.model.response.default as default

settings = api.namespace('settings', description="Settings namespace")


@settings.route("/<string:type>")
class Settings(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=response.settings_response, token=True)
    def get(self, type):
        if type not in ['web', 'api']:
            return {"message": f"Não existe uma configuração para \"{type}\""}, 404

        data = ByType(type)

        return {"message": "Recuperando configuração atual", "settings": data}, 200
    
    
        ####TODO fazer o @required corretamente e 
    # padronizar o return (Ajustar o DTO, schema que o Biel falou, e o status code de resposta)
    
@settings.route("")
class UserData(Resource):
    
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, request=request.user_data_request, token=True)
    def post(self, data):
        createUserData(data);
        return {"message": "User data created"}, 200
    
    
    
@settings.route("/<int:settingsId>")
class UserDataId(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=user_data_response.user_data, token=True)
    def get(self, settingsId):
        
        data = findUserDataById(settingsId);
        print(data)    
        print(data['user_data'])
        return {"message": "User data sucessfully found", "user data": data['user_data']}, 200
    

    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def delete(self, settingsId):
        
        data = deleteUserData(settingsId)
        print(data.user_data)
        return {"message": "User data sucessfully deleted", "settings": data}, 200
    

