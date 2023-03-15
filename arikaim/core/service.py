from arikaim.core.utils import *
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

class Service:
    
    def __init__(self, name, mount_path = None):
        self._routes = []      
        self._middlewares = []     
        self._name = name
        self._mounth_path = mount_path
        
    def boot(self):
        pass

    def init_routes(self):
        pass

    def init_container(self):
        pass

    def add_route(self, method, path, endpoint):
        self._routes.append(Route(path,endpoint,methods = method))           

    def add_websocket_route(self, path, endpoint):       
        self._routes.append(WebSocketRoute(path,endpoint = endpoint))

    def add_middleware(self, middleware_class):
        self._middlewares.append(Middleware(middleware_class))     

    def add_auth_middleware(self, backend):
        self._middlewares.append(Middleware(AuthenticationMiddleware, backend = backend))  

    @property 
    def mount_path(self, path):
        self._mounth_path = path

    @property
    def mount(self):
        if self._mounth_path == None:
            return self._name
        else:
            return self._mounth_path
        
    @property
    def routes(self):
        if self._mounth_path == None:
            self._mounth_path = self._name
            
        if len(self._routes) == 0:
            return None
        else:
            return Mount(
                "/" + self._mounth_path, 
                routes = self._routes, 
                name = self._name, 
                middleware = self._middlewares
            )