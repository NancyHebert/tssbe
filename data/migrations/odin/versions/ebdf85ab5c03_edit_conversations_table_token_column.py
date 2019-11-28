"""edit conversations table token column

Revision ID: ebdf85ab5c03
Revises: 5ee07322557b
Create Date: 2017-02-28 20:01:46.360641

"""

# revision identifiers, used by Alembic.
revision = 'ebdf85ab5c03'
down_revision = '5ee07322557b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
	op.add_column(
        'conversations',
         sa.Column('token', sa.Unicode())
    )

def downgrade():
	op.drop_column('conversations', 'token')