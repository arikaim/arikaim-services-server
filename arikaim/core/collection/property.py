

class Property:

    TYPE_NAMES = [
        'text',
        'number',
        'custom',
        'boolean',
        'list',
        'class',
        'password',
        'url',
        'text-area',
        'group',
        'oauth',
        'language-dropdown',
        'image'
    ]

    def __init__(self, name: str, data = None):
        self._name = name
        self._title = ''
        self._description = ''
        self._type = 'text'
        self._readonly = False
        self._required = False
        self._value = None
        
        if type(data) is dict:
            for key in data:
                setattr(self,key,data[key])

    def to_json(self):
        return {
            'name': self._name,
            'description': self._description,
            'type': self._type,
            'readonly': self._readonly,
            'value': self._value,
            'required': self._required,
            'title': self._title
        }
       
    def value(self, value: str):
        self._value = value
        return self
    
    def title(self, value: str):
        self._title = value
        return self
    
    def description(self, value: str):
        self._description = value

    def required(self, value: bool):
        self._required = value
        return self
    
    def readonly(self, value: bool):
        self._readonly = value
        return self
    
    def type(self, type_name: str):
        self._type = self.get_type_id(type_name)
        return self
    
    def get_type_id(self, type_name: str):
        try: 
            return self.TYPE_NAMES.index(type_name) 
        except ValueError: 
            return None       