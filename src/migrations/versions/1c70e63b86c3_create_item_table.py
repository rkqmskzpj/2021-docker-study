"""create item table

Revision ID: 1c70e63b86c3
Revises: 
Create Date: 2021-11-11 15:44:09.562195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c70e63b86c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=200)),
    )


def downgrade():
    op.drop_table('items')