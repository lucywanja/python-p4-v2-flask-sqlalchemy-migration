"""rename department

Revision ID: c2f542e305ab
Revises: cc06322c6e54
Create Date: 2024-08-18 18:19:19.316576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2f542e305ab'
down_revision = 'cc06322c6e54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.rename_table('departments', 'department')
    # ### end Alembic commands ###
