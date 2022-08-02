from sqlalchemy.orm import Session
from models import models
from schemas import couriers as couriers_schema


def create_courier(session: Session, courier: couriers_schema.CourierModelCreate):
    courier_to_create = models.Courier()
    courier_to_create.name = courier.name
    courier_to_create.email = courier.email
    courier_to_create.phone_number = courier.phone_number
    courier_to_create.address = courier.address
    courier_to_create.website = courier.website
    session.add(courier_to_create)
    session.commit()
    return courier_to_create


def get_courier_by_email(session: Session, email: str):
    return session.query(models.Courier) \
        .filter(models.Courier.email == email) \
        .first()


def get_courier_by_id(session: Session, courier_id: int):
    return session.query(models.Courier) \
        .filter(models.Courier.id == courier_id) \
        .first()


def get_all_couriers(session: Session):
    return session.query(models.Courier).all()
