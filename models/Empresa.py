#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from flask_login import UserMixin

class Empresa(UserMixin,db.Model):
    __tablename__ = 'empresas'
    id = db.Column(db.Integer, primary_key=True)
    nombre  = db.Column(db.String(120))
    password = db.Column(db.String(120))
    personaContacto  = db.Column(db.String(120))
    email = db.Column(db.String(120))
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(120))
    poblacion = db.Column(db.String(120))
    provincia = db.Column(db.String(120))
    codigoPostal = db.Column(db.String(15))
    pais = db.Column(db.String(120))
    urlWeb = db.Column(db.String(120))
    logo = db.Column(db.LargeBinary)
    render_logo = db.Column(db.Text)
    consentimientoNombre = db.Column(db.Boolean)
    buscaCandidatos = db.Column(db.Boolean)

    admin = db.Column(db.Boolean)

    #Eventos
    eventosFeriaEmpresas =db.relationship("EventoFeriaEmpresas")
    #eventosPresentacionProyectos = db.relationship('EventoPresentacionProyectos')
    #eventosSpeedMeetings = db.relationship('EventoSpeedMeetings')
    #eventosCharlas =  db.relationship('EventoCharlas'


    def __init__(self, id,nombre,password,personaContacto,email,telefono,direccion, \
                        poblacion,provincia,codigoPostal,pais,urlWeb,logo, \
                        render_logo,consentimientoNombre,buscaCandidatos):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.personaContacto = personaContacto
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.poblacion = poblacion
        self.provincia = provincia
        self.codigoPostal = codigoPostal
        self.pais = pais
        self.urlWeb = urlWeb
        self.logo = logo
        self.render_logo = render_logo
        self.consentimientoNombre = consentimientoNombre
        self.buscaCandidatos = buscaCandidatos
