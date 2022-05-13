from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade():
    # create items table
    op.create_table(
        'items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(
            length=50), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),

    )
    op.create_index(op.f('ix_item_id'), 'items', ['id'], unique=True)
    op.create_index(op.f('ix_item_name'), 'items', ['name'], unique=True)


def downgrade():
    op.drop_table('items')
