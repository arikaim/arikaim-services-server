from arikaim.core.collection.property import Property

class ApiDescriptor:

    def __init__(self):
        self._params = {}
        self._result = {}
        self._title = ''
        self._description = ''

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value: str):
        self._description = value

    def param(self, name: str):
        self._params[name] = Property(name)
        return self._params[name]
    
    def result(self, name: str):
        self._result[name] = Property(name)
        return self._result[name]
    
    @property
    def params(self):
        return self._params

    @property
    def result_fields(self):
        return self._result



def get_descriptor(cls):
    descriptor = ApiDescriptor()
    cls.init_descriptor(descriptor)
   
    return descriptor