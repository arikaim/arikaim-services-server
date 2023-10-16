import uvicorn
import os
from peewee import *
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from pymitter import EventEmitter

from arikaim.core.admin.admin import AdminService
from arikaim.core.path import Path
from arikaim.core.utils import *
from arikaim.core.db.db import *
from arikaim.core.container import di
from arikaim.core.errors import error_handlers
from arikaim.core.access.access import Access
from arikaim.core.queue.queue import Queue
from arikaim.core.logger import logger
from arikaim.core.packages import load_package_descriptor


class ArikaimServer:
    _app = None

    def __init__(self):
        self._version = '0.5.3'
        self._services = []
        self._services_instance = {}
        self._starlette = None
        self._config = None

    def system_init(self):
        logger.info('Init')

        # load config
        self.load_config()

        # create event emiter 
        events = EventEmitter(wildcard = True)
        di.add('events',events)

        # connect to db 
        db = Db(self._config.db)
        db.connect()
        # add to container
        di.add('db',db)
        
        # add access
        di.add('access',Access())

        # add queue
        di.add('queue',Queue())
        # add app
        di.add('app',self)

        # scan services
        for file in os.scandir(Path.services()):
            if file.is_dir() and not file.name.startswith('.'):             
                self._services.append(file.name)
                # add service path to system paths
                sys.path.append(Path.services(file.name))


    def boot(self):
        self.system_init()
        routes = self.boot_services()

        admin_routes = self.load_admin_routes()
        routes.append(admin_routes)

        # create app
        self._starlette = Starlette(
            debug = True, 
            routes = routes, 
            on_shutdown = [self.on_shutdown],
            middleware = [
                Middleware(CORSMiddleware, allow_origins = ['*'])
            ], 
            exception_handlers = error_handlers
        )

    def load_admin_routes(self):
        logger.info('Load admin routes')

        admin = AdminService('admin')
        admin.init_routes()

        return admin.routes

    def boot_console(self, service_name = None):
        logger.info('Boot console')
        self.system_init()   
        self.boot_services(False,True)
        
    def load_config(self):
        self._config = load_module('config',os.path.join(Path.config(),'config.py'))

    async def on_shutdown(self):
        logger.info('Shutdown server')

        di.get('db').close()
        logger.info('Db connection closed')
    
    def run(self): 
        uvicorn.run(
            self._starlette, 
            reload = False,
            host = self._config.settings['host'], 
            port = self._config.settings['port'], 
            log_level = self._config.settings.get('log_level','info')
        )
       
    @property
    def server_url(self):
        return 'http://' + self._config.settings['host'] + ':' + str(self._config.settings['port'])
    
    def run_queue_worker(self):
        # add jobs path
        for service_name in self._services:
            sys.path.append(Path.job_path(service_name))
        
        # run queue wroker
        di.get('queue').boot()
        di.get('queue').run()

    def get_service(self, name:str):
        if name in self._services_instance:
            return self._services_instance[name]
        else:
            return None
        
    @property 
    def services(self):
        return self._services
    
    @property 
    def version(self):
        return self._version

    @property
    def starlette(self):
        return self._starlette
    
    @property
    def config(self):
        if (self._config is None):
            self.load_config()
       
        return self._config

    def boot_services(self, load_routes: bool = True, init_container: bool = True):
        routes = []

        for service_name in self._services:            
            package = load_package_descriptor(service_name)
            package.setdefault('disabled',False)
          
            if package['disabled'] == True:
                # skip disabled service boot
                logger.info('service: ' + service_name + ' disabled ')
                continue

            logger.info('Boot service: ' + service_name)
            service_class = load_class(Path.services(service_name),service_name,service_name.capitalize())
            self._services_instance[service_name] = service_class(service_name) 
            
            if load_routes == True:
                self._services_instance[service_name].init_routes()
            if init_container == True:
                self._services_instance[service_name].init_container()

            # add service routes
            if self._services_instance[service_name].routes != None:
                routes.append(self._services_instance[service_name].routes)

        return routes   


    def load_console_commands(self, service_name, module_name = None):
        # load console module
        console = self.load_service_console_commands(service_name,'console')
        if console != False:
            call(console,'init')

        return self.load_service_console_commands(service_name, module_name)


    def load_service_console_commands(self, service_name: str, module_name = None):
        if not module_name:
            module_name = 'console'

        console_file = os.path.join(Path.console_path(service_name),module_name)
        
        if os.path.isfile(console_file + '.py') == True: 
            # append service path  
            sys.path.append(Path.services(service_name))            
            return load_module('console',console_file + '.py')                              
        else:
            return False

    @classmethod
    def app(clas):
        if ArikaimServer._app is None: 
            ArikaimServer._app = ArikaimServer()
          
        return ArikaimServer._app