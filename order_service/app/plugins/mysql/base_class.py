# Import all the models, so that Base has them before being
# imported by Alembic
from app.plugins.mysql.base_class import Base  # noqa
from app.models.items import Item  # noqa
from app.models.orders import Order  # noqa
