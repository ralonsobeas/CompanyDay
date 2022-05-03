from run import app,db

from flask import abort

from flask_admin import Admin
from flask_admin.base import expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action

from flask_login import current_user

from models import EventoFeriaEmpresas
from models.EventoFeriaEmpresas import EventoFeriaEmpresas

from models import EventoPresentacionProyectos
from models.EventoPresentacionProyectos import EventoPresentacionProyectos

from models import EventoCharlas
from models.EventoCharlas import EventoCharlas

from models import EventoSpeedMeeting
from models.EventoSpeedMeeting import EventoSpeedMeeting

from models import Empresa
from models.Empresa import Empresa

from models import Persona
from models.Persona import Persona

from controllers import EmpresaController
from controllers import EventoCharlaController
from controllers import EventoPresentacionProyectosController
from controllers import EventoFeriaEmpresasController
from controllers import PersonaController
from controllers import EventoSpeedMeetingController



# MODO ADMINISTRADOR
class SecureView(ModelView):
    def is_accessible(self):
        if not current_user.is_authenticated or not current_user.admin:
            return abort(404, description="Sin permisos")
        # only accessible if admin field is True
        if current_user.is_authenticated and not current_user.is_anonymous:
            return current_user.admin

        return False
    def _handle_view(self, name, **kwargs):
        if not current_user.is_authenticated:
            return abort(404, description="Sin permisos")
        if not self.is_accessible:
            return abort(404, description="Sin permisos")

class GeneralView(SecureView):
    can_export = True
    column_exclude_list = ('password')
    column_export_exclude_list = ('password')
    export_types = ['csv','xls']
    column_hide_backrefs = False
    column_display_pk = True

    def cambio_id_nombre(view, context, model, name):
        if model.empresa_id is None:
            return 'None'
        return EmpresaController.get_by_id(model.empresa_id).nombre


class EmpresaView(GeneralView):
    column_exclude_list = ['userHash']
    column_searchable_list = ['nombre', 'email']
    column_sortable_list = ['validado','confirmed','admin']
    column_list = ['validado', 'confirmed', 'nombre', 'email', 'personacontacto', 'telefono', 'direccion', 'poblacion', 'provincia', 'codigoPostal', 'pais', 'consentimientonombre', 'buscacandidatos','admin']
    @action('validar', 'Validar', '¿Seguro de que quieres validar las empresas seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EmpresaController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} Empresa (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las empresas seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EmpresaController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} Empresa (s) invalidada (s)".format(count))
    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        """Custom create view."""
        return self.render('registroEmpresa.html',edit=0)
    @expose('/edit/', methods=('GET', 'POST'))
    def create_view(self):
        """Custom create view."""
        return self.render('registroEmpresa.html',edit=1,EmpresaController=EmpresaController)

Empresa_View = EmpresaView(Empresa,db.session)


class EventoFeriaEmpresasView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'fecha', 'presencial']
    column_sortable_list = ['empresa_id', 'fecha']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }

EventoFeriaEmpresas_View = EventoFeriaEmpresasView(EventoFeriaEmpresas,db.session)


class EventoPresentacionProyectosView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'validado', 'presencial','videojuegos','disenoDigital','cortosAnimacion','ingenieria']
    column_sortable_list = ['empresa_id', 'validado', 'presencial','videojuegos','disenoDigital','cortosAnimacion','ingenieria']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }
    @action('validar', 'Validar', '¿Seguro de que quieres validar las presentaciones seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoPresentacionProyectosController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} Presentacion (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las presentaciones seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoPresentacionProyectosController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} Presentacion (s) invalidada (s)".format(count))

EventoPresentacionProyectos_View = EventoPresentacionProyectosView(EventoPresentacionProyectos,db.session)


class EventoCharlasView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'aprobada', 'fecha','titulo','tema','autor','presencialidad']
    column_sortable_list = ['empresa_id', 'fecha','aprobada']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }
    @action('validar', 'Validar', '¿Seguro de que quieres validar las charlas seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoCharlaController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} Charla (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las charlas seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoCharlaController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} Charla (s) invalidada (s)".format(count))

EventoCharlas_View = EventoCharlasView(EventoCharlas,db.session)


class EventoSpeedMeetingView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id', 'aprobada', 'fecha','pregunta','perfiles','horaInicio','horaFin']
    column_sortable_list = ['empresa_id', 'fecha','aprobada','horaInicio','horaFin']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }
    @action('validar', 'Validar', '¿Seguro de que quieres validar las speedmeetings seleccionadas?')
    def action_validar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoSpeedMeetingController.validar(_id,True)
            count += 1
        db.session.commit()
        flash("{0} SpeedMeeting (s) validadada (s)".format(count))

    @action('invalidar', 'Invalidar', '¿Seguro de que quieres invalidar las speedmeetings seleccionadas?')
    def action_invalidar(self, ids):
        count = 0
        for _id in ids:
            # Do some work with the id, e.g. call a service method
            EventoSpeedMeetingController.validar(_id,False)
            count += 1
        db.session.commit()
        flash("{0} SpeedMeeting (s) invalidada (s)".format(count))

EventoSpeedMeeting_View = EventoSpeedMeetingView(EventoSpeedMeeting,db.session)


class PersonaView(GeneralView):
    column_exclude_list = ['id']
    column_list = ['empresa_id','nombre', 'puesto','comentario']
    column_sortable_list = ['empresa_id','nombre']

    column_formatters = {
        'empresa_id': GeneralView.cambio_id_nombre
    }

Persona_View = PersonaView(Persona,db.session)


admin=Admin(app, name='Administrador',url="/admin", template_mode='bootstrap4')
admin.add_view(Empresa_View)
admin.add_view(EventoFeriaEmpresas_View)
admin.add_view(EventoPresentacionProyectos_View)
admin.add_view(EventoCharlas_View)
admin.add_view(EventoSpeedMeeting_View)
admin.add_view(Persona_View)

# FIN MODO ADMINISTRADOR
