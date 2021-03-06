"""empty message

Revision ID: ccfa3553172e
Revises: e9e59837e6d8
Create Date: 2016-04-10 11:58:42.259320

"""

# revision identifiers, used by Alembic.
revision = 'ccfa3553172e'
down_revision = 'e9e59837e6d8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notetype', sa.Column('tenant_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'notetype', 'tenant', ['tenant_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notetype', type_='foreignkey')
    op.drop_column('notetype', 'tenant_id')
    ### end Alembic commands ###
