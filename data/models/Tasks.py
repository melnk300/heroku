import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import ForeignKey

from data.db_session import SqlAlchemyBase


class Task(SqlAlchemyBase, SerializerMixin):  # название модели
    __tablename__ = 'tasks'  # Название таблицы

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # поля таблицы
    group_id = sqlalchemy.Column(sqlalchemy.Integer)
    task = sqlalchemy.Column(sqlalchemy.Text)
    author = sqlalchemy.Column(sqlalchemy.Text)
    date_task = sqlalchemy.Column(sqlalchemy.Text)
    subject = sqlalchemy.Column(sqlalchemy.Text)
