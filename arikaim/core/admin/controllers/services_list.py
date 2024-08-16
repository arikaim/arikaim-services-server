from arikaim.core.controller import Controller, get
from arikaim.core.services import services

class ServicesList(Controller):

    @get
    async def get(self, request, data):  
        self.field('services',services.services)
        self.message('Service list')
        