from flask import jsonify, abort, request, Blueprint

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

def if_group_already_created(group_name):
    sess = db_session.create_session()
    group = sess.query(Group.id).filter(Group.name == group_name).first()
    print(group)
    if group:
        abort(403, 'Group already created')

@blueprint.route('/api/group/<group_name>', methods=['POST'])
def register_group(group_name):
    if_group_already_created(group_name)
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

