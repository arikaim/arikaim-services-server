

class Propertiy:

    def __init__(self, name: str, data):
        self._name = name

        if type(data) is dict:
            for key in data:
                setattr(self,key,data[key])
    