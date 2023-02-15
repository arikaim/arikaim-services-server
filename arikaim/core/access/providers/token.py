from arikaim.core.db.models.users import Users
from arikaim.core.db.models.access_tokens import AccessTokens


class TokenAuthProvider:
    
    def authenticate(self, credentails):

        if "Authorization" not in credentails.headers:
            return False

        try:
            token = credentails.headers["Authorization"]
            access_tokens = AccessTokens.select().where(AccessTokens.token == token).get()
            
            return Users.get(Users.id == access_tokens.user_id)
        except (Users.DoesNotExist, AccessTokens.DoesNotExist):
            return False