from flask import Blueprint
from controllers.EventoCharlaController import index, store, show, update, delete,all

eventoCharla_bp = Blueprint('eventoCharla_bp', __name__)

eventoCharla_bp.route('/', methods=['GET'])(index)
eventoCharla_bp.route('/crear', methods=['GET','POST'])(store)
eventoCharla_bp.route('/<int:empresa_id>', methods=['GET','POST'])(show)
eventoCharla_bp.route('/<int:empresa_id>/editar', methods=['POST'])(update)
eventoCharla_bp.route('/<int:empresa_id>/delete', methods=['DELETE'])(delete)
eventoCharla_bp.route('/all', methods=['GET'])(all)
