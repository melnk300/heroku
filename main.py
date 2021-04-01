from flask import Flask
from api import users_api

app = Flask(__name__)
app.debug = True

if __name__ == "__main__":
    app.register_blueprint(users_api.blueprint)
    app.run(host='0.0.0.0')
