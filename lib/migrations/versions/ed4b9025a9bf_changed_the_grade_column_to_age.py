"""changed the grade column to age

Revision ID: ed4b9025a9bf
Revises: 33ff415560ff
Create Date: 2023-09-07 01:00:06.165509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed4b9025a9bf'
down_revision = '33ff415560ff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('grade','age')


def downgrade() -> None:
    op.alter_column('age','grade')
