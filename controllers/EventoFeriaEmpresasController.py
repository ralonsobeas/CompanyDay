import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_required

db = SQLAlchemy()


def index():
    return 'index'

"""
    Guardar EventoCharla en BBDD
"""
def store(eventoFeriaEmpresas):
    db.session.add(eventoFeriaEmpresas)
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        if re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, id repetido (%s)" % eventoFeriaEmpresas.id

            """
        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"
            """
        else:
            return False, str(error)

    return True, "";


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
