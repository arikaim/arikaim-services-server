from arikaim.core.container import di
from arikaim.core.service import Service
from arikaim.core.admin.controllers.services_list import ServicesList
from arikaim.core.admin.controllers.service import ServiceDescriptor
from arikaim.core.admin.controllers.service_routes import ServiceRoutes
from arikaim.core.admin.controllers.service_route import ServiceRoute
from arikaim.core.admin.controllers.info import Info

class AdminService(Service):

    def init_routes(self):

        auth = di.get('access').middleware('multiple',['token','php_session'])
        self.add_auth_middleware(auth)

        self.add_route(["GET"],"/info",Info)
        self.add_route(["GET"],"/services",ServicesList)
        self.add_route(["GET"],"/service/{name}",ServiceDescriptor)
        self.add_route(["GET"],"/service/routes/{name}",ServiceRoutes)
        self.add_route(["GET"],"/service/route/{name}/{path}",ServiceRoute)