from flask import Blueprint
from controllers.EventoSpeedMeetingController import index, store, show, update, delete,all
from modules.moduleRegistro.moduleRegistro import storeSpeedMeeting

"""
    Blueprints para EventoSpeedMeeting
"""

eventoSpeedMeeting_bp = Blueprint('eventoSpeedMeeting_bp', __name__)

#eventoSpeedMeeting_bp.route('/', methods=['GET'])(index)
# Guardar EventoPresentacionProyectos
eventoSpeedMeeting_bp.route('/crear', methods=['GET','POST'])(storeSpeedMeeting)
# Mostrar EventoPresentacionProyectos
#eventoSpeedMeeting_bp.route('/<int:empresa_id>', methods=['GET','POST'])(show)
# Guardar EventoPresentacionProyectos
eventoSpeedMeeting_bp.route('/<int:empresa_id>/editar', methods=['POST'])(update)
# Borrar EventoPresentacionProyectos
eventoSpeedMeeting_bp.route('/<int:empresa_id>/delete', methods=['DELETE'])(delete)
# Mostrar todos EventoPresentacionProyectos
#eventoSpeedMeeting_bp.route('/all', methods=['GET'])(all)
