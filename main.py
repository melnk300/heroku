import datetime as dt
import os
from flask_jwt_extended import JWTManager

from flask import Flask

from utils.cfg import CONFIG

from api import users_api
from api import groups_api
from api import tasks_api

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = CONFIG.JWT_SECRET
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = dt.timedelta(days=1)
jwt = JWTManager(app)
app.debug = True



if __name__ == "__main__":
    app.register_blueprint(users_api.blueprint)
    app.register_blueprint(groups_api.blueprint)
    app.register_blueprint(tasks_api.blueprint)
    app.run(host='0.0.0.0')
