"""empty message

Revision ID: 39a615fc59de
Revises: 24ee78998295
Create Date: 2025-01-14 08:39:57.998345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '39a615fc59de'
down_revision: Union[str, None] = '24ee78998295'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('oficinas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('impresoras', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('computadoras', sa.Integer(), nullable=False))
        batch_op.drop_column('numeroDispositivos')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('oficinas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('numeroDispositivos', sa.INTEGER(), nullable=False))
        batch_op.drop_column('computadoras')
        batch_op.drop_column('impresoras')

    # ### end Alembic commands ###
