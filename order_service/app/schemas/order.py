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
    total: Optional[int] = None
    status = Optional[Status] = None
    created_at: Optional[datetime] = None


class OrderInCreate(OrderBase):
    email: EmailStr


class OrderInUpdate(OrderBase):
    pass


class OrderInDBBase(OrderBase):
    id: int
    email: EmailStr
    total: int
    status: Status

    class Config:
        orm_mode = True


class Order(OrderInDBBase):
    pass


class OrderInDB(OrderInDBBase):
    pass
