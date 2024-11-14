from arikaim.core.response import ApiResponse
from starlette.middleware.base import BaseHTTPMiddleware
from arikaim.core.logger import logger
import traceback


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception as e:                 
            logger.error(str(e))
          
            return ApiResponse({
                'result': None,
                'status': 'error',
                'errors': ['Server error'],
                'code'  : 500
            })  
