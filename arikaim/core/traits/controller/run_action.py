from arikaim.core.utils import create_action

class RunAction():

    def run_action(self, 
        service_name: str, 
        module_name: str, 
        class_name: str, 
        options: dict = {}
    ):
        try:
            action = create_action(service_name,module_name,class_name,options)
            action.run()
            if action.has_error() == True:              
                self.error(action.error)
                return 
        
            for key, value in action.results.items():               
                self.field(key,value)
            
            self.field('message',action.get('message','Success!'))
            
        except Exception as error:          
            self.error('Error run action' + class_name)