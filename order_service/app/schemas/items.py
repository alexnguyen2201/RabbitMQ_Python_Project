from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[int] = None


class ItemInCreate(ItemBase):
    name: str
    quantity: int
    price: int


class ItemInUpdate(ItemBase):
    pass


class ItemInDBBase(ItemBase):
    id: int
    name: str
    quantity: int
    price: int

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    pass


class ItemInDB(ItemInDBBase):
    pass
