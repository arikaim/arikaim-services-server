

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
        self._example_value = None
        self._default = None

        if type(data) is dict:
            for key in data:
                setattr(self,key,data[key])


    def to_json(self):
        return {
            'name': self._name,
            'description': self._description,
            'example_value': self._example_value,
            'type': self._type,
            'readonly': self._readonly,
            'value': self._value,
            'default': self._default,
            'required': self._required,
            'title': self._title
        }
       
    @property
    def name(self):
        return self._nane

    def get_example_value(self):
        return self._example_value
    
    def default(self, value):
        self._default = value
        return self
    
    def value(self, value):
        self._value = value
        return self
    
    def example_value(self, value):
        self._example_value = value
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
        self._type = type_name
        return self
    
    def get_type_id(self, type_name: str):
        try: 
            return self.TYPE_NAMES.index(type_name) 
        except ValueError: 
            return None       