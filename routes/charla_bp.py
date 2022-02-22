from flask import Blueprint
from controllers.CharlaController import index, store, show, update, delete,all

charla_bp = Blueprint('charla_bp', __name__)

charla_bp.route('/', methods=['GET'])(index)
charla_bp.route('/crear', methods=['GET','POST'])(store)
charla_bp.route('/<int:empresa_id>', methods=['GET','POST'])(show)
charla_bp.route('/<int:empresa_id>/editar', methods=['POST'])(update)
charla_bp.route('/<int:empresa_id>/delete', methods=['DELETE'])(delete)
charla_bp.route('/all', methods=['GET'])(all)
