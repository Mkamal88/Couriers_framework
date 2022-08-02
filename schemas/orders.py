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
                'website': 'www.aramex.com',
                'phone_number': 'phone number in the format {number}',
                'email': 'myemail@mydomain.tld',
                'address': 'cairo - egypt'
            }
        }


class OrderStatusChange(BaseModel):
    status: OrderStatus
