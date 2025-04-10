from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    image_path = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    phone_number = Column(String(14), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(100), nullable=False)
    token = Column(Text, nullable=True, default='')
