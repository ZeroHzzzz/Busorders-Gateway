from flask import Flask
from flask import Blueprint
from api import api
from api.bus import bus

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

api.register_blueprint(bus, url_prefix='/bus')

if __name__ == "__main__":
    app.run(debug=True, port=5001)