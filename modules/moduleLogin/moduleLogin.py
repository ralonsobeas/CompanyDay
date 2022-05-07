from flask import Blueprint, render_template, flash, redirect, url_for
from modules.moduleRegistro.forms import EditEmpresaForm, EventoCharlasRegisterForm, EventoSpeedMeetingRegisterForm
from modules.moduleLogin.forms import LoginForm
from flask_login import login_user,login_required,current_user,logout_user
from shared.models import login_manager
from werkzeug.security import  check_password_hash
from controllers import EmpresaController, EventoCharlaController, EventoFeriaEmpresasController, EventoPresentacionProyectosController \
,EventoSpeedMeetingController, PersonaController

moduleLogin = Blueprint("moduleLogin", __name__,static_folder="static",template_folder="templates")

"""
    Login de empresa

    Recibe mail y password, busca el usuario y compara el password.
    Si es correcto redirige al perfil.
"""
def loginForm():
    form = LoginForm()

    email = form.email.data
    password = form.password.data
    remember = form.remember.data

    empresa = EmpresaController.get_by_email(email)

    if not empresa or not check_password_hash(empresa.password,password):
        flash('Usuario incorrecto.')
        return  redirect(url_for('index'))

    login_user(empresa,remember=remember)

    return  redirect(url_for('empresa_bp.userProfile', editable=0))

"""
    Login manager para flask_login
"""
@login_manager.user_loader
def loginManager(id):
    return EmpresaController.get_by_id(id)

"""
    Logout
"""
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



"""
    Mostrar perfil. Si editable 1, editable.
"""
def show(nombre,editable=0):
    empresa = EmpresaController.get_by_name(nombre)

    if empresa is None:
        flash("No existe la empresa"+empresa.nombre)
        return redirect(url_for('empresa_bp.all'))

    formEdit = EditEmpresaForm(data=empresa.as_dict())
    formEventoCharlas = EventoCharlasRegisterForm()
    formEventoSpeedMeeting = EventoSpeedMeetingRegisterForm()

    if(editable==1):
        editable=True
    else:
        editable=False

    empresa = EmpresaController.get_by_name(nombre)
    if not empresa or empresa.admin==True:
        return abort(404)
    eventosFeriaEmpresa = EventoFeriaEmpresasController.get_by_empresa_id_all(empresa.id)
    eventosPresentacionProyectos = EventoPresentacionProyectosController.get_by_empresa_id_all(empresa.id)
    eventosSpeedMeeting = EventoSpeedMeetingController.get_by_empresa_id_all(empresa.id)
    eventosCharla = EventoCharlaController.get_by_empresa_id_all(empresa.id)
    return render_template('empresa.html', formEdit=formEdit, \
                            formEventoCharlas=formEventoCharlas, formEventoSpeedMeeting=formEventoSpeedMeeting,
                            empresa=empresa,eventosFeriaEmpresa=eventosFeriaEmpresa, \
                            eventosPresentacionProyectos=eventosPresentacionProyectos, \
                            eventosSpeedMeeting=eventosSpeedMeeting,eventosCharla=eventosCharla,editable=editable)

"""
    Mostrar perfil del usuario actual.
"""
@login_required
def userProfile(editable=0):
    if(current_user.admin == 0):
        return show(current_user.nombre,editable)
    return redirect('/admin')

from test import debug_only
@debug_only
def moduleLogin_test():
    return 'OK'
