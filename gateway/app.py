import yaml
from flask import Flask, g, request
import logging
import time
from api.routes import api
from api.bus.routes import bus
from api.user.routes import user

def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def create_app(config_file='gateway\config.yaml'):
    app = Flask(__name__)

    # 加载配置
    config = load_config(config_file)
    app.config.update(config)

    # 根据配置文件设置测试模式
    app.config['TESTING'] = config.get('TESTING', False)
    app.config['DEBUG'] = config.get('DEBUG', False)

    # 设置日志记录
    logger = logging.getLogger(__name__)

    if app.config['LOG_TO_FILE'] and not app.config['TESTING']:
        # 仅在非测试模式下将日志记录到文件
        file_handler = logging.FileHandler(app.config['LOG_FILE_PATH'])
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        logging.basicConfig(level=logging.INFO)

    # 注册蓝图
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(bus, url_prefix='/api/bus')
    app.register_blueprint(user, url_prefix='/api/user')

    # 中间件：记录请求的开始时间
    @app.before_request
    def start_timer():
        g.start_time = time.time()

    # 中间件：记录请求和响应的详细信息
    @app.after_request
    def log_request(response):
        if not request.endpoint:  # 如果请求没有匹配到路由，不记录日志
            return response

        now = time.time()
        duration = round(now - g.start_time, 2)
        method = request.method
        url = request.url
        status_code = response.status_code
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)

        log_params = [
            ('method', method),
            ('url', url),
            ('status', status_code),
            ('duration', f"{duration}s"),
            ('ip', ip)
        ]

        log_message = " | ".join(f"{name}: {value}" for name, value in log_params)
        logger.info(log_message)

        return response

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
