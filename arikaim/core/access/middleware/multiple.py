from starlette.authentication import AuthenticationBackend, AuthCredentials
from arikaim.core.access.auth_error import AuthError
from arikaim.core.container import di

class MultipleAuthMiddleware(AuthenticationBackend):
    
    def __init__(self, auth_providers = []):
        self._providers = auth_providers

    def add_provider(self, auth_provider):
        if not auth_provider in self._providers:
            self._providers.append(auth_provider)

    async def authenticate(self, conn):      
        for provider in self._providers:
            user = di.get('access').authenticate(conn,provider)
            if user != False:
                return AuthCredentials(["authenticated"]), user

        raise AuthError(status_code = 401)
