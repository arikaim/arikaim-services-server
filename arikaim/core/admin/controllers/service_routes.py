from arikaim.core.controller import Controller, get
from arikaim.core.container import di
from arikaim.core.api_descriptor import *

class ServiceRoutes(Controller):

    @get
    async def get(self, request, data):  
        app = di.get('app').app()
        service = app.get_service(data['name'])
      
        routes = []
        for route in service.routes.routes:
            descriptor = get_descriptor(route.endpoint)

            routes.append({
                'path': route.path,     
                'endpoint': route.name,
                'methods': list(route.methods),
                'params': descriptor.params,
                'result': descriptor.result_fields          
            })

        self.field('name',data['name'])
        self.field('routes',routes)
        self.message('Service routes')
       
    