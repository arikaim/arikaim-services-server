

class Job:

    def __init__(self):
        self._schedule_time = None
        self._name = None
        self._interval = None

    def __call__(self):
        self.execute()

    def execute(self):
        pass

    @property
    def interval(self):
        return self._interval