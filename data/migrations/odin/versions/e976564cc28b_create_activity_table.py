"""create activity table

Revision ID: e976564cc28b
Revises: 7d3870fd3166
Create Date: 2016-07-28 17:23:22.445638

"""

# revision identifiers, used by Alembic.
revision = 'e976564cc28b'
down_revision = '7d3870fd3166'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    activity = op.create_table(
        'activity',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('owner_id', sa.Integer, nullable=True),
        sa.Column('assign_to', sa.Integer, nullable=True),
        sa.Column('area', sa.Unicode(30), nullable=True),
        sa.Column('category', sa.Unicode(30), nullable=True),
        sa.Column('status', sa.Unicode(30), nullable=True),
        sa.Column('activity_name', sa.Unicode(30), nullable=True),
        sa.Column('activity_description', sa.Unicode(255), nullable=True),
        sa.Column('priority', sa.Unicode(30), nullable=True),
        sa.Column('Duration', sa.Integer, nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('due_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('activity')

