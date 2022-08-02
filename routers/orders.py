from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from typing import (
    List
)
from sqlalchemy.orm import Session

from databases import database as database_dependencies
from structures import orders as order_structure
from structures import order_details as items_structure
from schemas import orders as order_schema
from schemas import order_details as items_schema

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


@router.post('/couriers/{courier_id}', status_code=201,
             responses={
                 400: {
                     'Error': 'Creating order Error'
                 }
             })
def create_order(courier_id: int, order: order_schema.OrderModelCreate,
                 session: Session = Depends(database_dependencies.get_db)):
    order_structure.create_order(session, order, courier_id)
    return {'status': status.HTTP_201_CREATED, 'message': 'order created successfully'}


@router.post('/{order_id}', status_code=201,
             responses={
                 400: {
                     'Error': 'Filling order Error'
                 }
             })
def fill_order(order_id: int, item_details: items_schema.OrderDetailsModelCreate,
               session: Session = Depends(database_dependencies.get_db)):
    items_structure.create_items(session, item_details, order_id)
    return {'status': status.HTTP_201_CREATED, 'message': 'order filled successfully'}


@router.get('/{order_id}/items', status_code=status.HTTP_200_OK)
def get_order_items(order_id: int, session: Session = Depends(database_dependencies.get_db)):
    return items_structure.get_order_items(session, order_id)


@router.get('', status_code=status.HTTP_200_OK)
def get_all_orders(session: Session = Depends(database_dependencies.get_db)):
    return order_structure.get_all_orders(session)


@router.get('/{order_id}/details', status_code=status.HTTP_200_OK)
def get_order_details(order_id: int, session: Session = Depends(database_dependencies.get_db)):
    return order_structure.get_order_details(session, order_id)


@router.put('/{order_id}/status', status_code=status.HTTP_200_OK)
def update_order_status(order_id: int,
                        order: order_schema.OrderStatusChange,
                        session: Session = Depends(database_dependencies.get_db)):
    return order_structure.update_order_status(session, order, order_id)
