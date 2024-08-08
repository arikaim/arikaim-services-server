from starlette.exceptions import HTTPException

class QuotaError(HTTPException):
    pass