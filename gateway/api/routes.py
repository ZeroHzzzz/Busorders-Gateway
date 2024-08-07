from flask import request
import utils
import service
from flask import Blueprint
from . import api

@api.route('/login', methods=['POST'])
def loginHandler():
    '''这里我只返回token，其他视情况需要返回'''
    data = request.get_json()
    phone = data.get('phone')
    pwd = data.get('password')
    if not phone or not pwd:
        return utils.generate_response(200400, 'Invalid Parameter'), 200
    code, msg, data = service.login(phone, pwd)
    if code == 200:
        return utils.generate_response(200200, msg, data.get('token'))
    elif code >= 500:
        return utils.generate_response(200500, msg)
    else:
        return utils.generate_response(200400, msg)