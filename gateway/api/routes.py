from flask import request
from utils import utils
import service
from flask import Blueprint
from utils import msg
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def loginHandler():
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
    
    code, message, data = service.login.login(phone, pwd)
    return utils.generate_response(code, message, data), code

@api.route('/test', methods=['GET'])
def testHandler():
    return utils.generate_response(200, msg.msg_success), 200
