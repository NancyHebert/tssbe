"""create_countries_table

Revision ID: 33a160b4dbc3
Revises: 889f7df1617a
Create Date: 2016-03-30 15:40:32.095781

"""

# revision identifiers, used by Alembic.
revision = '33a160b4dbc3'
down_revision = '4e18760ffee2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'countries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
    )


def downgrade():
    op.drop_table('countries')
