import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import ForeignKey

from data.db_session import SqlAlchemyBase
from data import db_session


class Group(SqlAlchemyBase, SerializerMixin):  # название модели
    __tablename__ = 'groups'  # Название таблицы

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # поля таблицы
    name = sqlalchemy.Column(sqlalchemy.Text)
    members = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Integer))
    admin = sqlalchemy.Column(sqlalchemy.Integer)