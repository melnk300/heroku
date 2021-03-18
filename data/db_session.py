import sqlalchemy as sa
from sqlalchemy import create_engine
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session, sessionmaker, create_session
import sqlalchemy.ext.declarative as dec
from utils.cfg import DevConfig as cfg

SqlAlchemyBase = dec.declarative_base()

some_engine = create_engine(f'postgresql+psycopg2://{cfg.PG["db_user"]}:{cfg.PG["password"]}@{cfg.PG["host"]}:5432/{cfg.PG["database"]}')

__factory = sessionmaker(bind=some_engine)

SqlAlchemyBase.metadata.create_all(some_engine)

def create_session() -> Session:
    global __factory
    return __factory()