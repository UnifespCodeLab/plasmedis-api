from api import api
from flask_restx import fields

notification = api.model("Notification", {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "content": fields.String,
    "read": fields.Boolean,
    "created_date": fields.DateTime,
    "updated_date": fields.DateTime,
})

notifications_list = api.model("Notifications List", {
    "count": fields.Integer(),
    "current": fields.Integer(),
    "limit": fields.Integer(),
    "previous": fields.String(),
    "next": fields.String(),
    "notifications": fields.List(fields.Nested(notification))
})