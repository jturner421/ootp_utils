from threading import Lock
from typing import Optional, List, Tuple

import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from app.config.config import DBConfig


class Base(DeclarativeBase):
    pass


class PostgresDbSessionMeta(type):
    """
        This is a thread-safe implementation of Singleton.
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class APIDbSession(metaclass=PostgresDbSessionMeta):
    """
    Manages Postgres DB sessions
    """
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    factory = None
    engine = None
    metadata = None

    def global_init(self):
        if APIDbSession.factory:
            return
        conn_str = DBConfig.POSTGRES_DATABASE_URI
        self.engine = create_engine(conn_str, echo=True, future=True)
        from app.models import Cities
        APIDbSession.engine = self.engine
        APIDbSession.factory = sqlalchemy.orm.sessionmaker(bind=self.engine)
        APIDbSession.metadata = [value for key, value in Base.metadata.tables.items()]
        APIDbSession.table_mapping = [key for key, value in Base.metadata.tables.items()]


def get_postgress_db_session():
    postgres_session = APIDbSession(value='api_session')
    postgres_session.global_init()
