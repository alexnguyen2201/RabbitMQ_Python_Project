from app.exceptions.base import ObjectNotFound, ObjectDuplicate


class ItemNotFound(ObjectNotFound):
    pass


class ItemDuplicate(ObjectDuplicate):
    pass
