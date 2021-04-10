from flask import jsonify, request, Blueprint, abort

from data import db_session
from data.models.Tasks import Task

blueprint = Blueprint('tasks_api', __name__)


def if_task_id_not_found(id):
    sess = db_session.create_session()
    task = sess.query(Task).get(id)
    if not task:
        abort(404, 'task not found')


@blueprint.route('/api/tasks/<group_id>/<data>', methods=['GET'])
def get_tasks_by_group(group_id, data):
    sess = db_session.create_session()
    res = sess.query(Task.id, Task.author, Task.subject, Task.task).filter(Task.data == data,
                                                                           Task.group_id == group_id).all()
    return jsonify({'tasks': [task.to_dict() for task in res]})


@blueprint.route('/api/tasks/<group_id>/<data>', methods=['POST'])
def add_tasks_by_group(data, group_id):
    req = request.get_json(force=True)  # subject: 'русский', task: '№434', author: ...
    sess = db_session.create_session()
    task = Task(
        group_id=group_id,
        date_task=data,
        author=req['author'],
        subject=req['subject'],
        task=req['task']
    )
    sess.add(task)
    sess.commit()
    return jsonify({'success': 'OK'}), 200


@blueprint.route('/api/tasks/<id>', methods=['DELETE'])
def delete_tasks_by_group(id):
    if_task_id_not_found(id)
    sess = db_session.create_session()
    sess.query(Task).filter(Task.id == id).delete()
    sess.commit()
    return jsonify({'success': 'OK'}), 200
