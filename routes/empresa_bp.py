from flask import Blueprint
from controllers.EmpresaController import index, login, userProfile, logout, store, show, update,all

"""
    Blueprints para Empresa
"""

empresa_bp = Blueprint('empresa_bp', __name__)

#empresa_bp.route('/', methods=['GET'])(index)

# Login de Empresa
empresa_bp.route('/login', methods=['GET','POST'])(login)
# Mostrar pefil de Empresa actual
empresa_bp.route('/user_profile/<int:editable>', methods=['GET','POST'])(userProfile)
# Logout de Empresa
empresa_bp.route('/logout', methods=['GET'])(logout)
# Crear Empresa
empresa_bp.route('/crear', methods=['GET','POST'])(store)
# Actualizar Empresa
empresa_bp.route('/update', methods=['GET','POST'])(update)
# Mostrar perfil de Empresa
empresa_bp.route('/<nombre>', methods=['GET','POST'])(show)
#empresa_bp.route('/<int:empresa_id>/update', methods=['POST'])(update)
#empresa_bp.route('/<int:empresa_id>', methods=['DELETE'])(delete)
# Mostrar todas las Empresas
empresa_bp.route('/all', methods=['GET'])(all)
