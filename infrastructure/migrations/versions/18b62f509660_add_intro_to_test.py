"""add intro to test

Revision ID: 18b62f509660
Revises: 3922302fdd42
Create Date: 2025-01-14 21:54:59.739285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18b62f509660'
down_revision: Union[str, None] = '3922302fdd42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('polls', sa.Column('intro', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('polls', 'intro')
    # ### end Alembic commands ###
