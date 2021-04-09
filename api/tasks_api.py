from flask import jsonify, abort, request, Blueprint
from flask_jwt import JWT, jwt_required, current_identity
from flask_jwt_extended import JWTManager

from pprint import pprint

from utils.utils import hash_password, check_password

from data import db_session
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('users_api', __name__)

@blueprint.route('/api/tasks/<group_id>', methods=['GET'])
def tasks_by_group(group_id):
