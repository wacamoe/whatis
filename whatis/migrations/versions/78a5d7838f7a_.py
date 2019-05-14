"""empty message

Revision ID: 78a5d7838f7a
Revises: 3fa6b2aa8a10
Create Date: 2019-05-14 00:41:26.120460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78a5d7838f7a'
down_revision = '3fa6b2aa8a10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('whatis', sa.Column('owner', sa.String(), nullable=False))
    op.add_column('whatis', sa.Column('point_of_contact', sa.String(), nullable=True))
    op.add_column('whatis', sa.Column('terminology', sa.String(), nullable=False))
    op.add_column('whatis', sa.Column('version', sa.Integer(), nullable=False))
    op.drop_column('whatis', 'terminiology')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('whatis', sa.Column('terminiology', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('whatis', 'version')
    op.drop_column('whatis', 'terminology')
    op.drop_column('whatis', 'point_of_contact')
    op.drop_column('whatis', 'owner')
    # ### end Alembic commands ###