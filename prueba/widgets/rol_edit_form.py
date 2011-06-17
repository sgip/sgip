"""Rol Form"""

from tw.api import WidgetsList
from tw.forms import TableForm, CalendarDatePicker, SingleSelectField, TextField, TextArea, Spacer, Label, CheckBoxTable, HiddenField
from prueba.model import DBSession, Permission


class RolEditForm(TableForm):

    opciones_permisos = DBSession.query(Permission.permission_id, Permission.permission_name).order_by(Permission.permission_id)

    fields = [
	TextField('nombre', label_text='Nombre:'),
	Spacer(),
	TextField('descripcion', label_text='Descripcion:'),
	Spacer(),
	Label(text='Puede seleccionar uno o mas permisos para el nuevo rol:'),
	CheckBoxTable('permiso', label_text='Permisos:', options=opciones_permisos),
	Spacer()]
    _method = TextField(attrs={'value':'PUT'}) 

    submit_text = 'Guardar'

editar_rol_form = RolEditForm("editar_rol_form", action='editarRol')

#TextArea('descripcion', atrs=dict(rows=3,cols=25))
