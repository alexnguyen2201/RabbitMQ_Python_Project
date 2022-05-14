from typing import Any

from fastapi import APIRouter, HTTPException, Depends
from app.exceptions.orders import OrderNotFound

from app import schemas
from app.db.repositories import orders, order_items
from app.db import repositories
from sqlalchemy.orm import Session
from app.api.api_v1.dependenies.database import get_db
from app.config import settings
from app.schemas.orders import Status
from app.services import mq_service

router = APIRouter()


@router.post("/", response_model=schemas.Order)
def create_order(
    *,
    body: schemas.OrderInCreate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Create new order.
    """
    db_obj = {}
    db_obj['email'] = body.email

    items_in_order = []

    for id, quantity in body.items:
        id, quantity = id[1], quantity[1]
        item_in_db = repositories.items.get(db, id)
        item_in_order = item_in_db
        item_in_order.quantity = quantity
        item_in_order.total = quantity * item_in_db.price
        items_in_order.append(schemas.ItemInOrder(**item_in_order.__dict__))

    db_obj['created_at'] = settings.current_time()
    db_obj['status'] = Status.pending
    db_obj['items'] = items_in_order
    db_obj['total'] = sum(
        [item_in_order.total for item_in_order in items_in_order])

    obj_in = schemas.OrderBase(email=body.email)
    order_in_db = orders.create(db, obj_in=obj_in, total=db_obj['total'])

    db_obj['id'] = order_in_db.id

    order_response = schemas.Order(**db_obj)

    for item_in_order in items_in_order:

        item_id = item_in_order.id
        quantity = item_in_order.quantity
        order_id = db_obj['id']
        total = item_in_order.total

        order_items.create(db, obj_in=schemas.OrderItemInCreate(
            item_id=item_id, quantity=quantity,
            order_id=order_id, total=total
        ))

    mq_service.exchange_services(order_response)

    return order_response


@router.get("/{order_id}", response_model=schemas.Order)
def read_order_by_id(
    order_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific order by id.
    """
    try:
        order = orders.get(db, id=order_id)
    except OrderNotFound:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order


@router.put("/{item_id}", response_model=schemas.Item)
def update_order_by_id(
    *,
    item_id: int,
    body: schemas.OrderInUpdate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Update a specific item by id.
    """
    try:
        item = orders.update(db, id=item_id, obj_in=body)
    except OrderNotFound:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    return item
