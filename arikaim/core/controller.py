from starlette.endpoints import HTTPEndpoint
from starlette.types import Receive, Scope, Send

from arikaim.core.api_descriptor import ApiDescriptor
from arikaim.core.response import ApiResponse

class Controller(HTTPEndpoint):
  
    def __init__(self, scope: Scope, receive: Receive, send: Send):
        """Constructor. """
        super().__init__(scope, receive, send)
        # response fields
        self._status = 'ok'
        self._errors = []
        self._code = 200 
        self._fields = {}
        self._descriptor = None

        self.boot()
        
    def boot(self):
        pass

    def response(self):       
        return ApiResponse(self.get_result())

    def message(self, value):
        self._fields['message'] = value

    def field(self, key, value):
        self._fields[key] = value

    def error(self, error):
        self._errors.append(error)

    @property
    def status(self,value):
        self._status = value
    
    @property
    def code(self, value):
        self._code = value

    def get_result(self):  

        if (len(self._errors) > 0):
            self._status = 'error'

        return {
            'result': self._fields,
            'status': self._status,
            'errors': self._errors,
            'code'  : self._code
        }

    @property
    def descriptor(self):
        if self._descriptor == None:
            self._descriptor = ApiDescriptor()

        return self._descriptor
    
    @classmethod
    def init_descriptor(cls, descriptor):               
        pass

# Decorators
def put(func):
    async def wrap(self, *args):
        query_params = args[0].query_params
        path_params = args[0].path_params
        body = await args[0].json()
        data = {**query_params,**path_params, **body}

        await func(self,args[0],data)
        return self.response()
    return wrap

def post(func):
    async def wrap(self, *args):
        query_params = args[0].query_params
        path_params = args[0].path_params
        body = await args[0].json()
        data = {**query_params,**path_params, **body}

        await func(self,args[0],data)
        return self.response()
    return wrap

def get(func):
    async def wrap(self, *args):
        query_params = args[0].query_params
        path_params = args[0].path_params
        data = {**query_params,**path_params}

        await func(self,args[0],data)      
        return self.response()
    return wrap

def delete(func):
    async def wrap(self, *args):
        query_params = args[0].query_params
        path_params = args[0].path_params
        data = {**query_params,**path_params}

        await func(self,args[0],data)
        return self.response()
    return wrap