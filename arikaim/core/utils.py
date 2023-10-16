import sys, os, importlib, imp
from string import Template
from datetime import datetime
from arikaim.core.path import Path

def inlcude_service_lib(service_name: str, module_name: str):
    path = os.path.join(Path.services(service_name),'lib',module_name + '.py')
    return load_module(module_name,path)

def load_service_config(service_name: str):
    return load_module('config',os.path.join(Path.services(service_name),'config.py'))

def call(object, method_name: str, **params):
    method = getattr(object,method_name,None)
    if not method:
        return False

    return method(**params)

def time_now() -> int:
    return datetime.now().timestamp()

def load_class(path, module_name, class_name):
    module_path = os.path.join(path)

    sys.path.append(module_path)
    module = importlib.import_module(module_name) 
   
    return getattr(module,class_name)

def load_module_vars(path, module_name):
    module_path = os.path.join(path)
    sys.path.append(module_path)

    return importlib.import_module(module_name, package = module_name)
   
def load_module(name, path):
    return imp.load_source(name,path)

def parse_text(text, vars):
    template = Template(text)
    return template.substitute(vars)

def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class2, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w, class2).__new__(class2, *args, **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w

def php_unserialize(text, delimiter = ';', var_delimiter = '|', value_delimiter = ':'):
    vars = {}
    text = text.replace('{','')
    text = text.replace('}','')

    items = text.split(delimiter)
    for item in items:
        sub_item = item.split(var_delimiter)
        key = sub_item[0]
        if key != '':          
            if len(sub_item) >= 2:
                value = sub_item[1].split(value_delimiter)
            else:
                value = ''
            if len(value) > 0:
                vars[key] = value[1]

    return vars