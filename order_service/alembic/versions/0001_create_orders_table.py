from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # create orders table
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=225), nullable=False),
        sa.Column('total', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('status', sa.Enum('pending', 'accepted',
                  'delivered', name='status_type')),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index(op.f('ix_order_email'), 'orders', ['email'], unique=True)


def downgrade():
    op.drop_table('items')
