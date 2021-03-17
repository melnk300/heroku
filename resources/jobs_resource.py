from flask_restful import reqparse, abort, Api, Resource
from ..data.Jobs import Job
from ..data.db_session import db_session


def abort_if_user_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Job).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource:
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Job).get(job_id)
        return jsonify({'job': job.to_dict()})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Job).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

class JobsListResource:
    def get(self):
        session = db_session.create_session()
        job = session.query(Job).all()
        return jsonify({'job': [item.to_dict()) for item in job]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Job(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size']
            collaborators=args['collaborators'],
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
