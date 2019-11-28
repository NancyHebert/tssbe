"""create researcher profile table

Revision ID: cfe3f3556b39
Revises: 2f433a92d30f
Create Date: 2016-02-09 09:55:29.027918

"""

# revision identifiers, used by Alembic.
revision = 'cfe3f3556b39'
down_revision = '2f433a92d30f'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'researchers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uniweb_number', sa.Unicode, nullable=False, unique=True),
        # sa.Column('name', sa.UnicodeText, nullable=False),
        sa.Column('available_date', sa.Date)
    )

def downgrade():
    op.drop_table('researchers')
