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

@login_required
def store():
    pregunta = request.form['pregunta']
    perfiles = request.form['perfiles']
    fecha = request.form['fecha']
    horaInicio = request.form['horaInicio']
    horaFin = request.form['horaFin']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    empresa_id = current_user.id
    aprobada = False

    eventoSpeedMeeting = EventoSpeedMeeting(presencialidad,fecha,horaInicio,horaFin,perfiles,pregunta,aprobada,empresa_id)
    db.session.add(eventoSpeedMeeting)
    db.session.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'

def show(empresa_id):
    return 'show'

def update(empresa_id):
    return 'update'

def delete(empresa_id):
    return 'delete'

def all():
    eventoSpeedMeeting = EventoSpeedMeeting.query.all()
    return render_template('registroSpeedMeeting.html',eventoSpeedMeeting=eventoSpeedMeeting)
    
def all_query():
    listaSpeedMeetingsAprobadas = EventoSpeedMeeting.query\
    .join(Empresa, EventoSpeedMeeting.empresa_id == Empresa.id)\
    .add_columns(EventoSpeedMeeting.presencialidad, EventoSpeedMeeting.fecha, EventoSpeedMeeting.horaInicio, EventoSpeedMeeting.horaFin, EventoSpeedMeeting.perfiles, EventoSpeedMeeting.pregunta, Empresa.logo, Empresa.nombre)\
    .filter(Empresa.validado == True)\
    .filter(EventoSpeedMeeting.aprobada == True)
    return listaCharlasAprobadas;
