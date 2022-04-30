from urllib import request
from flask import Flask, render_template, url_for, request, send_from_directory,redirect, abort, flash, jsonify
#from flaskext.mysql import MySQL

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from shared.models import db,login_manager
from flask_admin import Admin
from flask_admin.base import expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_login import current_user, login_required

from flask_babelex import Babel
from flask_bootstrap import Bootstrap
import urllib
import urllib.request

import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
# LANGUAGE
"""
babel = Babel(app)
@babel.localeselector
def get_locale():
        # Put your logic here. Application can store locale in
        # user profile, cookie, session, etc.
        #return 'es'

    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code
"""
# LOGIN
login_manager.init_app(app)
#   admin = Admin(app)

from routes.empresa_bp import empresa_bp
from routes.eventoFeriaEmpresas_bp import eventoFeriaEmpresas_bp
from routes.eventoPresentacionProyectos_bp import eventoPresentacionProyectos_bp
from routes.eventoCharla_bp import eventoCharla_bp
from routes.eventoSpeedMeeting_bp import eventoSpeedMeeting_bp


#SQLAlchemy
app.config.from_object('config')
#db = SQLAlchemy(app)

# INIT DB
db.init_app(app)
migrate = Migrate(app, db)

# REGISTER BLUEPRINTS
app.register_blueprint(empresa_bp, url_prefix='/empresas')
app.register_blueprint(eventoFeriaEmpresas_bp, url_prefix='/eventoFeriaEmpresas')
app.register_blueprint(eventoPresentacionProyectos_bp, url_prefix='/proyectos')
app.register_blueprint(eventoCharla_bp, url_prefix='/charlas')
app.register_blueprint(eventoSpeedMeeting_bp, url_prefix='/speedMeeting')

from models import EventoFeriaEmpresas
from models.EventoFeriaEmpresas import EventoFeriaEmpresas

from models import EventoPresentacionProyectos
from models.EventoPresentacionProyectos import EventoPresentacionProyectos

from models import EventoCharlas
from models.EventoCharlas import EventoCharlas

from models import EventoSpeedMeeting
from models.EventoSpeedMeeting import EventoSpeedMeeting

from models import Empresa
from models.Empresa import Empresa

from models import Persona
from models.Persona import Persona

from controllers import EmpresaController
from controllers import EventoCharlaController
from controllers import EventoPresentacionProyectosController
from controllers import EventoFeriaEmpresasController
from controllers import PersonaController
from controllers import EventoSpeedMeetingController


# MODO ADMINISTRADOR
class SecureView(ModelView):
    def is_accessible(self):
        if not current_user.is_authenticated or not current_user.admin:
            return abort(404, description="Sin permisos")
        # only accessible if admin field is True
        if current_user.is_authenticated and not current_user.is_anonymous:
            return current_user.admin

        return False
    def _handle_view(self, name, **kwargs):
        if not current_user.is_authenticated:
            return abort(404, description="Sin permisos")
        if not self.is_accessible:
            return abort(404, description="Sin permisos")

class GeneralView(SecureView):
    can_export = True
    column_exclude_list = ('password')
    column_export_exclude_list = ('password')
    export_types = ['csv','xls']
    column_hide_backrefs = False
    column_display_pk = True

    def cambio_id_nombre(view, context, model, name):
        if model.empresa_id is None:
            return 'None'
        return EmpresaController.get_by_id(model.empresa_id).nombre


class EmpresaView(GeneralView):
    column_exclude_list = ['userHash']
    column_searchable_list = ['nombre', 'email']
    column_sortable_list = ['validado','confirmed','admin']
    column_list = ['validado', 'confirmed', 'nombre', 'email', 'Personacontacto', 'Telefono', 'Direccion', 'Poblacion', 'Provincia', 'CodigoPostal', 'Pais', 'Consentimientonombre', 'Buscacandidatos','Admin']
    @action('validar', 'Validar', '¿Seguro de que quieres validar las empresas seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EmpresaController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} Empresa (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las empresas seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EmpresaController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} Empresa (s) invalidada (s)".format(count))
    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        """Custom create view."""
        return self.render('registroEmpresa.html',edit=0)
    @expose('/edit/', methods=('GET', 'POST'))
    def create_view(self):
        """Custom create view."""
        return self.render('registroEmpresa.html',edit=1,EmpresaController=EmpresaController)

Empresa_View = EmpresaView(Empresa,db.session)


class EventoFeriaEmpresasView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'fecha', 'presencial']
    column_sortable_list = ['empresa_id', 'fecha']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }

EventoFeriaEmpresas_View = EventoFeriaEmpresasView(EventoFeriaEmpresas,db.session)


