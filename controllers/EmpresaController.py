import sys

from flask import render_template, redirect, url_for, request, abort, flash, Flask, current_app
from models.Empresa import Empresa
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from models.EventoPresentacionProyectos import EventoPresentacionProyectos
from models.EventoSpeedMeeting import EventoSpeedMeeting
from models.EventoCharlas import EventoCharlas
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_required
import os
from os.path import join, dirname, realpath
import platform
from config import UPLOAD_FOLDER_LINUX,UPLOAD_FOLDER_WINDOWS

from flask_mail import Mail, Message
from threading import Thread

import base64

import random
import re

db = SQLAlchemy()

"""
    Store
"""
def store(empresa):
    db.session.add(empresa)

    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        if re.match("(.*)Duplicate entry(.*)for key 'nombre'", error.args[0]):
            return False, "Error, nombre repetido (%s)" % empresa.nombre
        elif re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, cif repetido (%s)" % empresa.id
        elif re.match("(.*)Duplicate entry(.*)for key 'email'", error.args[0]):
            return False, "Error, mail repetido (%s)" % empresa.mail
            """
        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"
            """
        else:
            return False, str(error)

    return True, "";

"""
    Actualizar usuario de empresa.
"""
@login_required
def update(empresa):

    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        if re.match("(.*)Duplicate entry(.*)for key 'nombre'", error.args[0]):
            return False, "Error, nombre repetido"
        elif re.match("(.*)Duplicate entry(.*)for key 'PRIMARY'", error.args[0]):
            return False, "Error, cif repetido"
        elif re.match("(.*)Duplicate entry(.*)for key 'email'", error.args[0]):
            return False, "Error, mail repetido"
            """
        elif "FOREIGN KEY constraint failed" in str(error):
            return False, "supplier does not exist"
            """
        else:
            return False, str(error)

    return True, "";


"""
    Obtener empresa por id.
"""
def get_by_id(id):
    empresa = db.session.query(Empresa).filter(Empresa.id==id).first()
    return empresa

"""
    Obtener empresa por nombre.
"""
def get_by_name(nombre):
    empresa =   db.session.query(Empresa).filter(Empresa.nombre==nombre).first()
    return empresa

"""
    Obtener empresa por nombre.
"""
def get_by_email(email):
    empresa =  db.session.query(Empresa).filter(Empresa.email==email).first()
    return empresa

"""
    Obtener todas las empresas validadas. Renderizar en html.
"""
def all():
    empresas = Empresa.query.filter_by(validado=True).all()
    return render_template('empresas.html',empresas=empresas)

"""
    Obtener todas las empresas.
"""
def all_query():
    return Empresa.query.filter_by(validado=True).all()

"""
    Validar empresa.
"""
def validar(id,valor):
    empresa = Empresa.query.filter_by(id=id).first()
    empresa.validado = valor
    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        return False, "Error al actualizar"

    return True, "";

"""
    Confirmar empresa.
"""
def confirmar(nombre):

    empresa= db.session.query(Empresa).filter_by(nombre=nombre).first()

    empresa.confirmed = 1
    empresa.userHash = ''

    try:
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()
        return False, "Error al actualizar"

    return True, "";
