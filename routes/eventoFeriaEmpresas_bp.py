from flask import Blueprint
from controllers.EventoFeriaEmpresasController import index, store, show, update, delete,all

eventoFeriaEmpresas_bp = Blueprint('eventoFeriaEmpresas_bp', __name__)

eventoFeriaEmpresas_bp.route('/', methods=['GET'])(index)
eventoFeriaEmpresas_bp.route('/crear', methods=['GET','POST'])(store)
eventoFeriaEmpresas_bp.route('/<int:eventoFeriaEmpresas_id>', methods=['GET','POST'])(show)
eventoFeriaEmpresas_bp.route('/<int:eventoFeriaEmpresas_id>/editar', methods=['POST'])(update)
eventoFeriaEmpresas_bp.route('/<int:eventoFeriaEmpresas_id>/delete', methods=['DELETE'])(delete)
eventoFeriaEmpresas_bp.route('/all', methods=['GET'])(all)
