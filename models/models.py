import datetime
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Unicode,
    DateTime,
    Float,
    ForeignKey
)
from sqlalchemy.orm import relationship
from dependencies.alchemy import Base


class Courier(Base):
    __tablename__ = "couriers"

    id = Column(Integer,
                primary_key=True,
                unique=True,
                index=True,
                nullable=False,
                )
    name = Column(String)
    website = Column(String)
    phone_number = Column(Unicode(25), index=True, nullable=False)
    email = Column(Unicode(255), index=True, unique=True)
    address = Column(String)
    registration_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=True)
    is_active = Column(Boolean, index=True, nullable=True, default=True)

    # Relations
    orders = relationship('Order', back_populates='courier',
                          cascade='all, delete-orphan')


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        nullable=False
    )
    creation_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    status = Column(Unicode(128), nullable=False, default='new')
    sender_name = Column(Unicode(255), nullable=False)
    receiver_name = Column(Unicode(255), nullable=False)
    receiver_address = Column(Unicode(255), nullable=False)
    courier_id = Column(Integer, ForeignKey('couriers.id'), nullable=False)

    # Relations
    courier = relationship('Courier', back_populates='orders')
    items = relationship('OrderDetails', back_populates='order', cascade='all, delete-orphan')


class OrderDetails(Base):
    __tablename__ = "orders_details"

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        nullable=False
    )
    item_name = Column(Unicode(255), nullable=False)
    item_qty = Column(Float)
    qty_unit = Column(Unicode(255))
    item_price = Column(Float, nullable=False)
    item_desc = Column(Unicode(255), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'))

    # Relations
    order = relationship('Order', back_populates='items')
