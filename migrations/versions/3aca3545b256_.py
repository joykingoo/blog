"""empty message

Revision ID: 3aca3545b256
Revises: 0e3c4d4b58b4
Create Date: 2019-02-19 09:15:21.383604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aca3545b256'
down_revision = '0e3c4d4b58b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_pic_path',
               existing_type=sa.VARCHAR(),
               nullable='False')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_pic_path',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
