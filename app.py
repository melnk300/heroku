from data.Users import User
from data.Jobs import Job

from data import db_session

db_session.global_init("db/mars_explorer.db")


def add_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

def add_job(team_leader, job, work_size, collaborators, is_finished):
    job_ = Job()
    job_.team_leader = team_leader
    job_.job = job
    job_.work_size = work_size
    job_.collaborators = collaborators
    job_.is_finished = is_finished
    db_sess = db_session.create_session()
    db_sess.add(job_)
    db_sess.commit()


users = [
    {
        'surname': 'Levin',
        'name': 'Ivan',
        'age': 20,
        'position': 'colonist',
        'speciality': 'research engineer',
        'address': 'module_1',
        'email': 'asdasdas@mars.org'
    },
    {
        'surname': 'Levin',
        'name': 'Ivan',
        'age': 20,
        'position': 'colonist',
        'speciality': 'research engineer',
        'address': 'module_1',
        'email': 'dsdasdasdas@mars.org'
    }
]

jobs = [{
    'team_leader': 1,
    'job': 'deployment of residential modules 1 and 2',
    'work_size': '15',
    'collaborators': '2, 3',
    'is_finished': False,
}]

# [add_user(*user.values()) for user in users]
[add_job(*job__.values()) for job__ in jobs]
