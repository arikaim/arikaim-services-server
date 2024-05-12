import os

class Path:
    base_path = ''

    @staticmethod
    def base():
        if Path.base_path is None:
            Path.base_path = os.getcwd()
            
        return Path.base_path

    @staticmethod
    def arikaim():
        return os.path.join(Path.base(),'arikaim')
    
    @staticmethod
    def model_path(service_name):
        if not service_name:
            return os.path.join(Path.base(),'db','models')
        else:
            return os.path.join(Path.services(service_name),'models')

    @staticmethod
    def job_path(service_name):
        if not service_name:
            return os.path.join(Path.base(),'queue','jobs')
        else:
            return os.path.join(Path.services(service_name),'jobs')

    @staticmethod
    def console_path(service_name):
        return os.path.join(Path.services(service_name),'console')

    @staticmethod
    def storage_path(path: str = ''):       
        return os.path.join(Path.base(),'arikaim','storage',path.strip('/'))
        
    @staticmethod
    def services(name = ''):
        services_path = os.path.join(Path.base(),'arikaim','services')
        if name != "":
            return os.path.join(services_path,name)
        return services_path

    @staticmethod
    def config(file_name = None):
        path = os.path.join(Path.base(),'arikaim','config')
        if (file_name != None): 
            path = os.path.join(path,file_name) 
        return path
        