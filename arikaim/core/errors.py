from starlette.exceptions import HTTPException
from starlette.requests import Request
from arikaim.core.response import ApiResponse

async def unauthorized_error(request: Request, exc: HTTPException): 
    return ApiResponse({
            'result': '',
            'status': 401,
            'errors': ['Access Denied'],
            'code'  : 401
    })  

async def not_found_error(request: Request, exc: HTTPException): 
    return ApiResponse({
            'result': '',
            'status': 404,
            'errors': ['Not found'],
            'code'  : 404
    })  

error_handlers = {
    401: unauthorized_error,
    404: not_found_error,
}