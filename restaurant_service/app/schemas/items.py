from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    pass


class ItemInCreate(ItemBase):
    name: str
    price: int


class ItemInUpdate(ItemBase):
    name: Optional[str] = None
    price: Optional[int] = None


class ItemInDBBase(ItemBase):
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    pass


class ItemInDB(ItemInDBBase):
    pass
