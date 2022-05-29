from flask import render_template, redirect, url_for, request, abort, flash, Flask, current_app, Blueprint
from config import UPLOAD_FOLDER_LINUX,UPLOAD_FOLDER_WINDOWS

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash

from os.path import join, dirname, realpath
import platform

from flask_mail import Mail, Message
from threading import Thread

from flask_login import login_required, current_user

from models.Empresa import Empresa
from models.EventoCharlas import EventoCharlas
from models.EventoFeriaEmpresas import EventoFeriaEmpresas
from models.EventoPresentacionProyectos import EventoPresentacionProyectos
from models.EventoSpeedMeeting import EventoSpeedMeeting
from models.Persona import Persona


from controllers import EmpresaController
from controllers import EventoCharlaController
from controllers import EventoFeriaEmpresasController
from controllers import EventoPresentacionProyectosController
from controllers import EventoSpeedMeetingController
from controllers import PersonaController

from modules.moduleRegistro.forms import ResetPasswordForm, SetNewPasswordForm, EmpresaRegisterForm\
, PersonaRegisterForm, PersonaRegisterForm1, PersonaRegisterForm2, PersonaRegisterForm3, EventoSpeedMeetingRegisterForm, EventoCharlasRegisterForm, EventoFeriaEmpresasRegisterForm, EditEmpresaForm


import random

moduleRegistro = Blueprint("moduleRegistro", __name__,static_folder="static",template_folder="templates")


