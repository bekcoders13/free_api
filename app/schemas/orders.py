from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List


class StatusType(str, Enum):
    waiting = 'kutimoqda'
    confirmed = 'tasdiqlandi'


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemRead(OrderItemBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    table_number: Optional[int] = None
    user_id: Optional[int] = None
    order_date: date
    total_price: float
    status: StatusType


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderRead(OrderBase):
    id: int
    items: List[OrderItemRead]

    class Config:
        orm_mode = True

