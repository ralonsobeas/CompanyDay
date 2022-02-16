# CompanyDay
 InicioCompanyDay
 
 Instalación
 - Base de datos
   - Crear BBDD MySQL, no hay que crear ninguna tabla
   - En el fichero config.py cambiar esto: SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USUARIO:PASSWORD@localhost/NOMBREBBDD'
   - El servidor se encarga solo de crear las tablas necesarias
 - Python
   - Instalar los paquetes necesarios como por ejemplo 
     - SQLAlchemy: pip install -U Flask-SQLAlchemy
     - PyMySQL: pip install PyMySQL
     - Migrate: pip install Flask-Migrate
     - Puede que haya más

Funcionamiento
- Página principal
- Pestaña registro empresa para crear una empresa
- Para ver una empresa con su id utilizar la url http://localhost:3001/empresas/IDEMPRESA
- Para ver todas las empresas utilizar la url http://localhost:3001/empresas/all


Cosas temporales

- Para poder ver una empresa ya creada /empresas/(id)
- Para poder ver todas las empresas creadas /empresas/all
