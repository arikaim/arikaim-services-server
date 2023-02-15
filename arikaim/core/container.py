import types
from inspect import isclass
from arikaim.core.utils import singleton


@singleton
class Container:
 
  def __init__(self):
    self._services = {} # Services registry

  def register(self, name: str):
    def wrap(fn):  
      self.add(name,fn)
    return wrap

  def add(self, name: str, item):
    if self.has(name):
      raise RuntimeError("Service name '{}' exists." . format(name))
    if isclass(item):
      def class_wrap(self):
        return item()

      self._services[name] = class_wrap
    else:
      self._services[name] = item
  
  def get(self, name: str):
    if not self.has(name):
      raise RuntimeError("Service '{}' not found." . format(name))
    item = self._services[name]
    if type(item) in [types.LambdaType, types.FunctionType]:
      item = item()
      self._services.pop(name)  
      self._services[name] = item

    return item

  def has(self, name: str) -> bool:
    return name in self._services.keys()


di = Container()