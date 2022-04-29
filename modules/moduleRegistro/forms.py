from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, HiddenField#, SelectField,
from wtforms.validators import InputRequired, Length, Email,EqualTo

class ResetPasswordForm(FlaskForm):
    email = StringField("E-mail", validators=[InputRequired(),Email(message="Email no es válido!"),Length(max=50)])


class SetNewPasswordForm(FlaskForm):
    username = HiddenField('username')
    userhash = HiddenField('userhash')
    password = PasswordField("Password / Contraseña ",validators=[InputRequired(), Length(min=4), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm password / Confirmar contraseña ", validators=[InputRequired()])
