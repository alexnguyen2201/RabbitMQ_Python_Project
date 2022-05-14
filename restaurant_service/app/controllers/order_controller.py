import time
from app.services import db_service


def accept_order(order):
    db_service.change_order_status(order, 'accepted')


def process_order(order):
    time.sleep(10)
    db_service.change_order_status(order, 'delivered')
