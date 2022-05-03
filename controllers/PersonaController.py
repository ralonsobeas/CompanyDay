import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoCharlas import EventoCharlas
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64

db = SQLAlchemy()


def index():
    return 'index'

"""
    Guardar Persona.
"""
def store(persona):
    db.session.add(persona)
    db.session.commit()


"""
    Buscar todas las personas
"""
def all_query():
    return Persona.query.all()
