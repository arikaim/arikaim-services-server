import os
import arikaim.core.globals as globals

class Path:

    @staticmethod
    def base():
        return globals.ARIKAIM_PATH

    @staticmethod
    def model_path(service_name):
        if not service_name:
            return os.path.join(globals.ARIKAIM_PATH,'db','models')
        else:
            return os.path.join(Path.services(service_name),'models')

    @staticmethod
    def job_path(service_name):
        if not service_name:
            return os.path.join(globals.ARIKAIM_PATH,'queue','jobs')
        else:
            return os.path.join(Path.services(service_name),'jobs')

    @staticmethod
    def console_path(service_name):
        return os.path.join(Path.services(service_name),'console')

    @staticmethod
    def storage_path(path: str = ''):       
        return os.path.join(globals.ARIKAIM_PATH,'arikaim','storage',path.strip('/'))
        
    @staticmethod
    def services(name = ''):
        services_path = os.path.join(globals.ARIKAIM_PATH,'arikaim','services')
        if name != "":
            return os.path.join(services_path,name)
        return services_path

    @staticmethod
    def config(file_name = None):
        path = os.path.join(globals.ARIKAIM_PATH,'arikaim','config')
        if (file_name != None): 
            path = os.path.join(path,file_name) 
        return path
        