class EventoPresentacionProyectosView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'validado', 'presencial','videojuegos','disenoDigital','cortosAnimacion','ingenieria']
    column_sortable_list = ['empresa_id', 'validado', 'presencial','videojuegos','disenoDigital','cortosAnimacion','ingenieria']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }
    @action('validar', 'Validar', '¿Seguro de que quieres validar las presentaciones seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoPresentacionProyectosController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} Presentacion (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las presentaciones seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoPresentacionProyectosController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} Presentacion (s) invalidada (s)".format(count))

EventoPresentacionProyectos_View = EventoPresentacionProyectosView(EventoPresentacionProyectos,db.session)


class EventoCharlasView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'aprobada', 'fecha','titulo','tema','autor','presencialidad']
    column_sortable_list = ['empresa_id', 'fecha','aprobada']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }
    @action('validar', 'Validar', '¿Seguro de que quieres validar las charlas seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoCharlaController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} Charla (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las charlas seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoCharlaController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} Charla (s) invalidada (s)".format(count))

EventoCharlas_View = EventoCharlasView(EventoCharlas,db.session)


class EventoSpeedMeetingView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'aprobada', 'fecha','pregunta','perfiles','horaInicio','horaFin']
    column_sortable_list = ['empresa_id', 'fecha','aprobada','horaInicio','horaFin']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }
    @action('validar', 'Validar', '¿Seguro de que quieres validar las speedmeetings seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoSpeedMeetingController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} SpeedMeeting (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las speedmeetings seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoSpeedMeetingController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} SpeedMeeting (s) invalidada (s)".format(count))

EventoSpeedMeeting_View = EventoSpeedMeetingView(EventoSpeedMeeting,db.session)


class PersonaView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id','nombre', 'puesto','comentario']
    column_sortable_list = ['empresa_id','nombre']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }

Persona_View = PersonaView(Persona,db.session)


admin=Admin(app, name='Administrador',url="/admin", template_mode='bootstrap4')
admin.add_view(Empresa_View)
admin.add_view(EventoFeriaEmpresas_View)
admin.add_view(EventoPresentacionProyectos_View)
admin.add_view(EventoCharlas_View)
admin.add_view(EventoSpeedMeeting_View)
admin.add_view(Persona_View)

# FIN MODO ADMINISTRADOR

from modules.moduleRegistro.forms import EmpresaRegisterForm, EventoCharlasRegisterForm,\
 EventoFeriaEmpresasRegisterForm, EventoPresentacionProyectosRegisterForm,\
 EventoSpeedMeetingRegisterForm, PersonaRegisterForm
# ROUTING
@app.route('/')
def index():
    empresas = EmpresaController.all_query()
    formEmpresa = EmpresaRegisterForm()
    formPersona1 = PersonaRegisterForm()
    formPersona2 = PersonaRegisterForm()
    formPersona3 = PersonaRegisterForm()
    formPersona4 = PersonaRegisterForm()
    formEventoCharlas = EventoCharlasRegisterForm()
    formEventoFeriaEmpresas = EventoFeriaEmpresasRegisterForm()
    formEventoPresentacionProyectos = EventoPresentacionProyectosRegisterForm()
    formEventoSpeedMeeting = EventoSpeedMeetingRegisterForm()

    return render_template('index3.html',empresas=empresas,formEmpresa=formEmpresa,\
    formPersona1=formPersona1,formPersona2=formPersona2,formPersona3=formPersona3,\
    formPersona4=formPersona4,formEventoCharlas=formEventoCharlas,\
    formEventoFeriaEmpresas=formEventoFeriaEmpresas,formEventoPresentacionProyectos=formEventoPresentacionProyectos,\
    formEventoSpeedMeeting=formEventoSpeedMeeting)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images/favicon'), 'favicon.ico')



@app.route('/proyecto')
def proyectos():
    proyectos = EventoPresentacionProyectosController.all_query()
    charlas = EventoCharlaController.all_query()
    return render_template('proyectos.html',proyectos=proyectos,charlas=charlas)


from modules.moduleLogin.forms import LoginForm
"""
    Crear variable global en jinja2 con el login form
"""
@app.context_processor
def login():
    loginForm = LoginForm()
    return dict(loginForm=loginForm)



# FINAL ROUTING

# ERRORES ROUTING

def page_not_found(e):
  return render_template('admin/denied.html',message="Page not found",e=e), 404
app.register_error_handler(404, page_not_found)
def not_registered(e):
  return render_template('admin/denied.html',message="Not registered",e=e), 400
app.register_error_handler(400, not_registered)
def invalid_url(e):
  return render_template('admin/denied.html',message="Invalid url",e=e), 403
app.register_error_handler(403, invalid_url)

# FINAL ERRORES ROUTING

"""
from flask_table import Col, Table

class ItemTableEmpresas(Table):
    password = Col('password')
    personaContacto  = Col('personaContacto')
    email = Col('email')
    telefono = Col('telefono')
    direccion = Col('direccion')
    poblacion = Col('poblacion')
    provincia = Col('provincia')
    codigoPostal = Col('codigoPostal')
    pais = Col('pais')
    urlWeb = Col('urlWeb')
    logo = Col('logo')
    consentimientoNombre = Col('consentimientoNombre')
    buscaCandidatos = Col('buscaCandidatos')

    admin = Col('admin')

class ItemTableProyectos(Table):
    validado = Col('validado')
    id = Col('id')
    presencial = Col('presencial')
    videojuegos = Col('videojuegos')
    disenoDigital = Col('disenoDigital')
    cortosAnimacion = Col('cortosAnimacion')
    ingenieria = Col('ingenieria')

@app.route('/pruebaTabla')
def method_name():
    empresas = EmpresaController.all_query()
    print(type(empresas))
    print(empresas)
    items = ItemTableEmpresas(empresas)
    return render_template("pruebaTablas.html", empresas = items)
    """



# START APP
if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(port = 3001, debug=True)
