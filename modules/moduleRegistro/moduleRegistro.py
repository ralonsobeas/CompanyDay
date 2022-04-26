from flask import render_template, redirect, url_for, request, abort, flash, Flask, current_app
from config import UPLOAD_FOLDER_LINUX,UPLOAD_FOLDER_WINDOWS

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash

from os.path import join, dirname, realpath
import platform

from flask_mail import Mail, Message
from threading import Thread

from models.Empresa import Empresa
from models.EventoCharlas import EventoCharlas
from models.EventoSpeedMeeting import EventoSpeedMeeting as SpeedMeeting


from controllers import EmpresaController
from controllers import EventoCharlaController
from controllers import EventoSpeedMeetingController


import random
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

    empresa = Empresa(id=id,validado=False,nombre=nombre,password=generate_password_hash(password, method='sha256'), \
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

    SpeedMeeting(presencialidad = presencial, fecha = dia, horaInicio = horaInicio, horaFin = horaFin, perfiles = perfiles, pregunta = pregunta, aprobada = aprobado, empresa_id = id)

    EventoSpeedMeetingController.store(eventoSpeedMeeting)
    # Mandar mail
    #send_email(email,'Bienvenido al Company Day en U-Tad', 'templateMail',url=url)
    send_email("companydayprueba@gmail.com",'Bienvenido al Company Day en U-Tad', 'templateMail',url=url)
    flash('Te has registrado! Revista tu email para confirmar tu cuenta.')

    #with app.app_context():
     #   msg = Message('Bienvenido al Company Day en U-Tad', sender =  'companydayprueba@gmail.com', recipients = ['companydayprueba@gmail.com'])
        #msg.html = render_template('templateMail.html')
      #  mail.send(msg)

    return render_template('index3.html')

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
        except:
            abort(500, description="An error has occurred.")

    return render_template('index3.html')


"""
    Mail asíncrono
"""
def async_send_mail(app, msg, mail):
    with app.app_context():
        mail.send(msg)

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
    #thr = Thread(target=async_send_mail, args=[current_app, msg, mail])
    #thr.start()
