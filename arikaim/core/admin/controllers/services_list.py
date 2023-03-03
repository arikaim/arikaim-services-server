from arikaim.core.controller import Controller, get
from arikaim.core.container import di

class ServicesList(Controller):

    @get
    async def get(self, request, data):  
        app = di.get('app').app()

        self.field('services',app.services)
        self.message('Service list')
        