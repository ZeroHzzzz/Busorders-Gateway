from flask import Flask
from flask import Blueprint
from api.routes import api
from api.bus.routes import bus

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

app.register_blueprint(bus, url_prefix='/api/bus')

if __name__ == "__main__":
    app.run(debug=True, port=5001)