from sqlalchemy import Column, Integer, Date, Double, String

from app.models.users import User
from database import Base
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_number = Column(Integer)
    user_id = Column(Integer)
    order_date = Column(Date, nullable=False)
    total_price = Column(Double, nullable=False)
    status = Column(String(50), default='kutilmoqda')

    user = relationship('User', foreign_keys=user_id,
                        primaryjoin=lambda: User.id == Order.user_id)
