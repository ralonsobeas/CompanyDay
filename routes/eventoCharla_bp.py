from flask import Blueprint
from controllers.EventoCharlaController import index, store, show, update, delete,all

"""
    Blueprints para EventoCharla
"""

eventoCharla_bp = Blueprint('eventoCharla_bp', __name__)

eventoCharla_bp.route('/', methods=['GET'])(index)
# Guardar EventoCharla
eventoCharla_bp.route('/crear', methods=['GET','POST'])(store)
# Mostrar EventoCharla
eventoCharla_bp.route('/<int:empresa_id>', methods=['GET','POST'])(show)
# Actualizar EventoCharla
eventoCharla_bp.route('/<int:empresa_id>/editar', methods=['POST'])(update)
# Borrar EventoCharla
eventoCharla_bp.route('/<int:empresa_id>/delete', methods=['DELETE'])(delete)
# Mostrar todos EventoCharlas
eventoCharla_bp.route('/all', methods=['GET'])(all)
