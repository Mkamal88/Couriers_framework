from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
)

SQLALCHEMY_DATABASE_URL = 'sqlite:///./couriers.db'
engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
_metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
      })

Base = declarative_base(metadata=_metadata)
