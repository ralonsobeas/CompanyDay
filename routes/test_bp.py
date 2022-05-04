from flask import Blueprint

from modules.moduleRegistro.moduleRegistro import moduleRegistro,moduleRegistro_test
from modules.moduleLogin.moduleLogin import moduleLogin,moduleLogin_test

test_bp = Blueprint('test_bp', __name__)
test_bp.register_blueprint(moduleRegistro)
test_bp.register_blueprint(moduleLogin)

# Test registro
test_bp.route('/testRegistro', methods=['GET'])(moduleRegistro_test)

# Test login
test_bp.route('/testLogin', methods=['GET'])(moduleLogin_test)
