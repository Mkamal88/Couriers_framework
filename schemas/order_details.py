from typing import Optional
from pydantic import (
    BaseModel,
    Extra,
    Field,
)


class OrderDetailsModelCreate(BaseModel):
    item_name: str = Field(..., min_length=1, max_length=255)
    item_qty: float
    qty_unit: Optional[str]
    item_price: float
    item_desc: str = Field(..., min_length=1, max_length=255)

    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'item_name': 'potatoes',
                'item_qty': '1',
                'item_unit': 'KG',
                'item_price': '50.00',
                'item_desc': 'short description about the item'
            }
        }

