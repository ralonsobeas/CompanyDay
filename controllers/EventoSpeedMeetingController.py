import sys

from flask import render_template, redirect, url_for, request, abort
from models.EventoSpeedMeeting import EventoSpeedMeeting
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import base64

db = SQLAlchemy()


def index():
    return 'index'

def store():


    return 'Su informacion ha sido guardada en nuestra base de datos'

def show(empresa_id):
    return 'show'

def update(empresa_id):
    return 'update'

def delete(empresa_id):
    return 'delete'

def all():
    return render_template('charlas.html',eventoCharlas=eventoCharlas)
