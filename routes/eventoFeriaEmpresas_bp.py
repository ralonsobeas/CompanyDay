from flask import Blueprint
from controllers.EventoFeriaEmpresasController import index, store, show, update, delete,all

"""
    Blueprints para EventoFeriaEmpresasController
"""


eventoFeriaEmpresas_bp = Blueprint('eventoFeriaEmpresas_bp', __name__)

#eventoFeriaEmpresas_bp.route('/', methods=['GET'])(index)
# Guardar EventoFeriaEmpresas
eventoFeriaEmpresas_bp.route('/crear', methods=['GET','POST'])(store)
# Mostrar EventoFeriaEmpresas
#eventoFeriaEmpresas_bp.route('/<int:eventoFeriaEmpresas_id>', methods=['GET','POST'])(show)
# Actualizar EventoFeriaEmpresas
eventoFeriaEmpresas_bp.route('/<int:eventoFeriaEmpresas_id>/editar', methods=['POST'])(update)
# Borrar EventoFeriaEmpresas
eventoFeriaEmpresas_bp.route('/<int:eventoFeriaEmpresas_id>/delete', methods=['DELETE'])(delete)
# Mostrar todos los EventoFeriaEmpresas
#eventoFeriaEmpresas_bp.route('/all', methods=['GET'])(all)
