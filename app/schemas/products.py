import datetime
from pydantic import BaseModel, Field


class CreateProduct(BaseModel):
    category_id: int
    name: str
    price: float = Field(..., gt=0)
    amount: int
    discount: float
    discount_price: float
    discount_start: datetime.date
    discount_end: datetime.date
    brand: str
    description: str


class UpdateProduct(CreateProduct):
    ident: int = Field(..., gt=0)
