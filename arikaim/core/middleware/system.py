import gc

from starlette.middleware.base import BaseHTTPMiddleware
from arikaim.core.utils import get_process_memory
from arikaim.core.logger import logger

class SystemMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        
        gc.collect()
        logger.info('Used memory ' + str(get_process_memory()))

        response = await call_next(request)
        return response
