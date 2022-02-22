from flask import Blueprint
from controllers.PresentacionProyectosController import index, store, show, update, delete, all

presentacionProyectos_bp = Blueprint('presentacionProyectos_bp', __name__)

presentacionProyectos_bp.route('/', methods=['GET'])(index)
presentacionProyectos_bp.route('/crear', methods=['GET','POST'])(store)
presentacionProyectos_bp.route('/<int:presentacion_id>', methods=['GET','POST'])(show)
presentacionProyectos_bp.route('/<int:presentacion>/editar', methods=['POST'])(update)
presentacionProyectos_bp.route('/<int:presentacion_id>/borrar', methods=['DELETE'])(delete)
presentacionProyectos_bp.route('/all', methods=['GET'])(all)
