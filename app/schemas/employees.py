import datetime
from enum import Enum
from pydantic import BaseModel, Field


class StatusType(str, Enum):
    active = 'faol'
    not_active = 'faol emas'


class CreateEmployee(BaseModel):
    full_name: str
    phone_number: str
    position: str
    salary: float
    hire_date: datetime.date
    status: StatusType


class UpdateEmployee(CreateEmployee):
    ident: int = Field(..., gt=0)
