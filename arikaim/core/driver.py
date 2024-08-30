


class DriverManager():
    _instance = None

    def __init__(self):     
        pass

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
    def get_config(driver_name: str):
        pass


drivers = DriverManager()
