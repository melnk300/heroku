from flask import Blueprint, Flask, jsonify, request, make_response

from data import db_session
from data.Jobs import Job

blueprint = Blueprint(
    'jobs_api',
    __name__
)

def add_job_(team_leader, job, work_size, collaborators, is_finished):
    job_ = Job()
    job_.team_leader = team_leader
    job_.job = job
    job_.work_size = work_size
    job_.collaborators = collaborators
    job_.is_finished = is_finished


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    ds = db_session.create_session()
    jobs = ds.query(Job).all()
    return jsonify([job.to_dict() for job in jobs])


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    print(request.get_json())
    add_job_(*request.data)
    return 'Job is added', 200

@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_jobs_by_id(job_id):
    ds = db_session.create_session()
    jobs = ds.query(Job).filter(Job.id == job_id)
    print([job for job in jobs])
    return jsonify([job.to_dict() for job in jobs]) if [job for job in jobs] else 'Id is invalid', 400
    