"""Fase Form"""

from tw.api import WidgetsList
from tw.forms import TableForm, SingleSelectField, TextField, Spacer
from prueba.model import DBSession, Proyecto
from tw.forms.validators import NotEmpty

class CampoForm(TableForm):

    opciones_tipos = ['String', 'Int', 'Date']

    fields = [
	TextField('nombre', label_text='Nombre:', validator=NotEmpty),
	Spacer(),
	SingleSelectField('tipo', label_text='Tipo:', options=opciones_tipos, size=10, validator=NotEmpty),
	Spacer()]

    submit_text = 'Guardar'

crear_campo_form = CampoForm("crear_campo_form", action='crearCampo')
