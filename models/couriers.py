import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Unicode,
    DateTime
)
from dependencies.alchemy import Base


class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    website = Column(String)
    phone_number = Column(Unicode(25), index=True, nullable=False)
    email = Column(Unicode(255), index=True, unique=True)
    address = Column(String)
    registration_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=True)
    is_active = Column(Boolean, index=True, nullable=True, default=True)
