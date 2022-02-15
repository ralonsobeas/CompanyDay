from urllib import request
from flask import Flask, render_template, url_for, request
from flask_mysqldb import MySQL
import urllib
import urllib.request

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'prueba'
mysql = MySQL(app)

#Tabla SQL
#create table empresa (nombre VARCHAR(50) NOT NULL, descripcion VARCHAR(500), fechaInicio DATE, fechaFinal DATE, correo VARCHAR(100), telefono VARCHAR(15), ubicacion VARCHAR(100));

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add contact', methods=['POST'])
def addContact():
    nombreEmpresa = request.form['nombreEmpresa']
    descripcion = request.form['descripcion']
    fechaInicio = request.form['fechaInicio']
    fechaFinal = request.form['fechaFinal']
    correo = request.form['correo']
    telefono = request.form['telefono']
    ubicacion = request.form['ubicacion']
    cur = mysql.connection.cursor()
    sqlQuery = "INSERT INTO empresa (nombre, descripcion, fechaInicio, fechaFinal, correo, telefono, ubicacion) VALUES ('" + nombreEmpresa + "', '" + descripcion + "', '"\
        + fechaInicio + "', '" + fechaFinal + "', '"+ correo + "', '" + telefono + "', '" + ubicacion + "')"
    print(sqlQuery)
    cur.execute(sqlQuery)
    mysql.connection.commit()

    return 'Su informacion ha sido guardada en nuestra base de datos'
        

app.run(port = 3000, debug=True)