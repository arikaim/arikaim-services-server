import abc
from arikaim.core.collection.descriptor import PropertiesDescriptor

class Action:

    def __init__(self, options = {}):
        self._name = ''
        self._title = ''
        self._description = ''
        self._error = None
        self._descriptor = None
        
        self._options = options
        self._result = {}
        self.init()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
    
    def __call__(self):
        return self.run()
    
    def init(self):
        pass

    @abc.abstractmethod
    def run(self):
        """Implement action run method"""
        return

    def hasError(self):
        if not self._error:
            return True
        else:
            return False

    def error(self, error):
        self._error = error
        return self
    
    @property
    def error(self):
        return self._error
    
    def options(self, options):
        self._options = options
        return self
    
    def option(self, name, value):
        self._options[name] = value
        return self
    
    def get_option(self, name, default = None):
        if name in self._options:
            return self._options[name]
        
        return default

    def result(self, name, value):
        self._result[name] = value
        return self
    
    def get(self, name, default = None):
        if name in self._result:
            return self._result[name]
        
        return default
    
    @classmethod
    def descriptor(cls):
        descriptor = PropertiesDescriptor()
        cls.init_descriptor(descriptor)
   
        return descriptor
    
    @classmethod
    def init_descriptor(cls, descriptor):               
        pass

    