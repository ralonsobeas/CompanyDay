from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, HiddenField, IntegerField, FileField#, SelectField,
from wtforms.validators import InputRequired, Length, Email,EqualTo

class RegisterForm(FlaskForm):
    #Parte 1 form
    cif = IntegerField("CIF", validators=[InputRequired(message="CIF no es válido!"),Length(max=50)])
    email = StringField("E-mail", validators=[InputRequired(),Email(message="Email no es válido!"),Length(max=120)])
    nombre = StringField("Nombre", validators=[InputRequired(message="Nombre no es válido!"),Length(max=120)])
    password = PasswordField("Contraseña ",validators=[InputRequired(), Length(min=4), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirmar contraseña ", validators=[InputRequired()])

    #Parte 2 form
    personaContacto = StringField("Persona de contacto", validators=[Length(max=120)])
    telefono = StringField("Teléfono", validators=[Length(max=15)])
    urlWeb = StringField("URL web", validators=[Length(max=15)])
    logo = FileField("Logo")

    #Parte 3 form
    direccion = StringField("Dirección", validators=[Length(max=120)])
    poblacion = StringField("Población", validators=[Length(max=120)])
    provincia = StringField("Provincia", validators=[Length(max=120)])
    codigoPostal = StringField("Código postal", validators=[Length(max=15)])
    pais = StringField("País", validators=[Length(max=120)])

    #Parte 4 form



class ResetPasswordForm(FlaskForm):
    email = StringField("E-mail", validators=[InputRequired(),Email(message="Email no es válido!"),Length(max=50)])


class SetNewPasswordForm(FlaskForm):
    username = HiddenField('username')
    userhash = HiddenField('userhash')
    password = PasswordField("Password / Contraseña ",validators=[InputRequired(), Length(min=4), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm password / Confirmar contraseña ", validators=[InputRequired()])
