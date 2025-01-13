"""empty message

Revision ID: a5f9d96fb18e
Revises: 
Create Date: 2025-01-06 08:28:40.445033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'a5f9d96fb18e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('direcciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sector', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ip', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('estado', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('direcciones')
    # ### end Alembic commands ###