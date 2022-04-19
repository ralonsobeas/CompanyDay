from flask import Blueprint
from controllers.EventoPresentacionProyectosController import index, store, show, update, delete, all

"""
    Blueprints para EventoPresentacionProyectos
"""

eventoPresentacionProyectos_bp = Blueprint('eventoPresentacionProyectos_bp', __name__)

eventoPresentacionProyectos_bp.route('/', methods=['GET'])(index)
# Crear EventoPresentacionProyectos
eventoPresentacionProyectos_bp.route('/crear', methods=['GET','POST'])(store)
# Mostrar EventoPresentacionProyectos
eventoPresentacionProyectos_bp.route('/<int:presentacion_id>', methods=['GET','POST'])(show)
# Actualizar EventoPresentacionProyectos
eventoPresentacionProyectos_bp.route('/<int:presentacion>/editar', methods=['POST'])(update)
# Borrar EventoPresentacionProyectos
eventoPresentacionProyectos_bp.route('/<int:presentacion_id>/borrar', methods=['DELETE'])(delete)
# Mostrar todos EventoPresentacionProyectos
eventoPresentacionProyectos_bp.route('/all', methods=['GET'])(all)
