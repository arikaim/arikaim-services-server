import json
import os
import pip
from arikaim.core.path import Path
from arikaim.core.logger import logger

def load_package_descriptor(service_name: str):
    package_file = os.path.join(Path.services(service_name),'arikaim-package.json')
    file = open(package_file,'r')
   
    data = json.loads(file.read())
    packages = data['require']['packages'];

    for package in packages:        
        logger.info('Install Package ' + package)
        
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])
    

def install_packages(app):
    
    for service_name in app.services:
        logger.info('Service ' + service_name)
        load_package_descriptor(service_name)