from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from databases import database as database_dependencies
from structures import couriers as courier_structure
from schemas import couriers as courier_schema

router = APIRouter(
    prefix="/couriers",
    tags=["couriers"],
)


@router.post("", status_code=201,
             responses={
                 400: {
                     'Error': 'Creating courier Error'
                 }
             })
def create_courier(courier: courier_schema.CourierModelCreate,
                   session: Session = Depends(database_dependencies.get_db)):
    if courier_structure.get_courier_by_email(session, courier.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'courier with email {courier.email} already exists')
    courier_structure.create_courier(session, courier)
    return {'status': status.HTTP_201_CREATED, 'message': 'courier created successfully'}


@router.get('', status_code=status.HTTP_200_OK)
def get_all_couriers(session: Session = Depends(database_dependencies.get_db)):
    return courier_structure.get_all_couriers(session)
