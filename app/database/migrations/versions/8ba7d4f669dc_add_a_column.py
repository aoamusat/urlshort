"""Add a column

Revision ID: 8ba7d4f669dc
Revises: 5816f3e9d160
Create Date: 2024-01-12 15:58:13.508202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ba7d4f669dc'
down_revision: Union[str, None] = '5816f3e9d160'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('accounts', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('accounts', 'last_transaction_date')
