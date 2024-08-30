from arikaim.core.utils import *
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from arikaim.core.access.middleware import AuthMiddleware
from arikaim.core.path import Path

class Service:
    
    def __init__(self, name: str, mount_path = None):
        self._routes = []      
        self._middlewares = []     
        self._route_middlewares = []     
        self._name = name
        self._mounth_path = mount_path
        
    def boot(self):
        pass

    def init_routes(self):
        pass

    def init_container(self):
        pass

    def add_route(self, method, path, endpoint, name = None, auth_providers = None):
        middleware = None
        if auth_providers != None:
            backend = AuthMiddleware(auth_providers)
            middleware = [Middleware(AuthenticationMiddleware, backend = backend)]
            
        self._routes.append(Route(
            path,
            endpoint = endpoint,
            name = name,
            methods = method,
            middleware = middleware
        ))           

    def add_websocket_route(self, path, endpoint):       
        self._routes.append(WebSocketRoute(path,endpoint = endpoint))

    def add_middleware(self, middleware_class):
        self._middlewares.append(Middleware(middleware_class))     

    def add_auth_middleware(self, auth_providers):
        backend = AuthMiddleware(auth_providers)
        self._middlewares.append(Middleware(AuthenticationMiddleware, backend = backend))  

    def path(self, path):
        self._mounth_path = path

    @property
    def mount_path(self): 
        if self._mounth_path == None:
            return str('/' + self._name)
        else:
            return str('/' + self._mounth_path)
        
    @property
    def routes(self):   
        if len(self._routes) == 0:
            return None
        else:
            return Mount(
                self.mount_path, 
                routes = self._routes, 
                name = self._name, 
                middleware = self._middlewares
            )
        

def create_instace(service_name):
    service_class = load_class(Path.services(service_name),service_name,service_name.capitalize())
    return service_class(service_name) 