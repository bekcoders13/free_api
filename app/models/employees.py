from sqlalchemy import Column, Integer, String, Date, Double
from database import Base


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    phone_number = Column(String(20))
    position = Column(String(50))
    salary = Column(Double)
    hire_date = Column(Date)
    status = Column(String(20), default='active')
