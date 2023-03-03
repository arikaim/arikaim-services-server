from arikaim.core.controller import Controller, get
from arikaim.core.container import di
from arikaim.core.packages import load_package_descriptor

class ServiceDescriptor(Controller):

    @get
    async def get(self, request, data):  
        app = di.get('app').app()

        descriptor = load_package_descriptor(data['name'])

        self.field('name',data['name'])
        self.field('descriptor',descriptor)
    