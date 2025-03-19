from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    image_path = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False)
    email_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(100), nullable=False)
    token = Column(Text, nullable=False)
    Refresh_token = Column(Text, nullable=False)
