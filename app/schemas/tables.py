from enum import Enum
from pydantic import BaseModel, Field


class StatusType(str, Enum):
    empty = 'bo\'sh'
    busy = 'band'


class CreateTable(BaseModel):
    table_number: int = Field(..., gt=0)
    capacity: int = Field(..., gt=0)
    status: StatusType


class UpdateTable(CreateTable):
    ident: int = Field(..., gt=0)
