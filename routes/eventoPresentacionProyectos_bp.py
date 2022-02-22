from flask import Blueprint
from controllers.EventoPresentacionProyectosController import index, store, show, update, delete, all

eventoPresentacionProyectos_bp = Blueprint('eventoPresentacionProyectos_bp', __name__)

eventoPresentacionProyectos_bp.route('/', methods=['GET'])(index)
eventoPresentacionProyectos_bp.route('/crear', methods=['GET','POST'])(store)
eventoPresentacionProyectos_bp.route('/<int:presentacion_id>', methods=['GET','POST'])(show)
eventoPresentacionProyectos_bp.route('/<int:presentacion>/editar', methods=['POST'])(update)
eventoPresentacionProyectos_bp.route('/<int:presentacion_id>/borrar', methods=['DELETE'])(delete)
eventoPresentacionProyectos_bp.route('/all', methods=['GET'])(all)
