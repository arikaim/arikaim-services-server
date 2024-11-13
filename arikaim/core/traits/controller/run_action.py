from typing import Union
from arikaim.core.utils import create_action
from arikaim.core.logger import logger
import traceback

class RunAction():

    def run_action(self, 
        class_name, 
        service_name: Union[str,None] = None, 
        module_name: Union[str,None] = None, 
        options: dict = {}
    ):
        try:
            if service_name and module_name:
                action = create_action(service_name,module_name,class_name,options)
            else:
                action = class_name(options)

            action.run()

            if action.has_error() == True:              
                self.error(action.error)
                return 
        
            for key, value in action.results.items():               
                self.field(key,value)
            
            self.field('message',action.get('message','Success!'))
            
        except Exception as error:      
            logger.error(traceback.format_exc())    
            self.error('Error run action: ' + str(error))