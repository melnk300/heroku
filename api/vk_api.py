import random
from flask import jsonify, abort, request, Blueprint
import vk
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, \
    set_refresh_cookies, set_access_cookies, unset_jwt_cookies
from pprint import pprint
from utils.cfg import CONFIG
from pickle import loads

from utils.utils import hash_password, check_password

from data import db_session
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('vk_api', __name__)


@blueprint.route('/api/vk/callbackreg', methods=['POST'])
def callback_reg():
    data = loads(request.data)
    token = CONFIG.VK_TOCKEN
    if 'type' not in data.keys():
        return 'not vk'
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v='5.110')
        user_id = data['object']['message']['from_id']
        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!',
                          random_id=random.getrandbits(64))
        return 'ok'
