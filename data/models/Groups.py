import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.schema import ForeignKey
from flask import abort

import data.db_session
from data.db_session import SqlAlchemyBase
from data import db_session


class Group(SqlAlchemyBase, SerializerMixin):  # название модели
    __tablename__ = 'groups'  # Название таблицы

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # поля таблицы
    name = sqlalchemy.Column(sqlalchemy.Text)
    members = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Integer))
    admin = sqlalchemy.Column(sqlalchemy.Integer)

    def if_group_not_found(group_id):
        sess = db_session.create_session()
        group = sess.query(Group).get(group_id)
        if not group:
            abort(404, 'Group id not found')

    def if_group_not_found_by_name(group_name):
        sess = db_session.create_session()
        group = sess.query(Group).filter(Group.name == group_name).first()
        if not group:
            abort(404, 'Group name not found')

    def if_user_is_not_admin(group_name, admin_id):
        sess = db_session.create_session()
        Group.if_group_not_found_by_name(group_name)
        if not admin_id == sess.query(Group.admin).filter(Group.name == group_name).first()[0]:
            abort(403, 'You\'re not an admin')

    def if_group_already_created(group_name):
        sess = db_session.create_session()
        group = sess.query(Group.id).filter(Group.name == group_name).first()
        if group:
            abort(403, 'Group already created')