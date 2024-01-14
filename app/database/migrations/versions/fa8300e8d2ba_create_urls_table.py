"""create urls table

Revision ID: fa8300e8d2ba
Revises: 8e0beb91fedc
Create Date: 2024-01-12 16:35:33.894014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = 'fa8300e8d2ba'
down_revision: Union[str, None] = '8e0beb91fedc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement="auto"),
        sa.Column("long_url", sa.String),
        sa.Column("short_code", sa.String, unique=True),
        sa.Column("created_at", sa.DateTime, nullable=True, default=datetime.utcnow)
    )

def downgrade() -> None:
    op.drop_table("urls")
