from typing import List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.db.repositories.base import RepositoryBase
from app.models.items import Item
from app.schemas.items import ItemInCreate, ItemInUpdate


class ItemsRepository(RepositoryBase[Item, ItemInCreate, ItemInUpdate]):
    def create_with_order(
        self, db: Session, *, obj_in: ItemInCreate, order_id: int
    ) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, order_id=order_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Item]:

        q = db.query(self.model)
        q = q.limit(limit)
        q = q.offset(skip)

        return q.all()


items = ItemsRepository(Item)
