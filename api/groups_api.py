from flask import jsonify, abort, request, Blueprint
from pprint import pprint
import logging
from utils.utils import hash_password, check_password

from data import db_session
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('groups_api', __name__)


@blueprint.route('/api/group/<group_name>', methods=['POST'])
def register_group(group_name):
    Group.if_group_already_created(group_name)
    sess = db_session.create_session()
    req = request.get_json(force=True)
    group = Group(
        name=group_name,
        members=[req['user_id']]
    )
    sess.add(group)
    sess.commit()
    created_group_id = sess.query(Group.id).filter(Group.name == group_name).first()[0]
    return jsonify({'success': 'OK', "group_id": created_group_id}), 200
