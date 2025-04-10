from sqlalchemy import Column, Integer, Double
from sqlalchemy.orm import relationship, backref

from app.models.orders import Order
from app.models.products import Product
from database import Base


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)

    product = relationship("Product", foreign_keys=product_id,
                           primaryjoin=lambda: Product.id == OrderItem.product_id)

    item = relationship('Order', foreign_keys=order_id,
                        primaryjoin=lambda: Order.id == OrderItem.order_id,
                        backref=backref('items'))
