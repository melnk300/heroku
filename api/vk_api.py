import random
from flask import jsonify, abort, request, Blueprint
import vk
from pprint import pprint
from utils.cfg import CONFIG
import json
from pprint import pprint

from utils.utils import hash_password, check_password, send_message

from data import db_session
from data.models.Users import User
from data.models.Groups import Group
from data.models.VkUsers import VkUser

blueprint = Blueprint('vk_api', __name__)


@blueprint.route('/api/vk/callbackreg', methods=['POST'])
def callback_reg():
    data = json.loads(request.data)
    token = CONFIG.VK_TOCKEN
    if 'type' not in data.keys():
        return 'not vk'
    elif data['type'] == 'message_new':
        user_id = data['object']['user_id']
        text = data['object']['body'].split()
        if text[0] in ["!группа", "!гр"]:
            sess = db_session.create_session()
            if Group.if_group_already_created('_'.join(text[1::])):
                group_id = sess.query(Group.id).filter(Group.name == '_'.join(text[1::])).first()[0]
                user_group = VkUser(
                    id=user_id,
                    group_id=group_id
                )
                sess.add(user_group)
                send_message(user_id, 'Вы добавлены в группу')
                return '200'
            else:
                send_message(user_id, 'Такой группы не существует')
                return '404'
    else:
        return 'ok'


