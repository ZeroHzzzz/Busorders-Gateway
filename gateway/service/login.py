import requests
import json
from utils import msg, api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def login(phone, pwd):
    headers = {'Content-Type': 'application/json'}
    ret = {
        'phone': phone,
        'password': pwd,
    }

    try:
        response = requests.post(api.login_url, headers=headers, data=json.dumps(ret))
        response.raise_for_status()
        status_code = response.status_code
        if status_code == 200:
            return status_code, msg.msg_success, response.json()
        elif status_code == 400:
            return status_code, msg.msg_wrongpwd, None
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
