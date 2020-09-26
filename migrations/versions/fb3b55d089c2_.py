"""empty message

Revision ID: fb3b55d089c2
Revises: cf751138847c
Create Date: 2020-09-26 23:00:57.246846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb3b55d089c2'
down_revision = 'cf751138847c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pay_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(length=3), nullable=True),
    sa.Column('amount', sa.String(length=13), nullable=True),
    sa.Column('desctiption', sa.Text(length=500), nullable=True),
    sa.Column('shop_id', sa.String(length=3), nullable=True),
    sa.Column('shop_order_id', sa.String(length=4), nullable=True),
    sa.Column('sign', sa.String(length=200), nullable=True),
    sa.Column('payway', sa.String(length=20), nullable=True),
    sa.Column('secret_key', sa.String(length=20), nullable=True),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pay_info')
    # ### end Alembic commands ###