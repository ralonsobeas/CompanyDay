import sys

from flask import render_template, redirect, url_for, request, abort
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64

db = SQLAlchemy()


def index():
    return 'index'

def store():
    id = request.form['id']
    nombre = request.form['nombreEmpresa']
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

    empresa = Empresa(id,nombre,personaContacto,email,telefono,direccion, \
                        poblacion,provincia,codigoPostal,pais,urlWeb,logo, \
                        render_logo,consentimientoNombre,buscaCandidatos)
    db.session.add(empresa)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'

def show(empresa_id):
    empresa = Empresa.query.get(empresa_id)
    return render_template('empresa.html',
                            empresa=empresa)

def update(empresa_id):
    return 'update'

def delete(empresa_id):
    return 'delete'

def all():
    empresas = Empresa.query.all()
    return render_template('empresas.html',empresas=empresas)

def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic
