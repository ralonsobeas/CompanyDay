import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

db = SQLAlchemy()


def index():
    return 'index'

def store():
    id = request.form['id']
    fecha = request.form['fecha']
    presencial = True if(request.form['presencial']=='True') else False

    eventoFeriaEmpresas = EventoFeriaEmpresas(id,fecha,presencial)
    db.session.add(eventoFeriaEmpresas)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'

def show(eventoFeriaEmpresas_id):
    eventoFeriaEmpresas = EventoFeriaEmpresas.query.get(eventoFeriaEmpresasa_id)
    return render_template('eventoFeriaEmpresas.html',
                            eventoFeriaEmpresas=eventoFeriaEmpresas)

def update(eventoFeriaEmpresas_id):
    return 'update'

def delete(eventoFeriaEmpresas_id):
    return 'delete'

def all():
    eventoFeriaEmpresas = EventoFeriaEmpresas.query.all()
    return render_template('eventosFeriaEmpresas.html',eventoFeriaEmpresas=eventoFeriaEmpresas)
