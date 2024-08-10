from arikaim.core.db.models.users import Users
from arikaim.core.db.models.access_tokens import AccessTokens
from arikaim.core.access.user import AuthUser

class TokenAuthProvider:
    
    def authenticate(self, credentails):

        if "Authorization" not in credentails.headers:
            return False
        try:
            token = credentails.headers["Authorization"]
            access_tokens = AccessTokens.select().where(AccessTokens.token == token).get()
            
            user = Users.get(Users.id == access_tokens.user_id)
        
            return AuthUser(id = user.id, uuid = user.uuid, username = user.user_name, email = user.email)
        except (Users.DoesNotExist, AccessTokens.DoesNotExist):
            return False