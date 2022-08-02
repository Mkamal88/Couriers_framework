import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime
)
from sqlalchemy.orm import relationship
from dependencies.alchemy import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    status = Column(Unicode(128), nullable=False, default='in progress')
    sender_name = Column(Unicode(255), nullable=False)
    receiver_name = Column(Unicode(255), nullable=False)
    receiver_address = Column(Unicode(255), nullable=False)

    # Relations
    courier_id = relationship('Courier', back_populates='orders', cascade='all, delete-orphan')
    items = relationship('OrderDetails', back_populates='order', cascade='all, delete-orphan')
