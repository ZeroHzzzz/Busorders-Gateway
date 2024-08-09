import requests
import json
from utils import msg, api
import logging
from utils.utils import log_request_details

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def businfo(page, page_size, search, auth_header):
    headers = {'Authorization': auth_header}
    query_params = {'page': page, 'page_size': page_size, 'search': search}
    url = api.bus_info_url
    
    log_request_details(url, headers, params=query_params)
    
    try:
        response = requests.get(url, params=query_params, headers=headers)
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")

        if status_code == 200:
            return status_code, msg.msg_success, response_data
        elif status_code == 400:
            if 'detail' in response_data and 'code' in response_data['detail']:
                if response_data['detail']['code'] == "AUTH_FAIL":
                    return 401, msg.msg_unauth, None
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None

def bustime(shuttle_type, id, auth_header):
    headers = {'Authorization': auth_header}
    query_params = {'shuttle_type': shuttle_type}
    path_params = {'id': id}
    url = api.bus_time_url.format(**path_params)
    
    log_request_details(url, headers, params=query_params)
    
    try:
        response = requests.get(url, params=query_params, headers=headers)
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")

        if status_code == 200:
            return status_code, msg.msg_success, response_data
        elif status_code == 400:
            if 'detail' in response_data and 'code' in response_data['detail']:
                if response_data['detail']['code'] == "AUTH_FAIL":
                    return 401, msg.msg_unauth, None
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None

def busdate(bus_time, bus_id, auth_header):
    headers = {'Authorization': auth_header}
    query_params = {'shuttle_bus_time': bus_time}
    path_params = {'id': bus_id}
    url = api.bus_date_url.format(**path_params)
    
    log_request_details(url, headers, params=query_params)
    
    try:
        response = requests.get(url, params=query_params, headers=headers)
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")

        if status_code == 200:
            return status_code, msg.msg_success, response_data
        elif status_code == 400:
            if 'detail' in response_data and 'code' in response_data['detail']:
                if response_data['detail']['code'] == "AUTH_FAIL":
                    return 401, msg.msg_unauth, None
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None

def busbook(bus_date, bus_station, auth_header):
    headers = {'Authorization': auth_header, 'Content-Type': 'application/json'}
    ret = {'shuttle_bus_date': bus_date, 'bus_station': bus_station, "has_ticket": False}
    url = api.bus_booking_url
    
    log_request_details(url, headers, data=ret)
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(ret))
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")
        
        if status_code == 200:
            return status_code, msg.msg_success, response_data
        elif status_code == 400:
            if 'detail' in response_data and 'code' in response_data['detail']:
                if response_data['detail']['code'] == "AUTH_FAIL":
                    return 401, msg.msg_unauth, None
            if 'detail' in response_data and 'non_field_errors' in response_data['detail']:
                return 404, response_data['detail']['non_field_errors'][0], None
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None

def bookrecord(page, page_size, status, auth_header):
    headers = {'Authorization': auth_header}
    query_params = {'page': page, 'page_size': page_size, 'status': status}
    url = api.bus_records_url
    
    log_request_details(url, headers, params=query_params)
    
    try:
        response = requests.get(url, params=query_params, headers=headers)
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")

        if status_code == 200:
            return status_code, msg.msg_success, response_data
        elif status_code == 400:
            if 'detail' in response_data and 'code' in response_data['detail']:
                if response_data['detail']['code'] == "AUTH_FAIL":
                    return 401, msg.msg_unauth, None
            return status_code, msg.msg_invalidparam, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None

def buscancel(id, auth_header):
    headers = {'Authorization': auth_header}
    path_params = {'id': id}
    url = api.bus_cancel_url.format(**path_params)
    
    log_request_details(url, headers)
    
    try:
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")

        if status_code == 200:
            return status_code, msg.msg_success, None
        elif status_code == 400:
            if 'detail' in response_data and 'code' in response_data['detail']:
                if response_data['detail']['code'] == "AUTH_FAIL":
                    return 401, msg.msg_unauth, None
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None

def getbulktask(page, page_size, auth_header):
    headers = {'Authorization': auth_header}
    query_params = {'page': page, 'page_size': page_size}
    url = api.bus_bulktask_url
    
    log_request_details(url, headers, params=query_params)
    
    try:
        response = requests.get(url, params=query_params, headers=headers)
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")

        if status_code == 200:
            return status_code, msg.msg_success, response_data
        elif status_code == 400:
            if 'detail' in response_data and 'code' in response_data['detail']:
                if response_data['detail']['code'] == "AUTH_FAIL":
                    return 401, msg.msg_unauth, None
            return status_code, msg.msg_invalidparam, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None
