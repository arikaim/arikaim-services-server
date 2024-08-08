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

async def api_call_quota_limit_error(request: Request, exc: HTTPException): 
    return ApiResponse({
        'result': '',
        'details': exc.detail,
        'status': exc.status_code,
        'errors': ['Api call quota limit reached error'],
        'code'  : exc.status_code
    }) 

async def api_call_quota_billing_error(request: Request, exc: HTTPException): 
    return ApiResponse({
        'result': '',
        'details': exc.detail,
        'status': exc.status_code,
        'errors': ['Api call billing limit reached'],
        'code'  : exc.status_code
    }) 

error_handlers = {
    401: unauthorized_error,
    404: not_found_error,
    500: server_error,
    429: api_call_quota_limit_error,
    430: api_call_quota_billing_error
}