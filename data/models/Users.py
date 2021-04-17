import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import ForeignKey

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, SerializerMixin):  # название модели
    __tablename__ = 'users'  # Название таблицы

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # поля таблицы
    login = sqlalchemy.Column(sqlalchemy.Text)
    password = sqlalchemy.Column(sqlalchemy.Text)
    group_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('groups.id'))

    def if_user_not_found_by_id(user_id):
        sess = db_session.create_session()
        user = sess.query(User).get(user_id)
        if not user:
            abort(404, 'User id not found')


    def if_user_not_found_by_name(user_name):
        sess = db_session.create_session()
        user = sess.query(User).filter(User.login == user_name).all()
        if not user:
            abort(404, 'User name not found')


    def if_user_not_found_by_group(user_group_id):
        sess = db_session.create_session()
        user = sess.query(User).filter(User.group_id == user_group_id).all()
        if not user:
            abort(404, 'User with this group_id name not found')


    def if_user_already_created(user_name):
        sess = db_session.create_session()
        user = sess.query(User).filter(User.login == user_name).all()
        if user:
            abort(403, 'User already created')
