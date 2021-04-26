from flask import jsonify, request, Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt_identity

from data import db_session
from data.models.Tasks import Task
from data.models.Users import User
from data.models.Groups import Group

blueprint = Blueprint('tasks_api', __name__)


@blueprint.route('/api/tasks/<group_id>/<data>', methods=['GET'])
@jwt_required()
def get_tasks_by_group(group_id, data):
    sess = db_session.create_session()
    res = sess.query(Task.id, Task.author, Task.subject, Task.task).filter(Task.date_task == data,
                                                                           Task.group_id == group_id).all()
    return jsonify({'tasks': res})


@blueprint.route('/api/tasks/<group_id>/<data>', methods=['POST'])
@jwt_required()
def add_tasks_by_group(data, group_id):
    user_id = get_jwt_identity()
    req = request.get_json(force=True)  # subject: 'русский', task: '№434', author: ...
    sess = db_session.create_session()
    task = Task(
        group_id=group_id,
        date_task=data,
        author=user_id,
        subject=req['subject'],
        task=req['task']
    )
    sess.add(task)
    sess.commit()
    return jsonify({'success': 'OK'}), 200


@blueprint.route('/api/tasks/<task_id>', methods=['DELETE'])
@jwt_required
def delete_tasks_by_id(task_id):
    Group.if_task_id_not_found(task_id)
    sess = db_session.create_session()
    user_id = get_jwt_identity()
    task_author, task_group_id = sess.query(Task.author, Task.group_id).filter(Task.id == task_id).all()[0]
    if task_author == user_id:
        sess.query(Task).filter(Task.id == task_id).delete()
        sess.commit()
        return jsonify({'success': 'OK'}), 200
    elif sess.query(Group.admin).filter(Group.id == task_group_id).all[0] == user_id:
        sess.query(Task).filter(Task.id == task_id).delete()
        sess.commit()
        return jsonify({'success': 'OK'}), 200
    else:
        abort(403, 'You can\'t delete this task')
