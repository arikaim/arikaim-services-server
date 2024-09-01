import json
from arikaim.core.db.db import load_model_class
from arikaim.core.collection.properties import Properties

class DriverManager():
    _instance = None

    def __init__(self):     
        pass

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    def get_config(self, driver_name: str):
        Drivers = load_model_class('Drivers','drivers')
        json_text = Drivers.get_config(driver_name)
        if not json_text:
            return None
        
        data = json.loads(json_text)
        properties = Properties(data)
 
        return properties


drivers = DriverManager()
