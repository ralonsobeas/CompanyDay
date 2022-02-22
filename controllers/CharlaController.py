import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoCharlas import EventoCharlas
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64

db = SQLAlchemy()


def index():
    return 'index'

def store():
    id = request.form['id']
    tema = request.form['tema']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    titulo = request.form['titulo']
    fecha = request.form['fecha']
    idempresa = request.form['idempresa']
    aprobada = False

    eventoCharla = EventoCharlas(id,tema,presencialidad,titulo,fecha,idempresa,aprobada)
    db.session.add(eventoCharla)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'

def show(empresa_id):
    return 'show'

def update(empresa_id):
    return 'update'

def delete(empresa_id):
    return 'delete'

def all():
    eventoCharlas = EventoCharlas.query.all()
    return render_template('charlas.html',eventoCharlas=eventoCharlas)
