#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db

class PresentacionProyectos(db.Model):
    __tablename__ = 'presentacionProyectos'
    id = db.Column(db.Integer, primary_key=True)
    presencial = db.Column(db.Boolean)
    videojuegos = db.Column(db.Boolean)
    disenoDigital = db.Column(db.Boolean)
    cortosAnimacion = db.Column(db.Boolean)
    ingenieria = db.Column(db.Boolean)

    def __init__(self, id, presencial, videojuegos, cortosAnimacion, disenoDigital, ingenieria):
        self.id = id
        self.presencial = presencial
        self.videojuegos = videojuegos
        self.cortosAnimacion = cortosAnimacion
        self.disenoDigital = disenoDigital
        self.ingenieria = ingenieria
