import os

LANGUAGES = ['es', 'en']

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key
SECRET_KEY = "hardsecretkey"

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://companyday:companyday@localhost/companyday'

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

#Carpeta para guardar imágenes
UPLOAD_FOLDER_WINDOWS = 'static\\images\\customlogos'
UPLOAD_FOLDER_LINUX = 'static/images/customlogos'
