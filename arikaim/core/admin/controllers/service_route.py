from arikaim.core.controller import Controller, get
from arikaim.core.container import di
from arikaim.core.api_descriptor import *

class ServiceRoute(Controller):

    @get
    async def get(self, request, data):  
        app = di.get('app').app()
        service = app.get_service(data['name'])
        path = data['path'].lstrip('/')
        result = {} 
        for route in service.routes.routes:
            if route.path.lstrip('/') == path:
                descriptor = get_descriptor(route.endpoint)
                result = {
                    'title': descriptor.title,
                    'description': descriptor.description,
                    'full_path': service.mount + route.path,     
                    'path': route.path,
                    'endpoint': route.name,
                    'methods': list(route.methods),
                    'params': descriptor.params,
                    'result': descriptor.result_fields          
                }
                break

        self.field('name',data['name'])
        self.field('path',data['path'])
        self.field('server_url',app.server_url)
        self.field('route',result)
        self.message('Service route')
    