import enum
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


class Status(str, enum.Enum):
    pending = 'pending'
    accepted = 'accepted'
    delivered = 'delivered'


class OrderBase(BaseModel):
    email: Optional[EmailStr] = None
    created_at: Optional[datetime] = None
    status = Optional[Status] = None


class OrderInCreate(OrderBase):
    email: EmailStr


class OrderInUpdate(OrderBase):
    pass


class OrderInDBBase(OrderBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class Order(OrderInDBBase):
    pass


class OrderInDB(OrderInDBBase):
    pass
