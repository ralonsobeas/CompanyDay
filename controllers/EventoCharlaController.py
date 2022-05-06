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

def store(eventoCharla):
    db.session.add(eventoCharla)
    db.session.commit()

"""
    Guardar EventoCharla en BBDD
"""
@login_required
def storeTemp():
    tema = request.form['tema']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    titulo = request.form['titulo']
    fecha = request.form['fecha']
    autor = request.form['autor']
    empresa_id = current_user.id
    aprobada = False

    eventoCharla = EventoCharlas(tema,presencialidad,titulo,fecha,aprobada,autor,empresa_id)
    db.session.add(eventoCharla)
    db.session.commit()

    return redirect(url_for('empresa_bp.userProfile',editable=0))

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
    .add_columns(EventoCharlas.tema, EventoCharlas.presencialidad, EventoCharlas.titulo, EventoCharlas.fecha, EventoCharlas.autor, Empresa.logo, Empresa.nombre)\
    .filter(Empresa.validado == True)\
    .filter(EventoCharlas.aprobada == True)
    return listaCharlasAprobadas;

"""
    Validar para Admin
"""

def validar(id,valor):
    charla = EventoCharlas.query.filter_by(id=id).first()
    charla.aprobada = valor
    db.session.commit()

"""
    Obtener EventoCharlas por id de empresa.
"""
def get_by_empresa_id_all(empresa_id):
    eventoCharlas = EventoCharlas.query.filter_by(empresa_id=empresa_id).all()
    return eventoCharlas
