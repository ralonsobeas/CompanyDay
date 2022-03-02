#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db


class EventoFeriaEmpresas(db.Model):
    __tablename__ = 'eventoferiaempresas'
    id = db.Column(db.Integer, primary_key=True)
    fecha  = db.Column(db.Date)
    presencial = db.Column(db.Boolean)

    #Relación con empresa
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'))

    def __init__(self, id,fecha,presencial,empresa_id):
        self.id = id
        self.fecha = fecha
        self.presencial = presencial

        self.empresa_id = empresa_id
