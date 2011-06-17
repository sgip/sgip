"""Fase Form"""

from tw.api import WidgetsList
from tw.forms import TableForm, CalendarDatePicker, SingleSelectField, TextField, TextArea, Spacer, Label
from prueba.model import DBSession, Proyecto


class FaseForm(TableForm):

    #opciones_permisos = DBSession.query(Permission.permission_id, Permission.permission_name).order_by(Permission.permission_id)

    fields = [
	TextField('nombre', label_text='Nombre:'),
	Spacer(),
	TextArea('descripcion', label_text='Descripcion:', atrs=dict(rows=10,cols=10)),
	Spacer(),
	CalendarDatePicker('fecha', label_text='Fecha:', date_format='%d-%m-%y'),
	Spacer()]

    submit_text = 'Guardar'

crear_fase_form = FaseForm("crear_fase_form", action='crearFase')
