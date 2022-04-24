import sys

from flask import render_template, redirect, url_for, request, abort, flash, Flask, current_app
from models.Empresa import Empresa
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from models.EventoPresentacionProyectos import EventoPresentacionProyectos
from models.EventoSpeedMeeting import EventoSpeedMeeting
from models.EventoCharlas import EventoCharlas
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from shared.models import login_manager
from flask_login import login_user,login_required,current_user,logout_user
import os
from os.path import join, dirname, realpath
import platform
from config import UPLOAD_FOLDER_LINUX,UPLOAD_FOLDER_WINDOWS

from flask_mail import Mail, Message
from threading import Thread

import base64

import random

db = SQLAlchemy()


def index():
    return 'index'

"""
    Login de empresa

    Recibe mail y password, busca el usuario y compara el password.
    Si es correcto redirige al index.
"""
def login():
    email = request.form['mail']
    password = request.form['password']
    remember = True if (request.form.get('remember')) else False

    user = Empresa.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password,password):
        flash('Please check your login details and try again.')
        return redirect(url_for('loginEmpresa'))

    flash('Usuario correcto')
    login_user(user,remember=remember)

    return redirect(url_for('index'))

"""
    Login manager para flask_login
"""
@login_manager.user_loader
def loginManager(id):
    return Empresa.query.get(id)

"""
    Logout
"""
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

"""
    Mail asíncrono
"""
def async_send_mail(app, msg, mail):
    with app.app_context():
        mail.send(msg)

"""
    Guardar empresa en BBDD
"""
def store():
    id = request.form['CIF']
    nombre = request.form['nombreEmpresa']
    password = request.form['password']
    personaContacto = request.form['personaContacto']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    poblacion = request.form['poblacion']
    provincia = request.form['provincia']
    codigoPostal = request.form['codigoPostal']
    pais = request.form['pais']
    urlWeb = request.form['urlWeb']
    consentimientoNombre = True
    buscaCandidatos = True

    logo = request.files['logo']
    logoFileName = id + ".png";

    # Cambiar barras dependiendo del sistema operativo
    if(platform.system()=='Windows'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_WINDOWS)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers\\", "")
        logo.save(UPLOADS_PATH+"\\"+logoFileName)
    elif(platform.system()=='Linux'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_LINUX)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers/", "")
        logo.save(UPLOADS_PATH+"/"+logoFileName)


    #Proceso validación usuario
    userHash = ''.join(random.choice('AILNOQVBCDEFGHJKMPRSTUXZabcdefghijklmnopqrstuvxz1234567890') for i in range(50))
    url = 'http://{}/empresas/confirmuser/{}/{}'.format(request.host,nombre,userHash)

    empresa = Empresa(id=id,validado=False,nombre=nombre,password=generate_password_hash(password, method='sha256'), \
                        personaContacto=personaContacto,email=email,telefono=telefono,direccion=direccion, \
                        poblacion=poblacion,provincia=provincia,codigoPostal=codigoPostal,pais=pais,urlWeb=urlWeb,logo=logoFileName, \
                        consentimientoNombre=consentimientoNombre,buscaCandidatos=buscaCandidatos,admin=False,userHash=userHash)
    db.session.add(empresa)
    db.session.commit()

    tema = request.form['tema']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    titulo = request.form['titulo']
    fecha = request.form['fecha']
    aprobada = False
    autor = ''

    eventoCharla = EventoCharlas(tema = tema,presencialidad = presencialidad,titulo = titulo,fecha = fecha,aprobada = aprobada, empresa_id = id, autor = autor)
    db.session.add(eventoCharla)

    db.session.commit()

    # Mandar mail

    """
    app = Flask(__name__)
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'companydayprueba@gmail.com'
    app.config['MAIL_PASSWORD'] = 'upcmiwagffbilunq'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    """
    #send_email(email,'Bienvenido al Company Day en U-Tad', 'templateMail',url=url)
    send_email("companydayprueba@gmail.com",'Bienvenido al Company Day en U-Tad', 'templateMail',url=url)
    flash('Te has registrado! Revista tu email para confirmar tu cuenta.')
    """
    mail= Mail(app)

    msg = Message('Bienvenido al Company Day en U-Tad', sender =  'companydayprueba@gmail.com', recipients = ['companydayprueba@gmail.com'])
    msg.html = render_template('templateMail.html')
    thr = Thread(target=async_send_mail, args=[app, msg, mail])
    thr.start()
    """
    #with app.app_context():
     #   msg = Message('Bienvenido al Company Day en U-Tad', sender =  'companydayprueba@gmail.com', recipients = ['companydayprueba@gmail.com'])
        #msg.html = render_template('templateMail.html')
      #  mail.send(msg)

    return render_template('index3.html')

def confirmUser(username,userhash):
    empresa = Empresa.query.filter_by(nombre=username).first()

    print(empresa.nombre)

    if not empresa:
        abort(403, description="Invalid url.")
    elif len(empresa.userHash) == 0 or empresa.userHash != userhash:
        abort(403, description="Invalid url.")
    else:
        try:
            print(empresa.nombre)
            empresa.confirmed = 1
            empresa.userHash = ''
            #No me funciona sin esta query (DEBERIA)
            db.session.query(Empresa).filter(Empresa.nombre==username).update({"confirmed":1,\
            "userHash":''})
            db.session.commit()
            flash('Has confirmado el usuario!')
        except:
            abort(500, description="An error has occurred.")

    return render_template('index3.html')


