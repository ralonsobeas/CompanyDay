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

def store():
    id = request.form['id']
    nombre = request.form['nombre']
    puesto = request.form['puesto']
    comentario = request.form['comentario']

    empresa_id = request.form['idempresa']

    persona = Persona(id,nombre,puesto,comentario,empresa_id)
    db.session.add(persona)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'


def all_query():
    return Persona.query.all()
