import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoSpeedMeeting import EventoSpeedMeeting
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_required,current_user
import base64

db = SQLAlchemy()


def index():
    return 'index'

"""
    Guardar EventoSpeedMeetingController
"""
@login_required
def store_new(eventoSpeedMeeting):
    db.session.add(eventoSpeedMeeting)
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        """
        if re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, id repetido (%s)" % eventoSpeedMeeting.id

        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"

        else:
            return False, str(error)
        """


@login_required
def store():
    pregunta = request.form['pregunta']
    perfiles = request.form['perfiles']
    fecha = request.form['fecha']
    horaInicio = request.form['horaInicio']
    horaFin = request.form['horaFin']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    empresa_id = current_user.id

    eventoSpeedMeeting = EventoSpeedMeeting(presencialidad,fecha,horaInicio,horaFin,perfiles,pregunta,empresa_id)
    store_new(eventoSpeedMeeting)

    return redirect(url_for('empresa_bp.userProfile',editable=0))


def show(empresa_id):
    return 'show'

def update(empresa_id):
    return 'update'

def delete(empresa_id):
    return 'delete'

"""
    Mostrar todos los EventoSpeedMeeting. Renderizar en registroSpeedMetting.html
"""
def all():
    eventoSpeedMeeting = EventoSpeedMeeting.query.all()
    return render_template('registroSpeedMeeting.html',eventoSpeedMeeting=eventoSpeedMeeting)

"""
    Buscar todos los EventoSpeedMeeting.
"""
def all_query():
    listaSpeedMeetingsAprobadas = EventoSpeedMeeting.query\
    .join(Empresa, EventoSpeedMeeting.empresa_id == Empresa.id)\
    .add_columns(EventoSpeedMeeting.presencialidad, EventoSpeedMeeting.fecha, EventoSpeedMeeting.horaInicio, EventoSpeedMeeting.horaFin, EventoSpeedMeeting.perfiles, EventoSpeedMeeting.pregunta, Empresa.logo, Empresa.nombre)\
    .filter(Empresa.validado == True)\
    .filter(EventoSpeedMeeting.aprobada == True)
    return listaCharlasAprobadas;

"""
    Validar para Admin
"""
@login_required
def validar(id,valor):
    speedmeeting = EventoSpeedMeeting.query.filter_by(id=id).first()
    speedmeeting.aprobada = valor
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        return False, "Error al actualizar"

    return True, "";

"""
    Obtener EventoSpeedMeeting por id de empresa.
"""
def get_by_empresa_id_all(empresa_id):
    eventoSpeedMeeting = EventoSpeedMeeting.query.filter_by(empresa_id=empresa_id).all()
    return eventoSpeedMeeting
