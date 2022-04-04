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
    aprobada = db.Column(db.Boolean)

    #Relación con empresa
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'))

    def __init__(self,tema,presencialidad,titulo,fecha,aprobada,empresa_id):
        self.tema = tema
        self.presencialidad = presencialidad
        self.titulo = titulo
        self.fecha = fecha
        self.aprobada = aprobada

        self.empresa_id = empresa_id
