import uvicorn
from peewee import *

from arikaim.core.logger import logger
from arikaim.core.utils import *

class ArikaimServer:
    _instance = None

    def __init__(self):
        self._version = '0.5.3'
        self._config = None
        
    def run(self, reload = False):

        self._config = load_module('config',os.path.join(Path.config(),'config.py'))
        
        if reload == True:
            logger.info('Dev mode (reload)')

        uvicorn.run(
            'arikaim.core.app:app', 
            reload = reload,
            host = self._config.settings['host'], 
            port = self._config.settings['port'], 
            log_level = self._config.settings.get('log_level','info')
        )
       
    @property
    def server_url(self):
        return 'http://' + self._config.settings['host'] + ':' + str(self._config.settings['port'])
    
    @property 
    def version(self):
        return self._version

    @classmethod
    def instance(cls):
        if cls._instance is None: 
            cls._instance = ArikaimServer()
          
        return cls._instance
    
arikaim_server = ArikaimServer.instance()