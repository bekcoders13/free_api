from sqlalchemy import Column, String, Integer, ForeignKey, Date

from app.models.categories import Categories
from database import Base
from sqlalchemy.orm import relationship


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    image_path = Column(String(255), nullable=True)
    category_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    rating_count = Column(Integer)
    discount = Column(Integer, nullable=True)
    discount_price = Column(Integer, nullable=True)
    discount_start = Column(Date, nullable=True)
    discount_end = Column(Date, nullable=True)

    category = relationship("Category", foreign_keys=category_id,
                            primaryjoin=lambda: Categories.id == Products.category_id)
