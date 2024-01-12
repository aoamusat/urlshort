"""create users table

Revision ID: 8e0beb91fedc
Revises: 
Create Date: 2024-01-12 16:35:28.030848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e0beb91fedc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement="auto"),
        sa.Column("name", sa.String),
        sa.Column("email", sa.String, unique=True),
        sa.Column("created_at", sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table("users")
