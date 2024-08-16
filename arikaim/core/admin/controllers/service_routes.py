from arikaim.core.controller import Controller, get
from arikaim.core.services import services

class ServiceRoutes(Controller):

    @get
    async def get(self, request, data):         
        service = services.get_service(data['name'])
        
        routes = []
        if service != None:
            routes = self.get_routes(service)
       
        self.field('name',data['name'])
        self.field('routes',routes)
        self.message('Service routes')
       
    def get_routes(self,service):
        routes = []
        for route in service.routes.routes:
            descriptor = route.endpoint.descriptor()
            routes.append({
                'title': descriptor.title,
                'description': descriptor.description,               
                'path': service.mount_path + route.path,
                'name': route.name,                
                'methods': list(route.methods),
                'params': descriptor.params,
                'result': descriptor.result_fields          
            })

        return routes