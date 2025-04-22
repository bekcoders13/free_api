from sqlalchemy import Column, String, Integer, Date, Text, Double
from sqlalchemy.orm import relationship

from app.models.categories import Category
from database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Double, nullable=False)
    amount = Column(Integer, nullable=False)
    image_path = Column(String(255), nullable=True)
    category_id = Column(Integer, nullable=False)
    discount = Column(Double, nullable=True)
    discount_price = Column(Double, nullable=True)
    discount_start = Column(Date, nullable=True)
    discount_end = Column(Date, nullable=True)
    brand = Column(String(50))
    description = Column(Text)
    created_at = Column(Date)

    category = relationship("Category", foreign_keys=category_id,
                            primaryjoin=lambda: Category.id == Product.category_id)
