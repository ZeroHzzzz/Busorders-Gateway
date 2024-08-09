import requests
import json
from utils import msg, api
import logging
from utils.utils import log_request_details

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def getqrcode(open_id, auth_header):
    headers = {'Authorization': auth_header}
    query_params = {'openid': open_id}
    url = api.user_qrcode_url

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

def getcompany(phone, pwd):
    headers = {'Content-Type': 'application/json'}
    ret = {'phone': phone, 'password': pwd}
    url = api.user_company_url

    log_request_details(url, headers, data=ret)
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(ret))
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")
        
        if status_code == 200:
            return status_code, msg.msg_success, response_data[0]
        elif status_code == 400:
            return status_code, msg.msg_wrongpwd, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None
