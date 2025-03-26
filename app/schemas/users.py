from enum import Enum
from fastapi import HTTPException
from pydantic import BaseModel, Field, validator
from typing import Optional

from app.models.users import Users
from database import SessionLocal

db = SessionLocal()


class RoleType(Enum):
    admin = 'admin'
    user = 'user'


class GetUser(BaseModel):
    id: int = 0
    name: Optional[str] = None


class GetAdmin(GetUser):
    role: RoleType


class CreateUser(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    password: str

    @validator('phone_number')
    def phone_validate(cls, phone_number):
        validate_my = db.query(Users).filter(
            Users.phone_number == phone_number,
        ).count()

        if validate_my != 0:
            raise HTTPException(400, 'Siz avval ro\'yxatdan o\'tgansiz. Iltimos login qiling !!!')
        return phone_number


class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    password: str


class UpdateRole(BaseModel):
    id: int = Field(..., gt=0)
    role: RoleType
