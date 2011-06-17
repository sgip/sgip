from sqlalchemy import *
from sqlalchemy.orm import mapper, relation, backref, relationship
from sqlalchemy.types import Integer, String, Text, Date
from prueba.model import DeclarativeBase, metadata, DBSession


#class Usuario(DeclarativeBase):
#    __tablename__ = 'usuario'
#    #column definitions
#    codusuario = Column(u'codusuario', Integer, primary_key=True)
#    nombre = Column(u'nombre', String(20), nullable=False)
#    apellido = Column(u'apellido', String(20), nullable=False)
#    contrasena = Column(u'contrasena', String(30), nullable=False)
#    telefono = Column(u'telefono', String(15), nullable=False)
#    direccion = Column(u'direccion', String(30), nullable=False)
#    email = Column(u'email', String(30), nullable=False)

#class Rol(DeclarativeBase):
#    __tablename__ = 'rol'
    #column definitions
#    codrol = Column(u'codrol', Integer, primary_key=True)
#    nombre = Column(u'nombre', String(20), nullable=False)   
#    descripcion = Column(u'descripcion', String(100), nullable=True)

class Proyecto(DeclarativeBase):
    __tablename__ = 'proyecto'
    #column definitions
    codproyecto = Column(u'codproyecto', Integer, primary_key=True)
    nombre = Column(u'nombre', String(20), nullable=False)
    estado = Column(u'estado', String(10), nullable=False)
    fecha = Column(u'fecha', Date, nullable=False)
    cantfases = Column(u'cantfases', Integer)
    def __repr__(self):
        return ('<Proyecto: id=%r, nombre=%r, estado=%r, fases=%r' % (
                self.codproyecto, self.nombre, self.estado, self.fases)).encode('utf-8')
    def __unicode__(self):
        return self.nombre

class Fase(DeclarativeBase):
    __tablename__ = 'fase'
    #column definitions
    codfase = Column(u'codfase', Integer, primary_key=True)
    codproyecto = Column(u'codproyecto', Integer, ForeignKey('proyecto.codproyecto'), nullable=False)
    #proyecto = relationship('Proyecto', backref='fases')
    proyecto = relation('Proyecto', backref='fases')
    nombre = Column(u'nombre', String(20), nullable=False)
    descripcion = Column(u'descripcion', String(100))
    estado = Column(u'estado', String(10), nullable=False)
    fecha = Column(u'fecha', Date, nullable=False)
    orden = Column(u'orden', Integer)
    def __repr__(self):
        return ('<Fase: id=%r, name=%r, descripcion=%r' % (
               self.codfase, self.nombre, self.descripcion)).encode('utf-8')
    def __unicode__(self):
        return self.nombre

<<<<<<< HEAD
class Modificacion(DeclarativeBase):
    __tablename__ = 'modificacion'
    #column definitions
    coditem = Column(u'coditem', Integer, primary_key=True, autoincrement=False)
    origen = Column(u'origen', Integer, nullable=False) ##1 si es origen de proceso de cambios, 0 si no es origen de cambios

class Revision(DeclarativeBase):
    __tablename__ = 'revision'
    #column definitions
    inicio = Column(u'inicio', Integer, primary_key=True, autoincrement=False)
    actual = Column(u'actual', Integer, primary_key=True, autoincrement=False)
    anterior = Column(u'anterior', Integer, primary_key=True, autoincrement=False)

=======
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
class Lineabase(DeclarativeBase):
    __tablename__ = 'lineabase'
    #column definitions
    codlineabase = Column(u'codlineabase', Integer, primary_key=True)
    codfase = Column(u'codfase', Integer, ForeignKey('fase.codfase'))
    descripcion = Column(u'descripcion', String(100), nullable=True)
    estado = Column(u'estado', String(10), nullable=False)

class Tipoitem(DeclarativeBase):
    __tablename__ = 'tipoitem'
    #column definitions
    codtipoitem = Column(u'codtipoitem', Integer, primary_key=True)
    codfase = Column(u'codfase', Integer, ForeignKey('fase.codfase'), nullable=True)
    fase = relation('Fase', backref="tipos_de_items")
    nombre = Column(u'nombre', String(20), nullable=False)

class Item(DeclarativeBase):
    __tablename__ = 'item'
    #column definitions
    coditem = Column(u'coditem', Integer, primary_key=True)
    nombre = Column(u'nombre', String(20), nullable=False)
    complejidad = Column(u'complejidad', Integer, nullable=False)
    prioridad = Column(u'prioridad', Integer, nullable=False)
    version = Column(u'version', Integer, nullable=False)
    estado = Column(u'estado', String(10), nullable=False)
    fecha = Column(u'fecha', Date, nullable=False)
    codtipoitem = Column(u'tipoitem', Integer, ForeignKey('tipoitem.codtipoitem'))
    tipoitem = relation('Tipoitem', backref='items')
    codfase = Column(u'fase', Integer, ForeignKey('fase.codfase'))
    fase = relation('Fase', backref='items')

