

class EventHandler:

    def __init__(self, params):
        self._params = params
        
    def __call__(self):
        self.execute()

    def execute(self):
        pass
