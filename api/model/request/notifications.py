from api import api
from flask_restx import fields

notification_create = api.model("Notification Create", {
    "user_id": fields.Integer(),
    "content": fields.String(),
    "action_type": fields.Integer(),
    "action_object_id": fields.Integer()
})


notifications_bulk_read = api.model("Notifications Bulk Read", {
    "ids": fields.List(fields.Integer())
})