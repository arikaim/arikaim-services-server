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
    def view(path: str = ''):       
        return os.path.join(Path.arikaim(),'view',path.strip('/'))
    
    @staticmethod
    def templates():       
        return os.path.join(Path.view(),'view','templates','python')
    
    @staticmethod
    def template(name: str):       
        return os.path.join(Path.templates(),name)
    
    @staticmethod
    def model(service_name):
        if not service_name:
            return os.path.join(Path.base(),'db','models')
        else:
            return os.path.join(Path.services(service_name),'models')

    @staticmethod
    def actions(service_name):
        if not service_name:
            return os.path.join(Path.base(),'actions')
        else:
            return os.path.join(Path.services(service_name),'actions')
        
    @staticmethod
    def job(service_name):
        if not service_name:
            return os.path.join(Path.base(),'queue','jobs')
        else:
            return os.path.join(Path.services(service_name),'jobs')

    @staticmethod
    def console(service_name):
        return os.path.join(Path.services(service_name),'console')

    @staticmethod
    def storage(path: str = ''):       
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
        