import datetime as dt
import os

from flask import Flask

from utils.cfg import CONFIG

from api import users_api
from api import tasks_api

app = Flask(__name__)
app.debug = True
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = dt.timedelta(days=1)


if __name__ == "__main__":
    app.register_blueprint(users_api.blueprint)
    app.register_blueprint(tasks_api.blueprint)
    app.run(host='0.0.0.0')
