from starlette.middleware.base import BaseHTTPMiddleware

class SanitizeMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def __call__(self, scope, receive, send):
        pass