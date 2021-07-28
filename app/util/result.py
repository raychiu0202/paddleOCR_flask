import json

from flask import Response

from app.util.errors import Errors


class Result:

    @staticmethod
    def ok(data=None):
        result = {"code": 0, "msg": "success", "data": data if data is not None else {}}
        return Response(json.dumps(result, ensure_ascii=False), mimetype='application/json')

    @staticmethod
    def error(err: Errors):
        result = {"code": err.code, "msg": err.msg, "data": {}}
        return Response(json.dumps(result, ensure_ascii=False), mimetype='application/json')
