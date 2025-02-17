"""empty message

Revision ID: ab344fe33ce8
Revises: 
Create Date: 2025-01-13 11:50:10.717702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'ab344fe33ce8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dispositivo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ip', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('tipo', sa.Integer(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=False),
    sa.Column('oficina_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oficinas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rack',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ip', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('estado', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rack')
    op.drop_table('oficinas')
    op.drop_table('dispositivo')
    # ### end Alembic commands ###
