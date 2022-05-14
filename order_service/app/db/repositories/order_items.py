from typing import List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.db.repositories.base import BaseRepository
from app.models.order_items import OrderItem
from app.schemas.order_items import OrderItemInCreate, OrderItemInUpdate


class OrderItemsRepository(BaseRepository[
        OrderItem,
        OrderItemInCreate,
        OrderItemInUpdate]):
    def create(
        self, db: Session, *, obj_in: OrderItemInCreate
    ) -> OrderItem:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[OrderItem]:

        q = db.query(self.model)
        q = q.limit(limit)
        q = q.offset(skip)

        return q.all()


order_items = OrderItemsRepository(OrderItem)
