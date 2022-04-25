from flask import Blueprint, render_template

module001 = Blueprint("module001", __name__,static_folder="static",template_folder="templates")

@module001.route('/')
def module001_index():
    return render_template("module001_index.html")

@module001.route('/test')
def module001_test():
    return 'OK'