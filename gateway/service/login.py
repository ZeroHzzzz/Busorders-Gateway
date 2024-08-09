import requests
import json
from utils import msg, api
import logging
from utils.utils import log_request_details

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def login(phone, pwd):
    headers = {'Content-Type': 'application/json'}
    ret = {'phone': phone, 'password': pwd}
    url = api.login_url

    # Log the request details
    log_request_details(url, headers, data=ret)

    try:
        response = requests.post(url, headers=headers, data=json.dumps(ret))
        status_code = response.status_code
        response_data = response.json()
        logger.info(f"Response: {response_data}")

        if status_code == 200:
            return status_code, msg.msg_success, response_data
        elif status_code == 400:
            return status_code, msg.msg_wrongpwd, None
        elif status_code == 404:
            return status_code, msg.msg_notfound, None
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return 500, msg.msg_unknown, None
