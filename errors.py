from run import app
from flask import  render_template

# ERRORES ROUTING

def page_not_found(e):
  return render_template('admin/denied.html',message="Page not found",e=e), 404
app.register_error_handler(404, page_not_found)
def not_registered(e):
  return render_template('admin/denied.html',message="Not registered",e=e), 400
app.register_error_handler(400, not_registered)
def invalid_url(e):
  return render_template('admin/denied.html',message="Invalid url",e=e), 403
app.register_error_handler(403, invalid_url)

# FINAL ERRORES ROUTING
