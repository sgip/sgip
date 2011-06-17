from repoze.what.predicates import Predicate
<<<<<<< HEAD
from prueba.model import DBSession, Group
=======
from classifieds.model import DBSession, Group
>>>>>>> 15d55ec2fd13456b8dc61812e944550c8230c666
from repoze.what.predicates import has_permission

class user_can_edit(Predicate):
    message = 'El usuario %(usuario)s no tiene permiso de editar el rol "%(rol)s"'

    def __init__(self, rol_id):
	self.rol_id = rol_id
    
    def evaluate(self, environ, credentials):

        # Obtener el ID del usuario actualmente loggeado
        username = credentials.get('repoze.what.userid')

        # Finding the classified in URLs like http://example.org/some-action/:classified:
        #vars = self.parse_variables(environ)
        #classified_id = (vars.get('named_args')).get('classified')

        # We got it, now let's load its object and poster:
        #query = DBSession.query(Classified)
        #classified = query.get(classified_id)
        #poster = classified.poster

        # Finally, let's compare them:
	permiso = 'RolEditar' + str(self.rol_id)
	can_edit = has_permission(permiso)
	return can_edit
	print can_edit
        if (can_edit) != True:
            # The current user didn't post the classified
            # specified in the URL! The predicate isn't met
            self.unmet(usuario=username, rol=self.rol_id)
	return can_edit
