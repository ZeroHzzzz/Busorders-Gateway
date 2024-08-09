from flask import request
from utils import utils
import service
from flask import Blueprint
from utils import msg
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api = Blueprint('api', __name__)

@api.route('/login/phone', methods=['POST'])
def loginByPhoneHandler():
    try:
        data = request.get_json()
        if not data:
            return utils.generate_response(400, msg.msg_invalidparam), 400

        phone = data.get('phone')
        pwd = data.get('password')

    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    if not phone or not pwd:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.login.loginByPhone(phone, pwd)
    return utils.generate_response(code, message, data), code


@api.route('/login/wx', methods=['POST'])
def loginByWXHandler():
    try:
        data = request.get_json()
        if not data:
            return utils.generate_response(400, msg.msg_invalidparam), 400

        corpcode = data.get('corpcode')
        openid = data.get('openid')

    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    if not openid or not corpcode:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.login.loginByWX(corpcode, openid)
    return utils.generate_response(code, message, data), code


@api.route('/test', methods=['GET'])
def testHandler():
    return utils.generate_response(200, msg.msg_success), 200
