from arikaim.core.collection.property import Property

class PropertiesDescriptor:

    def __init__(self):
        self._properties = {}
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

    def result(self, name: str):
        self._result[name] = Property(name)
        return self._result[name]
    
    @property
    def result_fields(self):
        return self._result

    def prop(self, name: str):
        self._properties[name] = Property(name)
        return self._properties[name]
    
    @property
    def props(self):
        return self._properties

    def param(self, name: str):
        self._properties[name] = Property(name)
        return self._properties[name]
    
    @property
    def params(self):
        return self._properties