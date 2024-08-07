# from . import utils
from . import msg
from flask import jsonify

def generate_response(status_code, message, data=None):
    ret = {
        "status": status_code,
        "message": message,
        "data": data
    }
    return jsonify(ret)