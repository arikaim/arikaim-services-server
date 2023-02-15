import json
import typing
from starlette.background import BackgroundTask
from starlette.responses import JSONResponse

class ApiResponse(JSONResponse):
    media_type = "application/json"

    def __init__(self, 
        content: typing.Any,
        status_code: int = 200,
        errors: typing.Optional[typing.Dict[str, str]] = [],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        media_type: typing.Optional[str] = None,
        background: typing.Optional[BackgroundTask] = None
    ) -> None:   
        self._status = 'ok'
        self._errors = errors
        self._code = status_code 
        self._fields = {}
        super().__init__(content, status_code, headers, media_type, background)
       

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(self.get_result(),
            ensure_ascii = False,
            allow_nan = False,
            indent = None,
            separators = (",", ":"),
        ).encode("utf-8")

    def get_result(self):  

        if (len(self._errors) > 0):
            self._status = 'error'

        return {
            'result': self._fields,
            'status': self._status,
            'errors': self._errors,
            'code'  : self._code
        }
     
    def field(self, key, value):
        self._fields[key] = value

    def message(self, msg):
        self.field('message',msg)
        
    def status(self, value):
        self._status = value
    
    def code(self, value):
        self._code = value

    def error(self, msg):
        self._errors.append(msg)
        