<<<<<<< HEAD
    def __cmp__( self, other ):
	if self.coditem < other.coditem:
        	rst = -1
      	elif self.coditem > other.coditem:
        	rst = 1
      	else:
        	rst = 0
	return rst

=======
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
class ArchivoExterno(DeclarativeBase):
    __tablename__ = 'archivo_externo'
    #column definitions
    codarchivo = Column(u'codarchivo', Integer, primary_key=True)
    descripcion = Column(u'descripcion', String(100), nullable=False)
    vinculo = Column(u'vinculo', String(20), nullable=False)

class Atributo(DeclarativeBase):
    __tablename__ = 'atributo'
    #column definitions
    codatributo = Column(u'codatributo', Integer, primary_key=True)
<<<<<<< HEAD
    codcampo = Column(u'codcampo', Integer, ForeignKey('campo.codcampo'), nullable=False)
    campo = relation('Campo', backref="atributos")
    coditem = Column(u'coditem', Integer, ForeignKey('item.coditem'), nullable=False)
    item = relation('Item', backref="atributos")
    valoratributo = Column(u'valoratributo', String(20), nullable=False)
    def __cmp__( self, other ):
	if self.codcampo < other.codcampo:
        	rst = -1
      	elif self.codcampo > other.codcampo:
        	rst = 1
      	else:
        	rst = 0
	return rst
=======
    codcampo = Column(u'codcampo', Integer, nullable=False)
    coditem = Column(u'coditem', Integer, ForeignKey('item.coditem'), nullable=False)
    valoratributo = Column(u'valoratributo', String(20), nullable=False)
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

class Campo(DeclarativeBase):
    __tablename__ = 'campo'
    #column definitions
    codcampo = Column(u'codcampo', Integer, primary_key=True)
    codtipoitem = Column(u'codtipoitem', Integer, ForeignKey('tipoitem.codtipoitem'), nullable=False)
    tipoitem = relation('Tipoitem', backref="campos")
    nombre = Column(u'nombre', String(15), nullable=False)
    tipo = Column(u'tipo', String(10), nullable=False)
<<<<<<< HEAD
    tmp = Column(u'tmp', String(20), nullable=True)
    error=Column(u'error', String(100), nullable=True)
    def __cmp__( self, other ):
	if self.codcampo < other.codcampo:
        	rst = -1
      	elif self.codcampo > other.codcampo:
        	rst = 1
      	else:
        	rst = 0
	return rst
=======
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

class HistorialItem(DeclarativeBase):
    __tablename__ = 'historial_item'
    #column definitions
    codhistorial = Column(u'codhistorial', Integer, primary_key=True)
<<<<<<< HEAD
    coditem = Column(u'coditem', Integer, nullable=False)
=======
    codlineabase = Column(u'codlineabase', Integer, ForeignKey('lineabase.codlineabase'))
    descripcion = Column(u'descripcion', String(100), nullable=False)
    fechacreacion = Column(u'fechacreacion', Date, nullable=False)
    fechamodificacion = Column(u'fechamodificacion', Date, nullable=False)
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666

class HistorialLineabase(DeclarativeBase):
    __tablename__ = 'historial_lineabase'
    #column definitions
    cod_lineabase = Column(u'cod_lineabase', Integer, ForeignKey('lineabase.codlineabase'), nullable=False)
    codhistorial = Column(u'codhistorial', Integer, primary_key=True, nullable=False)
    descripcion = Column(u'descripcion', String(100), nullable=True)
    fecha = Column(u'fecha', Date, nullable=False)

class Relacion(DeclarativeBase):
    __tablename__ = 'relacion'
    #column definitions
<<<<<<< HEAD
    codrelacion = Column(u'codrelacion', Integer, primary_key=True)
    coditeminicio = Column(u'coditeminicio', Integer, ForeignKey('item.coditem'), nullable=False)
    iteminicio = relationship("Item", backref="items_inicio_relaciones", primaryjoin=coditeminicio==Item.coditem)
    coditemfin = Column(u'coditemfin', Integer, ForeignKey('item.coditem'), nullable=False)
    itemfin = relationship("Item", backref="items_fin_relaciones", primaryjoin=coditemfin==Item.coditem)
    tipo = Column(u'tipo', String(20), nullable=False)

=======
    coditemfin = Column(u'coditemfin', Integer, ForeignKey('item.coditem'), nullable=False)
    #itemfin = relation('Item', backref='relaciones_fin')
    coditeminicio = Column(u'coditeminicio', Integer, ForeignKey('item.coditem'), nullable=False)
    #iteminicio = relation('Item', backref='relaciones_inicio')
    codrelacion = Column(u'codrelacion', Integer, primary_key=True)
    tipo = Column(u'tipo', String(20), nullable=False)

#class Permiso(DeclarativeBase):
#    __tablename__ = 'permiso'
    #column definitions
#    codpermiso = Column(u'codpermiso', Integer, primary_key=True)
#    descripcion = Column(u'descripcion', String(100), nullable=True)
#    nombre = Column(u'nombre', String(20), nullable=False)

