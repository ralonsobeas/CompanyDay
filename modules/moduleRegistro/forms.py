from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, HiddenField, IntegerField, FileField, DateField, TimeField#, SelectField,
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length, Email,EqualTo




class EmpresaRegisterForm(FlaskForm):
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



class EventoCharlasRegisterForm(FlaskForm):
    tema = StringField("Tema", validators=[Length(max=4096)])
    presencialidad = BooleanField("Presencial")
    titulo = StringField("Título", validators=[Length(max=120)])
    fecha =  DateField('Fecha')
    autor = StringField("Autor", validators=[Length(max=516)])

class EventoFeriaEmpresasRegisterForm(FlaskForm):
    fecha =  DateField('Fecha')
    presencialidad = BooleanField("Presencial")

class EventoPresentacionProyectosRegisterForm(FlaskForm):
    presencial = BooleanField("Presencial")
    videojuegos = BooleanField("Videojuegos")
    disenoDigital = BooleanField("Diesño digital")
    cortosAnimacion = BooleanField("Cortos de animación")
    ingenieria = BooleanField("Ingeniería")

class EventoSpeedMeetingRegisterForm(FlaskForm):
    presencialidad = BooleanField("Presencial")
    fecha =  DateField('Fecha') #Añadir restricciones en los dias
    horaInicio = TimeField("Hora de inicio")
    horaFin = TimeField("Hora de finalización")
    perfiles = StringField("Perfiles que se buscan", widget=TextArea(), validators=[Length(max=4096)])
    pregunta = StringField("Pregunta", validators=[Length(max=4096)])

class PersonaRegisterForm(FlaskForm):
    nombrePersona = StringField("Nombre", validators=[Length(max=500)])
    puesto = StringField("Puesto", validators=[Length(max=120)])
    comentario = StringField("Comentario", widget=TextArea(), validators=[Length(max=500)])

class PersonaRegisterForm1(FlaskForm):
    nombrePersona1 = StringField("Nombre2", validators=[Length(max=500)])
    puesto1 = StringField("Puesto", validators=[Length(max=120)])
    comentario1 = StringField("Comentario", widget=TextArea(), validators=[Length(max=500)])

class PersonaRegisterForm2(FlaskForm):
    nombrePersona2 = StringField("Nombre", validators=[Length(max=500)])
    puesto2 = StringField("Puesto", validators=[Length(max=120)])
    comentario2 = StringField("Comentario", widget=TextArea(), validators=[Length(max=500)])

class PersonaRegisterForm3(FlaskForm):
    nombrePersona3 = StringField("Nombre", validators=[Length(max=500)])
    puesto3 = StringField("Puesto", validators=[Length(max=120)])
    comentario3 = StringField("Comentario", widget=TextArea(), validators=[Length(max=500)])

class ResetPasswordForm(FlaskForm):
    email = StringField("E-mail", validators=[InputRequired(),Email(message="Email no es válido!"),Length(max=50)])


class SetNewPasswordForm(FlaskForm):
    username = HiddenField('username')
    userhash = HiddenField('userhash')
    password = PasswordField("Password / Contraseña ",validators=[InputRequired(), Length(min=4), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm password / Confirmar contraseña ", validators=[InputRequired()])

class EditEmpresaForm(FlaskForm):
    id = HiddenField('cif', render_kw={'readonly': True})
    nombre = StringField("Nombre", validators=[InputRequired(message="Nombre no es válido!"),Length(max=120)])
    personaContacto = StringField("Persona de contacto", validators=[Length(max=120)])
    telefono = StringField("Teléfono", validators=[Length(max=15)])
    urlWeb = StringField("URL web", validators=[Length(max=15)])
    logo = FileField("Logo")
    direccion = StringField("Dirección", validators=[Length(max=120)])
    poblacion = StringField("Población", validators=[Length(max=120)])
    provincia = StringField("Provincia", validators=[Length(max=120)])
    codigoPostal = StringField("Código postal", validators=[Length(max=15)])
    pais = StringField("País", validators=[Length(max=120)])
