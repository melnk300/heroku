import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import ForeignKey
from flask import abort

import data.db_session
from data.db_session import SqlAlchemyBase
from data import db_session


class VkUser(SqlAlchemyBase, SerializerMixin):  # название модели
    __tablename__ = 'vk_users'  # Название таблицы

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_name = sqlalchemy.Column(sqlalchemy.Text)
    group_id = sqlalchemy.Column(sqlalchemy.Integer)
