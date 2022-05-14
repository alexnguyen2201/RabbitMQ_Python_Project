
from typing import Any, Dict, Union

from sqlalchemy.orm import Session
from app.db.repositories.base import BaseRepository
from app.models.orders import Order
from app.schemas.orders import OrderInCreate, OrderInUpdate


class OrdersRepository(BaseRepository[Order, OrderInCreate, OrderInUpdate]):
    def update(
        self, db: Session, *,
        db_obj: Order, obj_in: Union[OrderInUpdate, Dict[str, Any]]
    ) -> Order:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


orders = OrdersRepository(Order)
