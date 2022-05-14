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


class OrderInCreate(OrderBase):
    pass


class OrderInUpdate(OrderBase):
    status: Optional[Status] = None


class OrderInDBBase(OrderBase):
    id: int
    email: EmailStr
    created_at: datetime
    status: Status
    total: int

    class Config:
        orm_mode = True


class Order(OrderInDBBase):
    pass


class OrderInDB(OrderInDBBase):
    pass
