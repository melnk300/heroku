import random
from flask import jsonify, abort, request, Blueprint
from datetime import datetime as dt
import vk
from pprint import pprint
from utils.cfg import CONFIG
import json
from pprint import pprint

from utils.utils import hash_password, check_password, send_message

from data import db_session
from data.models.Users import User
from data.models.Tasks import Task
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
            if not sess.query(VkUser.id).filter(VkUser.id == user_id).first():
                if Group.if_group_already_created__vk('_'.join(text[1::])):
                    group_id = sess.query(Group.id).filter(Group.name == '_'.join(text[1::])).first()[0]
                    user_group = VkUser(
                        id=user_id,
                        user_name=text[-1],
                        group_id=group_id
                    )
                    sess.add(user_group)
                    sess.commit()
                    send_message(user_id, 'Вы добавлены в группу')
                    return 'ok'
                else:
                    send_message(user_id, 'Такой группы не существует')
                    return 'ok'
            else:
                send_message(user_id, 'Вы уже добавлены в группу')
                return 'ok'
        elif text[0] in ["!дз"]:
            sess = db_session.create_session()
            if len(text) == 1:
                date = dt.now().strftime('%Y-%m-%d')
            else:
                date = text[1]
            user_group_id = sess.query(VkUser.group_id).filter(VkUser.id == user_id).first()[0]
            tasks = sess.query(Task.subject, Task.author, Task.task).filter(Task.group_id == user_group_id, Task.date_task == date)
            if tasks:
                send_message(user_id, '\n'.join([f'{task[0]} @{task[1]}\n{task[2]}\n' for task in tasks]))
                return 'ok'
            else:
                send_message(user_id, 'Заданий нет')
                return 'ok'
        elif text[0] in ['!задание']:  # TODO: need research and DB-refactor
            sess = db_session.create_session()
            author, group_id = sess.query(VkUser.user_name, VkUser.group_id).filter(VkUser.id == user_id).first()
            task = Task(
                date_task=text[1],
                subject=' '.join(text[2].split('_')),
                task=' '.join(text[2::]),
                author=author,
                group_id=group_id
            )
            sess.add(task)
            sess.commit()
            send_message(user_id, 'Задание добавлено')
            return 'ok'
        elif text[0] in ['!help', '!помощь', '!команды']:
            send_message(user_id, '!гр <группа> <ваще имя> - привязывает ваш профиль к группе\n!дз <date> - показывает задание на заданную дату (либо не сегодня если не задана)\n')
            return 'ok'
    else:
        return 'ok'


