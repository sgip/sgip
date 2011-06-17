# -*- coding: utf-8 -*-
"""Setup the prueba application"""

import logging
from tg import config
from prueba import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup prueba here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
	u = model.User()
        u.user_name = u'admin'
	u.user_fullname = u'admin'
	u.password = u'admin'
	u.user_telefono = u'admin'
	u.user_direccion = u'admin'
        u.email_address = u'admin@admin.com'
        model.DBSession.add(u)
    
        g1 = model.Group()
        g1.group_name = u'ADMIN'
        g1.users.append(u)
        model.DBSession.add(g1)

        g2 = model.Group()
        g2.group_name = u'RolPorDefecto1'
        g2.users.append(u)
        model.DBSession.add(g2)

	p1 = model.Permission()
        p1.permission_name = u'iniciar_sesion'
	p1.permission_type = u'Sistema'
        p1.description = u'Iniciar sesion'

        p2 = model.Permission()
        p2.permission_name = u'crear_usuario'
	p2.permission_type = u'Usuario'
        p2.description = u'Crear un usuario nuevo'

        p3 = model.Permission()
        p3.permission_name = u'crear_rol'
	p3.permission_type = u'Rol'
        p3.description = u'Crear un rol nuevo'

        p4 = model.Permission()
        p4.permission_name = u'crear_proyecto'
	p4.permission_type = u'Proyecto'
        p4.description = u'Crear un proyecto nuevo'

	p1.groups.append(g1)
	p2.groups.append(g1)
	p3.groups.append(g1)
	p4.groups.append(g1)
	
	p1.groups.append(g2)
		   
        model.DBSession.add(p1)
	model.DBSession.add(p2)
	model.DBSession.add(p3)
	model.DBSession.add(p4)
	    
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'
        

    # <websetup.bootstrap.after.auth>
