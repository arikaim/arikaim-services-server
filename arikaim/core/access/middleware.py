from starlette.authentication import AuthenticationBackend, AuthCredentials
from arikaim.core.access.auth_error import AuthError
from arikaim.core.access.access import access
from arikaim.core.access.user import AuthUser

class AuthMiddleware(AuthenticationBackend):
    
    def __init__(self, auth_providers = []):
        self._providers = auth_providers

    def add_provider(self, auth_provider):
        if not auth_provider in self._providers:
            self._providers.append(auth_provider)

    async def authenticate(self, conn): 
        for provider in self._providers:
            user = access.authenticate(conn,provider)
        
            if isinstance(user,AuthUser) == True:
                return AuthCredentials(["authenticated"]), user

        raise AuthError(status_code = 401)
