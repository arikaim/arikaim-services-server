import html
from schema import *
from starlette.endpoints import HTTPEndpoint
from starlette.types import Receive, Scope, Send
from starlette.responses import Response

from arikaim.core.collection.descriptor import PropertiesDescriptor
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
        self._schema = None
        self._media_type = 'application/json'
        self.boot()
        
    def media_type(self, value):
        self._media_type = value

    def schema(self, schema_def):
        self._schema = Schema(schema_def)

    def validate(self, data):
        if self._schema == None:
            return True
    
        try:
            return self._schema.validate(data)
        except SchemaError as e:
            self.error(str(e))
            return False

    def boot(self):
        pass

    def response(self):       
        if self._media_type == 'application/json':
            return ApiResponse(
                self.get_result(), 
                media_type = self._media_type
            )
        else:
            return Response(
                content = self._fields['content'], 
                media_type = self._media_type
            )
        
    def message(self, value):
        self._fields['message'] = value

    def field(self, key, value):
        self._fields[key] = value

    def content(self, value):
        self._fields['content'] = value

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

    @classmethod
    def descriptor(cls):
        descriptor = PropertiesDescriptor()
        cls.init_descriptor(descriptor)
   
        return descriptor
    
    @classmethod
    def init_descriptor(cls, descriptor):               
        pass


async def get_request_data(request):
    query_params = {}
    path_params = {}

    if request.query_params:
        query_params = request.query_params
    if request.path_params:
        path_params = request.path_params
  
    try:
        if request.headers['content-type'] == 'application/json':
            body = await request.json()
            data = {**query_params,**path_params,**body}
            # sanitize
            for key, val in body.items():
                if type(val) == str:
                    data[key] = html.escape(val)

        else:
            form = await request.form()
            data = dict(form)
    except: 
        return {**query_params,**path_params}
   
    return data

def decorator(func):
    async def wrap(self, request):
        data = await get_request_data(request)
        if self.validate(data) == False:
            return self.response()
        else:
            await func(self,request,data)
        return self.response()
    
    return wrap

# Decorators
def put(func):
    return decorator(func)

def post(func):
    return decorator(func)

def get(func):
    return decorator(func)

def delete(func):
    return decorator(func)