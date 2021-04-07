from flask import jsonify, abort, request, Blueprint
from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import JWTManager

from pprint import pprint

from utils.utils import hash_password, check_password

from data import db_session
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('groups_api', __name__)


def if_group_not_found(group_id):
    sess = db_session.create_session()
    group = sess.query(Group).get(group_id)
    if not group:
        abort(404, 'Group id not found')

def