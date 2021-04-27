from flask import jsonify, abort, request, Blueprint
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, \
    set_refresh_cookies, set_access_cookies, unset_jwt_cookies
from pprint import pprint

from utils.utils import hash_password, check_password

from data import db_session
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('users_api', __name__)


@blueprint.route('/api/users/<group_id>', methods=['GET'])
def users_by_group_id(group_id):
    group_id = int(group_id)
    User.if_user_not_found_by_group(group_id)
    sess = db_session.create_session()
    users = sess.query(User.id, User.login, Group.name).filter(User.group_id == group_id).join(Group,
                                                                                               Group.id == group_id).all()
    users = [{'id': user[0], 'name': user[1], 'group_name': user[2]} for user in users]
    return jsonify({'users': users}), 200


@blueprint.route('/api/user/<user_id>', methods=['GET'])
def user_by_id(user_id):
    User.if_user_not_found_by_id(user_id)
    sess = db_session.create_session()
    user = sess.query(User.id, User.login, Group.id, Group.name).filter(User.id == user_id).join(Group,
                                                                                                 Group.id == User.group_id).first()
    return jsonify({'id': user[0], 'login': user[1], 'group_id': user[2], 'group_name': user[3]}), 200


@blueprint.route('/api/user/', methods=['PUT'])
def register_user():
    req = request.get_json(force=True)
    User.if_user_already_created(req['login'])
    sess = db_session.create_session()
    user = User(
        login=req['login'],
        password=hash_password(req['password'])
    )
    sess.add(user)
    sess.commit()
    user_id = sess.query(User.id).filter(User.login == req['login']).first()
    access_token = create_access_token(identity=user_id)
    res = jsonify({'success': 'OK'})
    set_access_cookies(res, access_token)
    return res


@blueprint.route('/api/user/', methods=['POST'])
def login_user():
    req = request.get_json(force=True)
    User.if_user_not_found_by_name(req['login'])
    sess = db_session.create_session()
    user_id, user_password, group_id = sess.query(User.id, User.password, User.group_id).filter(User.login == req['login']).all()[0]
    if check_password(req['password'], user_password):
        access_token = create_access_token(identity=user_id)
        res = jsonify({'success': 'OK', 'group_id': group_id})
        set_access_cookies(res, access_token)
        return res
    else:
        abort(401, 'Password - login pair is incorrect')


@blueprint.route('/api/user/', methods=['DELETE'])
@jwt_required()
def logout_user():
    res = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(res)
    return res


@blueprint.route('/api/user/test', methods=['GET', 'POST'])
def ping_test():
    return 'Hello world'
