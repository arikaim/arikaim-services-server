from arikaim.core.db.models.users import Users
from arikaim.core.db.models.access_tokens import AccessTokens


class RedisSessionAuthProvider:
    
    def __init__(self):
        pass

    def authenticate(self, credentails):
        session_id = credentails.cookies.get('PHPSESSID')
        if not session_id:
            return False
        
        try:
            
            return False
  
            return Users.get(Users.id == session_data['auth.id'])

        except (Users.DoesNotExist, AccessTokens.DoesNotExist):
            return False
