from urllib import request
from flask import Flask, render_template, url_for, request, send_from_directory
#from flaskext.mysql import MySQL

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from shared.models import db

import urllib
import urllib.request

import os

from routes.empresa_bp import empresa_bp
from routes.presentacionProyectos_bp import presentacionProyectos_bp

app = Flask(__name__)

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
app.register_blueprint(presentacionProyectos_bp, url_prefix='/proyectos')

from models import Empresa
from models.Empresa import Empresa

@app.route('/')
def index():
    empresas = Empresa.query.all()
    return render_template('index.html',empresas=empresas)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images/favicon'), 'favicon.ico')

@app.route('/add_contact', methods=['POST'])
def addContact():
    nombreEmpresa = request.form['nombreEmpresa']

    cur = mysql.get_db().cursor()

    #Cuidado con las consultas Manoel quiere que usemos un ORM
    cur.execute("INSERT INTO empresa VALUES ('" + nombreEmpresa + "');")
    #mysql.connection.commit()
    mysql.get_db().commit()

    return 'received'

@app.route('/registro_empresa')
def registroEmpresa():

    # show the form, it wasn't submitted
    return render_template('registroEmpresa.html')

@app.route('/registro_presentacion')
def registroPresentacion():
    return render_template('registroPresentaciones.html')

@app.route('/contacto')
def contacto():

    # show the form, it wasn't submitted
    return render_template('contacto.html')

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(port = 3001, debug=True)
