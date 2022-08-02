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
    prefix="/courier",
    tags=["courier"],
)


@router.post("", status_code=201,
             responses={
                 400: {
                     'Error': 'Creating courier'
                 }
             })
def create_user(user: courier_schema.CourierModelCreate,
                db: Session = Depends(database_dependencies.get_db)):

    if users_structure.get_user_by_phone(db, user.phone_number):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'user with number {user.phone_number} already exists')
    created_user = users_structure.create_user(session=db, user=user)
    return created_user


@router.get('/couriers', status_code=status.HTTP_200_OK)
def users(db: Session = Depends(database_dependencies.get_db)):
    return users_structure.get_all_users(session=db)
