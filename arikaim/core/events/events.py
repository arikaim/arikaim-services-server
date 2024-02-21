from arikaim.core.db.db import load_model_class


class Events:

    def __init__(self):
        pass

    def register(event_name, event_handler):
        pass
    
    def unregister(event_name, event_handler):
        pass
    
    def unregister_all(event_name):
        pass

    def fire(event_name, params):
        pass