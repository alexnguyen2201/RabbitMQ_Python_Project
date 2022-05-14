from app.exceptions.base import ObjectNotFound, ObjectDuplicate


class OrderNotFound(ObjectNotFound):
    pass


class OrderDuplicate(ObjectDuplicate):
    pass
