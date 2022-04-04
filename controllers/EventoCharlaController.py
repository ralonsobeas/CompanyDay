import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoCharlas import EventoCharlas
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_required,current_user
import base64

db = SQLAlchemy()


def index():
    return 'index'

@login_required
def store():
    tema = request.form['tema']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    titulo = request.form['titulo']
    fecha = request.form['fecha']
    empresa_id = current_user.id
    aprobada = False

    eventoCharla = EventoCharlas(tema,presencialidad,titulo,fecha,aprobada,empresa_id)
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
    return render_template('registroCharlas.html',eventoCharlas=eventoCharlas)
    
def all_query():
    listaCharlasAprobadas = EventoCharlas.query\
    .join(Empresa, EventoCharlas.empresa_id == Empresa.id)\
    .add_columns(EventoCharlas.tema, EventoCharlas.presencialidad, EventoCharlas.titulo, EventoCharlas.fecha, Empresa.logo, Empresa.nombre)\
    .filter(Empresa.validado == True)\
    .filter(EventoCharlas.aprobada == True)
    return listaCharlasAprobadas;
