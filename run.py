from urllib import request
from flask import Flask, render_template, url_for, request, send_from_directory,redirect, abort
#from flaskext.mysql import MySQL

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from shared.models import db,login_manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

import urllib
import urllib.request

import os

app = Flask(__name__)


login_manager.init_app(app)
#   admin = Admin(app)

from routes.empresa_bp import empresa_bp
from routes.eventoFeriaEmpresas_bp import eventoFeriaEmpresas_bp
from routes.eventoPresentacionProyectos_bp import eventoPresentacionProyectos_bp
from routes.eventoCharla_bp import eventoCharla_bp
from routes.eventoSpeedMeeting_bp import eventoSpeedMeeting_bp


"""
MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'prueba'
mysql = MySQL()
mysql.init_app(app)
"""

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

from models import Empresa
from models.Empresa import Empresa

from models import EventoFeriaEmpresas
from models.EventoFeriaEmpresas import EventoFeriaEmpresas

from models import EventoPresentacionProyectos
from models.EventoPresentacionProyectos import EventoPresentacionProyectos

from models import EventoCharlas
from models.EventoCharlas import EventoCharlas

from models import EventoSpeedMeeting
from models.EventoSpeedMeeting import EventoSpeedMeeting




class AdminView(ModelView):
    ModelView.can_export = True
    ModelView.column_exclude_list = ('password','logo','render_logo')
    ModelView.column_export_exclude_list = ('password','logo','render_logo')
    def is_accessible(self):
        if not current_user.is_authenticated:
            print("AUT "+ str(current_user.is_authenticated))
            return abort(404, description="Sin permisos")
        return current_user.admin

    def _handle_view(self, name, **kwargs):
        if not current_user.is_authenticated:
            return render_template("admin/denied.html")
        if not self.is_accessible:
            return render_template("admin/denied.html")

admin=Admin(app, name='Administrador',url="/admin", template_mode='bootstrap4')

admin.add_view(AdminView(Empresa,db.session))
admin.add_view(AdminView(EventoFeriaEmpresas,db.session))
admin.add_view(AdminView(EventoPresentacionProyectos,db.session))
admin.add_view(AdminView(EventoCharlas,db.session))
admin.add_view(AdminView(EventoSpeedMeeting,db.session))


@app.route('/')
def index():
    empresas = Empresa.query.filter_by(admin=False).all()
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

@app.route('/registro_presentacion')
def registroPresentacion():
    return render_template('registroPresentaciones.html')

@app.route('/registro_charla')
def registroCharla():
    return render_template('charlas.html')

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
  return render_template('admin/denied.html'), 404
app.register_error_handler(404, page_not_found)


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(port = 3001, debug=True)
