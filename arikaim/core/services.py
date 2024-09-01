
from arikaim.core.logger import logger
from arikaim.core.utils import *
from arikaim.core.packages import load_package_descriptor

class Services:
    _instance = None

    def __init__(self):        
        self._services = []
        self._services_instance = {}
        self._routes = []
        
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
   
    def boot_services(self, load_routes: bool = True, init_container: bool = True):

        for service_name in self._services: 
            package = load_package_descriptor(service_name)
            package.setdefault('language','nodejs')
            package.setdefault('disabled',False)
            
            if package['language'] != 'python':
                # load only pyhton services
                continue
          
            if package['disabled'] == True:
                # skip disabled service boot
                logger.info('service: ' + service_name + ' disabled ')
                continue

            logger.info('Boot service: ' + service_name)
            service_class = load_class(Path.services(service_name),service_name,service_name.capitalize())
            self._services_instance[service_name] = service_class(service_name) 

            self._services_instance[service_name].boot()
            
            if load_routes == True:
                self._services_instance[service_name].init_routes()
            if init_container == True:
                self._services_instance[service_name].init_container()
        
            # add service routes
            if self._services_instance[service_name].routes != None:
                self._routes.append(self._services_instance[service_name].routes)

    def scan_services(self):
        for file in os.scandir(Path.services()):
            if file.is_dir() and not file.name.startswith('.'):             
                self._services.append(file.name)
                # add service path to system paths
                sys.path.append(Path.services(file.name))

    def get_service(self, name:str):
        if name in self._services_instance:
            return self._services_instance[name]
        else:
            return None
        
    @property 
    def services(self):
        return self._services
    
    @property 
    def routes(self):
        return self._routes
    
services = Services()
