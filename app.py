from datetime import datetime as dt
import datetime as dt_
import os
import logging

from flask_jwt_extended import JWTManager, set_access_cookies, create_access_token, get_jwt_identity, get_jwt
from flask_cors import CORS
from flask import Flask
from utils.cfg import CONFIG

from api import users_api
from api import groups_api
from api import tasks_api

logging.basicConfig(filename='log.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
cors = CORS(app, supports_credentials=True, resource=r'/*')
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = CONFIG.JWT_SECRET
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_CSRF_CHECK_FORM'] = False
app.debug = True


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = dt.now(dt_.timezone.utc)
        target_timestamp = dt.timestamp(now + dt_.timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response

    except (RuntimeError, KeyError):
        return response


app.register_blueprint(users_api.blueprint)
app.register_blueprint(groups_api.blueprint)
app.register_blueprint(tasks_api.blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
