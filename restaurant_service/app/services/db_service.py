from app.dependencies.database import get_db
from app.db.repositories import orders
from app.models.orders import Order
from app.models.items import Item  # noqa
from app.models.order_items import OrderItem  # noqa


db = next(get_db())


def change_order_status(order, status):
    db_obj = Order(id=order['id'], email=order['email'],
                   created_at=order['created_at'],
                   total=order['total'], status=order['status'])

    orders.update(db, db_obj=db_obj, obj_in={'status': status})
