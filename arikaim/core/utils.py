import sys, os, importlib, imp
from string import Template
from datetime import datetime
from arikaim.core.path import Path
import psutil

def create_action(service_name, module_name, class_name):   
    class_name = load_class(Path.actions(service_name),module_name,class_name) 
    return class_name()

def get_process_memory():
    process = psutil.Process(os.getpid())
    return (process.memory_info().rss / 1024)

def load_service_module(service_name: str, module_name: str):
    path = os.path.join(Path.services(service_name),module_name + '.py')  
    return load_module(module_name,path)

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
    try:
        return imp.load_source(name,path)
    except BaseException as e:
        print(format(e))       
        return None
    
def parse_text(text, vars):
    template = Template(text)
    return template.substitute(vars)

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