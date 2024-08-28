import gc

from starlette.applications import Starlette
from starlette.middleware import Middleware

from arikaim.core.packages import load_package_descriptor
from arikaim.core.services import services
from arikaim.core.redis import redis_connect
from arikaim.core.utils import *
from arikaim.core.db.db import *
from arikaim.core.errors import error_handlers
from arikaim.core.logger import logger

from arikaim.core.admin.admin import AdminService
from arikaim.core.middleware.system import SystemMiddleware

class ArikaimApp:
    _instance = None

    def __init__(self):             
        self._starlette = None
        self._config = None
        self._middlewares = []
        self._default_middlewares = [
            Middleware(SystemMiddleware)
        ]
    
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    def add_middleware(self, middleware):
        self._middlewares.append(middleware)

    def load_service_console_commands(self, service_name: str, module_name = None):
        if not module_name:
            module_name = 'console'

        console_file = os.path.join(Path.console(service_name),module_name)
        
        if os.path.isfile(console_file + '.py') == True: 
            # append service path  
            sys.path.append(Path.services(service_name))            
            return load_module('console',console_file + '.py')                              
        else:
            return False
        
    def load_console_commands(self, service_name, module_name = None):
        # load console module
        console = self.load_service_console_commands(service_name,'console')
        if console != False:
            call(console,'init')

        return self.load_service_console_commands(service_name, module_name)

    def load_config(self):
        self._config = load_module('config',os.path.join(Path.config(),'config.py'))
        if self._config is None:
            logger.error('Config file not found!')
            return False
        return self._config
    
    def system_init(self):
        logger.info('Init')
        
        # enable GC
        gc.enable()

        # load config
        if self.load_config() == False:
            return False

        # connect ro teds
        redis_connect(self._config.redis)

        # connect to db        
        db.connect(self._config.db)
       
    def boot(self):
        logger.info('Boot')

        self.system_init()
        # scan services
        services.scan_services()
      
        # load services routes
        services.boot_services()

        # load admin routes
        self.load_admin_routes()

        # middlewares
        middlewares = self._default_middlewares + self._config.middleware + self._middlewares
        for middleware in middlewares:
            logger.info('Add ' + str(middleware))
     
        # starlette instance
        self._starlette = Starlette(
            debug = True, 
            routes = services.routes, 
            on_shutdown = [self.on_shutdown],
            middleware = middlewares, 
            exception_handlers = error_handlers
        )

        return self.starlette

    async def on_shutdown(self):
        logger.info('Shutdown server')

        db.close()
        logger.info('Db connection closed')

    def load_admin_routes(self):
        logger.info('Load admin routes')

        admin = AdminService('admin','')
        admin.init_routes()

        services.routes.append(admin.routes)

    @property
    def starlette(self):
        return self._starlette

    @property
    def config(self):
        return self._config


app = ArikaimApp()
