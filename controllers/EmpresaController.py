import sys

from flask import render_template, redirect, url_for, request, abort, flash
from models.Empresa import Empresa
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


def index():
    return 'index'

def login():
    id = request.form['id']
    password = request.form['password']
    remember = True if (request.form.get('remember')) else False

    user = Empresa.query.filter_by(id=id).first()

    if not user or not check_password_hash(user.password,password):
        flash('Please check your login details and try again.')
        return redirect(url_for('loginEmpresa'))

    flash('Usuario correcto')
    login_user(user,remember=remember)

    return redirect(url_for('index'))


@login_manager.user_loader
def loginManager(id):
    return Empresa.query.get(id)

@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

def store():
    id = request.form['id']
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
    consentimientoNombre = True if(request.form['consentimientoNombre']=='True') else False
    buscaCandidatos = True if(request.form['buscaCandidatos']=='True') else False

    #Guardar logo
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

    return 'Su informacion ha sido guardada en nuestra base de datos'

@login_required
def show(empresa_id):
    empresa = Empresa.query.get(empresa_id)
    return render_template('empresa.html',
                            empresa=empresa)
@login_required
def userProfile():
    empresa = current_user
    return render_template('empresa.html',
                            empresa=empresa)
def update(empresa_id):
    return 'update'

def delete(empresa_id):
    return 'delete'

def all():
    empresas = Empresa.query.filter_by(validado=True).all()
    return render_template('empresas.html',empresas=empresas)

def all_query():
    return Empresa.query.filter_by(validado=True).all()

def validar(id,valor):
    empresa = Empresa.query.filter_by(id=id).first()
    empresa.validado = valor
    db.session.commit()

def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic
