import datetime as dt
import os

from flask import Flask
from flask_jwt_extended import JWTManager

from utils.cfg import CONFIG

from api import users_api

app = Flask(__name__)
app.debug = True
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = dt.timedelta(days=1)
jwt = JWTManager(app)

if __name__ == "__main__":
    app.register_blueprint(users_api.blueprint)
    app.run(host='0.0.0.0')
