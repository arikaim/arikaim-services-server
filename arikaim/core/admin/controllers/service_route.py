from arikaim.core.controller import Controller, get
from arikaim.core.services import services

class ServiceRoute(Controller):

    @get
    async def get(self, request, data):       
        service = services.get_service(data['name'])
        path = data['path'].lstrip('/')
        result = {} 
        
        for route in service.routes.routes:
            service_path = route.path
           
            if service_path.lstrip('/') == path:
                descriptor = route.endpoint.descriptor()
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
    