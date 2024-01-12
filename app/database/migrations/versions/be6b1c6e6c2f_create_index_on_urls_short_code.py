"""create index on urls short_code

Revision ID: be6b1c6e6c2f
Revises: fa8300e8d2ba
Create Date: 2024-01-12 16:52:39.971725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "be6b1c6e6c2f"
down_revision: Union[str, None] = "fa8300e8d2ba"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        index_name="short_code_index", table_name="urls", columns=["short_code"]
    )


def downgrade() -> None:
    op.drop_index("short_code_index", "urls")