"""
    Guardar empresa en BBDD con WTForm
"""
def store():
    formEmpresa = EmpresaRegisterForm()

    id = formEmpresa.cif.data
    nombre = formEmpresa.nombre.data
    password = generate_password_hash(formEmpresa.password.data)
    personaContacto = formEmpresa.personaContacto.data
    email = formEmpresa.email.data
    telefono = formEmpresa.telefono.data
    direccion = formEmpresa.direccion.data
    poblacion = formEmpresa.poblacion.data
    provincia = formEmpresa.provincia.data
    codigoPostal = formEmpresa.codigoPostal.data
    pais = formEmpresa.pais.data
    urlWeb = formEmpresa.urlWeb.data
    consentimientoNombre = True
    buscaCandidatos = True

    logo = formEmpresa.logo.data
    logoFileName = str(id) + ".png";

    # Cambiar barras dependiendo del sistema operativo
    if(platform.system()=='Windows'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_WINDOWS)
        UPLOADS_PATH = UPLOADS_PATH.replace("modules\\moduleRegistro", "")
        logo.save(UPLOADS_PATH+"\\"+logoFileName)
    elif(platform.system()=='Linux'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_LINUX)
        UPLOADS_PATH = UPLOADS_PATH.replace("modules/moduleRegistro/", "")
        logo.save(UPLOADS_PATH+"/"+logoFileName)


    #Proceso validación usuario
    userHash = ''.join(random.choice('AILNOQVBCDEFGHJKMPRSTUXZabcdefghijklmnopqrstuvxz1234567890') for i in range(50))
    url = 'http://{}/empresas/confirmuser/{}/{}'.format(request.host,nombre,userHash)

    empresa = Empresa(id=id,validado=False,nombre=nombre,password=password, \
                        personaContacto=personaContacto,email=email,telefono=telefono,direccion=direccion, \
                        poblacion=poblacion,provincia=provincia,codigoPostal=codigoPostal,pais=pais,urlWeb=urlWeb,logo=logoFileName, \
                        consentimientoNombre=consentimientoNombre,buscaCandidatos=buscaCandidatos,admin=False,userHash=userHash)

    aniadido, msg = EmpresaController.store(empresa)
    if not aniadido:
        flash(msg)
        return redirect(url_for('index'))

    #Añadir personas
    formPersona1 = PersonaRegisterForm()
    #saveFormPersona(formPersona1,empresa.id)
    if formPersona1.nombrePersona.data != '':
        nombre = formPersona1.nombrePersona.data
        puesto = formPersona1.puesto.data
        comentario = formPersona1.comentario.data

        persona = Persona(nombre=nombre,puesto=puesto,comentario=comentario,empresa_id=id)

        PersonaController.store(persona)

    formPersona2 = PersonaRegisterForm1()
    #saveFormPersona(formPersona2,empresa.id)
    if formPersona2.nombrePersona1.data != '':
        nombre = formPersona2.nombrePersona1.data
        puesto = formPersona2.puesto1.data
        comentario = formPersona2.comentario1.data

        persona = Persona(nombre=nombre,puesto=puesto,comentario=comentario,empresa_id=id)

        PersonaController.store(persona)


    formPersona3 = PersonaRegisterForm2()
    #saveFormPersona(formPersona3,empresa.id)
    if formPersona3.nombrePersona2.data != '':
        nombre = formPersona3.nombrePersona2.data
        puesto = formPersona3.puesto2.data
        comentario = formPersona3.comentario2.data

        persona = Persona(nombre=nombre,puesto=puesto,comentario=comentario,empresa_id=id)

        PersonaController.store(persona)


    formPersona4 = PersonaRegisterForm3()
    #saveFormPersona(formPersona4,empresa.id)
    if formPersona4.nombrePersona3.data != '':
        nombre = formPersona4.nombrePersona3.data
        puesto = formPersona4.puesto3.data
        comentario = formPersona4.comentario3.data

        persona = Persona(nombre=nombre,puesto=puesto,comentario=comentario,empresa_id=id)

        PersonaController.store(persona)

    #Añadir eventos
    formEventoSpeedMeeting = EventoSpeedMeetingRegisterForm()
    if formEventoSpeedMeeting.pregunta.data != '':
        presencialidad = formEventoSpeedMeeting.presencialidad.data
        fecha = formEventoSpeedMeeting.fecha.data
        horaInicio = formEventoSpeedMeeting.horaInicio.data
        horaFin = formEventoSpeedMeeting.horaFin.data
        perfiles = formEventoSpeedMeeting.perfiles.data
        pregunta = formEventoSpeedMeeting.pregunta.data

        eventoSpeedMeeting = EventoSpeedMeeting(presencialidad=presencialidad,fecha=fecha,\
        horaInicio=horaInicio,horaFin=horaFin,perfiles=perfiles,pregunta=pregunta,empresa_id=empresa.id)

        EventoSpeedMeetingController.store(eventoSpeedMeeting)

    formEventoCharlas = EventoCharlasRegisterForm()
    if formEventoCharlas.tema.data != '':
        tema = formEventoCharlas.tema.data
        presencialidad = formEventoCharlas.presencialidad.data
        titulo = formEventoSpeedMeeting.titulo.data
        fecha = formEventoSpeedMeeting.fecha.data
        autor = formEventoSpeedMeeting.autor.data


        eventoCharlas = EventoCharlas(tema=tema,presencialidad=presencialidad,titulo=titulo,\
        fecha=fecha,autor=autor,empresa_id=empresa.id)

        EventoCharlaController.store(eventoCharlas)

    formEventoFeriaEmpresas = EventoFeriaEmpresasRegisterForm()
    if formEventoFeriaEmpresas.fecha.data != None:
        fecha = fformEventoFeriaEmpresas.fecha.data
        presencialidad = formEventoCharlas.presencialidad.data

        eventoFeriaEmpresas = EventoFeriaEmpresas(fecha=fecha,presencialidad=presencialidad,empresa_id=empresa.id)

        EventoFeriaEmpresasController.store(eventoCharlas)
    #formEventoPresentacionProyectos = EventoPresentacionProyectosRegisterForm()

    # Mandar mail
    send_email(email,'Bienvenido al Company Day en U-Tad', 'mail/templateMail',url=url)
    #send_email("companydayprueba@gmail.com",'Bienvenido al Company Day en U-Tad', 'mail/templateMail',url=url)
    flash('Te has registrado! Revista tu email para confirmar tu cuenta.')

    return  redirect(url_for('index'))

"""
    Guardar formulario persona
"""
def saveFormPersona(formPersona,id):
    if formPersona.nombrePersona.data != '':
        nombre = formPersona.nombrePersona.data
        puesto = formPersona.puesto.data
        comentario = formPersona.comentario.data

        persona = Persona(nombre=nombre,puesto=puesto,comentario=comentario,empresa_id=id)

        PersonaController.store(persona)

"""
    Confirmar usuario
"""
def confirmUser(username,userhash):
    empresa=EmpresaController.get_by_name(username)

    if not empresa:
        abort(403, description="Invalid url.")
    elif len(empresa.userHash) == 0 or empresa.userHash != userhash:
        abort(403, description="Invalid url.")
    else:
        confirmado, msg = EmpresaController.confirmar(empresa)
        if not confirmado:
            flash(msg)
        flash('Has confirmado el usuario!')
        #Mandar mail a admin
        send_email("companydayprueba@gmail.com",'Se ha registrado un nuevo usuario al CompanyDay', 'mail/templateMailAdmin',nombre=username)

    return  redirect(url_for('index'))


