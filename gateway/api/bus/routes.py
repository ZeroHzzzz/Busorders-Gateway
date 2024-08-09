from flask import request, jsonify
import service
from flask import Blueprint
from utils import msg, utils
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bus = Blueprint('bus', __name__)

@bus.route('/info', methods=['GET'])
def businfoHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
    
    page = request.args.get('source', default=1, type=int)
    page_size = request.args.get('page_size', default=8, type=int)
    search = request.args.get('search')
    
    code, message, data = service.bus.businfo(page, page_size, search, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), code

@bus.route('/time', methods=['GET'])
def bustimeHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
    
    try:
        data = request.get_json()
        shuttle_type = data.get('shuttle_type')
        bus_id = data.get('id')
    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    if not shuttle_type or not bus_id:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.bus.bustime(shuttle_type, bus_id, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data), 200
    else:
        return utils.generate_response(code, message), code

@bus.route('/date', methods=['GET'])
def busdateHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
    
    try:
        data = request.get_json()
        bus_time = data.get('bus_time')
        bus_id = data.get('bus_id')
    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    if not bus_time or not bus_id:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.bus.busdate(bus_time, bus_id, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), code

@bus.route('/book', methods=['POST'])
def bookHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
    
    try:
        data = request.get_json()
        bus_date = data.get('bus_date')
        bus_station = data.get('bus_station')
    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    if not bus_date or not bus_station:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.bus.busbook(bus_date, bus_station, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data), 200
    else:
        return utils.generate_response(code, message), code

@bus.route('/bookrecord', methods=['GET'])
def bookrecordHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
  
    page = request.args.get('source', default=1, type=int)
    page_size = request.args.get('page_size', default=8, type=int)
    status = request.args.get('status', default=20, type=int)
    
    code, message, data = service.bus.bookrecord(page, page_size, status, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), code

@bus.route('/cancelbook', methods=['POST'])
def cancelbookHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
    
    try:
        data = request.get_json()
        bus_id = data.get('id')
    except Exception as e:
        logger.error(f"Error occurred while processing the request: {e}")
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    if not bus_id:
        return utils.generate_response(400, msg.msg_invalidparam), 400
    
    code, message, data = service.bus.buscancel(bus_id, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message), 200
    else:
        return utils.generate_response(code, message), code

@bus.route('/bulktask', methods=['GET'])
def bulktaskHandler():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return utils.generate_response(401, msg.msg_unauth), 401
  
    page = request.args.get('source', default=1, type=int)
    page_size = request.args.get('page_size', default=8, type=int)
  
    code, message, data = service.bus.getbulktask(page, page_size, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), code
