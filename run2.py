from urllib import request
from flask import Flask, render_template, url_for, request, send_from_directory,redirect, abort, flash, jsonify
#from flaskext.mysql import MySQL

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from shared.models import db,login_manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_login import current_user, login_required

from flask_babelex import Babel

import urllib
import urllib.request

import os

app = Flask(__name__)
babel = Babel(app)
@babel.localeselector
def get_locale():
        # Put your logic here. Application can store locale in
        # user profile, cookie, session, etc.
        return 'es'

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

db.init_app(app)
migrate = Migrate(app, db)
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


class AdminView(ModelView):
    ModelView.can_export = True
    ModelView.column_exclude_list = ('password')
    ModelView.column_export_exclude_list = ('password')
    ModelView.export_types = ['csv','xls']
    ModelView.column_hide_backrefs = False
    ModelView.column_display_pk = True
    def scaffold_sortable_columns(self):
        return {'Empresa':'empresa_id'}
    def is_accessible(self):
        if not current_user.is_authenticated or not current_user.admin:
            return abort(404, description="Sin permisos")

        return current_user.admin

    def _handle_view(self, name, **kwargs):
        if not current_user.is_authenticated:
            return render_template("admin/denied.html")
        if not self.is_accessible:
            return render_template("admin/denied.html")
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

admin=Admin(app, name='Administrador',url="/admin", template_mode='bootstrap4')

admin.add_view(AdminView(Empresa,db.session))
admin.add_view(AdminView(EventoFeriaEmpresas,db.session))
admin.add_view(AdminView(EventoPresentacionProyectos,db.session))
admin.add_view(AdminView(EventoCharlas,db.session))
admin.add_view(AdminView(EventoSpeedMeeting,db.session))


@app.route('/')
def index():
    empresas = EmpresaController.all_query()
    return render_template('index.html',empresas=empresas)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images/favicon'), 'favicon.ico')


@app.route('/login_empresa')
def loginEmpresa():

    # show the form, it wasn't submitted
    return render_template('login.html')

@app.route('/registro_empresa')
def registroEmpresa():

    # show the form, it wasn't submitted
    return render_template('registroEmpresa.html')

@login_required
@app.route('/registro_presentacion')
def registroPresentacion():
    eventosPresentacionProyectos = EventoPresentacionProyectos.query.filter_by().all()
    return render_template('registroPresentaciones.html', eventosPresentacionProyectos = eventosPresentacionProyectos)

@app.route('/proyecto')
def proyectos():
    proyectos = EventoPresentacionProyectosController.all_query()
    print(type(proyectos))
    return render_template('proyectos.html',proyectos=proyectos)

@login_required
@app.route('/registro_charla')
def registroCharla():
    eventosCharla = EventoCharlas.query.filter_by().all()
    return render_template('registroCharlas.html', eventosCharla = eventosCharla)

@app.route('/charla')
def charlas():
    charlas = EventoCharlaController.all_query()
    return render_template('charlas.html',charlas=charlas)

@app.route('/registro_prueba')
def registroFinal():
    return render_template("registroPrueba.html")

@app.route('/calendar')
def calendar():
    eventos = EventoFeriaEmpresasController.all_query()
    return render_template('calendar.html',eventos=eventos)

@app.route('/contacto')
def contacto():

    # show the form, it wasn't submitted
    return render_template('contacto.html')

@app.route('/pruebajs')
def pruebajs():
    empresas = Empresa.query.all()
    return render_template('prueba.html',empresas=empresas)

@app.route('/chulo')
def chulo():
    empresas = Empresa.query.all()
    return render_template('chulo.html',empresas=empresas)

def page_not_found(e):
  return render_template('admin/denied.html',message="Page not found",e=e), 404
app.register_error_handler(404, page_not_found)
def not_registered(e):
  return render_template('admin/denied.html',message="Not registered",e=e), 400
app.register_error_handler(400, not_registered)

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


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(port = 3001, debug=True)