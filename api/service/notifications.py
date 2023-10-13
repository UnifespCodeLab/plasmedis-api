from api import db
from api.model.database.notifications import Notificacao

ACTION_TYPES = {
    1: "Sem ação",
    2: "Selecionar categoria com ID {id}",
    3: "Abrir post com ID {id}",
    4: "Abrir gereciamento de posts",
    5: "Redirecionar para a tela de perfil",
    6: "Redirecionar para a tela de controle de usuários",
}


def All(user_id=None):
    if user_id is not None:
        notifications = Notificacao.query.filter_by(user_id=user_id).order_by(Notificacao.created_date.desc()).all()
    else:
        notifications = Notificacao.query.order_by(Notificacao.created_date.desc()).all()

    response = []
    for notification in notifications:
        obj = notification.serialize()
        obj['action']['description'] = ACTION_TYPES[obj['action']['id']]
        if '{' and '}' in obj['action']['description']:
            obj['action']['description'] = obj['action']['description'].format(id=obj['action']['object_id'])
        response.append(obj)

    return response


def Create(data):

    new_notification = Notificacao(action_type=data['action_type'], action_object_id=data['action_object_id'], action_description=ACTION_TYPES[data['action_type']], user_id=data['user_id'], content=data['content'])

    db.session.add(new_notification)
    db.session.commit()

    return new_notification.id


def UpdateRead(id, read=True):
    notification = Notificacao.query.get_or_404(id)
    notification.read = read

    db.session.commit()

