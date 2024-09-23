from arikaim.core.controller import Controller, get
from arikaim.core.services import services

class ServiceRoute(Controller):

    @get
    async def get(self, request, data):       
        service = services.get_service(data['name'])
        route_name = data['route_name']
        result = {} 
        
        for route in service.routes.routes:
           
            if route.name == route_name:
                descriptor = route.endpoint.descriptor()
                result = {
                    'title': descriptor.title,
                    'description': descriptor.description,
                    'path': service.mount_path + route.path,                         
                    'name': route.name,
                    'methods': list(route.methods),
                    'params': descriptor.params,
                    'result': descriptor.result_fields,
                    'example_values': descriptor.get_example_values()     
                }
                break

        self.field('name',data['name'])
        self.field('path',service.mount_path + route.path)       
        self.field('route',result)
        self.message('Service route')
    