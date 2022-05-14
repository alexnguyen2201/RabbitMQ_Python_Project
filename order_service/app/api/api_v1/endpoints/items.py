from typing import Any, List

from fastapi import APIRouter, HTTPException, Depends
from app.exceptions.items import (
    ItemNotFound, ItemDuplicate
)
from app import schemas
from app.db.repositories import items
from sqlalchemy.orm import Session
from app.api.api_v1.dependenies.database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> Any:
    """
    Retrieve items by admin.
    """
    return items.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    body: schemas.ItemInCreate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Create new item by admin.
    """
    try:
        item = items.create(db, obj_in=body)
    except ItemDuplicate:
        raise HTTPException(
            status_code=409,
            detail="Item with this name already exists"
        )

    return item


@router.get("/{item_id}", response_model=schemas.Item)
def read_item_by_id(
    item_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific item by id.
    """
    try:
        item = items.get(db, id=item_id)
    except ItemNotFound:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    return item


@router.put("/{item_id}", response_model=schemas.Item)
def update_item(
    *,
    item_id: int,
    body: schemas.ItemInUpdate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Update a specific item by id.
    """
    try:
        item = items.update(db, id=item_id, obj_in=body)
    except ItemNotFound:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )
    except ItemDuplicate:
        raise HTTPException(
            status_code=409,
            detail="Item with this name already exists"
        )

    return item
