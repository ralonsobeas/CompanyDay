import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoSpeedMeeting import EventoSpeedMeeting
from models.Empresa import Empresa
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_login import login_required,current_user
import base64

from shared.models import db


def index():
    return 'index'

"""
    Guardar EventoSpeedMeetingController
"""
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


def store(eventoSpeedMeeting):
    db.session.add(eventoSpeedMeeting)
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        if re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, id repetido (%s)" % eventoSpeedMeeting.id

            """
        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"
            """
        else:
            return False, str(error)

    return True, "";

def show(empresa_id):
    return 'show'

def update(empresa_id):
    return 'update'

@login_required
def delete(eventoSpeedMeeting_id):
    current_speedMeeting = EventoSpeedMeeting.query.filter_by(id=eventoSpeedMeeting_id).first()
    if current_user.id == current_speedMeeting.empresa_id:
        db.session.delete(EventoSpeedMeeting.query.filter_by(id=eventoSpeedMeeting_id).first())
        db.session.commit()
    return redirect("/empresas/user_profile/0")

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
    eventoSpeedMeeting = ' '
    try:
        eventoSpeedMeeting = EventoSpeedMeeting.query.filter_by(empresa_id=empresa_id).all()
    except:
        db.session.rollback()
    return eventoSpeedMeeting
