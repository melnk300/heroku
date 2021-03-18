import flask
from flask import jsonify, abort
from pprint import pprint

from data import db_session
from data.models.Users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
)



@blueprint.route('/api/users')
def get_all_users():
    sess = db_session.create_session()
    users = sess.query(User).all()
    return jsonify([user.to_dict() for user in users])

@blueprint.route('/api/users<user_id>')
def get_user_by_id(user_id):
    sess = db_session.create_session()
    users = sess.query(User).all()
    return jsonify([user.to_dict() for user in users])

