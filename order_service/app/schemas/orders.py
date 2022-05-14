import enum
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, EmailStr
from app.schemas.items import ItemBase, Item


class Status(str, enum.Enum):
    pending = 'pending'
    accepted = 'accepted'
    delivered = 'delivered'


class OrderBase(BaseModel):
    email: Optional[EmailStr] = None


class ItemInCreateOrder(ItemBase):
    id: int
    quantity: int


class OrderInCreate(OrderBase):
    email: EmailStr
    items: List[ItemInCreateOrder]


class OrderInUpdate(OrderBase):
    items: Optional[List[ItemInCreateOrder]] = None


class OrderInDBBase(OrderBase):
    id: int
    email: EmailStr
    created_at: datetime
    status: Status
    total: int

    class Config:
        orm_mode = True


class ItemInOrder(Item):
    quantity: int
    total: int


class Order(OrderInDBBase):
    items: List[ItemInOrder]


class OrderInDB(OrderInDBBase):
    pass
