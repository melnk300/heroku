from flask import jsonify, request, Blueprint

from data import db_session
from data.models.Tasks import Task

blueprint = Blueprint('tasks_api', __name__)


@blueprint.route('/api/tasks/<group_id>', methods=['GET'])
def get_tasks_by_group(group_id):
    pass


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


