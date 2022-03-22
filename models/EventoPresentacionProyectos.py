#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db

class EventoPresentacionProyectos(db.Model):
    __tablename__ = 'presentacionProyectos'
    validado = db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key=True)
    presencial = db.Column(db.Boolean)
    videojuegos = db.Column(db.Boolean)
    disenoDigital = db.Column(db.Boolean)
    cortosAnimacion = db.Column(db.Boolean)
    ingenieria = db.Column(db.Boolean)

    #Relación con empresa
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'))

    def __init__(self, validado, id, presencial, videojuegos, cortosAnimacion, disenoDigital, ingenieria,empresa_id):
        self.validado = validado
        self.id = id
        self.presencial = presencial
        self.videojuegos = videojuegos
        self.cortosAnimacion = cortosAnimacion
        self.disenoDigital = disenoDigital
        self.ingenieria = ingenieria
        self.empresa_id = empresa_id
