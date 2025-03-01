import json
import typing

from starlette.responses import JSONResponse

class ApiResponse(JSONResponse):
    
    def render(self, content: typing.Any) -> bytes:
        return json.dumps(content,
            ensure_ascii = False,
            allow_nan = False,
            indent = 4,
            default = lambda obj : obj.to_json(),
            separators = (",", ":"),
        ).encode("utf-8")
        