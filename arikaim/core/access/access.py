from arikaim.core.utils import *
from arikaim.core.db.db import load_model_class
from arikaim.core.access.auth_error import AuthError

class Access:
    
    DEFAULT_AUTH_PROVIDER = 'token'

    def __init__(self):
        self._auth_middleware_classes = {
            'multiple': 'MultipleAuthMiddleware'
        }
        self._auth_provider_classes = {
            'token': 'TokenAuthProvider',
            'php_session': 'PhpSessionAuthProvider'
        }

    def authenticate(self, credentails, auth_name = None):
        if auth_name == None:
            auth_name = Access.DEFAULT_AUTH_PROVIDER

        provider = self.provider(auth_name)
                
        return provider.authenticate(credentails)


    def middleware(self, auth_name, auth_providers):
        if auth_name in self._auth_middleware_classes:
            middleware_class = Access.load_moddleware_class(auth_name,self._auth_middleware_classes[auth_name])
            return middleware_class(auth_providers)
    
        else:
            return None


    def provider(self, auth_name):
        if auth_name in self._auth_provider_classes:
            provider_class = Access.load_provider_class(auth_name,self._auth_provider_classes[auth_name])
            return provider_class()

        else:
            return None


    def has_permission(self, name, user_id):
        Permissions = load_model_class('Permissions','permissions')
        PermissionRelations = load_model_class('PermissionRelations','permission_relations')
    
        try:
            permission = Permissions.select().where(Permissions.name == name).get()
            relation = PermissionRelations.get(
                PermissionRelations.relation_id == user_id and 
                PermissionRelations.permission_id == permission.id
            )
            return relation.relation_id == user_id

        except (Permissions.DoesNotExist, PermissionRelations.DoesNotExist):
            return False

    def is_admin_user(self, user_id):
        return self.has_permission('ControlPanel',user_id)

    def require_admin_user(self, user_id):       
        if self.is_admin_user(user_id) == False:          
            raise AuthError(status_code = 401)            


    @staticmethod
    def load_moddleware_class(module_name, class_name):
        module = importlib.import_module('arikaim.core.access.middleware.' + module_name,class_name)
        return getattr(module,class_name)


    @staticmethod
    def load_provider_class(module_name, class_name):
        module = importlib.import_module('arikaim.core.access.providers.' + module_name,class_name)
        return getattr(module,class_name)