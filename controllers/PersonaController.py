import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoCharlas import EventoCharlas
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_required
import base64

db = SQLAlchemy()


def index():
    return 'index'

"""
    Guardar Persona.
"""
@login_required
def store(persona):
    db.session.add(persona)
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        if re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, id repetido (%s)" % persona.id

            """
        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"
            """
        else:
            return False, str(error)

    return True, "";


"""
    Buscar todas las personas
"""
def all_query():
    return Persona.query.all()

"""
    Obtener Persona por id de empresa.
"""
def get_by_empresa_id_all(empresa_id):
    persona = Persona.query.filter_by(empresa_id=empresa_id).all()
    return persona
