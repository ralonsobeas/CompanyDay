#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db

"""
    Modelo Persona
"""
class Persona(db.Model):
    __tablename__ = 'personas'
    id = db.Column(db.Integer, primary_key=True)
    nombre  = db.Column(db.String(500))
    puesto  = db.Column(db.String(120))
    comentario  = db.Column(db.String(500))

    #Relación con empresa
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id', ondelete='CASCADE'))

    def __init__(self,nombre,puesto,comentario,empresa_id):
        self.nombre = nombre
        self.puesto = puesto
        self.comentario = comentario

        self.empresa_id = empresa_id
