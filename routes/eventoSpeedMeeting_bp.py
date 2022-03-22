from flask import Blueprint
from controllers.EventoSpeedMeetingController import index, store, show, update, delete,all

eventoSpeedMeeting_bp = Blueprint('eventoSpeedMeeting_bp', __name__)

eventoSpeedMeeting_bp.route('/', methods=['GET'])(index)
eventoSpeedMeeting_bp.route('/crear', methods=['GET','POST'])(store)
eventoSpeedMeeting_bp.route('/<int:empresa_id>', methods=['GET','POST'])(show)
eventoSpeedMeeting_bp.route('/<int:empresa_id>/editar', methods=['POST'])(update)
eventoSpeedMeeting_bp.route('/<int:empresa_id>/delete', methods=['DELETE'])(delete)
eventoSpeedMeeting_bp.route('/all', methods=['GET'])(all)
