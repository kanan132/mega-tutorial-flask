"""add language to posts

Revision ID: 90281de069a3
Revises: d9fd5d31a81b
Create Date: 2020-08-28 00:01:21.054733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90281de069a3'
down_revision = 'd9fd5d31a81b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###