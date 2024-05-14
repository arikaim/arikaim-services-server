from starlette.exceptions import HTTPException
from starlette.requests import Request
from arikaim.core.response import ApiResponse

async def server_error(request: Request, exc: HTTPException): 
    return ApiResponse({
        'result': '',
        'details': exc.detail,
        'status': exc.status_code,
        'errors': ['Server errror'],
        'code'  : exc.status_code
    }) 

async def unauthorized_error(request: Request, exc: HTTPException): 
    return ApiResponse({
        'result': '',
        'details': exc.detail,
        'status': exc.status_code,
        'errors': ['Access Denied'],
        'code'  : exc.status_code
    })  

async def not_found_error(request: Request, exc: HTTPException): 
    return ApiResponse({
        'result': '',
        'details': exc.detail,
        'status': exc.status_code,
        'errors': ['Not found'],
        'code'  : exc.status_code
    })  

error_handlers = {
    401: unauthorized_error,
    404: not_found_error,
    500: server_error,
}