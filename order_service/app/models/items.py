from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.plugins.mysql.base_class import Base

if TYPE_CHECKING:
    from .order_items import OrderItem  # noqa: F401


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    price = Column(Integer, nullable=False)

    order_item = relationship(
        "OrderItem", back_populates="item", cascade="all,delete")

    def __repr__(self):
        return f"""
                    name: {self.name},
                    quantity: {self.quantity}
                """
