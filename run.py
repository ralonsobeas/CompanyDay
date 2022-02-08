from urllib import request
from flask import Flask, render_template, url_for, request
from flaskext.mysql import MySQL
import urllib
import urllib.request

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'prueba'
mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add contact', methods=['POST'])
def addContact():
    nombreEmpresa = request.form['nombreEmpresa']

    cur = mysql.get_db().cursor()

    cur.execute("INSERT INTO empresa VALUES ('" + nombreEmpresa + "');")
    #mysql.connection.commit()
    mysql.get_db().commit()

    return 'received'


app.run(port = 3000, debug=True)