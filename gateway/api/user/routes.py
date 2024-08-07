from flask import request
import utils
import service
from flask import Blueprint
from utils import msg

user = Blueprint('user', __name__)

@user.route('/qrcode', methods=['GET'])
def qrcodeHandler():
    auth_header = request.headers.get('Authorization')
    data = request.get_json()
    open_id = data.get('openid')
    
    if auth_header is None:
        return utils.generate_response(401, msg.msg_unauth), 200
    if not open_id:
        return utils.generate_response(400, msg.msg_invalidparam), 200
    
    code, message, data = service.user.getqrcode(open_id, auth_header)
    if code == 200:
        return utils.generate_response(code, message, data), 200
    else:
        return utils.generate_response(code, message), 200

@user.route('/getcompany', methods=['POST'])
def companyHandler():
    data = request.get_json()
    phone = data.get('phone')
    pwd = data.get('password')
    
    if not phone or not pwd:
        return utils.generate_response(400, msg.msg_invalidparam), 200
    
    code, message, data = service.user.getcompany(phone, pwd)
    if code == 200:
        return utils.generate_response(code, message, data), 200
    else:
        return utils.generate_response(code, message), 200
