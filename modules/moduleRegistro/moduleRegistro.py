from flask import render_template, redirect, url_for, request, abort, flash, Flask, current_app, Blueprint
from config import UPLOAD_FOLDER_LINUX,UPLOAD_FOLDER_WINDOWS

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash

from os.path import join, dirname, realpath
import platform

from flask_mail import Mail, Message
from threading import Thread

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

from modules.moduleRegistro.forms import ResetPasswordForm, SetNewPasswordForm, EmpresaRegisterForm, PersonaRegisterForm,\
EventoSpeedMeetingRegisterForm, EventoCharlasRegisterForm, EventoFeriaEmpresasRegisterForm, EditEmpresaForm


import random

moduleRegistro = Blueprint("moduleRegistro", __name__,static_folder="static",template_folder="templates")

"""
    Guardar empresa en BBDD
"""
def store():
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

    EmpresaController.store(empresa)

    tema = request.form['tema']
    presencialidad = True if(request.form['presencialidad']=='True') else False
    titulo = request.form['titulo']
    fecha = request.form['fecha']
    aprobada = False
    autor = ''

    eventoCharla = EventoCharlas(tema = tema,presencialidad = presencialidad,titulo = titulo,fecha = fecha,aprobada = aprobada, empresa_id = id, autor = autor)

    EventoCharlaController.store(eventoCharla)

    presencial = True if(request.form['presencialidad']=='True') else False
    dia = request.form['dia']
    horaInicio = request.form['horaInicio']
    horaFin = request.form['horaFin']
    perfiles = request.form['perfiles']
    pregunta = request.form['pregunta']
    aprobado = False
    eventoSpeedMeeting=EventoSpeedMeeting(presencialidad = presencial, fecha = dia, horaInicio = horaInicio, horaFin = horaFin, perfiles = perfiles, pregunta = pregunta, aprobada = aprobado, empresa_id = id)



    EventoSpeedMeetingController.store(eventoSpeedMeeting)
    # Mandar mail
    #send_email(email,'Bienvenido al Company Day en U-Tad', 'templateMail',url=url)
    send_email("companydayprueba@gmail.com",'Bienvenido al Company Day en U-Tad', 'templateMail',url=url)
    flash('Te has registrado! Revista tu email para confirmar tu cuenta.')

    return  redirect(url_for('index'))

"""
    Guardar empresa en BBDD con WTForm
"""
def store2():
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

    empresa = Empresa(id=id,validado=False,nombre=nombre,password=password, method='sha256', \
                        personaContacto=personaContacto,email=email,telefono=telefono,direccion=direccion, \
                        poblacion=poblacion,provincia=provincia,codigoPostal=codigoPostal,pais=pais,urlWeb=urlWeb,logo=logoFileName, \
                        consentimientoNombre=consentimientoNombre,buscaCandidatos=buscaCandidatos,admin=False,userHash=userHash)

    aniadido, msg = EmpresaController.store(empresa)
    if not aniadido:
        flash(msg)
        return redirect(url_for('index'))

    #Añadir personas
    formPersona1 = PersonaRegisterForm()
    saveFormPersona(formPersona1,empresa.id)

    formPersona2 = PersonaRegisterForm()
    saveFormPersona(formPersona2,empresa.id)

    formPersona3 = PersonaRegisterForm()
    saveFormPersona(formPersona3,empresa.id)

    formPersona4 = PersonaRegisterForm()
    saveFormPersona(formPersona4,empresa.id)

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
    #send_email(email,'Bienvenido al Company Day en U-Tad', 'templateMail',url=url)
    send_email("companydayprueba@gmail.com",'Bienvenido al Company Day en U-Tad', 'mail/templateMail',url=url)
    flash('Te has registrado! Revista tu email para confirmar tu cuenta.')

    return  redirect(url_for('index'))

"""
    Guardar formulario persona
"""
def saveFormPersona(formPersona,id):
    if formPersona.nombre.data != '':
        nombre = formPersona.nombre.data
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
        try:
            EmpresaController.confirmar(username)
            flash('Has confirmado el usuario!')
            #Mandar mail a admin
            send_email("companydayprueba@gmail.com",'Se ha registrado un nuevo usuario al CompanyDay', 'mail/templateMail',nombre=username)
        except:
            abort(500, description="An error has occurred.")

    return  redirect(url_for('index'))


from flask import current_app

"""
    Enviar mail
"""
def send_email(to, subject, template, url, **kwargs):
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
    msg.html = render_template(template + '.html', **kwargs, url=url)
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
                    #send_email(form.email.data,'Confirmar cambio de contraseña.', 'templateMail',url=url)
                    send_email("companydayprueba@gmail.com",'Confirmar cambio de contraseña.', 'mail/templateMailContrasenia',url=url)
                    EmpresaController.store(empresa)

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
            EmpresaController.store(empresa)
            flash('Contraseña cambiada.')
            return  redirect(url_for('index'))

    return render_template("setnewpassword.html", form=form)

def editEmpresa():
    formEdit = EditEmpresaForm()
    id = formEdit.id.data
    empresa = EmpresaController.get_by_id(id)
    nombre = formEdit.nombre.data
    telefono = formEdit.telefono.data
    direccion = formEdit.direccion.data
    poblacion = formEdit.poblacion.data
    provincia = formEdit.provincia.data
    codigoPostal = formEdit.codigoPostal.data
    pais = formEdit.pais.data
    urlWeb = formEdit.urlWeb.data
    consentimientoNombre = True
    buscaCandidatos = True

    logo = formEdit.logo.data
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
    EmpresaController.update(empresa.nombre, nombre, telefono, direccion, poblacion, provincia, codigoPostal, pais, urlWeb, consentimientoNombre, buscaCandidatos, logoFileName)
    return redirect(url_for('empresa_bp.show',nombre=nombre))
    
    

def moduleRegistro_test():
    return 'OK'
