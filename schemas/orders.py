from enum import Enum
from pydantic import (
    BaseModel,
    Extra,
    Field,
)


class OrderStatus(str, Enum):
    New = 'new'
    InProgress = 'in progress'
    Completed = 'completed'
    Canceled = 'canceled'


class OrderModelCreate(BaseModel):
    sender_name: str = Field(..., min_length=1, max_length=255)
    receiver_name: str = Field(..., min_length=1, max_length=255)
    receiver_address: str = Field(..., min_length=1, max_length=255)

    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'sender_name': 'Mohamed Kamal Aly',
                'receiver_name': 'Ahmed Mohamed Khalid',
                'receiver_address': 'Cairo, Egypt'
            }
        }


class OrderStatusChange(BaseModel):
    status: OrderStatus
