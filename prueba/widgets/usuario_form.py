"""Usuario Form"""

from tw.api import WidgetsList
from tw.forms import TableForm, CalendarDatePicker, SingleSelectField, TextField, TextArea, Spacer, Label, PasswordField, MultipleSelectField, CheckBoxTable
from tw.forms.validators import NotEmpty
from prueba.model import DBSession, Group


class UsuarioForm(TableForm):

    opciones_roles = DBSession.query(Group.group_id, Group.group_name).order_by(Group.group_id)

    fields = [
	TextField('nombre', label_text='*Nombre de usuario:', validator=NotEmpty),
#	Spacer(),
	PasswordField('contrasena', label_text='*Contrasena:', validator=NotEmpty),
	Spacer(),
	Label(text='Datos del usuario:'),
	TextField('apellido', label_text='*Nombre completo:', validator=NotEmpty),
#	Spacer(),
	TextField('telefono', label_text='*Telefono:', validator=NotEmpty),
#	Spacer(),
	TextField('direccion', label_text='*Direccion:', validator=NotEmpty),
#	Spacer(),
	TextField('email', label_text='*Email:', validator=NotEmpty),
#	Spacer(),
	Spacer(),
	Label(text='Puede seleccionar uno o mas roles para el nuevo usuario:'),
	#CheckBoxTable('rol', label_text='Roles:', options=opciones_roles),
	MultipleSelectField('rol', label_text='Rol:', options=opciones_roles, size=10),
	Spacer()]

    submit_text = 'Guardar'

crear_usuario_form = UsuarioForm("crear_usuario_form", action='crearUsuario')
