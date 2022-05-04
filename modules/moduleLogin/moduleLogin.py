from flask import Blueprint, render_template, flash, redirect, url_for
from modules.moduleLogin.forms import LoginForm
from flask_login import login_user,login_required,current_user,logout_user
from shared.models import login_manager
from werkzeug.security import  check_password_hash
from controllers import EmpresaController

moduleLogin = Blueprint("moduleLogin", __name__,static_folder="static",template_folder="templates")

def loginForm():
    form = LoginForm()

    email = form.email.data
    password = form.password.data
    remember = form.remember.data

    empresa = EmpresaController.get_by_email(email)

    if not empresa or not check_password_hash(empresa.password,password):
        flash('Usuario incorrecto.')
        return  redirect(url_for('index'))

    login_user(empresa,remember=remember)

    return  redirect(url_for('empresa_bp.userProfile', editable=0))

"""
    Login manager para flask_login
"""
@login_manager.user_loader
def loginManager(id):
    return EmpresaController.get_by_id(id)

"""
    Logout
"""
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def moduleLogin_test():
    return 'OK'
