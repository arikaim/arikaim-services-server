from arikaim.core.controller import Controller, get
from arikaim.core.packages import load_package_descriptor

class ServiceDescriptor(Controller):

    @get
    async def get(self, request, data):  
        try:
            descriptor = load_package_descriptor(data['name'])
        except BaseException:
            self.error('Service not found')
            return
    
        self.field('name',data['name'])
        self.field('descriptor',descriptor)
    