from flask import current_app

"""
    Enviar mail
"""
def send_email(to, subject, template, **kwargs):
    app = Flask(__name__)

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'companydayprueba@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ghcjtlcchwhjbuyw'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail = Mail(current_app)
    app.config.from_object('config')
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    #msg.body = render_template(template + '.txt', **kwargs, url=url)
    msg.html = render_template(template + '.html', **kwargs)
    # flash("send_email: {}".format(url))
    mail.send(msg)

"""
    Resetear password mandar mail
"""
def resetpassword():
    form =  ResetPasswordForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            empresa = EmpresaController.get_by_email(form.email.data)
            if empresa:
                    empresa.userHash = ''.join(random.choice('AILNOQVBCDEFGHJKMPRSTUXZabcdefghijklmnopqrstuvxz1234567890') for i in range(50))
                    url = 'http://{}/empresas/setnewpassword/{}/{}'.format(request.host,empresa.nombre,empresa.userHash)
                    send_email(form.email.data,'Confirmar cambio de contraseña.', 'mail/templateMailContrasenia',url=url)
                    #send_email("companydayprueba@gmail.com",'Confirmar cambio de contraseña.', 'mail/templateMailContrasenia',url=url)

                    actualizado, msg = EmpresaController.update(empresa)
                    if not actualizado:
                        flash(msg)

            flash('Se ha enviado un mensaje al correo electrónico si existe')
    return render_template("resetpassword.html", form=form)

"""
    Set password
"""
def setnewpassword_get(username,userhash):
    form = SetNewPasswordForm()
    empresa = EmpresaController.get_by_name(username)
    if not empresa:
        flash('Url inválida.')
    elif len(empresa.userHash)==0 or empresa.userHash != userhash:
        flash('Url inválida.')
    else:
        form.username.data = username
        form.userhash.data = userhash
    return render_template("setnewpassword.html", form=form)


def setnewpassword_post():
    form = SetNewPasswordForm()
    if form.validate_on_submit():
        empresa = EmpresaController.get_by_name(form.username.data)
        if not empresa:
            flash('Url inválida.')
            return  redirect(url_for('index'))
        elif len(empresa.userHash)==0 or empresa.userHash != form.userhash.data:
            flash('Url inválida.')
            return  redirect(url_for('index'))
        else:
            empresa.userHash = ''
            empresa.password = generate_password_hash(form.password.data)
            empresa.confirmed = 1
            actualizado, msg = EmpresaController.update(empresa)
            if not actualizado:
                flash(msg)
            flash('Contraseña cambiada.')
            return  redirect(url_for('index'))

    return render_template("setnewpassword.html", form=form)

"""
    Editar empresa desde perfil
"""


@login_required
def editEmpresa():
    formEdit = EditEmpresaForm()
    id = formEdit.id.data
    empresa = EmpresaController.get_by_id(id)
    empresa.nombre = formEdit.nombre.data
    empresa.personaContacto =  formEdit.personaContacto.data
    empresa.telefono = formEdit.telefono.data
    empresa.direccion = formEdit.direccion.data
    empresa.poblacion = formEdit.poblacion.data
    empresa.provincia = formEdit.provincia.data
    empresa.codigoPostal = formEdit.codigoPostal.data
    empresa.pais = formEdit.pais.data
    empresa.urlWeb = formEdit.urlWeb.data
    empresa.consentimientoNombre = True
    empresa.buscaCandidatos = True

    if(formEdit.logo.data != None):
        logo = formEdit.logo.data
        empresa.logoFileName = str(id) + ".png";

    # Cambiar barras dependiendo del sistema operativo
        if(platform.system()=='Windows'):
            UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_WINDOWS)
            UPLOADS_PATH = UPLOADS_PATH.replace("modules\\moduleRegistro", "")
            logo.save(UPLOADS_PATH+"\\"+empresa.logoFileName)
        elif(platform.system()=='Linux'):
            UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_LINUX)
            UPLOADS_PATH = UPLOADS_PATH.replace("modules/moduleRegistro/", "")
            logo.save(UPLOADS_PATH+"/"+empresa.logoFileName)

    aniadido, msg = EmpresaController.update(empresa)
    if not aniadido:
        flash(msg)

    return redirect(url_for("empresa_bp.userProfile",editable=0))

"""
    Guardar evento charla
"""

