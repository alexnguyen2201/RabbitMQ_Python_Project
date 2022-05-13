from typing import TYPE_CHECKING
import enum

from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from app.plugins.mysql.base_class import Base

if TYPE_CHECKING:
    from .order_items import OrderItem  # noqa: F401


class Status(enum.Enum):
    pending = 'pending'
    accepted = 'accepted'
    delivered = 'delivered'


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    email = Column((String(255)), unique=True, index=True, nullable=False)
    created_at = Column(DateTime)
    status = Column(Enum(Status), index=True)

    order_item = relationship(
        "OrderItem", back_populates="order", cascade="all,delete")

    def __repr__(self):
        return f"""
                    email: {self.email},
                    total: {self.total},
                    created_at: {self.created_at},
                    status: {self.status}
                """
