from flask import request
import utils
import service
from flask import Blueprint
from utils import msg

bus = Blueprint('bus', __name__)

@bus.route('/info', methods=['GET'])
def businfoHandler():
    auth_header = request.headers.get('Authorization')
    page = request.args.get('source', 1)
    page_size = request.args.get('page_size', 8)
    search = request.args.get('search', None)
    
    if auth_header is None:
        return utils.generate_response(200401, msg.msg_unauth), 200 
    code, message, data = service.bus.businfo(page, page_size, search, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), 200

@bus.route('/time', methods=['GET'])
def bustimeHandler():
    '''通过线路id查询该线路的时间表'''
    auth_header = request.headers.get('Authorization')
    data = request.get_json()
    shuttle_type = data.get('shuttle_type')
    id = data.get('id')
    if auth_header is None:
        return utils.generate_response(200401, msg.msg_unauth), 200
    if not shuttle_type or not id:
        return utils.generate_response(400, msg.msg_invalidparam), 200
    code, message, data = service.bus.bustime(shuttle_type, id, auth_header)
    
    if code == 200:
        return utils.generate_response(code, message, data), 200
    else:
        return utils.generate_response(code, message), 200

@bus.route('/date', methods=['GET'])
def busdateHandler():
    auth_header = request.headers.get('Authorization')
    data = request.get_json()
    bus_time = data.get('bus_time')
    bus_id = data.get('bus_id')
    
    if auth_header is None:
        return utils.generate_response(200401, msg.msg_unauth), 200
    if not bus_time or not bus_id:
        return utils.generate_response(400, msg.msg_invalidparam), 200
    
    code, message, data = service.bus.busdate(bus_time, bus_id, auth_header)
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), 200
    
@bus.route('/book', methods=['POST'])
def bookHandler():
    auth_header = request.headers.get('Authorization')
    data = request.get_json()
    bus_date = data.get('bus_date')
    bus_station = data.get('bus_station')
    
    if auth_header is None:
        return utils.generate_response(200401, msg.msg_unauth), 200
    if not bus_date or not bus_station:
        return utils.generate_response(400, msg.msg_invalidparam), 200
    
    code, message, data = service.bus.busbook(bus_date, bus_station, auth_header)
    if code == 200:
        return utils.generate_response(code, message, data), 200
    else:
        return utils.generate_response(code, message), 200
    
@bus.route('/bookrecord', methods=['GET'])
def bookrecordHandler():
    auth_header = request.headers.get('Authorization')
    page = request.args.get('source', 1)
    page_size = request.args.get('page_size', 8)
    status = request.args.get('status', 20)
    
    if auth_header is None:
        return utils.generate_response(200401, msg.msg_unauth), 200
    
    code, message, data = service.bus.bookrecord(page, page_size, status, auth_header)
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), 200
    
@bus.route('/cancelbook', methods=['GET'])
def cancelbookHandler():
    auth_header = request.headers.get('Authorization')
    data = request.get_json()
    id = data.get('id')
    
    if auth_header is None:
        return utils.generate_response(200401, msg.msg_unauth), 200
    if not id:
        return utils.generate_response(400, msg.msg_invalidparam), 200
    
    code, message, data = service.bus.buscancel(id, auth_header)
    if code == 200:
        return utils.generate_response(code, message), 200
    else:
        return utils.generate_response(code, message), 200
    
@bus.route('/bulktask', methods=['GET'])
def bulktaskHandler():
    auth_header = request.headers.get('Authorization')
    page = request.args.get('source', 1)
    page_size = request.args.get('page_size', 8)
    
    if auth_header is None:
        return utils.generate_response(200401, msg.msg_unauth), 200
    
    code, message, data = service.bus.getbulktask(page, page_size, auth_header)
    if code == 200:
        return utils.generate_response(code, message, data.get('results')), 200
    else:
        return utils.generate_response(code, message), 200