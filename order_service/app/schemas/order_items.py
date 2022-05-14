from pydantic import BaseModel


class OrderItemBase(BaseModel):
    pass


class OrderItemInCreate(OrderItemBase):
    order_id: int
    item_id: int
    quantity: int
    total: int


class OrderItemInUpdate(OrderItemBase):
    pass


class OrderItemInDBBase(OrderItemBase):
    id: int
    order_id: int
    item_id: int
    quantity: int
    total: int

    class Config:
        orm_mode = True


class OrderItem(OrderItemInDBBase):
    pass


class OrderItemInDB(OrderItemInDBBase):
    pass
