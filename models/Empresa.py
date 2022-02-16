#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db

class Empresa(db.Model):
    __tablename__ = 'empresas'
    id = db.Column(db.Integer, primary_key=True)
    nombre  = db.Column(db.String(120))
    descripcion = db.Column(db.String(120))
    correo = db.Column(db.String(120))
    telefono = db.Column(db.String(15))
    ubicacion = db.Column(db.String(120))
    logo = db.Column(db.LargeBinary)
    render_logo = db.Column(db.Text)

    def __init__(self, id,nombre,descripcion,correo,telefono,ubicacion,logo,render_logo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.correo = correo
        self.telefono = telefono
        self.ubicacion = ubicacion
        self.logo = logo
        self.render_logo = render_logo
