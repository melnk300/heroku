from flask import jsonify, abort, request, Blueprint
import vkapi
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, \
    set_refresh_cookies, set_access_cookies, unset_jwt_cookies
from pprint import pprint

from utils.utils import hash_password, check_password

from data import db_session
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('vk_api', __name__)


@blueprint.route('/api/vk/callbackreg', methods=['POST'])
def callback_reg():
    return 'ecae930f'
