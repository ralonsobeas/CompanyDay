import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

db = SQLAlchemy()


def index():
    return 'index'

"""
    Guardar EventoFeriaEmpresas
"""
def store():
    db.session.add(eventoFeriaEmpresas)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'

"""
    Mostrar EventoFeriaEmpresas. Renderiza en eventoFeriaEmpresas.html
"""
def show(eventoFeriaEmpresas_id):
    eventoFeriaEmpresas = EventoFeriaEmpresas.query.get(eventoFeriaEmpresasa_id)
    return render_template('eventoFeriaEmpresas.html',
                            eventoFeriaEmpresas=eventoFeriaEmpresas)


def update(eventoFeriaEmpresas_id):
    return 'update'

def delete(eventoFeriaEmpresas_id):
    return 'delete'

"""
    Mostrar todos los EventoFeriaEmpresas. Renderiza en eventosFeriaEmpresas.html
"""
def all():
    eventoFeriaEmpresas = EventoFeriaEmpresas.query.all()
    return render_template('eventosFeriaEmpresas.html',eventoFeriaEmpresas=eventoFeriaEmpresas)

"""
    Buscar todos los EventoFeriaEmpresas
"""
def all_query():
    return EventoFeriaEmpresas.query.all()

"""
    Obtener EventoFeriaEmpresas por id de empresa.
"""
def get_by_empresa_id_all(empresa_id):
    eventoFeriaEmpresas = EventoFeriaEmpresas.query.filter_by(empresa_id=empresa_id).all()
    return eventoFeriaEmpresas
