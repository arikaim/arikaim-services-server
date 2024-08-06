from starlette.authentication import BaseUser

class AuthUser(BaseUser):

    def __init__(self, username: str = '', id = None, email: str = '', uuid: str = '', authenticated: bool = True) -> None:
        self._username = username
        self._id = id
        self._email = email
        self._uuid = uuid
        self._authenticated = authenticated

    @property
    def is_authenticated(self) -> bool:
        return self._authenticated

    @property
    def id(self):
        return self._id
    
    @property
    def uuid(self) -> str:
        return self._id
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def display_name(self) -> str:
        return self._username
