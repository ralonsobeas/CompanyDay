from flask import Blueprint
from controllers.EmpresaController import index, store, show, update, delete,all

empresa_bp = Blueprint('empresa_bp', __name__)

empresa_bp.route('/', methods=['GET'])(index)
empresa_bp.route('/crear', methods=['GET','POST'])(store)
empresa_bp.route('/<int:empresa_id>', methods=['GET','POST'])(show)
empresa_bp.route('/<int:empresa_id>/editar', methods=['POST'])(update)
empresa_bp.route('/<int:empresa_id>', methods=['DELETE'])(delete)
empresa_bp.route('/all', methods=['GET'])(all)
