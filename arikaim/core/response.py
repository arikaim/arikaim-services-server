import json
import typing

from starlette.responses import JSONResponse

class ApiResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(content,
            ensure_ascii = False,
            allow_nan = False,
            indent = None,
            default = lambda obj : obj.to_json(),
            separators = (",", ":"),
        ).encode("utf-8")
        