from api import db
from api.model.database.notifications import Notificacao


def All():
    notifications = Notificacao.query.order_by(Notificacao.created_date.desc()).all()

    return [notification.serialize() for notification in notifications]