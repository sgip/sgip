# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect, tmpl_context, validate
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
from repoze.what import predicates

from prueba.lib.base import BaseController
from prueba.model import DBSession, metadata
<<<<<<< HEAD
from prueba.model import User, Group, Permission, Proyecto, Fase, Tipoitem, Campo, Item, Relacion, Atributo, Modificacion, Revision, HistorialItem
from prueba.model import ItemHistorial, AtributoHistorial, RelacionHistorial
=======
from prueba.model import User, Group, Permission, Proyecto, Fase, Tipoitem, Campo, Item, Relacion
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
from prueba import model
from prueba.controllers.secure import SecureController
from prueba.widgets.rol_form import crear_rol_form, editar_rol_form
from prueba.widgets.usuario_form import crear_usuario_form
from prueba.widgets.proyecto_form import crear_proyecto_form
from prueba.widgets.fase_form import crear_fase_form
from prueba.widgets.campo_form import crear_campo_form
<<<<<<< HEAD
from tw.forms.validators import NotEmpty, Int, DateValidator
=======
from tw.forms.validators import NotEmpty, Int
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

from prueba.controllers.error import ErrorController
from repoze.what.predicates import not_anonymous
from repoze.what.predicates import Any, is_user, has_permission
from prueba.lib.authz import user_can_edit

from tgext.crud import CrudRestController
from sprox.tablebase import TableBase
from sprox.fillerbase import TableFiller
from sprox.formbase import EditableForm
from sprox.fillerbase import EditFormFiller

<<<<<<< HEAD
from sqlalchemy import or_, func, distinct
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
import formencode
from formencode import validators
from formencode.validators import DateConverter


=======
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
__all__ = ['RootController']

#Rol
class RolTable(TableBase):
    __model__ = Group
rol_table = RolTable(DBSession)

class RolTableFiller(TableFiller):
    __model__ = Group
rol_table_filler = RolTableFiller(DBSession)

class RolEditForm(EditableForm):
    __model__= Group
rol_edit_form = RolEditForm(DBSession)

class RolEditFiller(EditFormFiller):
    __model__ = Group
rol_edit_filler = RolEditFiller(DBSession)

class RolController(CrudRestController):
    model = Group
    table = rol_table
    table_filler = rol_table_filler
    new_form = crear_rol_form
    edit_filler = rol_edit_filler
    edit_form = rol_edit_form

#Usuario
class UserTable(TableBase):
    __model__ = User
    __omit_fields__ = ['_password']
user_table = UserTable(DBSession)

class UserTableFiller(TableFiller):
    __model__ = User
user_table_filler = UserTableFiller(DBSession)

class UserEditForm(EditableForm):
    __model__= User
    __omit_fields__ = ['_password']
user_edit_form = UserEditForm(DBSession)

class UserEditFiller(EditFormFiller):
    __model__ = User
user_edit_filler = UserEditFiller(DBSession)

class UserController(CrudRestController):
    model = User
    table = user_table
    table_filler = user_table_filler
    new_form = crear_usuario_form
    edit_filler = user_edit_filler
    edit_form = user_edit_form

#Proyecto
class ProyectoTable(TableBase):
    __model__ = Proyecto
proyecto_table = ProyectoTable(DBSession)

class ProyectoTableFiller(TableFiller):
    __model__ = Proyecto
proyecto_table_filler = ProyectoTableFiller(DBSession)

class ProyectoEditForm(EditableForm):
    __model__= Proyecto
proyecto_edit_form = ProyectoEditForm(DBSession)

class ProyectoEditFiller(EditFormFiller):
    __model__ = Proyecto
proyecto_edit_filler = ProyectoEditFiller(DBSession)

class ProyectoController(CrudRestController):
    model = Proyecto
    table = proyecto_table
    table_filler = proyecto_table_filler
    new_form = crear_proyecto_form
    edit_filler = proyecto_edit_filler
    edit_form = proyecto_edit_form

<<<<<<< HEAD
class PwdSchema(formencode.Schema):
    nombre = validators.NotEmpty()
=======
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

