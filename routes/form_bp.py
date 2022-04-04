from flask import Blueprint
from controllers.FormController import store

form_bp = Blueprint('form_bp', __name__)

#empresa_bp.route('/', methods=['GET'])(index)
form_bp.route('/crear', methods=['GET','POST'])(store)
