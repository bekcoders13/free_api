from sqlalchemy import Column, Integer, Date, ForeignKey

from app.models.products import Products
from app.models.users import Users
from database import Base
from sqlalchemy.orm import relationship


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer)
    user_id = Column(Integer)
    order_date = Column(Date, nullable=False)
    total_price = Column(Integer, nullable=False)

    product = relationship("Products", foreign_keys=product_id,
                           primaryjoin=lambda: Products.id == Orders.product_id)
    user = relationship("Users", foreign_keys=user_id,
                        primaryjoin=lambda: Users.id == Orders.user_id)
