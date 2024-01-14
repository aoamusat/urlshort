"""Remove user_id column from urls

Revision ID: baba67b2fe93
Revises: be6b1c6e6c2f
Create Date: 2024-01-14 17:27:53.850179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'baba67b2fe93'
down_revision: Union[str, None] = 'be6b1c6e6c2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('urls', "user_id")


def downgrade() -> None:
    op.add_column('urls', sa.Column('user_id', sa.Integer, nullable=False))
