from flask import request
from utils import utils
import service
from flask import Blueprint
from utils import msg
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user = Blueprint('user', __name__)

@user.route('/qrcode', methods=['GET'])
def qrcodeHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
    
    try:
        data = request.get_json()
        open_id = data.get('openid')
    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400

    if not open_id:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.user.getqrcode(open_id, auth_header)
    return utils.generate_response(code, message, data), code

@user.route('/company', methods=['GET'])
def companyHandler():
    try:
        data = request.get_json()
        phone = data.get('phone')
        pwd = data.get('password')
    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400

    if not phone or not pwd:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.user.getcompany(phone, pwd)
    return utils.generate_response(code, message, data), code
