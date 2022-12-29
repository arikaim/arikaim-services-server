from starlette.endpoints import HTTPEndpoint
from starlette.types import Receive, Scope, Send
from starlette.responses import JSONResponse

class Controller(HTTPEndpoint):
  
    def __init__(self, scope: Scope, receive: Receive, send: Send):
        """Constructor. """
        super().__init__(scope, receive, send)
        # response fields
        self._status = 'ok'
        self._errors = []
        self._code = 200 
        self._fields = {}
    
        self.boot()
        
    def boot(self):
        pass

    def response(self):       

        if (len(self._errors) > 0):
            self._status = 'error'
            
        return JSONResponse({
            'result': self._fields,
            'status': self._status,
            'errors': self._errors,
            'code'  : self._code
        })

    def message(self, value):
        self.field('message',value)

    def field(self,key,value):
        self._fields[key] = value

    def error(self, error):
        self._errors.append(error)

    @property
    def status(self,value):
        self._status = value
    
    @property
    def code(self, value):
        self._code = value

   

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