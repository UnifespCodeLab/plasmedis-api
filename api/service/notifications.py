from api import db
from api.model.database.notifications import Notificacao


def All(user_id=None):
    if user_id is not None:
        notifications = Notificacao.query.filter_by(user_id=user_id).order_by(Notificacao.created_date.desc()).all()
    else:
        notifications = Notificacao.query.order_by(Notificacao.created_date.desc()).all()

    return [notification.serialize() for notification in notifications]


def Create(data):
    new_notification = Notificacao(user_id=data['user_id'], content=data['content'])

    db.session.add(new_notification)
    db.session.commit()

    return new_notification.id


def UpdateRead(id, read):
    notification = Notificacao.query.get_or_404(id)
    notification.read = read

    db.session.commit()

