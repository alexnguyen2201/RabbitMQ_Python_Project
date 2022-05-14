from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.plugins.mysql.base_class import Base

if TYPE_CHECKING:
    from .orders import Order  # noqa: F401
    from .items import Item  # noqa: F401


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"))
    order = relationship("Order", back_populates="order_item")

    item_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"))
    item = relationship("Item", back_populates="order_item")

    def __repr__(self):
        return f"""
                    name: {self.name},
                    quantity: {self.quantity}
                """
