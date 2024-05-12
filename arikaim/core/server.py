import uvicorn
from peewee import *

from arikaim.core.logger import logger
from arikaim.core.utils import *
from arikaim.core.app import app

class ArikaimServer:
    _instance = None

    def __init__(self,config):
        self._version = '0.5.6'
        self._config = config
        
    def run(self, reload = False):
  
        if reload == True:
            logger.info('Dev mode (reload)')

        uvicorn.run(
            'arikaim.core.app:app.boot', 
            reload = reload,
            factory = True,
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
            cls._instance = ArikaimServer(app.config)
          
        return cls._instance
    
arikaim_server = ArikaimServer.instance()