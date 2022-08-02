from sqlalchemy.orm import Session
from models import models
from schemas import orders as order_schema
import datetime
from structures import couriers as courier_structure
from fastapi import (
    HTTPException,
    status
)


def create_order(session: Session, order: order_schema.OrderModelCreate, courier_id: int):
    if not (courier_structure.get_courier_by_id(session, courier_id)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'courier with id {courier_id} is not exists')
    order_to_create = models.Order()
    order_to_create.courier_id = courier_id
    order_to_create.creation_date = datetime.datetime.utcnow()
    order_to_create.sender_name = order.sender_name
    order_to_create.receiver_name = order.receiver_name
    order_to_create.receiver_address = order.receiver_address
    session.add(order_to_create)
    session.commit()
    return order_to_create


def get_all_orders(session: Session):
    return session.query(models.Order).all()


def get_order_details(session: Session, order_id: int):
    return session.query(models.Order).filter(models.Order.id == order_id).first()


def update_order_status(session: Session, order: order_schema.OrderStatusChange, order_id: int):
    data = order.dict(exclude_unset=True)
    data.update({'status': order.status})
    num_row = session.query(models.Order) \
        .filter(models.Order.id == order_id) \
        .update(data, synchronize_session='fetch')
    session.commit()
    return num_row
