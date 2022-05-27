import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoPresentacionProyectos import EventoPresentacionProyectos
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_required
import base64

from shared.models import db


def index():
    return 'index'

"""
    Guardar EventoPresentacionProyectos
"""
def store_new(presentacionProyectos):
    db.session.add(presentacionProyectos)
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        if re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, id repetido (%s)" % presentacionProyectos.id

            """
        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"
            """
        else:
            return False, str(error)

    return True, "";

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
    store_new(presentacionProyectos)

def show(presentacion_id):
    return 'show'

def update(presentacion_id):
    return 'update'

def delete(presentacion_id):
    return 'delete'

def all(presentacion_id):
    return 'all'

"""
    Buscar todos los EventoPresentacionProyectos.
"""
def all_query():
    listaProyectosAprobados = EventoPresentacionProyectos.query\
    .join(Empresa, EventoPresentacionProyectos.empresa_id == Empresa.id)\
    .add_columns(EventoPresentacionProyectos.url,EventoPresentacionProyectos.presencial, EventoPresentacionProyectos.videojuegos, EventoPresentacionProyectos.disenoDigital, EventoPresentacionProyectos.cortosAnimacion, EventoPresentacionProyectos.ingenieria, Empresa.logo, Empresa.nombre)\
    .filter(Empresa.validado == True)\
    .filter(EventoPresentacionProyectos.validado == True)
    return listaProyectosAprobados;

"""
    Validar para Admin EventoPresentacionProyectos
"""
@login_required
def validar(id,valor):
    presentacion = EventoPresentacionProyectos.query.filter_by(id=id).first()
    presentacion.validado = valor
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        return False, "Error al actualizar"

    return True, "";

"""
    Obtener EventoPresentacionProyectos por id de empresa.
"""
def get_by_empresa_id_all(empresa_id):
    try:
        eventoPresentacionProyectos = EventoPresentacionProyectos.query.filter_by(empresa_id=empresa_id).all()
    except:
        db.session.rollback()
    return eventoPresentacionProyectos
