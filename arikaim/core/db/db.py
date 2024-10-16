from arikaim.core.path import Path
import imp,os,importlib;
from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker

class Db: 
    _instance = None

    def __init__(self):
        self._config = None
        self._engine = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    def connect(self, config):     
        self._config = config
        connect = 'mysql+pymysql://' + self._config['username'] + ':' + self._config['password'] + '@' + self._config['host'] + '/' +  self._config['database']      
        echo = False
        if echo in self._config:
            echo = self._config['echo']

        self._engine = create_engine(connect, echo = echo)
       
    def close(self):
        if not self._engine:
            return False
        self._engine.dispose()
        
        return True

    @property
    def engine(self):
        return self._engine
    
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