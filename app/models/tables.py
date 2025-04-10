from sqlalchemy import Column, Integer, String

from database import Base


class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, autoincrement=True, primary_key=True)
    table_number = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False, default='Bo\'sh')
    