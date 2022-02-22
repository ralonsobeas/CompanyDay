#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db

class EventoSpeedMeeting(db.Model):
    __tablename__ = 'EventoSpeedMeeting'
    id = db.Column(db.Integer, primary_key=True)
    presencialidad  = db.Column(db.Boolean)
    fecha = db.Column(db.Date)
    duracion = db.Column(db.Integer)
    perfiles = db.Column(db.String(4096))
    pregunta = db.Column(db.String(4096))
    idempresa = db.Column(db.Integer)
    aprobada = db.Column(db.Boolean)


    def __init__(self, id,tema,presencialidad,titulo,fecha,idempresa,aprobada):
        self.id = id
        self.presencialidad = presencialidad
        self.fecha = fecha
        self.duracion = duracion
        sel.perfiles = perfiles
        self.pregunta = pregunta
        self.idempresa = idempresa
        self.aprobada = aprobada
