from flask_restful import reqparse, abort, Api, Resource
from ..data.Users import User
from ..data.db_session import db_session


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UsersResource:
 def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict()})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(user).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

class UsersListResource:
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict()) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = user(
            surname=args['surname'],
            name=args['name'],
            age=args['age']
            position=args['position'],
            address=args['address'],
            email=args['email']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
