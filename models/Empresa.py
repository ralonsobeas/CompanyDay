#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from shared.models import db
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from models.EventoCharlas import EventoCharlas
from models.EventoPresentacionProyectos import EventoPresentacionProyectos
from models.EventoSpeedMeeting import EventoSpeedMeeting
from flask_login import UserMixin

"""
    Modelo de Empresa
"""
class Empresa(UserMixin,db.Model):
    __tablename__ = 'empresas'
    validado = db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key=True)
    nombre  = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    personaContacto  = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(120))
    poblacion = db.Column(db.String(120))
    provincia = db.Column(db.String(120))
    codigoPostal = db.Column(db.String(15))
    pais = db.Column(db.String(120))
    urlWeb = db.Column(db.String(120))
    logo = db.Column(db.String(120))
    consentimientoNombre = db.Column(db.Boolean)
    buscaCandidatos = db.Column(db.Boolean)

    admin = db.Column(db.Boolean)

    #Validación de usuario
    confirmed = db.Column(db.Integer, default=0)
    userHash = db.Column(db.String(50))

    #Eventos
    eventosFeriaEmpresas = db.relationship('EventoFeriaEmpresas', backref=db.backref('empresa'))
    eventosPresentacionProyectos = db.relationship('EventoPresentacionProyectos', backref='empresa', lazy='dynamic')
    eventosSpeedMeetings = db.relationship('EventoSpeedMeeting', backref='empresa', lazy='dynamic')
    eventosCharlas = db.relationship('EventoCharlas', backref='empresa', lazy='dynamic')



    def __init__(self, id,validado,nombre,password,personaContacto,email,telefono,direccion, \
                        poblacion,provincia,codigoPostal,pais,urlWeb,logo, \
                        consentimientoNombre,buscaCandidatos,admin,userHash):
        self.id = id
        self.validado = validado
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
        self.consentimientoNombre = consentimientoNombre
        self.buscaCandidatos = buscaCandidatos
        self.admin = admin
        self.userHash = userHash
        
    def __unicode__(self):
        return self.nombre
    def __repr__(self):
        return self.nombre
