import requests
import json
from utils import msg, api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def businfo(page, page_size, search, auth_header):
    headers = {'Authorization':auth_header}
    query_params = {
        'page': page,
        'page_size': page_size,
        'search': search,
    }
    
    try:
        response = requests.get(api.bus_info_url, params=query_params, headers=headers)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, response.json()
        elif status_code == 400:
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            return status_code, msg.msg_unknown, None

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return 502, msg.msg_badgateway, None
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return 503, msg.msg_connectionerror, None
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return 504, msg.msg_timeout, None
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        return 500, msg.msg_unknown, None
    
def bustime(shuttle_type, id, auth_header):
    headers = {'Authorization':auth_header}
    query_params = {
        'shuttle_type': shuttle_type
    }
    path_params = {
        'id':id
    }
    url = api.bus_time_url.format(**path_params)
    
    try:
        response = requests.get(url, params=query_params, headers=headers)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, response.json()
        elif status_code == 400:
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            return status_code, msg.msg_unknown, None

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return 502, msg.msg_badgateway, None
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return 503, msg.msg_connectionerror, None
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return 504, msg.msg_timeout, None
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        return 500, msg.msg_unknown, None
    
def busdate(bus_time, bus_id, auth_header):
    headers = {'Authorization':auth_header}
    query_params = {
        'shuttle_bus_time': bus_time
    }
    path_params = {
        'id': bus_id
    }
    url = api.bus_date_url.format(**path_params)
    
    try:
        response = requests.get(url, params=query_params, headers=headers)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, response.json()
        elif status_code == 400:
            return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            return status_code, msg.msg_unknown, None

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return 502, msg.msg_badgateway, None
    
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return 503, msg.msg_connectionerror, None
    
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return 504, msg.msg_timeout, None
    
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        return 500, msg.msg_unknown, None
    
    
def busbook(bus_date, bus_station, auth_header):
    headers = {
        'Authorization':auth_header,
        'Content-Type': 'application/json'
    }
    ret = {
        'shuttle_bus_date': bus_date,
        'bus_station': bus_station,
        "has_ticket": False
    }
    try:
        response = requests.post(api.bus_booking_url, headers=headers, data=json.dumps(ret))
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, response.json()
        elif status_code == 400:
            response_data = response.json()
            # 这里查询不到是400，不是404
            if 'detail' in response_data and 'non_field_errors' in response_data['detail']:
                return status_code, response_data['detail']['non_field_errors'], None
            else:
                return status_code, msg.msg_invalidparam, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            return status_code, msg.msg_unknown, None

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return 502, msg.msg_badgateway, None
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return 503, msg.msg_connectionerror, None
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return 504, msg.msg_timeout, None
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        return 500, msg.msg_unknown, None
    
def bookrecord(page, page_size, status, auth_header):
    headers = {'Authorization':auth_header}
    query_params = {
        'page':page,
        'page_size':page_size,
        'status':status 
    }
    try:
        response = requests.get(api.bus_records_url, params=query_params, headers=headers)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, response.json()
        elif status_code == 400:
            return status_code, msg.msg_invalidparam, None
        else:
            return status_code, msg.msg_unknown, None
        
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return 502, msg.msg_badgateway, None
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return 503, msg.msg_connectionerror, None
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return 504, msg.msg_timeout, None
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        return 500, msg.msg_unknown, None

def buscancel(id, auth_header):
    headers = {'Authorization':auth_header}
    path_params = {
        'id': id
    }
    url = api.bus_cancel_url.format(**path_params)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, None
        elif status_code == 400:
            return status_code, msg.msg_invalidparam, None
        else:
            return status_code, msg.msg_unknown, None
        
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return 502, msg.msg_badgateway, None
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return 503, msg.msg_connectionerror, None
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return 504, msg.msg_timeout, None
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        return 500, msg.msg_unknown, None
    
def getbulktask(page, page_size, auth_header):
    headers = {'Authorization':auth_header}
    query_params = {
        'page':page,
        'page_size':page_size,
    }
    
    try:
        response = requests.get(api.bus_bulktask_url, params=query_params, headers=headers)
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, response.json()
        elif status_code == 400:
            return status_code, msg.msg_invalidparam, None
        else:
            return status_code, msg.msg_unknown, None
        
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return 502, msg.msg_badgateway, None
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return 503, msg.msg_connectionerror, None
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return 504, msg.msg_timeout, None
    except Exception as err:
        logger.error(f"An unexpected error occurred: {err}")
        return 500, msg.msg_unknown, None