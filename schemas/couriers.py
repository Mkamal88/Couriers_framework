from typing import Optional

from pydantic import (
    BaseModel,
    Extra,
    Field,
    EmailStr,
)


class CourierModelCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    website: str = Field(..., min_length=1, max_length=255)
    phone_number: str = Field(..., min_length=1, max_length=255)
    email: Optional[EmailStr]
    address: str

    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'name': 'aramex',
                'website': 'www.aramex.com',
                'phone_number': 'phone number in the format {number}',
                'email': 'myemail@mydomain.tld',
                'address': 'cairo - egypt'
            }
        }
