from flask import jsonify, abort, request, Blueprint
from pprint import pprint
import logging
from utils.utils import hash_password, check_password
from flask_jwt_extended import jwt_required, get_jwt_identity

from data import db_session
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('groups_api', __name__)


@blueprint.route('/api/group/<group_name>', methods=['POST'])
@jwt_required()
def register_group(group_name):
    Group.if_group_already_created(group_name)
    sess = db_session.create_session()
    req = request.get_json(force=True)
    user_id = get_jwt_identity()
    group = Group(
        name=group_name,
        members=[user_id],  # must be iterable
        admin=user_id
    )
    sess.add(group)
    sess.commit()
    created_group_id = sess.query(Group.id).filter(Group.name == group_name).first()[0]
    return jsonify({'success': 'OK', "group_id": created_group_id}), 200


@blueprint.route('/api/group/<group_name>', methods=['PATCH'])
@jwt_required()
def update_group_name(group_name):
    user_id = int(get_jwt_identity())
    Group.if_group_not_found_by_name(group_name)
    Group.if_user_is_not_admin(group_name, user_id)
    req = request.get_json(force=True)
    sess = db_session.create_session()
    group = sess.query(Group).filter(Group.admin == user_id, Group.name == group_name).update({Group.name: req['new_group_name']}, synchronize_session=False)
    sess.commit()
    return jsonify({'success': 'OK'}), 200

