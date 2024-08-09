from flask import jsonify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_response(status_code, message, data=None):
    ret = {
        "code": status_code,
        "message": message,
        "data": data
    }
    return jsonify(ret)

def log_request_details(url, headers, params=None, data=None):
    logger.info(f"Request URL: {url}")
    logger.info(f"Headers: {headers}")
    if params:
        logger.info(f"Query Parameters: {params}")
    if data:
        logger.info(f"Payload: {data}")