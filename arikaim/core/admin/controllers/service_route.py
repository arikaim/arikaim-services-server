from arikaim.core.controller import Controller, get
from arikaim.core.container import di
from arikaim.core.api_descriptor import *

class ServiceRoute(Controller):

    @get
    async def get(self, request, data):  
        app = di.get('app')
        service = app.get_service(data['name'])
        path = data['path'].lstrip('/')
        result = {} 
        
        for route in service.routes.routes:
            service_path = service.mount_path + route.path
            if service_path.lstrip('/') == path:
                descriptor = get_descriptor(route.endpoint)
                result = {
                    'title': descriptor.title,
                    'description': descriptor.description,
                    'path': service_path,                         
                    'name': route.name,
                    'methods': list(route.methods),
                    'params': descriptor.params,
                    'result': descriptor.result_fields          
                }
                break

        self.field('name',data['name'])
        self.field('path',data['path'])       
        self.field('route',result)
        self.message('Service route')
    