from arikaim.core.controller import Controller, get
from arikaim.core.container import di

class ServiceRoutes(Controller):

    @get
    async def get(self, request, data):  
        app = di.get('app').app()

        service = app.get_service(data['name'])
        service.init_routes()
       
        routes = []
        for route in service.routes.routes:
            routes.append({
                'path': route.path,     
                'endpoint': route.name,
                'methods': list(route.methods)           
            })
       
        self.field('name',data['name'])
        self.field('routes',routes)
        self.message('Service routes')
       
    