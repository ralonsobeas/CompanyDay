from flask import Blueprint
from controllers.EmpresaController import index, login, userProfile, logout, store, show, update, delete,all

empresa_bp = Blueprint('empresa_bp', __name__)

#empresa_bp.route('/', methods=['GET'])(index)
empresa_bp.route('/login', methods=['GET','POST'])(login)
empresa_bp.route('/user_profile/<int:editable>', methods=['GET','POST'])(userProfile)
empresa_bp.route('/logout', methods=['GET'])(logout)
empresa_bp.route('/crear', methods=['GET','POST'])(store)
empresa_bp.route('/<nombre>', methods=['GET','POST'])(show)
#empresa_bp.route('/<int:empresa_id>/update', methods=['POST'])(update)
#empresa_bp.route('/<int:empresa_id>', methods=['DELETE'])(delete)
empresa_bp.route('/all', methods=['GET'])(all)
