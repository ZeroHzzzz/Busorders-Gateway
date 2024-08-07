from flask import Flask
from api.routes import api
from api.bus.routes import bus
from api.user.routes import user

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

app.register_blueprint(bus, url_prefix='/api/bus')

app.register_blueprint(user, url_prefix='/api/user')

if __name__ == "__main__":
    app.run(debug=True, port=5001)