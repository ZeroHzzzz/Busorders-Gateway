from flask import request
import utils
import service
from flask import Blueprint
from utils import msg

api = Blueprint('api', __name__)
@api.route('/login', methods=['POST'])
def loginHandler():
    '''这里我只返回token，其他视情况需要返回'''
    data = request.get_json()
    phone = data.get('phone')
    pwd = data.get('password')
    if not phone or not pwd:
        return utils.generate_response(400, msg.msg_invalidparam), 200
    code, message, data = service.login.login(phone, pwd)
    if code == 200:
        return utils.generate_response(code, message, data.get('token')), 200
    # elif code >= 500:
    #     return utils.generate_response("200"+code, message)
    else:
        return utils.generate_response(code, message), 200
