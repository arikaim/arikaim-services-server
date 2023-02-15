import uvicorn
import os
from peewee import *
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from pymitter import EventEmitter

from arikaim.core.path import Path
from arikaim.core.utils import *
from arikaim.core.db.db import *
from arikaim.core.container import di
from arikaim.core.errors import error_handlers
from arikaim.core.access.access import Access
from arikaim.core.queue.queue import Queue
from arikaim.core.logger import logger


class ArikaimServer:
    _app = None

    def __init__(self):
        self._version = '0.5.0'
        self._services = []
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
       
        # scan services
        for file in os.scandir(Path.services()):
            if file.is_dir() and not file.name.startswith('.'):             
                self._services.append(file.name)
                # add service path to system paths
                sys.path.append(Path.services(file.name))


    def boot(self):
        self.system_init()
        routes = self.load_routes()

        # create app
        self._starlette = Starlette(
            debug = True, 
            routes = routes, 
            middleware = [
                Middleware(CORSMiddleware, allow_origins = ['*'])
            ], 
            exception_handlers = error_handlers
        )


    def boot_console(self, service_name = None):
        logger.info('Boot console')
        self.system_init()   

    def load_config(self):
        self._config = load_module('config',os.path.join(Path.config(),'config.py'))

    def run(self): 
        uvicorn.run(
            self._starlette, 
            host = self._config.settings['host'], 
            port = self._config.settings['port'], 
            log_level = self._config.settings.get('log_level','info')
        )
       
    def run_queue_worker(self):
        # add jobs path
        for service_name in self._services:
            sys.path.append(Path.job_path(service_name))
        
        # run queue wroker
        di.get('queue').boot()
        di.get('queue').run()

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
        if (self._confif is None):
            self.load_config()

        return self._config

    def load_routes(self):
        routes = []

        for service_name in self._services:            
            logger.info('Boot service: ' + service_name)
            service_class = load_class(Path.services(service_name),service_name,service_name.capitalize())
          
            service = service_class(service_name) 
            service.boot()

            # add service routes
            if service.routes != None:
                routes.append(service.routes)

        return routes   


    def load_console_commands(self, service_name, module_name = None):

        # load console module
        console = self.load_service_console_commands(service_name,'console')
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


    @classmethod
    def app(clas):
        if ArikaimServer._app is None: 
            ArikaimServer._app = ArikaimServer()
          
        return ArikaimServer._app