from typing import Optional

from pydantic import BaseModel, EmailStr


class OrderItemBase(BaseModel):
    email: Optional[EmailStr] = None
    total: Optional[int] = None
    order_id: Optional[int] = None
    item_id: Optional[int] = None
    quality: Optional[int] = None


class OrderItemInCreate(OrderItemBase):
    email: EmailStr


class OrderItemInUpdate(OrderItemBase):
    pass


class OrderItemInDBBase(OrderItemBase):
    id: int
    email: EmailStr
    total: int

    class Config:
        orm_mode = True


class Order(OrderItemInDBBase):
    pass


class OrderInDB(OrderItemInDBBase):
    pass
