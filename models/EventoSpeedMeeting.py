#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db

"""
    Modelo EventoSpeedMeeting
"""
class EventoSpeedMeeting(db.Model):
    __tablename__ = 'eventospeedmeeting'
    id = db.Column(db.Integer, primary_key=True)
    presencialidad  = db.Column(db.Boolean)
    fecha = db.Column(db.Date)
    horaInicio = db.Column(db.Time)
    horaFin = db.Column(db.Time)
    perfiles = db.Column(db.String(4096))
    pregunta = db.Column(db.String(4096))
    aprobada = db.Column(db.Boolean)

    #Relación con empresa
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'))

    def __init__(self,presencialidad,fecha,horaInicio,horaFin,perfiles,pregunta,empresa_id):
        self.presencialidad = presencialidad
        self.fecha = fecha
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.perfiles = perfiles
        self.pregunta = pregunta
        self.aprobada = False

        self.empresa_id = empresa_id
