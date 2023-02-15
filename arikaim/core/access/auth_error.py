from starlette.exceptions import HTTPException

class AuthError(HTTPException):
    pass