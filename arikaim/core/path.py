import os

class Path:
    base_path = ''

    @staticmethod
    def base(relative = True):
        if Path.base_path is None:
            Path.base_path = os.getcwd()

        if relative == True:
            return Path.base_path
           
        return os.path.abspath(Path.base_path)

    @staticmethod
    def arikaim(relative = True):
        return os.path.join(Path.base(relative),'arikaim')
    
    @staticmethod
    def view(path: str = '', relative = True):       
        return os.path.join(Path.arikaim(relative),'view',path.strip('/'))
    
    @staticmethod
    def templates(relative = True):       
        return os.path.join(Path.view(relative = relative),'templates')
    
    @staticmethod
    def template(name: str, relative = True):       
        return os.path.join(Path.templates(relative),name)
    
    @staticmethod
    def model(service_name, relative = True):
        if not service_name:
            return os.path.join(Path.base(relative),'db','models')
        else:
            return os.path.join(Path.services(service_name, relative = relative),'models')

    @staticmethod
    def actions(service_name, relative = True):
        if not service_name:
            return os.path.join(Path.base(relative),'actions')
        else:
            return os.path.join(Path.services(service_name, relative = relative),'actions')
        
    @staticmethod
    def job(service_name, relative = True):
        if not service_name:
            return os.path.join(Path.base(relative),'queue','jobs')
        else:
            return os.path.join(Path.services(service_name, relative = relative),'jobs')

    @staticmethod
    def console(service_name, relative = True):
        return os.path.join(Path.services(service_name, relative = relative),'console')

    @staticmethod
    def storage(path: str = '', relative = True):       
        return os.path.join(Path.base(relative),'arikaim','storage',path.strip('/'))
        
    @staticmethod
    def services(name = '', relative = True):
        services_path = os.path.join(Path.base(relative),'arikaim','services')
        if name != "":
            return os.path.join(services_path,name)
        return services_path

    @staticmethod
    def config(file_name = None, relative = True):
        path = os.path.join(Path.base(relative),'arikaim','config')
        if (file_name != None): 
            path = os.path.join(path,file_name) 
        return path
        