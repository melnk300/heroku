from data import db_session
import jobs_api
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
app.debug = True

def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run()

if __name__ == "__main__":
    main()