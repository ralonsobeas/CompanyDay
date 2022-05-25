import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoCharlas import EventoCharlas
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_required,current_user
import base64
from shared.models import db


def index():
    return 'index'


"""
    Guardar EventoCharla en BBDD
"""
def store(eventoCharla):
    db.session.add(eventoCharla)
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        if re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, id repetido (%s)" % eventoCharla.id

            """
        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"
            """
        else:
            return False, str(error)

    return True, "";

def show(empresa_id):
    return 'show'

def update(empresa_id):
    return 'update'

def delete(empresa_id):
    return 'delete'

"""
    Mostrar todos los EventoCharlas. Renderiza en registroCharlas.html
"""
def all():
    eventoCharlas = EventoCharlas.query.all()
    return render_template('registroCharlas.html',eventoCharlas=eventoCharlas)

"""
    Buscar todos los EventoCharlas.
"""
def all_query():
    listaCharlasAprobadas = EventoCharlas.query\
    .join(Empresa, EventoCharlas.empresa_id == Empresa.id)\
    .add_columns(EventoCharlas.url,EventoCharlas.tema, EventoCharlas.presencialidad, EventoCharlas.titulo, EventoCharlas.fecha, EventoCharlas.autor, Empresa.logo, Empresa.nombre)\
    .filter(Empresa.validado == True)\
    .filter(EventoCharlas.aprobada == True)
    return listaCharlasAprobadas;

"""
    Validar para Admin
"""
@login_required
def validar(id,valor):
    charla = EventoCharlas.query.filter_by(id=id).first()
    charla.aprobada = valor
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        return False, "Error al actualizar"

    return True, "";

"""
    Obtener EventoCharlas por id de empresa.
"""
def get_by_empresa_id_all(empresa_id):
    try:
        eventoCharlas = EventoCharlas.query.filter_by(empresa_id=empresa_id).all()
    except:
        db.session.rollback()
    return eventoCharlas
