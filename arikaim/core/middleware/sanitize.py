from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Message
import bleach
import json

class SanitizeMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):
        await self.set_body(request)

        if request.method == 'POST' or request.method == 'PUT':
            json_body = await request.json()
            sanitize_body = {key: self.sanitize_array(value) if isinstance(
                value, list) else bleach.clean(value) for key, value in json_body.items()}
            request._body = json.dumps(
                sanitize_body, indent=2).encode('utf-8')
            request = await self.set_body(request)

        response = await call_next(request)
        return response

    async def set_body(self, request):
        receive_ = await request._receive()
        async def receive():
            return receive_

        request._receive = receive
        return request

    @staticmethod
    def sanitize_array(array_values):
        for index, value in enumerate(array_values):
            if isinstance(value, dict):
                array_values[index] = {key: bleach.clean(
                    value) if isinstance(value, str) else value for key, value in value.items()}
            else:
                array_values[index] = bleach.clean(value) if isinstance(value, str) else value
        
        return array_values
