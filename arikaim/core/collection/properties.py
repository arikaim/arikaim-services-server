from arikaim.core.collection.property import Property

class Properties:

    def __init__(self, data):
        self._data = data
    
    def get_value(self, name: str, default = None):
        if name in self._data:
            return self._data[name]['value']
        else:
            return default
        
    @property
    def data(self):
        return self._data
    
    