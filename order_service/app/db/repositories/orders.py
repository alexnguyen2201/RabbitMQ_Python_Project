from typing import List
from typing import Any, Dict, Union

from sqlalchemy.orm import Session
from app.schemas.datetime import DateTime
from app.db.repositories.base import BaseRepository
from app.models.orders import Order
from app.schemas.orders import OrderInCreate, OrderInUpdate
from app.config import settings
from app.schemas.orders import Status


class OrdersRepository(BaseRepository[Order, OrderInCreate, OrderInUpdate]):
    def create(self, db: Session, *,
               obj_in: OrderInCreate, total: int) -> Order:
        db_obj = Order()
        exclude_keys_in_orders_model = ['created_at', 'status']

        for key, value in obj_in.__dict__.items():
            if key not in exclude_keys_in_orders_model:
                setattr(db_obj, key, value)

        db_obj.created_at = settings.current_time()
        db_obj.status = Status.pending
        db_obj.total = total
        return super().create(db, obj_in=db_obj)

    def update(
        self, db: Session, *,
        db_obj: Order, obj_in: Union[OrderInUpdate, Dict[str, Any]]
    ) -> Order:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100,
        date_start: DateTime = None,
        date_end: DateTime = None,
    ) -> List[Order]:

        q = db.query(self.model)

        if date_start is None:
            date_start = DateTime(datetime=settings.past_week())
        q = q.filter(Order.created_at >= date_start.datetime)

        if date_end is None:
            date_end = DateTime(datetime=settings.current_time())
        q = q.filter(Order.created_at <= date_end.datetime)

        q = q.limit(limit)
        q = q.offset(skip)

        return q.all()


orders = OrdersRepository(Order)
