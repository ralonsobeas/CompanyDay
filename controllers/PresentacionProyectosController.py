import sys

from flask import render_template, redirect, url_for, request, abort
from models.PresentacionProyectos import PresentacionProyectos
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64

db = SQLAlchemy()


def index():
    return 'index'

def store():
    id = request.form['id']
    #presencial = True if(request.form['presencial']=='True') 
    try:
        request.form['presencial'] == 'True'
        presencial = True
    except:
        presencial = False

    try:
        request.form['videojuegos'] == 'True'
        videojuegos = True
    except:
        videojuegos = False

    try:
        request.form['disenoDigital'] == 'True'
        disenoDigital = True
    except:
        disenoDigital = False

    try:
        request.form['cortosAnimacion'] == 'True'
        cortosAnimacion = True
    except:
        cortosAnimacion = False

    try:
        request.form['ingenieria'] == 'True'
        ingenieria = True
    except:
        ingenieria = False

    presentacionProyectos = PresentacionProyectos(id, presencial, videojuegos, disenoDigital, ingenieria, cortosAnimacion)
    db.session.add(presentacionProyectos)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'

def show(presentacion_id):
    presentacionProyectos = PresentacionProyectos.query.get(presentacion_id)
    return render_template('empresa.html',
                            empresa=presentacionProyectos)

def update(presentacion_id):
    return 'update'

def delete(presentacion_id):
    return 'delete'

def all():
    empresas = PresentacionProyectos.query.all()
    return render_template('empresas.html',empresas=empresas)

