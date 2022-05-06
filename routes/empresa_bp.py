from flask import Blueprint
from controllers.EmpresaController import index, login, userProfile, logout, storeAdmin, show, updateAdmin,all

from modules.moduleRegistro.moduleRegistro import moduleRegistro, store, store2, confirmUser, resetpassword, setnewpassword_get, setnewpassword_post, editEmpresa
from modules.moduleLogin.moduleLogin import moduleLogin, loginForm

"""
    Blueprints para Empresa
"""

empresa_bp = Blueprint('empresa_bp', __name__)
empresa_bp.register_blueprint(moduleRegistro)
empresa_bp.register_blueprint(moduleLogin)
#empresa_bp.route('/', methods=['GET'])(index)

# Login de Empresa
#empresa_bp.route('/login', methods=['GET','POST'])(login)
empresa_bp.route('/login', methods=['GET','POST'])(loginForm)

# Mostrar pefil de Empresa actual
empresa_bp.route('/user_profile/<int:editable>', methods=['GET','POST'])(userProfile)
# Logout de Empresa
empresa_bp.route('/logout', methods=['GET'])(logout)
# Crear Empresa
empresa_bp.route('/crear', methods=['GET','POST'])(store2)
empresa_bp.route('/crearAdmin', methods=['GET','POST'])(storeAdmin)
# Actualizar Empresa
empresa_bp.route('/update', methods=['GET','POST'])(editEmpresa)
empresa_bp.route('/updateAdmin', methods=['GET','POST'])(updateAdmin)
# Mostrar perfil de Empresa
empresa_bp.route('/<nombre>', methods=['GET','POST'])(show)
#empresa_bp.route('/<int:empresa_id>/update', methods=['POST'])(update)
#empresa_bp.route('/<int:empresa_id>', methods=['DELETE'])(delete)
# Mostrar todas las Empresas
empresa_bp.route('/all', methods=['GET'])(all)
#Confirmar usuario
empresa_bp.route('/confirmuser/<username>/<userhash>', methods=['GET','POST'])(confirmUser)
#Cambiar contraseña
empresa_bp.route('/resetpassword', methods=['GET','POST'])(resetpassword)
empresa_bp.route('/setnewpassword/<username>/<userhash>', methods=['GET'])(setnewpassword_get)
empresa_bp.route('/setnewpassword', methods=['POST'])(setnewpassword_post)
