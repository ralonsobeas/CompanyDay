import sys

from flask import render_template, redirect, url_for, request, abort, flash
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from shared.models import login_manager
from flask_login import login_user,login_required,current_user,logout_user


import base64

db = SQLAlchemy()


def index():
    return 'index'

def login():
    id = request.form['id']
    password = request.form['password']
    remember = True if (request.form.get('remember')) else False

    user = Empresa.query.filter_by(id=id).first()

    if not user or not check_password_hash(user.password, password):
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
    file = request.files['logo']
    logo = file.read()

    render_logo = render_picture(logo)

    empresa = Empresa(id=id,nombre=nombre,password=generate_password_hash(password, method='sha256'), \
                        personaContacto=personaContacto,email=email,telefono=telefono,direccion=direccion, \
                        poblacion=poblacion,provincia=provincia,codigoPostal=codigoPostal,pais=pais,urlWeb=urlWeb,logo=logo, \
                        render_logo=render_logo,consentimientoNombre=consentimientoNombre,buscaCandidatos=buscaCandidatos)
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
    empresas = Empresa.query.filter_by(admin=False).all()
    return render_template('empresas.html',empresas=empresas)


def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic