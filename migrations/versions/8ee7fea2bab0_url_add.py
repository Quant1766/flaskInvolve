"""url add

Revision ID: 8ee7fea2bab0
Revises: 591275f6ee1e
Create Date: 2020-09-26 23:22:09.665624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee7fea2bab0'
down_revision = '591275f6ee1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pay_info', sa.Column('ref_url', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pay_info', 'ref_url')
    # ### end Alembic commands ###
