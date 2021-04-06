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