#class UsuarioRolProyecto(DeclarativeBase):
#    __table__ = 'usuario_rol_proyecto'

#usuario_rol = Table(u'usuario_rol', metadata,
#    Column(u'codigousuario', Integer, ForeignKey('usuario.codusuario'), primary_key=True, nullable=False),
#    Column(u'codigorol', Integer, ForeignKey('rol.codrol'), primary_key=True, nullable=False),
#)

>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
item_proyecto = Table(u'item_proyecto', metadata,
    Column(u'coditem', Integer, ForeignKey('item.coditem'), primary_key=True, nullable=False),
    Column(u'codproyecto', Integer, ForeignKey('proyecto.codproyecto'), primary_key=True, nullable=False),
)

#usuario_rol_proyecto = Table(u'usuario_rol_proyecto', metadata,
#    Column(u'codusuario', Integer, ForeignKey('usuario.codusuario'), primary_key=True, nullable=False),
#    Column(u'codproyecto', Integer, ForeignKey('proyecto.codproyecto'), primary_key=True, nullable=False),
#    Column(u'codrol', Integer, ForeignKey('rol.codrol'), primary_key=True, nullable=False),
#)

#permiso_fase = Table(u'permiso_fase', metadata,
#    Column(u'codpermiso', Integer, ForeignKey('permiso.codpermiso'), primary_key=True, nullable=False),
#    Column(u'codfase', Integer, ForeignKey('fase.codfase'), primary_key=True, nullable=False),
#)

<<<<<<< HEAD
class ItemHistorial(DeclarativeBase):
    __tablename__ = 'item_historial'
    #column definitions
    coditem = Column(u'coditem', Integer, primary_key=True, autoincrement=False)
    version = Column(u'version', Integer, primary_key=True, autoincrement=False)
    codhistorial = Column(u'codhistorial', Integer, ForeignKey('historial_item.codhistorial'))
    historial = relation('HistorialItem', backref='versiones')
    nombre = Column(u'nombre', String(20), nullable=False)
    complejidad = Column(u'complejidad', Integer, nullable=False)
    prioridad = Column(u'prioridad', Integer, nullable=False)
    estado = Column(u'estado', String(10), nullable=False)
    fecha = Column(u'fecha', Date, nullable=False)
    codtipoitem = Column(u'tipoitem', Integer, ForeignKey('tipoitem.codtipoitem'))
    codfase = Column(u'fase', Integer, ForeignKey('fase.codfase'))
    def __cmp__( self, other ):
	if self.coditem < other.coditem:
        	rst = -1
      	elif self.coditem > other.coditem:
        	rst = 1
      	else:
        	rst = 0
	return rst

class AtributoHistorial(DeclarativeBase):
    __tablename__ = 'atributo_historial'
    #column definitions
    codatributo = Column(u'codatributo', Integer, primary_key=True)
    coditem = Column(u'coditem', Integer, nullable=False)
    version = Column(u'version', Integer, nullable=False)
    item = relation("ItemHistorial", backref=backref("atributos", uselist=True), primaryjoin=and_(coditem==ItemHistorial.coditem, version==ItemHistorial.version), foreign_keys=[ItemHistorial.coditem, ItemHistorial.version])
    codcampo = Column(u'codcampo', Integer, ForeignKey('campo.codcampo'), nullable=False)
    campo = relation('Campo')
    valor = Column(u'valor', String(20), nullable=False)
    ForeignKeyConstraint(['coditem', 'version'], ['item_historial.coditem', 'item_historial.version'])
    def __cmp__( self, other ):
	if self.codcampo < other.codcampo:
        	rst = -1
      	elif self.codcampo > other.codcampo:
        	rst = 1
      	else:
        	rst = 0
	return rst

class RelacionHistorial(DeclarativeBase):
    __tablename__ = 'relacion_historial'
    #column definitions
    codrelacion = Column(u'codrelacion', Integer, primary_key=True)
    coditem1 = Column(u'coditem1', Integer, nullable=False)
    version1 = Column(u'version1', Integer, nullable=False)
    item = relationship("ItemHistorial", backref=backref("relaciones", uselist=True), primaryjoin=and_(coditem1==ItemHistorial.coditem, version1==ItemHistorial.version), foreign_keys=[ItemHistorial.coditem, ItemHistorial.version])
    coditem2 = Column(u'coditem2', Integer, nullable=False)
    version2 = Column(u'version2', Integer, nullable=False)
    tipo = Column(u'tipo', String(20), nullable=False)
    ForeignKeyConstraint(['coditem1', 'version1'], ['item_historial.coditem', 'item_historial.version'])

##faltaria archivo_externo_historial
=======
#permiso_rol = Table(u'permiso_rol', metadata,
#    Column(u'codigorol', Integer, ForeignKey('rol.codrol'), primary_key=True, nullable=False),
#    Column(u'codigopermiso', Integer, ForeignKey('permiso.codpermiso'), primary_key=True, nullable=False),
#)

>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
