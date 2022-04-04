import sys

from flask import render_template, redirect, url_for, request, abort, flash
from models.Empresa import Empresa
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from models.EventoPresentacionProyectos import EventoPresentacionProyectos
from models.EventoSpeedMeeting import EventoSpeedMeeting
from models.EventoCharlas import EventoCharlas
from models.Persona import Persona
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from shared.models import login_manager
from flask_login import login_user,login_required,current_user,logout_user
import os
from os.path import join, dirname, realpath
import platform
from config import UPLOAD_FOLDER_LINUX,UPLOAD_FOLDER_WINDOWS

import base64

db = SQLAlchemy()

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

    #estaría bien guardar esto con paths relativos... pero por ahora funciona
    """
    logopath = os.path.dirname(os.path.realpath(__file__))
    logopath = logopath.replace("controllers", "static/images/customlogos/"+ logo.filename)
    logo.save(logopath)
    logopath = "/static/images/customlogos/" + logo.filename
    """


    if(platform.system()=='Windows'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_WINDOWS)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers\\", "")
        logo.save(UPLOADS_PATH+"\\"+logo.filename)
    elif(platform.system()=='Linux'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_LINUX)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers/", "")
        logo.save(UPLOADS_PATH+"/"+logo.filename)



    logo = logo.filename

    empresa = Empresa(id=id,validado=False,nombre=nombre,password=generate_password_hash(password, method='sha256'), \
                        personaContacto=personaContacto,email=email,telefono=telefono,direccion=direccion, \
                        poblacion=poblacion,provincia=provincia,codigoPostal=codigoPostal,pais=pais,urlWeb=urlWeb,logo=logo, \
                        consentimientoNombre=consentimientoNombre,buscaCandidatos=buscaCandidatos,admin=False)
    db.session.add(empresa)
    db.session.commit()

    #id2 = request.form['id']
    tema = request.form['tema']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    titulo = request.form['titulo']
    fecha = request.form['fecha']
    aprobada = False
    autor = ''

    eventoCharla = EventoCharlas(tema = tema,presencialidad = presencialidad,titulo = titulo,fecha = fecha,aprobada = aprobada, empresa_id = id, autor = autor)
    db.session.add(eventoCharla)

    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'