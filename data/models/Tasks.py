import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import ForeignKey
from flask import abort

from data.db_session import SqlAlchemyBase
from data import db_session


class Task(SqlAlchemyBase, SerializerMixin):  # название модели
    __tablename__ = 'tasks'  # Название таблицы

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # поля таблицы
    group_id = sqlalchemy.Column(sqlalchemy.Integer)
    task = sqlalchemy.Column(sqlalchemy.Text)
    author = sqlalchemy.Column(sqlalchemy.Text)
    date_task = sqlalchemy.Column(sqlalchemy.Text)
    subject = sqlalchemy.Column(sqlalchemy.Text)

    def if_task_id_not_found(id):
        sess = db_session.create_session()
        task = sess.query(Task).get(id)
        if not task:
            abort(404, 'task not found')
