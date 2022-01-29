from api import db
import datetime

class Postagem(db.Model):
    __tablename__ = 'postagens'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(400), nullable=False)
    texto = db.Column(db.String(400), nullable=False)
    criador = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    selo = db.Column(db.Boolean, default=False, nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    def __init__(self, titulo, texto, criador, categoria):
        self.titulo = titulo
        self.texto = texto
        self.criador = criador
        self.categoria = categoria