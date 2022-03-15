import os
import jwt
from api import app
from flask import request

from api.model.database import users

def get_authorized_user() -> int:
    """
    Busca o usuário que está associado ao token.
    """
    token = request.headers['Authorization'].split("Bearer ")[1]
    payload = jwt.decode(token, app.config['SECRET_KEY'], issuer=os.environ.get('ME', 'plasmedis-api-local'),
                         algorithms=["HS256"],
                         options={"require": ["exp", "sub", "iss", "aud"], "verify_aud": False, "verify_iat": False,
                                  "verify_nbf": False})
    id = payload['sub']

    return users.Usuario.query.get(id)

