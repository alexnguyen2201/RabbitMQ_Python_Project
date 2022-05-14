from app.exceptions.base import ObjectNotFound, ObjectDuplicate


class OrderItemNotFound(ObjectNotFound):
    pass


class OrderItemDuplicate(ObjectDuplicate):
    pass
