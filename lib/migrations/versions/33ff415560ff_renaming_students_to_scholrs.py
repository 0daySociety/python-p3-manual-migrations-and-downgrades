"""renaming students to scholrs

Revision ID: 33ff415560ff
Revises: 791279dd0760
Create Date: 2023-09-07 00:46:50.998267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33ff415560ff'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students','scholars')


def downgrade() -> None:
    op.rename_table('scholars','students')