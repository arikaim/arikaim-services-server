from peewee import *
from arikaim.core.path import Path
import imp,os,importlib;

class Db: 
    _instance = None

    def __init__(self, ):
        self._config = None
        self._peewee = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    def connect(self, config):     
        self._config = config

        self._peewee = MySQLDatabase(
            self._config['database'],
            user = self._config['username'],
            password = self._config['password'],
            host = self._config['host']
        )

    def close(self):
        if not self._peewee:
            return False
        self._peewee.close()
        
        return True

    def bind(self, models):
        self._peewee.bind(models)

    @property
    def peewee(self):
        return self._peewee
    
    def load_model(self,model_class, module_name, service_name = None):
        return load_model_class(model_class,module_name,service_name)



db = Db()



def load_model_class(model_class, module_name, service_name = None):
    if not service_name:        
        module = importlib.import_module('arikaim.core.db.models.' + module_name,model_class)
    else:
        path = os.path.join(Path.model(service_name),module_name)      
        module = imp.load_source(module_name,path + '.py')

    return getattr(module,model_class)