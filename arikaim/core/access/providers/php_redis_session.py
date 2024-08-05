from arikaim.core.db.models.users import Users
from arikaim.core.db.models.access_tokens import AccessTokens
from arikaim.core.redis import redis
from arikaim.core.utils import php_unserialize

class RedisPHPSessionAuthProvider:
    
    def __init__(self):
        pass

    def authenticate(self, credentails):
        session_id = credentails.cookies.get('PHPSESSID')       
        if not session_id:
            return False
        
        try:
            session_data = redis.get(session_id)
            if not session_data:
                return False
            
            session = php_unserialize(str(session_data))

            if 'auth.id' in session:
                auth_id = session['auth.id']
            else:
                return False
            
            print(auth_id)

            #return Users.get(Users.id == session_data['auth.id'])

        except (Users.DoesNotExist, AccessTokens.DoesNotExist):
            return False