class RootController(BaseController):
    """
    The root controller for the prueba application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()

    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    usuarios = UserController(DBSession)
    roles = RolController(DBSession)
    proyectos = ProyectoController(DBSession)

    @expose('prueba.templates.index')
    def index(self):
        """Handle the front-page."""
	op = ('roles', 'usuarios', 'proyectos')
        return dict(page='index', opciones=op)

    #################### INICIO_ROLES ####################
    ##### Crear rol
    @expose('prueba.templates.rol_form')
    @require(not_anonymous(msg='Debe estar logueado'))
    @require(Any(has_permission('crear_rol'), msg='Solo los usuarios con permisos pueden crear roles'))
    def NuevoRol(self, **kw):
    	"""Show form to add new movie data record."""
    	tmpl_context.form = crear_rol_form
    	return dict(modelname='Rol', value=kw)

    ##### Crear rol
    #@expose('prueba.templates.rol_edit_form')
    #def editar_rol(self, rol_id, **kw):
    #	tmpl_context.form = editar_rol_form
    #	rol = DBSession.query(Group).filter_by(group_id=rol_id).one()
    #	value = {'nombre':"", 'description':""}
    #	value['nombre']=rol.group_name
    #	value['descripcion']=rol.group_description
    #	return dict(modelname='Rol', value=value)

    @validate(crear_rol_form, error_handler=NuevoRol)
    @expose()
    def crearRol(self, **kw):
    	rol = Group()
	rol.group_name = kw['nombre']
	rol.group_description = kw['descripcion']
    	DBSession.add(rol)
	#Agregar los permisos
	permisos = kw[u'permiso']
	for permiso_id in permisos:
	    permiso = DBSession.query(Permission).filter_by(permission_id=permiso_id).one()
            permiso.groups.append(rol)
	# Se crean los permisos de consulta, edicion y eliminacion de este rol
	
	rol = DBSession.query(Group).filter_by(group_name=kw['nombre']).one()
	
	permiso_consultar = Permission()
	permiso_consultar.permission_name='ConsultarRol' + str(rol.group_id)
	DBSession.add(permiso_consultar)

	permiso_editar = Permission()
	permiso_editar.permission_name='EditarRol' + str(rol.group_id)
	DBSession.add(permiso_editar)
	
	permiso_eliminar = Permission()
	permiso_eliminar.permission_name='EliminarRol' + str(rol.group_id)
	DBSession.add(permiso_eliminar)

	#grupo = DBSession.query(Group).filter_by(group_id='2').one()
	#permiso_editar.groups.append(grupo)
	#permiso_eliminar.groups.append(grupo)

	#Agregar los permisos de consulta, edicion y eliminacion al rol por defecto del usuario creador del rol
	identity = request.environ['repoze.who.identity']
	usuario_creador_de_usuario = identity['user']
	rol = DBSession.query(Group).filter_by(group_name='RolPorDefecto' + str(usuario_creador_de_usuario.user_id)).one()
	rol.permissions.append(permiso_consultar)
	rol.permissions.append(permiso_editar)
	rol.permissions.append(permiso_eliminar)
	flash("El rol fue creado con exito")
    	redirect("ListarRoles")

    @expose('prueba.templates.editar_rol')
    def EditarRol(self, rol_id, **kw):
	rol = DBSession.query(Group).filter_by(group_id=rol_id).one()
	permisos_del_rol = rol.permissions #Permisos del rol
	todos_los_permisos = DBSession.query(Permission).all() #Todos los permisos de la BD
	return dict(page='Edicion de roles', rol_id=rol_id, rol=rol, pdr= permisos_del_rol, tlp=todos_los_permisos, value=kw)

    @expose()
    @validate({"nombre": NotEmpty()}, error_handler=EditarRol)
    def editarRol(self, rol_id, nombre, descripcion, permisos=None, **kw):
	rol = DBSession.query(Group).filter_by(group_id=rol_id).one()
	rol.group_name = nombre
	rol.group_description = descripcion
	
	if permisos is not None:
		if not isinstance(permisos, list):
			permisos = [permisos]
		permisos = [DBSession.query(Permission).get(permiso) for permiso in permisos]
	else:
		permisos=list()
	rol.permissions = permisos
	DBSession.flush()
	flash("El rol fue actualizado con exito")
	redirect("/ListarRoles")

    @expose()
    def EliminarRol(self, rol_id, **kw):
	DBSession.delete(DBSession.query(Group).get(rol_id))
	#DBSession.query(Permission).filter_by(permission_name=('EditarRol' + rol_id)).one()
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('ConsultarRol' + rol_id)).one())
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EditarRol' + rol_id)).one())
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EliminarRol' + rol_id)).one())
	redirect("/ListarRoles")

    @expose('prueba.templates.listar_roles')
    def ListarRoles(self, **kw):
    	roles = DBSession.query(Group).order_by(Group.group_id)
	### Para determinar si el usuario actualmente loggeado tiene permiso para crear nuevos roles
	permiso_para_crear = has_permission('crear_rol')
	### Para determinar si el usuario actualmente loggeado tiene permiso para editar roles existentes
	r=list()
	editar=list()
	identity = request.environ['repoze.who.identity']
	usuario = identity['user']
	cant=0
	for rol in roles:
		permiso = 'ConsultarRol' + str(rol.group_id)
		if has_permission(permiso):
			r.append(rol)
		permiso = 'EditarRol' + str(rol.group_id)
		if has_permission(permiso):
			editar.append(True)
		else:
			editar.append(False)
		cant = cant +1
		#can_edit = has_permission(permiso)
		#print can_edit
		#checker = user_can_edit(rol.group_id)
		#can_edit = checker.is_met(request.environ)
		#if can_edit != Nonw
		#	my_list.append(True)
		#if can_edit == None
		#	my_list.append(False)
	print type(roles)
	print type(r)
	## Paginacion
	from webhelpers import paginate
	count = cant
	page = int(kw.get('page', '1'))
	currentPage = paginate.Page(r, page, item_count=count, items_per_page=5,)
	r = currentPage.items
	
	
	return dict(page='Listado de Roles', roles=r, currentPage = currentPage, p=permiso_para_crear, editar=editar)
    #################### FIN_ROLES ####################

    #################### INICIO_USUARIOS ####################
    ### Crear usuario
    @expose('prueba.templates.usuario_form')
    @require(not_anonymous(msg='Debe estar logueado'))
    @require(Any(has_permission('crear_usuario'), msg='Solo los usuarios con permisos pueden crear usuarios'))
    def NuevoUsuario(self, **kw):
    	"""Show form to add new movie data record."""
    	tmpl_context.form = crear_usuario_form
    	return dict(modelname='Usuario', value=kw)

    @validate(crear_usuario_form, error_handler=NuevoUsuario)
    @expose()
    def crearUsuario(self, **kw):
    	usuario = User()
	usuario.user_name = kw['nombre']
	usuario.user_fullname = kw[u'apellido']
	usuario.password = kw[u'contrasena']
	usuario.user_telefono = kw[u'telefono']
	usuario.user_direccion = kw[u'direccion']
	usuario.email_address = kw[u'email']
	DBSession.add(usuario)
	#Agregar los roles
	roles = kw[u'rol']
	for rol_id in roles:
	    rol = DBSession.query(Group).filter_by(group_id=rol_id).one()
            rol.users.append(usuario)
	#Crear el rol por defecto para este usuario
	rol_por_defecto = Group()
	rol_por_defecto.group_name = 'RolPorDefecto' + str(usuario.user_id)
	DBSession.add(rol_por_defecto)
	rol_por_defecto.users.append(usuario) #Asociar el rol por defecto con el usuario
	# Se crean los permisos de consulta, edicion y eliminacion de este usuario
	permiso_consultar = Permission()
	permiso_consultar.permission_name='ConsultarUsuario' + str(usuario.user_id)
	DBSession.add(permiso_consultar)
	permiso_editar = Permission()
	permiso_editar.permission_name='EditarUsuario' + str(usuario.user_id)
	DBSession.add(permiso_editar)
	permiso_eliminar = Permission()
	permiso_eliminar.permission_name='EliminarUsuario' + str(usuario.user_id)
	DBSession.add(permiso_eliminar)
	#Asociar el rol por defecto con el usuario
	#rol_por_defecto.users.append(usuario)
	#rol_por_defecto.permissions.append()
	#Agregar los permisos de consulta, edicion y eliminacion al rol por defecto del usuario creador de usuario
	identity = request.environ['repoze.who.identity']
	usuario_creador_de_usuario = identity['user']
	rol = DBSession.query(Group).filter_by(group_name='RolPorDefecto' + str(usuario_creador_de_usuario.user_id)).one()
	rol.permissions.append(permiso_consultar)
	rol.permissions.append(permiso_editar)
	rol.permissions.append(permiso_eliminar)
	#Asignarle al usuario recien creado el permiso de consulta de sus datos
	rol_por_defecto.permissions.append(permiso_consultar)
    	flash("El usuario fue creado satisfactoriamente")
    	redirect("NuevoUsuario")

    @expose('prueba.templates.editar_usuario')
    def EditarUsuario(self, usuario_id, **kw):
	usuario = DBSession.query(User).filter_by(user_id=usuario_id).one()
	roles_del_usuario = usuario.groups #Roles del usuario
	todos_los_roles = DBSession.query(Group).all() #Todos los roles de la BD
	return dict(page='Edicion de usuarios', usuario_id=usuario_id, usuario=usuario, rdu= roles_del_usuario, tlr=todos_los_roles, value=kw)

    @expose()
    @validate({"username": NotEmpty(), "contrasena": NotEmpty(), "nombre_completo": NotEmpty(), "telefono": NotEmpty(), "direccion": NotEmpty(), "email": NotEmpty()}, error_handler=EditarUsuario)
    def editarUsuario(self, usuario_id, username, contrasena, nombre_completo, telefono, direccion, email, roles=None, **kw):
	usuario = DBSession.query(User).filter_by(user_id=usuario_id).one()
	usuario.user_name = username
	usuario.password = contrasena
	usuario.user_fullname = nombre_completo
	usuario.user_telefono = telefono
	usuario.user_direccion = direccion
	usuario.email_address = email
		
	if roles is not None:
		if not isinstance(roles, list):
			roles = [roles]
		roles = [DBSession.query(Group).get(rol) for rol in roles]
	else:
		roles=list()
	usuario.groups = roles 
	DBSession.flush()
	flash("El usuario fue actualizado con exito")
	redirect("/ListarUsuarios")

    @expose()
    def EliminarUsuario(self, usuario_id, **kw):
	DBSession.delete(DBSession.query(User).get(usuario_id))
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('ConsultarUsuario' + usuario_id)).one())
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EditarUsuario' + usuario_id)).one())
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EliminarUsuario' + usuario_id)).one())
	DBSession.delete(DBSession.query(Group).filter_by(group_name=('RolPorDefecto' + usuario_id)).one())
	redirect("/ListarUsuarios")

    @expose('prueba.templates.listar_usuarios')
    def ListarUsuarios(self, **kw):
    	usuarios = DBSession.query(User).order_by(User.user_id)
	## Paginacion
	from webhelpers import paginate
	count = usuarios.count()
	page = int(kw.get('page', '1'))
	currentPage = paginate.Page(usuarios, page, item_count=count, items_per_page=5,)
	usuarios = currentPage.items
	### Para determinar si el usuario actualmente loggeado tiene permiso para crear nuevos roles
	permiso_para_crear = has_permission('crear_usuario')
	### Para determinar si el usuario actualmente loggeado tiene permiso para editar roles existentes
	return dict(page='Listado de Usuarios', usuarios=usuarios, currentPage = currentPage, p=permiso_para_crear)
    #################### FIN_USUARIOS ####################

    #################### INICIO_PROYECTOS ####################
    ### Crear proyecto
    @expose('prueba.templates.proyecto_form')
    def NuevoProyecto(self, **kw):
	tmpl_context.form = crear_proyecto_form
    	return dict(modelname='Proyecto', value=kw)

    @validate(crear_proyecto_form, error_handler=NuevoProyecto)
    @expose()
    def crearProyecto(self, **kw):
    	proyecto = Proyecto()
	proyecto.nombre = kw['nombre']
	proyecto.estado = 'definicion'
	proyecto.fecha = kw['fecha']
	DBSession.add(proyecto)
	proyecto = DBSession.query(Proyecto).filter_by(nombre=kw['nombre']).one()
	# Se crean los permisos de consulta, edición y eliminación del proyecto
	permiso_consultar = Permission()
	permiso_consultar.permission_name='ConsultarProyecto' + str(proyecto.codproyecto)
	DBSession.add(permiso_consultar)
	permiso_editar = Permission()
	permiso_editar.permission_name='EditarProyecto' + str(proyecto.codproyecto)
	DBSession.add(permiso_editar)
	permiso_eliminar = Permission()
	permiso_eliminar.permission_name='EliminarProyecto' + str(proyecto.codproyecto)
	DBSession.add(permiso_eliminar)
	permiso_definir_fases = Permission()
	permiso_definir_fases.permission_name='DefinirFases' + str(proyecto.codproyecto)
	DBSession.add(permiso_definir_fases)
	#Agregar los permisos de consulta, edicion y eliminacion al rol por defecto del usuario creador de proyecto
	identity = request.environ['repoze.who.identity']
	usuario_creador_de_proyecto = identity['user']
	rol = DBSession.query(Group).filter_by(group_name='RolPorDefecto' + str(usuario_creador_de_proyecto.user_id)).one()
	rol.permissions.append(permiso_consultar)
	rol.permissions.append(permiso_editar)
	rol.permissions.append(permiso_eliminar)
	rol.permissions.append(permiso_definir_fases)
	flash("El proyecto fue creado con exito")
    	redirect("ListarProyectos")

    @expose('prueba.templates.definir_fases')
    def DefinirFases(self, proyecto_id, **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	fases = list()
	#for fase in proyecto.fases:
	#	fases.append(int(fase.codfase));
	#print proyecto.nombre
	#print proyecto.codproyecto
	#print proyecto.estado
	#print proyecto.fecha
	#print proyecto.fases
	#print type(proyecto.fases)
	fases = proyecto.fases
	if not isinstance(fases, list):
		fases = [fases]
	return dict(page='Definicion de fases', proyecto_id=proyecto_id, proyecto=proyecto, fases=fases, value=kw)

    @expose('')
    def IniciarProyecto(self, proyecto_id, **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	proyecto.cantfases=len(proyecto.fases)
	proyecto.estado="desarrollo"
	fases = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).order_by(Fase.codfase).all()
	i=1
	for fase in fases:
		fase.orden=i;
		if i==1:
			fase.estado="desarrollo"
		else:
			fase.estado="inicial"
		i=i+1
	DBSession.flush()
	redirect("/ListarProyectos")

    @expose('prueba.templates.ingresar_proyecto')
    def IngresarProyecto(self, proyecto_id, **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	fases = proyecto.fases
	if not isinstance(fases, list):
		fases = [fases]
	return dict(modelname='Proyecto', proyecto=proyecto, fases=fases, value=kw)

    @expose('prueba.templates.ingresar__proyecto')
    def Ingresar_Proyecto(self, proyecto_id, **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	fases = proyecto.fases
	if not isinstance(fases, list):
		fases = [fases]
	return dict(modelname='Proyecto', proyecto=proyecto, fases=fases, value=kw)

    @expose()
    def EliminarProyecto(self, proy_id, **kw):
	proyecto = DBSession.query(Proyecto).get(proy_id)
	fases = proyecto.fases
	if not isinstance(fases, list):
		fases = [fases]
	for fase in fases:
		DBSession.delete(fase)	
	DBSession.delete(DBSession.query(Proyecto).get(proy_id))
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('ConsultarProyecto' + proy_id)).one())
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EditarProyecto' + proy_id)).one())
	DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EliminarProyecto' + proy_id)).one())
	redirect("/ListarProyectos/")

    @expose('prueba.templates.listar_proyectos')
    def ListarProyectos(self, **kw):
    	proyectos = DBSession.query(Proyecto).order_by(Proyecto.codproyecto)
	## Paginacion
	from webhelpers import paginate
	count = proyectos.count()
	page = int(kw.get('page', '1'))
	currentPage = paginate.Page(proyectos, page, item_count=count, items_per_page=5,)
	proyectos = currentPage.items
	### Para determinar si el usuario actualmente loggeado tiene permiso para crear nuevos roles
	permiso_para_crear = has_permission('crear_usuario')
<<<<<<< HEAD
	return dict(page='Listado de Proyectos', proyectos=proyectos, currentPage = currentPage, p=permiso_para_crear,permiso='crear_proyecto')  
=======
	return dict(page='Listado de Proyectos', proyectos=proyectos, currentPage = currentPage, p=permiso_para_crear)  
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

    #################### INICIO_FASES ####################
    ### Crear fase
    @expose('prueba.templates.crear_fase')
    def NuevaFase(self, proy_id, **kw):
	nombre="" 
	descripcion=""
	if ('nombre' in kw or 'description' in kw):
		nombre=kw['nombre']
		descripcion=kw['descripcion'] 
	return dict(page='Creacion de Fases', proy_id=proy_id, nombre=nombre, descripcion=descripcion, value=kw)

    @expose()
    @validate({"nombre": NotEmpty()}, error_handler=NuevaFase)
    def crearFase(self, proy_id, **kw):
	fase = Fase()
	fase.nombre = kw['nombre']
	fase.descripcion = kw['descripcion']
	fase.estado = "definicion"
	import datetime
	fase.fecha = datetime.date.today()
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proy_id).one()
	fase.proyecto = proyecto
	proyecto.fases.append(fase)
	#fase.codproyecto=int(proy_id)
	DBSession.add(fase)
	self.CrearTipoItemBasico(proy_id, fase)
    	flash("La fase fue creada con exito")
    	redirect("/DefinirFases/"+proy_id)

    @expose('prueba.templates.ingresar_fase')
    def IngresarFase(self, proyecto_id, fase_id, **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
<<<<<<< HEAD
	fases = proyecto.fases
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	items = fase.items
	items.sort()
	if not isinstance(items, list):
		items = [items]
	return dict(modelname='Proyecto', proyecto=proyecto, fases=fases, fase=fase, items=items, value=kw)
=======
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	items = fase.items
	if not isinstance(items, list):
		items = [items]
	return dict(modelname='Proyecto', proyecto=proyecto, fase=fase, items=items, value=kw)
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
    
    @expose()
    def CrearTipoItemBasico(self, proyecto_id, fase):
	t = Tipoitem()
	t.nombre='Basico'
	t.fase=fase
<<<<<<< HEAD
	#c1 = Campo()
	#c1.nombre = 'Nombre'
	#c1.tipo = 'String'
	#c2 = Campo()
	#c2.nombre = 'Complejidad'
	#c2.tipo = 'Int'
	#c3 = Campo()
	#c3.nombre = 'Prioridad'
	#c3.tipo = 'Int'
	#c4 = model.Campo()
	#c4.nombre = 'Version'
	#c4.tipo = 'Int'
	#c5 = model.Campo()
	#c5.nombre = 'Estado'
	#c5.tipo = 'String'
	#c6 = model.Campo()
	#c6.nombre = 'Fecha'
	#c6.tipo = 'Date'
	#t.campos.append(c1)
	#t.campos.append(c2)
	#t.campos.append(c3)
	#t.campos.append(c4)
	#t.campos.append(c5)
	#t.campos.append(c6)
	DBSession.add(t)
=======
	c1 = Campo()
	c1.nombre = 'Nombre'
	c1.tipo = 'String'
	c2 = Campo()
	c2.nombre = 'Complejidad'
	c2.tipo = 'Int'
	c3 = Campo()
	c3.nombre = 'Prioridad'
	c3.tipo = 'Int'
	c4 = model.Campo()
	c4.nombre = 'Version'
	c4.tipo = 'Int'
	c5 = model.Campo()
	c5.nombre = 'Estado'
	c5.tipo = 'String'
	c6 = model.Campo()
	c6.nombre = 'Fecha'
	c6.tipo = 'Date'
	t.campos.append(c1)
	t.campos.append(c2)
	t.campos.append(c3)
	t.campos.append(c4)
	t.campos.append(c5)
	t.campos.append(c6)
	DBSession.flush()
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

    @expose('prueba.templates.editar_fase')
    def EditarFase(self, proyecto_id, fase_id, **kw):
	fase=Fase()
	if ('nombre' in kw or 'description' in kw):
		fase.nombre=kw['nombre']
		fase.descripcion=kw['descripcion'] 
	else:
		fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	#roles_del_usuario = usuario.groups #Roles del usuario
	#todos_los_roles = DBSession.query(Group).all() #Todos los roles de la BD
	return dict(page='Edicion de fases', fase_id=fase_id, proy_id=proyecto_id, fase=fase, value=kw)

    @expose()
    @validate({"nombre": NotEmpty(),}, error_handler=EditarFase)
    def editarFase(self, proy_id, fase_id, nombre="", descripcion="", **kw):
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	fase.nombre = nombre
	fase.descripcion = descripcion
	DBSession.flush()
	flash("La fase fue actualizada con exito")
	redirect("/DefinirFases/"+proy_id)

    @expose()
    def EliminarFase(self, proy_id, fase_id, **kw):
	DBSession.delete(DBSession.query(Fase).get(fase_id))
	#DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('ConsultarUsuario' + usuario_id)).one())
	#DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EditarUsuario' + usuario_id)).one())
	#DBSession.delete(DBSession.query(Permission).filter_by(permission_name=('EliminarUsuario' + usuario_id)).one())
	#DBSession.delete(DBSession.query(Group).filter_by(group_name=('RolPorDefecto' + usuario_id)).one())
	redirect("/DefinirFases/"+proy_id)

    #################### INICIO_TIPO_ITEMS ####################
    ### Crear Tipo de Ítems
    @expose('prueba.templates.crear_tipoitem')
<<<<<<< HEAD
    def NuevoTipoDeItem(self, proyecto_id, fase_id, nombre="", **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()	
	if 'nombre' in kw:
		nombre=kw['nombre']
	return dict(page='Creacion de tipos de item', proyecto=proyecto, fase=fase, nombre=nombre, value=kw)

    @expose()
    @validate({"nombre": NotEmpty(),}, error_handler=NuevoTipoDeItem)
    def crearTipoDeItem(self, proyecto_id, fase_id, **kw):
	print '******!'
	print kw
	tipoitem = Tipoitem()
	tipoitem.nombre = kw['nombre']
	tipoitem.fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	DBSession.add(tipoitem)
	tipoitem_id = DBSession.query(Tipoitem.codtipoitem).filter_by(nombre=kw['nombre']).one()
	tipoitem_id = int(tipoitem_id[0])
	redirect("/CamposTipoDeItem/"+str(proyecto_id)+"/"+str(fase_id)+"/"+str(tipoitem_id))
	
    @expose('prueba.templates.crear_campos_tipoitem')
    def CamposTipoDeItem(self, proyecto_id, fase_id, tipoitem_id, **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	tipoitem = DBSession.query(Tipoitem).filter_by(codtipoitem=tipoitem_id).one()
	if 'nombre' and 'tipo' in kw:
		campo = Campo()
		campo.nombre=kw['nombre']
		campo.tipo=kw['tipo']
		campo.tipoitem = tipoitem
		DBSession.add(campo)
	campos = tipoitem.campos
	if not isinstance(campos, list):
		campos=[campos]
=======
    def NuevoTipoDeItem(self, proyecto_id, fase_id, **kw):
	#print kw
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
	#nombre=""
	#atributos=list()	
	#if 'nombre' in kw:
	#	nombre=kw['nombre']
	#if 'atributos' in kw:
	#	if not isinstance(fases, list):
	#		atributos=[atributos]
	#	atributos=atributos
<<<<<<< HEAD
	return dict(page='Creacion de tipos de item', proyecto=proyecto, fase=fase, tipoitem=tipoitem, campos=campos, value=kw)
    
=======
	return dict(page='Creacion de tipos de item', value=kw)
    
    @expose()
    def crearTipoDeItem(self, **kw):
	print kw
	#Fase = Fase()
	#fase.nombre = kw['nombre']
	#fase.descripcion = kw['descripcion']
	#fase.estado = "definicion"
	#import datetime
	#fase.fecha = datetime.date.today()
	#proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proy_id).one()
	#fase.proyecto = proyecto
	#proyecto.fases.append(fase)
	#fase.codproyecto=int(proy_id)
	#DBSession.add(fase)
    	flash("El tipo de item fue creado con exito")
    	#redirect("/NuevoTipoDeItem/"+proyecto_id+fase_id+atributo)

>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
    @expose('prueba.templates.tipos_de_items')
    def TipoDeItem(self, proyecto_id, fase_id, **kw):
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	fases = proyecto.fases
	if not isinstance(fases, list):
		fases = [fases]
	return dict(page='Tipos de item', proyecto=proyecto, fases=fases, fase=fase, value=kw)

    @expose('prueba.templates.campo_form')
    def NuevoCampo(self, proyecto_id, fase_id, **kw):
    	tmpl_context.form = crear_campo_form
    	return dict(modelname='Campo de Tipo de Item', value=kw)

    @expose('prueba.templates.elegir_tipoitem')
    def ElegirTipoItem(self, proyecto_id, fase_id, **kw):
	tipos_item = DBSession.query(Tipoitem).filter_by(codfase=fase_id).all()
	if not isinstance(tipos_item, list):
		tipos_item = [tipos_item]
	return dict(page='Creacion de Items', proyecto_id=proyecto_id, fase_id=fase_id, tipos_item=tipos_item, value=kw)

    @expose('prueba.templates.crear_item')
<<<<<<< HEAD
    def NuevoItem(self, proyecto_id, fase_id, tipoitem_id, **kw):
=======
    def NuevoItem(self, proyecto_id, fase_id, tipo_item, **kw):
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
	#en caso de error de validacion al crear item
	if 'nombre' in kw:
		nombre = kw['nombre']
	else:	
		nombre=""
	if 'complejidad' in kw:
		complejidad=kw['complejidad']
	else: 
		complejidad=""
	if 'prioridad' in kw:
		prioridad=kw['prioridad']
<<<<<<< HEAD
	else: 
		prioridad=""
	tipoitem = DBSession.query(Tipoitem).filter_by(codtipoitem=tipoitem_id).one()
	for campo in tipoitem.campos:
		campo.error=''
		if campo.nombre in kw:
			campo.tmp = kw[campo.nombre]
			if campo.tipo=="Integer":
				try:
					validator = validators.Int()
					validator.to_python(kw[campo.nombre])
				except formencode.Invalid, e:
					campo.error=unicode(e)
			if campo.tipo=="String":
				try:
					validator = validators.String()
					validator.to_python(kw[campo.nombre])
				except formencode.Invalid, e:
					campo.error=unicode(e)
			if campo.tipo=="Date":
				try:
					validator = validators.DateConverter()
					validator.to_python(kw[campo.nombre])
				except formencode.Invalid, e:
					campo.error=unicode(e)
		else:
			campo.tmp = ''
=======
	else:
		prioridad=""
	tipoitem = DBSession.query(Tipoitem).filter_by(codtipoitem=tipo_item).one()
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
	return dict(page='Creacion de Items', proyecto_id=proyecto_id, fase_id=fase_id, tipo_item=tipoitem, nombre=nombre, complejidad=complejidad, prioridad=prioridad, value=kw)

    @expose('')
    @validate({"nombre": NotEmpty(), "complejidad": Int(min=1, max=10), "prioridad": Int(min=1, max=10), }, error_handler=NuevoItem)
    def crearItem(self, proyecto_id, fase_id, tipoitem_id, **kw):
<<<<<<< HEAD
	tipoitem = DBSession.query(Tipoitem).filter_by(codtipoitem=tipoitem_id).one()
	#Valida cada atributo especifico del tipo de item
	for campo in tipoitem.campos:
		if campo.nombre in kw:
			if campo.tipo=="Integer":
				validator = validators.Int()
				validator.to_python(kw[campo.nombre])
			elif campo.tipo=="String":
				validator = validators.String()
				validator.to_python(kw[campo.nombre])
			elif campo.tipo=="Date":
				validator = validators.DateConverter()
				validator.to_python(kw[campo.nombre])
	##Una vez validados todos los campos, se crea el item
=======
	#print tipoitem_id
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
	item = Item()
	item.nombre=kw['nombre']
	item.complejidad=kw['complejidad']
	item.prioridad=kw['prioridad']
	item.version=1
	item.estado='desarrollo'
	import datetime
	item.fecha=datetime.date.today()
<<<<<<< HEAD
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	item.fase = fase
	item.tipoitem = tipoitem
	DBSession.add(item)
	fase.items.append(item)
	tipoitem.items.append(item)
	##Crear un atributo por cada campo del tipo de item
	for campo in tipoitem.campos:
		atributo = Atributo()
		atributo.campo = campo
		atributo.item = item
		if campo.nombre in kw:
			if campo.tipo=="Integer":
				atributo.valoratributo=kw[campo.nombre]
			elif campo.tipo=="String":
				atributo.valoratributo=kw[campo.nombre]
			elif campo.tipo=="Date":
				atributo.valoratributo=kw[campo.nombre]
		else:
			if campo.tipo=="Integer":
				atributo.valoratributo="0"
			elif campo.tipo=="String":
				atributo.valoratributo="."
			elif campo.tipo=="Date": 
				atributo.valoratributo=datetime.date.today()
		DBSession.add(atributo)
	self.crearHistorialDeItem(item)
	redirect("/IngresarFase/"+proyecto_id+"/"+fase_id)

    @expose('prueba.templates.consultar_item')
    def ConsultarItem(self, proyecto_id, fase_id, item_id, **kw):
	item=DBSession.query(Item).filter_by(coditem=item_id).one()
	aux=DBSession.query(Fase.orden).filter_by(codfase=fase_id).one()
	fase_orden=aux[0]
	aux=DBSession.query(Proyecto.cantfases).filter_by(codproyecto=proyecto_id).one()
	cantfases = aux[0]
	##Antecesores
	items_izq_id=DBSession.query(Relacion.coditeminicio).filter_by(coditemfin=item_id).filter_by(tipo="antecesor-sucesor").all()
	items_izq_nombre=list()
	for item_izq_id in items_izq_id:
		aux = DBSession.query(Item.nombre).filter_by(coditem=item_izq_id).one()
		items_izq_nombre.append(aux[0])
	##Sucesores
	items_der_id=DBSession.query(Relacion.coditemfin).filter_by(coditeminicio=item_id).filter_by(tipo="antecesor-sucesor").all()
	items_der_nombre=list()
	for item_der_id in items_der_id:
		aux = DBSession.query(Item.nombre).filter_by(coditem=item_der_id).one()
		items_der_nombre.append(aux[0])
	##Padres
	items_pad_id=DBSession.query(Relacion.coditeminicio).filter_by(coditemfin=item_id).filter_by(tipo="padre-hijo").all()
	items_pad_nombre=list()
	for item_pad_id in items_pad_id:
		aux = DBSession.query(Item.nombre).filter_by(coditem=item_pad_id).one()
		items_pad_nombre.append(aux[0])
	##Hijos
	items_hij_id=DBSession.query(Relacion.coditemfin).filter_by(coditeminicio=item_id).filter_by(tipo="padre-hijo").all()
	items_hij_nombre=list()
	for item_hij_id in items_hij_id:
		aux = DBSession.query(Item.nombre).filter_by(coditem=item_hij_id).one()
		items_hij_nombre.append(aux[0])
	return dict(page='Consulta de items', proyecto_id=proyecto_id, fase_id=fase_id, item=item, items_izq=items_izq_nombre, items_der=items_der_nombre, items_pad=items_pad_nombre, items_hij=items_hij_nombre, fase_orden=fase_orden, cantfases=cantfases, value=kw)

    @expose('prueba.templates.modificar_item')
    def Modificar_Item(self, proyecto_id, fase_id, item_id, **kw):
	fase_orden = DBSession.query(Fase.orden).filter_by(codfase=fase_id).one() ##orden de la fase
	fase_orden=fase_orden[0]
	cantfases=DBSession.query(Proyecto.cantfases).filter_by(codproyecto=proyecto_id).one()
	cantfases=cantfases[0]
	return dict(page="Modificacion de items", proyecto_id=proyecto_id, fase_id=fase_id, item_id=item_id, fase_orden=fase_orden, cantfases=cantfases)

    @expose('prueba.templates.editar_atributos')
    def ModificarAtributos(self, proyecto_id, fase_id, item_id, **kw):
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	estado = item.estado
	#en caso de error de validacion al crear item
	if 'nombre' in kw:
		nombre = kw['nombre']
	else:	
		nombre=item.nombre
	if 'complejidad' in kw:
		complejidad=kw['complejidad']
	else: 
		complejidad=item.complejidad
	if 'prioridad' in kw:
		prioridad=kw['prioridad']
	else: 
		prioridad=item.prioridad
	campos = item.tipoitem.campos
	atributos = item.atributos
	campos.sort()
	atributos.sort()
	for i, campo in enumerate(campos):
		if i==len(atributos):
			break
		if campo.nombre in kw:
			campo.tmp = kw[campo.nombre]
			campo.error=''
			if campo.tipo=="Integer":
				try:
					validator = validators.Int()
					validator.to_python(kw[campo.nombre])
				except formencode.Invalid, e:
					campo.error=unicode(e)
			if campo.tipo=="String":
				try:
					validator = validators.String()
					validator.to_python(kw[campo.nombre])
				except formencode.Invalid, e:
					campo.error=unicode(e)
			if campo.tipo=="Date":
				try:
					validator = validators.DateConverter(month_style="dd/mm/yyyy")
					validator.to_python(kw[campo.nombre])
				except formencode.Invalid, e:
					campo.error=unicode(e)
		else:
			campo.tmp = atributos[i].valoratributo
			campo.error=''
	return dict(page='Edicion de Items', proyecto_id=proyecto_id, fase_id=fase_id, item=item, estado=estado, nombre=nombre, complejidad=complejidad, prioridad=prioridad, campos=campos, value=kw)

    @expose()
    @validate({"nombre": NotEmpty(), "complejidad": Int(min=1, max=10), "prioridad": Int(min=1, max=10), }, error_handler=ModificarAtributos)
    def modificarAtributos(self, proyecto_id, fase_id, item_id, **kw):
	item=DBSession.query(Item).filter_by(coditem=item_id).one()
	tipoitem = item.tipoitem
	#Valida cada atributo especifico del tipo de item
	for campo in tipoitem.campos:
		campo.tmp=''
		campo.error=''
		if campo.nombre in kw:
			if campo.tipo=="Integer":
				validator = validators.Int()
				validator.to_python(kw[campo.nombre])
			elif campo.tipo=="String":
				validator = validators.String()
				validator.to_python(kw[campo.nombre])
			elif campo.tipo=="Date":
				validator = validators.DateConverter(month_style='dd/mm/yyyy')
				validator.to_python(kw[campo.nombre])
	#Actualiza historial de item
	self.actualizarHistorialDeItem(item)
	#Actualiza atributos comunes del item
	item.nombre=kw['nombre']
	item.complejidad=kw['complejidad']
	item.prioridad=kw['prioridad']
	item.version=item.version+1 #version['version']+1
	item.estado='espera'
	import datetime
	item.fecha=datetime.date.today()
	DBSession.flush()
	#Actualiza atributos especificos del tipo de item
	tipoitem.campos.sort()
	item.atributos.sort()
	cont=0 
	while(cont<len(item.atributos)):
		if tipoitem.campos[cont].nombre in kw: 
			#print 'campo.codcampo'
			#print tipoitem.campos[cont].codcampo
			item.atributos[cont].valoratributo=kw[tipoitem.campos[cont].nombre]
			#print item.atributos[cont].codcampo
		cont=cont+1
	##Verifica si el tipo de item tiene campos nuevos
	while(cont<len(tipoitem.campos)):
		atributo = Atributo()
		atributo.campo=tipoitem.campos[cont]
		atributo.item=item
		if kw[tipoitem.campos[cont].nombre] != '':
			atributo.valoratributo=kw[tipoitem.campos[cont].nombre]
		else:
			if tipoitem.campos[cont].tipo=="Integer":
				atributo.valoratributo=0
			if tipoitem.campos[cont].tipo=="String":
				atributo.valoratributo=' '
			if tipoitem.campos[cont].tipo=="Date":
				import datetime
				atributo.valoratributo=datetime.date.today()
		DBSession.add(atributo)
		cont=cont+1
	DBSession.flush()	
	redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)

    @expose('prueba.templates.crear_nuevo_antecesor')
    def CrearNuevoAntecesor(self, proyecto_id, fase_id, item_id, **kw):
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	#hallar antecesores actuales
	ant = DBSession.query(Relacion.coditeminicio).filter_by(coditemfin=item_id).filter_by(tipo='antecesor-sucesor').all()
	antecesores=list() ##lista de codigos de items
	for a in ant:
		antecesores.append(a[0])
	#hallar items de la fase anterior que no son antecesores
	fase_actual_orden = DBSession.query(Fase.orden).filter_by(codfase=fase_id).one()
	fase_anterior = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=fase_actual_orden[0]-1).one()
	todos = fase_anterior.items
	no_antecesores=list() ##lista de items
	for t in todos:
		if t.coditem not in antecesores:
			no_antecesores.append(t)	
	return dict(page="Crear nueva relacion", proyecto_id=proyecto_id, fase_id=fase_id, item=item, antecesores=antecesores, no_antecesores=no_antecesores)

    @expose()
    def crearNuevoAntecesor(self, proyecto_id, fase_id, item_id, **kw):
	if 'antecesor' not in kw:
		redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)	
	antecesor_id = kw['antecesor']
	relacion = Relacion()
	relacion.coditeminicio= antecesor_id
	relacion.coditemfin=item_id
	relacion.tipo='antecesor-sucesor'
	DBSession.add(relacion)
	redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)

    @expose('prueba.templates.eliminar_antecesor')
    def EliminarAntecesor(self, proyecto_id, fase_id, item_id, **kw):
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	#hallar antecesores actuales
	ant = DBSession.query(Relacion.coditeminicio).filter_by(coditemfin=item_id).filter_by(tipo='antecesor-sucesor').all()
	antecesores=list() ##lista de items
	for a in ant:
		aux = DBSession.query(Item).filter_by(coditem=a[0]).one()
		antecesores.append(aux)
	return dict(page="Eliminar relacion", proyecto_id=proyecto_id, fase_id=fase_id, item=item, antecesores=antecesores)

    @expose()
    def eliminarAntecesor(self, proyecto_id, fase_id, item_id, **kw):
	if 'antecesor' not in kw:
		redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)	
	antecesor_id = kw['antecesor']
	DBSession.delete(DBSession.query(Relacion).filter_by(coditeminicio=antecesor_id).filter_by(coditemfin=item_id).filter_by(tipo='antecesor-sucesor').one())
	redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)

    @expose('prueba.templates.crear_nuevo_sucesor')
    def CrearNuevoSucesor(self, proyecto_id, fase_id, item_id, **kw):
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	#hallar antecesores actuales
	suc = DBSession.query(Relacion.coditemfin).filter_by(coditeminicio=item_id).filter_by(tipo='antecesor-sucesor').all()
	sucesores=list() ##lista de codigos de items
	for s in suc:
		sucesores.append(s[0])
	#hallar items de la fase anterior que no son antecesores
	fase_actual_orden = DBSession.query(Fase.orden).filter_by(codfase=fase_id).one()
	fase_posterior = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=fase_actual_orden[0]+1).one()
	todos = fase_posterior.items
	no_sucesores=list() ##lista de items
	for t in todos:
		if t.coditem not in sucesores:
			no_sucesores.append(t)	
	return dict(page="Crear nueva relacion", proyecto_id=proyecto_id, fase_id=fase_id, item=item, sucesores=sucesores, no_sucesores=no_sucesores)

    @expose()
    def crearNuevoSucesor(self, proyecto_id, fase_id, item_id, **kw):
	if 'sucesor' not in kw:
		redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)	
	sucesor_id = kw['sucesor']
	relacion = Relacion()
	relacion.coditeminicio= item_id
	relacion.coditemfin=sucesor_id
	relacion.tipo='antecesor-sucesor'
	DBSession.add(relacion)
	redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)

    @expose('prueba.templates.eliminar_sucesor')
    def EliminarSucesor(self, proyecto_id, fase_id, item_id, **kw):
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	#hallar antecesores actuales
	suc = DBSession.query(Relacion.coditemfin).filter_by(coditeminicio=item_id).filter_by(tipo='antecesor-sucesor').all()
	sucesores=list() ##lista de items
	for s in suc:
		aux = DBSession.query(Item).filter_by(coditem=s[0]).one()
		sucesores.append(aux)
	return dict(page="Eliminar relacion", proyecto_id=proyecto_id, fase_id=fase_id, item=item, sucesores=sucesores)

    @expose()
    def eliminarSucesor(self, proyecto_id, fase_id, item_id, **kw):
	if 'sucesor' not in kw:
		redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)	
	sucesor_id = kw['sucesor']
	DBSession.delete(DBSession.query(Relacion).filter_by(coditeminicio=item_id).filter_by(coditemfin=sucesor_id).filter_by(tipo='antecesor-sucesor').one())
	redirect("/ConsultarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)

    @expose('prueba.templates.confirmacion_eliminacion')
    def EliminarItem(self, proyecto_id, fase_id, item_id, **kw):
	item=DBSession.query(Item).filter_by(coditem=item_id).one()
	return dict(page=u"Confirmacion de eliminación de item", proyecto_id=proyecto_id, fase_id=fase_id, item_id=item_id, item=item)

    @expose()
    def eliminarItem(self, proyecto_id, fase_id, item_id, **kw):
	if 'aceptar' in kw:
		item=DBSession.query(Item).filter_by(coditem=item_id).one()
		item.estado="eliminado"
		#Actualiza historial de item
		self.actualizarHistorialDeItem(item)
		relaciones = DBSession.query(Relacion).filter(or_(Relacion.coditeminicio==item_id, Relacion.coditemfin==item_id)).all()
		for relacion in relaciones:
			DBSession.delete(relacion)
		for atributo in item.atributos:
			DBSession.delete(atributo)
		DBSession.delete(item)
	redirect("/IngresarFase/"+proyecto_id+"/"+fase_id)

    @expose('prueba.templates.listar_items_eliminados')
    def ListarItemsEliminados(self, proyecto_id, fase_id, **kw):
	items = DBSession.query(ItemHistorial).filter_by(estado="eliminado").filter_by(codfase=fase_id).all()
	return dict(page=u"Lista de ítems eliminados de la fase", proyecto_id=proyecto_id, fase_id=fase_id, items=items)

    @expose()
    def RevivirItem(self, proyecto_id, fase_id, item_id, version):
    	itemhistorial = DBSession.query(ItemHistorial).filter_by(coditem=item_id).filter_by(version=version).one()
	itemhistorial.estado="revivido"
	DBSession.flush()
	item = Item()
	##Atributos comunes 
	item.coditem=itemhistorial.coditem
	item.nombre=itemhistorial.nombre
	item.complejidad=itemhistorial.complejidad
	item.prioridad=itemhistorial.prioridad
	item.version=itemhistorial.version+1
	item.estado='desarrollo'
	import datetime
	item.fecha=datetime.date.today()
	item.codfase=itemhistorial.codfase
	item.codtipoitem=itemhistorial.codtipoitem
	DBSession.add(item)
	##Atributos específicos
	tipoitem = DBSession.query(Tipoitem).filter_by(codtipoitem=itemhistorial.codtipoitem).one()
	campos = tipoitem.campos
	atributos = itemhistorial.atributos
	print 'atributos'
	print atributos
	cont=0 
	for atrib in atributos:
		atributo=Atributo()
		atributo.codcampo=atrib.codcampo
		atributo.coditem=atrib.coditem
		atributo.valoratributo=atrib.valor
		DBSession.add(atributo)
		cont = cont+1
	if (len(campos)>cont):
		while(cont<len(campos)):
			atributo=Atributo()
			atributo.codcampo=campos[cont].codcampo
			atributo.coditem=itemhistorial.coditem
			if campos[cont].tipo=="Integer":
				atributo.valoratributo=0
			if campos[cont].tipo=="String":
				atributo.valoratributo=' '
			if campos[cont].tipo=="Date":
				import datetime
				atributo.valoratributo=datetime.date.today()
			cont=cont+1
=======
	tipoitem = DBSession.query(Tipoitem).filter_by(codtipoitem=tipoitem_id).one()
	item.tipoitem = tipoitem
	fase = DBSession.query(Fase).filter_by(codfase=fase_id).one()
	#print fase
	#print item.fase
	item.fase = fase
	#print tipoitem
	DBSession.add(item)
	fase.items.append(item)
	tipoitem.items.append(item)
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
	redirect("/IngresarFase/"+proyecto_id+"/"+fase_id)

    @expose('prueba.templates.editar_item')
    def ModificarItem(self, proyecto_id, fase_id, item_id, **kw):
<<<<<<< HEAD
=======
	print kw
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	tipoitem = item.tipoitem
	###Listar items de la fase anterior y de la fase posterior
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	orden_fase = item.fase.orden
	orden_izq = orden_fase-1
	orden_der =  orden_fase+1
	items_izq=list()
	items_der=list()
<<<<<<< HEAD
	izq=list()
	der=list()
	if orden_fase > 1:
		fase_izq = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=orden_izq).one() #fase anterior
		items_izq = fase_izq.items #todos los items de la fase anterior 
		relaciones_izq = DBSession.query(Relacion).filter_by(coditemfin=item_id).all()
		for relacion in relaciones_izq:
			izq.append(relacion.coditeminicio)
		##poner en revision los antecesores
		#rel_ant = DBSession.query(Relacion).filter_by(coditemfin=item_id).filter_by(tipo='antecesor-sucesor').all()
		#print rel_ant
		#for relacion in rel_ant:
		#	item = DBSession.query(Item).get()
	if orden_fase < proyecto.cantfases:
		fase_der = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=orden_der).one()
		items_der = fase_der.items
		relaciones_der = DBSession.query(Relacion).filter_by(coditeminicio=item_id).all()
		for relacion in relaciones_der:
			der.append(relacion.coditemfin)
	#Listar ítems de la fase actual
	items_act = item.fase.items
	#relaciones_act = DBSession.query(Relacion).filter(or_(Relacion.coditeminicio=item_id, Relacion.coditemfin=item_id)).all()
	#for relacion in relaciones_act:
	#	act.append(relacion.coditeminicio)
	estado = item.estado
	return dict(page='Edicion de Items', proyecto_id=proyecto_id, fase_id=fase_id, item=item, tipoitem=tipoitem, items_izq=items_izq, items_der=items_der, items_act=items_act, izq=izq, der=der, estado=estado, value=kw)

    @expose('prueba.templates.revisar_item')
    def RevisarItem(self, proyecto_id, fase_id, item_id, **kw):
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	tipoitem = item.tipoitem
	###Listar items de la fase anterior y de la fase posterior
	proyecto = DBSession.query(Proyecto).filter_by(codproyecto=proyecto_id).one()
	orden_fase = item.fase.orden
	orden_izq = orden_fase-1
	orden_der =  orden_fase+1
	items_izq=list()
	items_der=list()
	izq=list()
	der=list()
	if orden_fase > 1:
		fase_izq = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=orden_izq).one() #fase anterior
		items_izq = fase_izq.items #todos los items de la fase anterior 
		relaciones_izq = DBSession.query(Relacion).filter_by(coditemfin=item_id).all()
		for relacion in relaciones_izq:
			izq.append(relacion.coditeminicio)		
	if orden_fase < proyecto.cantfases:
		fase_der = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=orden_der).one()
		items_der = fase_der.items
		relaciones_der = DBSession.query(Relacion).filter_by(coditeminicio=item_id).all()
		for relacion in relaciones_der:
			der.append(relacion.coditemfin)
	#Listar ítems de la fase actual
	items_act = item.fase.items
	#relaciones_act = DBSession.query(Relacion).filter(or_(Relacion.coditeminicio=item_id, Relacion.coditemfin=item_id)).all()
	#for relacion in relaciones_act:
	#	act.append(relacion.coditeminicio)
	return dict(page='Revision de Items', proyecto_id=proyecto_id, fase_id=fase_id, item=item, tipoitem=tipoitem, items_izq=items_izq, items_der=items_der, items_act=items_act, izq=izq, der=der, value=kw)

    @expose()
    def revisarItem(self, proyecto_id, fase_id, item_id, **kw):
	if 'modificar' in kw:
		if kw['modificar']=='Modificar':
			redirect("/ModificarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)
		elif kw['modificar']=='NO Modificar':
			print '**'
			
#@expose(...)
#def handle_form(self, *args, **kwargs):
#  if 'submit_foo' in kwargs:
#    return self.handle_form_foo(*args, **kwargs)
#  elif 'submit_bar' in kwargs:
#    return self.handle_form_bar(*args, **kwargs)
#def handle_form_foo(self, *args, **kwargs):
  # Do foo things
#def handle_form_bar(self, *args, **kwargs):
  # Do bar things
    @expose()
    def modificarItem(self, proyecto_id, fase_id, item_id, **kw):
	if 'modificar' in kw:
		#redirect("/editarItem/"+proyecto_id+"/"+fase_id+"/"+item_id)
		self.editarItem(proyecto_id, fase_id, item_id, **kw)
	if 'revision' in kw:
		self.editarItemPorRevision(proyecto_id, fase_id, item_id, **kw)
=======
	if orden_fase > 1:
		fase_izq = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=orden_izq).one()
		items_izq = fase_izq.items
	if orden_fase < proyecto.cantfases:
		fase_der = DBSession.query(Fase).filter_by(codproyecto=proyecto_id).filter_by(orden=orden_der).one()
		items_der = fase_der.items
	return dict(page='Edicion de Items', proyecto_id=proyecto_id, fase_id=fase_id, item=item, tipoitem=tipoitem, items_izq=items_izq, items_der=items_der, value=kw)
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

    @expose('')
    @validate({"nombre": NotEmpty(), "complejidad": Int(min=1, max=10), "prioridad": Int(min=1, max=10), }, error_handler=ModificarItem)
    def editarItem(self, proyecto_id, fase_id, item_id, **kw):
<<<<<<< HEAD
	#Actualiza tipo de item
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	#self.actualizarHistorialDeItem(item)
	#Actualiza atributos comunes del item
	item.nombre=kw['nombre']
	item.complejidad=kw['complejidad']
	item.prioridad=kw['prioridad']
	item.version=item.version+1 #version['version']+1
	item.estado='espera'
	import datetime
	item.fecha=datetime.date.today()
	DBSession.flush()
	#Actualiza atributos especificos del tipo de item
	#for campo in tipoitem.campos:
	#	if campo.nombre in kw:
	#		atributo.valoratributo=kw[campo.nombre]
	#	else:
	#		if campo.tipo=="Integer":
	#			atributo.valoratributo=0
	#		if campo.tipo=="String":
	#			atributo.valoratributo=''
	#		if campo.tipo=="Date":
	#			import datetime
	#			item.fecha=datetime.date.today()
	#	DBSession.flush()
	#	print atributovalortributo
	#		DBSession.add()
	##########Guardar en la tabla 'modificacion'
	##########modificacion = Modificacion()
	##########modificacion.coditem = item.coditem
	##########modificacion.origen = 1
	##########DBSession.add(modificacion)
	##Crear las relaciones
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	#print 'version'
	#print item.version
	  ## items_izq es una lista con los items seleccionados en el <select> como antecesores
	if 'items_izq' in kw: 
		items_izq = kw['items_izq']
		if not isinstance(items_izq, list):
			items_izq = [items_izq]
	else:
		items_izq=list()
	  ## items_der es una lista con los items seleccionados en el <select> como sucesores
	if 'items_der' in kw: 
		items_der = kw['items_der']
		if not isinstance(items_der, list):
			items_der = [items_der]
	else:
		items_der=list()
	for item_izq in items_izq:
		relacion = Relacion()
		relacion.coditeminicio= int(item_izq)
		relacion.coditemfin=item_id
		relacion.tipo='antecesor-sucesor'
		try:
			DBSession.query(Relacion).filter_by(coditeminicio=int(item_izq)).filter_by(coditemfin=item_id).one()
		except NoResultFound, e:
			DBSession.add(relacion)
		##Poner en revision a los items antecesores
		##########antecesor = DBSession.query(Item).filter_by(coditem=relacion.coditeminicio).one()
		##########antecesor.estado='revision'
		##########DBSession.flush()
	#	  ##Agregar a la tabla 'modificacion'
	#	##########modificacion = Modificacion()
	#	##########modificacion.coditem = relacion.coditeminicio
	#	##########modificacion.origen = 0
	#	##########DBSession.add(modificacion)
	#	  ##Agregar a la tabla 'revision'
	#	##########revision = Revision()
	#	##########revision.inicio=item.coditem
	#	##########revision.actual=relacion.coditeminicio
	#	##########revision.anterior=item.coditem
	#	##########DBSession.add(revision)
	for item_der in items_der:
		relacion = Relacion()
		relacion.coditeminicio= item_id
		relacion.coditemfin=int(item_der)
		relacion.tipo='antecesor-sucesor'
		try:
			DBSession.query(Relacion).filter_by(coditeminicio=item_id).filter_by(coditemfin=int(item_der)).one()
		except NoResultFound, e:
			DBSession.add(relacion)
	#	##Poner en revision a los items sucesores
	#	##########sucesor = DBSession.query(Item).filter_by(coditem=relacion.coditemfin).one()
	#	##########sucesor.estado='revision'
	#	##########DBSession.flush()
	#	  ##Agregar a la tabla 'modificacion'
	#	##########modificacion = Modificacion()
	#	##########modificacion.coditem = relacion.coditemfin
	#	##########modificacion.origen = 0
	#	##########DBSession.add(modificacion)
	#	  ##Agregar a la tabla 'revision'
	#	##########revision = Revision()
	#	##########revision.inicio=item.coditem
	#	##########revision.actual=relacion.coditemfin
	#	##########revision.anterior=item.coditem
	#	##########DBSession.add(revision)
	redirect("/IngresarFase/"+proyecto_id+"/"+fase_id)

    @expose('')
    @validate({"nombre": NotEmpty(), "complejidad": Int(min=1, max=10), "prioridad": Int(min=1, max=10), }, error_handler=ModificarItem)
    def editarItemPorRevision(self, proyecto_id, fase_id, item_id, **kw):
=======
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	item.nombre=kw['nombre']
	item.complejidad=kw['complejidad']
	item.prioridad=kw['prioridad']
	item.version=1
<<<<<<< HEAD
	item.estado='espera'
	import datetime
	item.fecha=datetime.date.today()
	DBSession.flush()
        ##Buscar apariciones  de item_id en revision.actual
	procesos = DBSession.query(distinct(Revision.inicio)).filter_by(actual=item_id).all()
	##Crear las relaciones
	item = DBSession.query(Item).filter_by(coditem=item_id).one()
	  ## items_izq es una lista con los items seleccionados en el <select> como antecesores
	if 'items_izq' in kw: 
=======
	item.estado='definicion'
	import datetime
	item.fecha=datetime.date.today()
	DBSession.flush()
	##Crear las relaciones
	if 'items_izq' in kw:
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
		items_izq = kw['items_izq']
		if not isinstance(items_izq, list):
			items_izq = [items_izq]
	else:
		items_izq=list()
<<<<<<< HEAD
	  ## items_der es una lista con los items seleccionados en el <select> como sucesores
	if 'items_der' in kw: 
=======
	if 'items_der' in kw:
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
		items_der = kw['items_der']
		if not isinstance(items_der, list):
			items_der = [items_der]
	else:
		items_der=list()
<<<<<<< HEAD
	cont=0
	for item_izq in items_izq:
		relacion = Relacion()
		relacion.coditeminicio= int(item_izq)
		relacion.coditemfin=item_id
		relacion.tipo='antecesor-sucesor'
		try:
			DBSession.query(Relacion).filter_by(coditeminicio=int(item_izq)).filter_by(coditemfin=item_id).one()
		except NoResultFound, e:
			DBSession.add(relacion)
		##Poner en revision a los items sucesores
		agregado = self.procesarRevision(item_id, int(item_izq), procesos)
		if agregado['agregado']==True:
			cont=cont+1
	for item_der in items_der:
		relacion = Relacion()
		relacion.coditeminicio= item_id
		relacion.coditemfin=int(item_der)
		relacion.tipo='antecesor-sucesor'
		try:
			DBSession.query(Relacion).filter_by(coditeminicio=item_id).filter_by(coditemfin=int(item_der)).one()
		except NoResultFound, e:
			DBSession.add(relacion)
		##Poner en revision a los items sucesores
		agregado = self.procesarRevision(item_id, int(item_der), procesos)
		if agregado['agregado']==True:
			cont=cont+1
	if cont==0:
		##Se eliminan las filas de revision donde revision.actual=item_id
		revisiones = DBSession.query(Revision).filter_by(actual=item_id).all()
		for revision in revisiones:
			DBSession.delete(revision)
			try:
				rev = DBSession.query(Revision).filter_by(anterior=revision.anterior).one()
			except:
				self.funcion(revision.inicio, revision.actual, revision.anterior, revision.actual)
		##Se elimina la fila de la tabla modificacion donde modificacion.coditem=item_id
		DBSession.delete(DBSession.query(Modificacion).filter_by(coditem=item_id).one())
		##Se cambia el estado al item
		item=DBSession.query(Item).filter_by(coditem=item_id).one()
		item.estado="desarrollo"
		DBSession.flush()
	redirect("/IngresarFase/"+proyecto_id+"/"+fase_id)

    @expose('')
    def funcion(self, inicio, actual, anterior, ant):
	if (inicio==anterior):
		##Comprobar si se debe eliminar de la tabla revision
		try:
			rev = DBSession.query(Revision).filter_by(actual=ant).one()
			DBSession.delete(DBSession.query(Revision).filter_by(inicio=inicio).filter_by(actual=actual).filter_by(anterior=anterior).one())			
			DBSession.delete(DBSession.query(Modificacion).filter_by(coditem=actual).one())
			item = DBSession.query(Item).filter_by(coditem=actual).one()
			item.estado="desarrollo"
			DBSession.flush()
		except:
			print 'k'
		##Comprobar si se debe eliminar de la tabla modificacion
		rev = DBSession.query(Revision).filter_by(actual=actual).first()
		if rev is None:
			DBSession.delete(DBSession.query(Modificacion).filter_by(coditem=actual).one())
			item = DBSession.query(Item).filter_by(coditem=actual).one()
			item.estado="desarrollo"
			DBSession.flush()
		##Comprobar si se debe eliminar de la tabla de modificacion el origen de proceso
		try:
			rev = DBSession.query(Revision).filter_by(inicio=inicio).one()
			DBSession.delete(DBSession.query(Modificacion).filter_by(coditem=inicio).one())
			item = DBSession.query(Item).filter_by(coditem=inicio).one()
			item.estado="desarrollo"
			DBSession.flush()
		except:
			print 'k'
		return
	else:
		rev = DBSession.query(Revision).filter_by(actual=anterior).all()
		for r in rev:
			self.funcion(r.inicio, r.actual, r.anterior, ant)
		DBSession.delete(DBSession.query(Revision).filter_by(inicio=inicio).filter_by(actual=actual).filter_by(anterior=anterior).one())
		item = DBSession.query(Item).filter_by(coditem=actual).one()
		item.estado="desarrollo"
		DBSession.flush()

    @expose('')
    def procesarRevision(self, item_id, item_der, procesos):
	agregado=False
	##esta sucesor_id en revision.actual?
	esta_en_actual=False
	revision = DBSession.query(Revision).filter_by(actual=item_der).first()
	if revision is not None:
		esta_en_actual=True ##esta_en_actual=True significa que sucesor_id esta en revision.actual
	##esta sucesor_id en revision.inicio?	
	esta_en_inicio=False
	revision = DBSession.query(Revision).filter_by(inicio=item_der).first()
	if revision is None:
		esta_en_inicio=True ##esta_en_inicio=True significa que sucesor_id no esta en revision.inicio
	##esta sucesor_id en revision.anterior?
	esta_en_anterior = False
	revision = DBSession.query(Revision).filter_by(anterior=item_der).first()
	if revision is None:
		esta_en_anterior=True ##esta_en_anterior=True significa que sucesor_id no esta en revision.anterior
	##iterar procesos --> si sucesor_id esta en revision.actual
	if esta_en_actual and esta_en_inicio and esta_en_anterior:
		for proceso in procesos:
			ini = proceso[0]
			#directo = False
			#revision = DBSession.query(Revision).filter_by(inicio=ini).filter_by(actual=item_der).filter_by(anterior=ini).first()
			#if revision is None:
			#	directo=True
			inverso = False
			revision = DBSession.query(Revision).filter_by(inicio=ini).filter_by(actual=item_id).filter_by(anterior=item_der).first()
			if revision is None:
				inverso=True
			#if directo and inverso:
			if inverso:
				revision=Revision()
				revision.inicio=ini
				revision.actual=item_der
				revision.anterior=item_id
				DBSession.add(revision)
				agregado=True
				sucesor = DBSession.query(Item).filter_by(coditem=item_der).one()
				sucesor.estado='revision'
				DBSession.flush()
	##iterar procesos --> si sucesor_id no esta en revision.actual
	if esta_en_actual==False and esta_en_inicio:
		modificacion = Modificacion()
		modificacion.coditem=item_der
		modificacion.origen=0
		DBSession.add(modificacion)
		for proceso in procesos:
			ini = proceso[0]
			inverso = False
			revision = DBSession.query(Revision).filter_by(inicio=ini).filter_by(actual=item_id).filter_by(anterior=item_der).first()
			if revision is None:
				inverso=True
			if inverso:
				revision=Revision()
				revision.inicio=ini
				revision.actual=item_der
				revision.anterior=item_id
				DBSession.add(revision)
				agregado=True
				sucesor = DBSession.query(Item).filter_by(coditem=item_der).one()
				sucesor.estado='revision'
				DBSession.flush()
	return dict(agregado=agregado)
 
    @expose()
    def crearHistorialDeItem(self, item):
	historial = HistorialItem()
	historial.coditem = item.coditem
	DBSession.add(historial)	
	return

    @expose()
    def actualizarHistorialDeItem(self, item):
	historial = DBSession.query(HistorialItem).filter_by(coditem=item.coditem).one()
	item_historial = ItemHistorial()
	item_historial.coditem=item.coditem
	item_historial.version=item.version
	item_historial.historial=historial
	item_historial.nombre=item.nombre
	item_historial.complejidad=item.complejidad
	item_historial.prioridad=item.prioridad
	item_historial.estado=item.estado
	item_historial.fecha=item.fecha
	item_historial.codtipoitem=item.codtipoitem
	item_historial.codfase=item.codfase
	DBSession.add(item_historial)
	#historial.versiones.append(item_historial)
	##Copia los atributos especificos del tipo de item
	for atributo in item.atributos:
		atributo_historial = AtributoHistorial()
		atributo_historial.coditem=item_historial.coditem
		atributo_historial.version=item_historial.version
		atributo_historial.codcampo=atributo.codcampo
		atributo_historial.valor=atributo.valoratributo
		DBSession.add(atributo_historial)
	##Copia las relaciones
	antecesores=DBSession.query(Relacion).filter_by(coditemfin=item.coditem).filter_by(tipo='antecesor-sucesor').all()
	sucesores=DBSession.query(Relacion).filter_by(coditeminicio=item.coditem).filter_by(tipo='antecesor-sucesor').all()
	padres=DBSession.query(Relacion).filter_by(coditemfin=item.coditem).filter_by(tipo='padre-hijo').all()
	hijos=DBSession.query(Relacion).filter_by(coditeminicio=item.coditem).filter_by(tipo='padre-hijo').all()
	  ##Antecesores
	for antecesor in antecesores:
		relacion_historial=RelacionHistorial()
		relacion_historial.coditem2=antecesor.coditeminicio
		item_a=DBSession.query(Item).filter_by(coditem=antecesor.coditeminicio).one()
		relacion_historial.version2=item_a.version
		relacion_historial.coditem1=item.coditem
		relacion_historial.version1=item.version
		relacion_historial.tipo='antecesor'
		DBSession.add(relacion_historial)
	  ##Sucesores
	for sucesor in sucesores:
		relacion_historial=RelacionHistorial()
		relacion_historial.coditem2=sucesor.coditemfin
		item_s=DBSession.query(Item).filter_by(coditem=sucesor.coditemfin).one()
		relacion_historial.version2=item_s.version
		relacion_historial.coditem1=item.coditem
		relacion_historial.version1=item.version
		relacion_historial.tipo='sucesor'
		DBSession.add(relacion_historial)
	  ##Padres
	for padre in padres:
		relacion_historial=RelacionHistorial()
		relacion_historial.coditem2=padre.coditeminicio
		item_p=DBSession.query(Item).filter_by(coditem=padre.coditeminicio).one()
		relacion_historial.version2=item_p.version
		relacion_historial.coditem1=item.coditem
		relacion_historial.version1=item.version
		relacion_historial.tipo='padre'
		DBSession.add(relacion_historial)
	  ##Hijos
	for hijo in hijos:
		relacion_historial=RelacionHistorial()
		relacion_historial.coditem2=hijo.coditemfin
		item_h=DBSession.query(Item).filter_by(coditem=hijo.coditemfin).one()
		relacion_historial.version2=item_h.version
		relacion_historial.coditem1=item.coditem
		relacion_historial.version1=item.version
		relacion_historial.tipo='hijo'
		DBSession.add(relacion_historial)
	return

    @expose('prueba.templates.ingresar_historial')
    def IngresarHistorial(self, proyecto_id, fase_id, item_id, **kw):
	#items = DBSession.query(ItemHistorial).filter_by(coditem=item_id).all()
	historial = DBSession.query(HistorialItem).filter_by(coditem=item_id).one()
	return dict(page='Historial de item', proyecto_id=proyecto_id, fase_id=fase_id, historial=historial, value=kw)

    @expose('prueba.templates.ingresar_historial_para_revertir')
    def IngresarHistorialParaRevertir(self, proyecto_id, fase_id, item_id, **kw):
	#items = DBSession.query(ItemHistorial).filter_by(coditem=item_id).all()
	historial = DBSession.query(HistorialItem).filter_by(coditem=item_id).one()
	return dict(page='Historial de item', proyecto_id=proyecto_id, fase_id=fase_id, historial=historial, value=kw)

    @expose()
    def RevertirItem(self, proyecto_id, fase_id, item_id, version):
	#Guardar version actual en el historial
	item_version_actual = DBSession.query(Item).filter_by(coditem=item_id).one()
	self.actualizarHistorialDeItem(item_version_actual)
	#Traer del historial la version a revertir
	item_version_anterior = DBSession.query(ItemHistorial).filter_by(coditem=item_id).filter_by(version=version).one()
	#Actualizar atributos comunes
	
	
	redirect('/ConsultarItem/' + proyecto_id + '/' + fase_id + '/' + item_id)

    @expose('prueba.templates.consultar_itemhistorial')
    def ConsultarItemHistorial(self, proyecto_id, fase_id, item_id, item_version, **kw):
	#Para la informacion general
	item=DBSession.query(ItemHistorial).filter_by(coditem=item_id).filter_by(version=item_version).one()
	tipoitem=DBSession.query(Tipoitem).filter_by(codtipoitem=item.codtipoitem).one()
	#Para los atributos especificos del tipo de item
	atributos=DBSession.query(AtributoHistorial).filter_by(coditem=item_id).filter_by(version=item_version).all()
	#Para recuperar las relaciones
	aux=DBSession.query(Fase.orden).filter_by(codfase=fase_id).one()
	fase_orden=aux[0]
	aux=DBSession.query(Proyecto.cantfases).filter_by(codproyecto=proyecto_id).one()
	cantfases = aux[0]
	#print 'EMPIEZA'
	#relaciones = item.relaciones
	#for relacion in relaciones:
	#	print type(relacion)
	#	print 'relaciones'
	#	print relacion.coditem1
        #	print relacion.version1
	#	print relacion.coditem2
	#	print relacion.version2
	#	print relacion.tipo
	##Antecesores
	items_izq = DBSession.query(RelacionHistorial).filter_by(coditem1=item_id).filter_by(version1=item_version).filter_by(tipo='antecesor').all()
	##Sucesores
	items_der = DBSession.query(RelacionHistorial).filter_by(coditem1=item_id).filter_by(version1=item_version).filter_by(tipo='sucesor').all()
	##Padres
	items_pad = DBSession.query(RelacionHistorial).filter_by(coditem1=item_id).filter_by(version1=item_version).filter_by(tipo='padre').all()
	##Hijos
	items_hij = DBSession.query(RelacionHistorial).filter_by(coditem1=item_id).filter_by(version1=item_version).filter_by(tipo='hijo').all()
	return dict(page='Consulta de item historial', proyecto_id=proyecto_id, fase_id=fase_id, item=item, tipoitem=tipoitem, fase_orden=fase_orden, cantfases=cantfases, atributos=atributos, items_izq=items_izq, items_der=items_der, items_pad=items_pad, items_hij=items_hij, value=kw)

=======
	for item in items_izq:
		relacion = Relacion()
		relacion.coditeminicio= int(item)
		relacion.coditemfin=item_id
		relacion.tipo='antecesor-sucesor'
		DBSession.add(relacion)
	for item in items_der:
		relacion = Relacion()
		relacion.coditeminicio= item_id
		relacion.coditemfin=int(item)
		relacion.tipo='antecesor-sucesor'
		DBSession.add(relacion)
	redirect("/IngresarFase/"+proyecto_id+"/"+fase_id)

>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
    @expose('prueba.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('prueba.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(environment=request.environ)

    @expose('prueba.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params=kw)

    @expose('prueba.templates.authentication')
    def auth(self):
        """Display some information about auth* on this application."""
        return dict(page='auth')

    @expose('prueba.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('prueba.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('prueba.templates.login')
    def login(self, came_from=url('/')):
        """Start the user login."""
        login_counter = request.environ['repoze.who.logins']
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)

    @expose()
    def post_login(self, came_from='/'):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ['repoze.who.logins'] + 1
            redirect('/login', came_from=came_from, __logins=login_counter)
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from=url('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)
<<<<<<< HEAD

#>>> from sqlalchemy.orm.exc import NoResultFound
#>>> try: 
#...     user = query.filter(User.id == 99).one()
#... except NoResultFound, e:
#...     print e
#No row was found for one()

#>>> from sqlalchemy.orm.exc import MultipleResultsFound
#>>> try: 
#...     user = query.one()
#... except MultipleResultsFound, e:
#...     print e
# Multiple rows were found for one()
=======
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
