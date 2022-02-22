#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db

class EventoCharlas(db.Model):
    __tablename__ = 'EventoCharlas'
    id = db.Column(db.Integer, primary_key=True)
    tema  = db.Column(db.String(4096))
    presencialidad  = db.Column(db.Boolean)
    titulo = db.Column(db.String(120))
    fecha = db.Column(db.Date)
    idempresa = db.Column(db.Integer)
    aprobada = db.Column(db.Boolean)
    

    def __init__(self, id,tema,presencialidad,titulo,fecha,idempresa,aprobada):
        self.id = id
        self.tema = tema
        self.presencialidad = presencialidad
        self.titulo = titulo
        self.fecha = fecha
        self.idempresa = idempresa
        self.aprobada = aprobada
