"""init_db

Revision ID: 8d85159eb9c7
Revises: 
Create Date: 2023-07-05 20:14:15.636496

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8d85159eb9c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('pk_id')
    )
    op.create_table('games',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('player_pk_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('total_kills', sa.Integer(), nullable=False),
    sa.Column('kills', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.ForeignKeyConstraint(['player_pk_id'], ['players.pk_id'], ),
    sa.PrimaryKeyConstraint('pk_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    op.drop_table('players')
    # ### end Alembic commands ###