"""
    Guardar empresa en BBDD ADMIN
"""

def storeAdmin():
    id = request.form['CIF']
    nombre = request.form['nombreEmpresa']
    password = request.form['password']
    personaContacto = request.form['personaContacto']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    poblacion = request.form['poblacion']
    provincia = request.form['provincia']
    codigoPostal = request.form['codigoPostal']
    pais = request.form['pais']
    urlWeb = request.form['urlWeb']
    consentimientoNombre = True
    buscaCandidatos = True

    logo = request.files['logo']
    logoFileName = id + ".png";

    if(platform.system()=='Windows'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_WINDOWS)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers\\", "")
        logo.save(UPLOADS_PATH+"\\"+logoFileName)
    elif(platform.system()=='Linux'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_LINUX)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers/", "")
        logo.save(UPLOADS_PATH+"/"+logoFileName)

    empresa = Empresa(id=id,validado=False,nombre=nombre,password=generate_password_hash(password, method='sha256'), \
                        personaContacto=personaContacto,email=email,telefono=telefono,direccion=direccion, \
                        poblacion=poblacion,provincia=provincia,codigoPostal=codigoPostal,pais=pais,urlWeb=urlWeb,logo=logoFileName, \
                        consentimientoNombre=consentimientoNombre,buscaCandidatos=buscaCandidatos,admin=False)
    db.session.add(empresa)
    db.session.commit()
    return redirect('../admin/empresa')



"""
    Mostrar perfil. Si editable 1, editable.
"""
def show(nombre,editable=0):
    if(editable==1):
        editable=True
    else:
        editable=False

    empresa = Empresa.query.filter_by(nombre=nombre).first()
    if not empresa or empresa.admin==True:
        return abort(404)
    eventosFeriaEmpresa = EventoFeriaEmpresas.query.filter_by(empresa_id = empresa.id).all()
    eventosPresentacionProyectos = EventoPresentacionProyectos.query.filter_by(empresa_id = empresa.id).all()
    eventosSpeedMeeting = EventoSpeedMeeting.query.filter_by(empresa_id = empresa.id).all()
    eventosCharla = EventoCharlas.query.filter_by(empresa_id = empresa.id).all()
    return render_template('empresa.html',
                            empresa=empresa,eventosFeriaEmpresa=eventosFeriaEmpresa, \
                            eventosPresentacionProyectos=eventosPresentacionProyectos, \
                            eventosSpeedMeeting=eventosSpeedMeeting,eventosCharla=eventosCharla,editable=editable)

"""
    Mostrar perfil del usuario actual.
"""
@login_required
def userProfile(editable=0):
    return show(current_user.nombre,editable)

"""
    Actualizar usuario de empresa.
"""
@login_required
def update():
    if(request.form['cancel'] != '1'):
        db.session.query(Empresa).filter(Empresa.id==current_user.id).update({"personaContacto":request.form['personaContacto'],\
        "email":request.form['email'],\
        "telefono":request.form['telefono'],\
        "direccion":request.form['direccion'],\
        "provincia":request.form['provincia'],\
        "pais":request.form['pais'],\
        "codigoPostal":request.form['codigoPostal']})
        db.session.commit()
    return render_template('profileRedirect.html')

"""
    Actualizar usuario de empresa Admin.
"""

def updateAdmin():
    if request.form['consentimientoNombre'] == 'True':
        consentimientoNombre = True;
    else:
        consentimientoNombre = False;
    if request.form['buscaCandidatos'] == 'True':
        buscaCandidatos = True;
    else:
        buscaCandidatos = False;
    db.session.query(Empresa).filter(Empresa.id==request.form['CIF']).update({\
        "nombre":request.form['nombreEmpresa'],\
        "personaContacto":request.form['personaContacto'],\
        "email":request.form['email'],\
        "telefono":request.form['telefono'],\
        "direccion":request.form['direccion'],\
        "poblacion":request.form['poblacion'],\
        "provincia":request.form['provincia'],\
        "pais":request.form['pais'],\
        "codigoPostal":request.form['codigoPostal'],\
        "urlWeb":request.form['urlWeb'],\
        "consentimientoNombre":consentimientoNombre,\
        "buscaCandidatos":buscaCandidatos})
    db.session.commit()
    return redirect('../admin/empresa')

"""
    Obtener empresa por id.
"""
def get_by_id(id):
    empresa = Empresa.query.filter_by(id=id).first()
    return empresa

"""
    Obtener todas las empresas validadas. Renderizar en html.
"""
def all():
    empresas = Empresa.query.filter_by(validado=True).all()
    return render_template('empresas.html',empresas=empresas)

"""
    Obtener todas las empresas.
"""
def all_query():
    return Empresa.query.filter_by(validado=True).all()

"""
    Validar empresa.
"""
def validar(id,valor):
    empresa = Empresa.query.filter_by(id=id).first()
    empresa.validado = valor
    db.session.commit()

from flask import current_app

def send_email(to, subject, template, url, **kwargs):
    app = Flask(__name__)

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'companydayprueba@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ghcjtlcchwhjbuyw'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail = Mail(current_app)
    app.config.from_object('config')
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    #msg.body = render_template(template + '.txt', **kwargs, url=url)
    msg.html = render_template(template + '.html', **kwargs, url=url)
    # flash("send_email: {}".format(url))
    mail.send(msg)
    #thr = Thread(target=async_send_mail, args=[app, msg, mail])
    #thr.start()
