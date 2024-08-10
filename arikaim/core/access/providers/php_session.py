from os.path import exists
import subprocess
import json

from arikaim.core.db.models.users import Users
from arikaim.core.db.models.access_tokens import AccessTokens
from arikaim.core.utils import php_unserialize
from arikaim.core.logger import logger
from arikaim.core.path import Path 
from arikaim.core.access.user import AuthUser

class PhpSessionAuthProvider:
    
    def __init__(self):
        self._php_session_path = None
        self.resolve_session_path()

    def authenticate(self, credentails):
        session_id = credentails.cookies.get('PHPSESSID')
        if not session_id:
            return False
        try:
            session_data = self.read_php_session(session_id)
            if 'auth.id' not in session_data:
                return False
  
            user = Users.get(Users.id == session_data['auth.id'])

            return AuthUser(id = user.id, uuid = user.uuid, username = user.user_name, email = user.email)
        except (Users.DoesNotExist, AccessTokens.DoesNotExist):
            return False

    def read_php_session(self, session_id):
        file_name = self._php_session_path + '/sess_' + session_id

        if exists(file_name) == False:
            return {}
      
        logger.info('Read php session file: ' + file_name)
        try:
            file = open(file_name,'r')
            content = file.read()
            file.close()
        except IOError:
            return False
        
        return php_unserialize(content)
    
    def resolve_session_path(self):
        try:
            response = subprocess.Popen(
                'php cli session:info --output json',
                shell = True,
                cwd = Path.base(),
                stdout = subprocess.PIPE          
            )

            json_text = response.stdout.read()
            data = json.loads(json_text)
        except BaseException:
            self._php_session_path = None
            return
        
        self._php_session_path = data['save_path']