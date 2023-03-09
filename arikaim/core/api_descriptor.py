from arikaim.core.collection.property import Property

class ApiDescriptor:

    def __init__(self):
        self._params = {}
        self._result = {}

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