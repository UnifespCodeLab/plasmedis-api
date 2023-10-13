from api import db


class Notificacao(db.Model):
    __tablename__ = 'notificacoes'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    action_type = db.Column(db.Integer, nullable=False)
    action_object_id = db.Column(db.Integer)

    content = db.Column(db.String(400), nullable=False)
    read = db.Column(db.Boolean, default=False, nullable=False)

    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def update(self, data):
        for key in data:
            setattr(self, key, data[key])

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "action_type": self.action_type,
            "action_object_id": self.action_object_id,
            "content": self.content,
            "read": self.read,
            "created_date": self.created_date.strftime("%Y-%m-%dT%H:%M:%S"),
            "updated_date": self.updated_date.strftime("%Y-%m-%dT%H:%M:%S"),
        }