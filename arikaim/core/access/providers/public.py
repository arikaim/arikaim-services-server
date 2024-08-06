from arikaim.core.access.user import AuthUser

class PublicAuthProvider:
    
    def authenticate(self, credentails):
        return AuthUser(authenticated = False, id = None)