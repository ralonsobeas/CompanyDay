from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField,BooleanField
from wtforms.validators import InputRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[InputRequired(),Email(message="Email no es válido!"),Length(max=120)])
    password = PasswordField("Contraseña ",validators=[InputRequired()])
    remember = BooleanField("Remember ")
