from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0003'
down_revision = '0002'
branch_labels = None
depends_on = None


def upgrade():
    # create order_items table
    op.create_table(
        'order_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('quanlity', sa.Integer(), nullable=False),
        sa.Column('total', sa.Integer(), nullable=False),

        sa.Column('order_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['order_id'], ['orders.id'], ondelete='CASCADE'),

        sa.Column('item_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ['item_id'], ['items.id'], ondelete='CASCADE'),

        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_items_id'),
                    'order_items', ['id'], unique=False)


def downgrade():
    op.drop_table('items')
