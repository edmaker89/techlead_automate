"""initial empty migration

Revision ID: 20260322_000001
Revises:
Create Date: 2026-03-22 00:00:01
"""

from collections.abc import Sequence

import sqlalchemy as sa  # noqa: F401
from alembic import op  # noqa: F401

revision: str = "20260322_000001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
