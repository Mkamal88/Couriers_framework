import datetime
from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    Unicode,
    DateTime,
    Float
)
from sqlalchemy.orm import relationship
from dependencies.alchemy import Base


class OrderDetails(Base):
    __tablename__ = "orders_details"

    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    item_name = Column(Unicode(255), nullable=False)
    qty_unit = Column(Float, nullable=False)
    item_unit = Column(Unicode(255), nullable=False)
    item_price = Column(Float, nullable=False)
    item_desc = Column(Unicode(255), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'))

    # Relations
    order = relationship('Order', back_populates='items', cascade='all, delete-orphan')
