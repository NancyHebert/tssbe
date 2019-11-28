"""create city table

Revision ID: 4b037fab812c
Revises: 1cd702276a4e
Create Date: 2016-07-27 18:57:29.532656

"""

# revision identifiers, used by Alembic.
revision = '4b037fab812c'
down_revision = '1cd702276a4e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    city = op.create_table(
        'city',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('country_id', sa.Integer, nullable=True),
        sa.Column('area', sa.Integer, nullable=True),
        sa.Column('ascii_name', sa.Unicode(50), nullable=True),
        sa.Column('timezone', sa.Unicode(50), nullable=True),
        sa.Column('population', sa.Integer, nullable=True),
        sa.Column('latitude', sa.Integer, nullable=True),
        sa.Column('longtitude', sa.Integer, nullable=True),
        sa.Column('valid_date', sa.DateTime, nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('city')
