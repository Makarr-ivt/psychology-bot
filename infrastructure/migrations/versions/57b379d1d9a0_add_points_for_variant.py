"""add points for variant

Revision ID: 57b379d1d9a0
Revises: 18b62f509660
Create Date: 2025-01-14 23:41:37.591639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57b379d1d9a0'
down_revision: Union[str, None] = '18b62f509660'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('polls', 'name',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.alter_column('questions', 'content',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.add_column('variants', sa.Column('points', sa.SMALLINT(), nullable=False, server_default='0'))
    op.alter_column('variants', 'content',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=False)
    op.drop_column('variants', 'is_correct')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('variants', sa.Column('is_correct', sa.BOOLEAN(), autoincrement=False, nullable=False, server_default='false'))
    op.alter_column('variants', 'content',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.drop_column('variants', 'points')
    op.alter_column('questions', 'content',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.alter_column('polls', 'name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    # ### end Alembic commands ###