@login_required
def storeCharla():
    formEventoCharlas = EventoCharlasRegisterForm()
    if formEventoCharlas.tema.data != '':
        tema = formEventoCharlas.tema.data
        presencialidad = formEventoCharlas.presencialidad.data
        titulo = formEventoCharlas.titulo.data
        fecha = formEventoCharlas.fecha.data
        autor = formEventoCharlas.autor.data
        eventoCharlas = EventoCharlas(tema=tema,presencialidad=presencialidad,titulo=titulo,\
        fecha=fecha,autor=autor,empresa_id=current_user.id)
        EventoCharlaController.store(eventoCharlas)
    return redirect(url_for("empresa_bp.userProfile",editable=0))

"""
    Guardar evento speedmeeting
"""

@login_required
def storeSpeedMeeting():
    formEventoSpeedMeeting = EventoSpeedMeetingRegisterForm()
    if formEventoSpeedMeeting.pregunta.data != '':
        presencialidad = formEventoSpeedMeeting.presencialidad.data
        fecha = formEventoSpeedMeeting.fecha.data
        horaInicio = formEventoSpeedMeeting.horaInicio.data
        horaFin = formEventoSpeedMeeting.horaFin.data
        perfiles = formEventoSpeedMeeting.perfiles.data
        pregunta = formEventoSpeedMeeting.pregunta.data
        eventoSpeedMeeting = EventoSpeedMeeting(presencialidad=presencialidad,fecha=fecha,\
        horaInicio=horaInicio,horaFin=horaFin,perfiles=perfiles,pregunta=pregunta,empresa_id=current_user.id)
        EventoSpeedMeetingController.store(eventoSpeedMeeting)
    return redirect(url_for("empresa_bp.userProfile",editable=0))

"""
    Guardar empresa en BBDD ADMIN
"""
@login_required
def storeAdmin():
    id = request.form['CIF']
    nombre = request.form['nombreEmpresa']
    password = request.form['password']
    personaContacto = request.form['personaContacto']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    poblacion = request.form['poblacion']
    provincia = request.form['provincia']
    codigoPostal = request.form['codigoPostal']
    pais = request.form['pais']
    urlWeb = request.form['urlWeb']
    consentimientoNombre = True
    buscaCandidatos = True

    logo = request.files['logo']
    logoFileName = id + ".png";

    if(platform.system()=='Windows'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_WINDOWS)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers\\", "")
        logo.save(UPLOADS_PATH+"\\"+logoFileName)
    elif(platform.system()=='Linux'):
        UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER_LINUX)
        UPLOADS_PATH = UPLOADS_PATH.replace("controllers/", "")
        logo.save(UPLOADS_PATH+"/"+logoFileName)

    empresa = Empresa(id=id,validado=False,nombre=nombre,password=generate_password_hash(password, method='sha256'), \
                        personaContacto=personaContacto,email=email,telefono=telefono,direccion=direccion, \
                        poblacion=poblacion,provincia=provincia,codigoPostal=codigoPostal,pais=pais,urlWeb=urlWeb,logo=logoFileName, \
                        consentimientoNombre=consentimientoNombre,buscaCandidatos=buscaCandidatos,admin=False)

    aniadido, msg = EmpresaController.store(empresa)
    if not aniadido:
        flash(msg)


    return redirect('../admin/empresa')


"""
    Actualizar usuario de empresa Admin.
"""
@login_required
def updateAdmin():
    if request.form['consentimientoNombre'] == 'True':
        consentimientoNombre = True;
    else:
        consentimientoNombre = False;
    if request.form['buscaCandidatos'] == 'True':
        buscaCandidatos = True;
    else:
        buscaCandidatos = False;

    empresa = Empresa.get_by_id(request.form['CIF'])

    empresa.nombre = request.form['nombreEmpresa']
    empresa.personaContacto = request.form['personaContacto']
    emresa.email = request.form['email']
    empresa.telefono = request.form['telefono']
    empresa.direccion = request.form['direccion']
    empresa.poblacion = request.form['poblacion']
    empresa.provincia = request.form['provincia']
    empresa.codigoPostal = request.form['codigoPostal']
    empresa.pais = request.form['pais']
    empresa.urlWeb = request.form['urlWeb']
    empresa.consentimientoNombre = consentimientoNombre
    empresa.buscaCandidatos = buscaCandidatos
    #empresa.logoFileName = logoFileName

    aniadido, msg = EmpresaController.update(empresa)
    if not aniadido:
        flash(msg)

    return redirect('../admin/empresa')

def generatePass():
    print(generate_password_hash("admin", method='sha256'))

from test import debug_only
@debug_only
def moduleRegistro_test():
    return 'OK'
