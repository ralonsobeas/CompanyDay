import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoPresentacionProyectos import EventoPresentacionProyectos
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64

db = SQLAlchemy()


def index():
    return 'index'

"""
    Guardar EventoPresentacionProyectos
"""
def store():
    id = request.form['IdPresentacion']
    empresa_id = request.form['IdEmpresa']
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

    presentacionProyectos = EventoPresentacionProyectos(False ,id, presencial, videojuegos, disenoDigital, ingenieria, cortosAnimacion, empresa_id)
    db.session.add(presentacionProyectos)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'

"""
    Mostrar EventoPresentacionProyectos por id. Renderizar en empresa.html
"""
def show(presentacion_id):
    presentacionProyectos = EventoPresentacionProyectos.query.get(presentacion_id)
    return render_template('empresa.html',
                            empresa=presentacionProyectos)

def update(presentacion_id):
    return 'update'

def delete(presentacion_id):
    return 'delete'

"""
    Mostrar todas las empresas. Renderizar en empresas.html
"""
def all():
    empresas = EventoPresentacionProyectos.query.all()
    return render_template('empresas.html',empresas=empresas)

"""
    Buscar todas las empresas.
"""
def all_query():
    listaProyectosAprobados = EventoPresentacionProyectos.query\
    .join(Empresa, EventoPresentacionProyectos.empresa_id == Empresa.id)\
    .add_columns(EventoPresentacionProyectos.presencial, EventoPresentacionProyectos.videojuegos, EventoPresentacionProyectos.disenoDigital, EventoPresentacionProyectos.cortosAnimacion, EventoPresentacionProyectos.ingenieria, Empresa.logo, Empresa.nombre)\
    .filter(Empresa.validado == True)\
    .filter(EventoPresentacionProyectos.validado == True)
    return listaProyectosAprobados;
    
"""
    Validar para Admin
"""

def validar(id,valor):
    presentacion = EventoPresentacionProyectos.query.filter_by(id=id).first()
    presentacion.validado = valor
    db.session.commit()
