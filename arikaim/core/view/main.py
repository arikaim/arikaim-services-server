from jinja2 import Environment, FileSystemLoader, select_autoescape
from arikaim.core.path import Path

class View():
    _instance = None

    def __init__(self):   
        self._templates_path = Path.templates()

        self._env = Environment(
            loader = FileSystemLoader(self._templates_path),
            autoescape = select_autoescape()
        )  
        pass

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


    def render_template(self, path, data = {}):
        template = self._env.get_template(path)
        content = template.render(data)
        return content



view = View()
