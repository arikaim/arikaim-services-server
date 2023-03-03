from arikaim.core.controller import Controller, get
from arikaim.core.container import di
from arikaim.core.packages import load_package_descriptor

class Info(Controller):

    @get
    async def get(self, request, data):  
        app = di.get('app').app()

        self.field('host',app.config.settings['host'])
        self.field('port',app.config.settings['port'])
        self.field('version',app.version)
    