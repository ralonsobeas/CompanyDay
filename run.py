from flask import Flask, render_template, request, send_from_directory

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from shared.models import db,login_manager

from flask_babelex import Babel
from flask_bootstrap import Bootstrap
import urllib
from urllib import request

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



#SQLAlchemy
app.config.from_object('config')
#db = SQLAlchemy(app)

# INIT DB
db.init_app(app)
migrate = Migrate(app, db)
# He cambiado esto para lanzar bien migracion $env:FLASK_APP = "run.py"
# Para migración se lanza en consola "flask db init" inicialmente. Para actualizar version "flask db migrate"
# Para actualizar BBDD "flask db upgrade". Para bajar de versión "flask db downgrade"

# REGISTER BLUEPRINTS
from routes.empresa_bp import empresa_bp
from routes.eventoFeriaEmpresas_bp import eventoFeriaEmpresas_bp
from routes.eventoPresentacionProyectos_bp import eventoPresentacionProyectos_bp
from routes.eventoCharla_bp import eventoCharla_bp
from routes.eventoSpeedMeeting_bp import eventoSpeedMeeting_bp

app.register_blueprint(empresa_bp, url_prefix='/empresas')
app.register_blueprint(eventoFeriaEmpresas_bp, url_prefix='/eventoFeriaEmpresas')
app.register_blueprint(eventoPresentacionProyectos_bp, url_prefix='/proyectos')
app.register_blueprint(eventoCharla_bp, url_prefix='/charlas')
app.register_blueprint(eventoSpeedMeeting_bp, url_prefix='/speedMeeting')


from controllers import EmpresaController
from controllers import EventoCharlaController
from controllers import EventoPresentacionProyectosController
from controllers import EventoFeriaEmpresasController
from controllers import PersonaController
from controllers import EventoSpeedMeetingController




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



@app.route('/actividades')
def actividades():
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


# Errores routing
from errors import *

#Modo admin
from admin import *

# Start app
if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(port = 3001, debug=True)
