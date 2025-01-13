
class Job:

    def __init__(self, name = None, interval = None, datetime = None):     
        self._name = name
        self._interval = interval
        self._datetime = datetime

    def __call__(self):
        self.execute()

    def execute(self):
        raise Exception('Job execute methos not implemented')
    
    @property
    def interval(self):
        return self._interval
    
    @property
    def datetime(self):
        return self._datetime