from flask import Blueprint
from test import tests, testBBDD
from modules.moduleRegistro.moduleRegistro import moduleRegistro,moduleRegistro_test
from modules.moduleLogin.moduleLogin import moduleLogin,moduleLogin_test

test_bp = Blueprint('test_bp', __name__)
test_bp.register_blueprint(moduleRegistro)
test_bp.register_blueprint(moduleLogin)

# Test main
test_bp.route('/', methods=['GET'])(tests)

# Test BBDD
test_bp.route('/testBBDD', methods=['GET'])(testBBDD)

# Test registro
test_bp.route('/moduleRegistro', methods=['GET'])(moduleRegistro_test)

# Test login
test_bp.route('/moduleLogin', methods=['GET'])(moduleLogin_test)
