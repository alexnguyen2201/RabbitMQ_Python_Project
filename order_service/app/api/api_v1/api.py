
from fastapi import APIRouter

from app.api.api_v1.endpoints import orders, items

api_router = APIRouter()
api_router.include_router(orders.router, prefix="/order", tags=["order"])
api_router.include_router(items.router, prefix="/item", tags=["item"])
