from arikaim.core.db.models.users import Users
from arikaim.core.db.models.access_tokens import AccessTokens

class PublicAuthProvider:
    
    def authenticate(self, credentails):
        return True