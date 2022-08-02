from sqlalchemy.orm import Session
from models import models
from schemas import order_details as details_schema


def create_items(session: Session, item_details: details_schema.OrderDetailsModelCreate, order_id: int):
    item_to_create = models.OrderDetails()
    item_to_create.item_name = item_details.item_name
    item_to_create.item_qty = item_details.item_qty
    item_to_create.qty_unit = item_details.qty_unit
    item_to_create.item_price = item_details.item_price
    item_to_create.item_desc = item_details.item_desc
    item_to_create.order_id = order_id
    session.add(item_to_create)
    session.commit()


def get_all_items(session: Session):
    return session.query(models.OrderDetails).all()


def get_order_items(session: Session, order_id: int):
    return session.query(models.OrderDetails)\
        .filter(models.OrderDetails.order_id == order_id).all()
