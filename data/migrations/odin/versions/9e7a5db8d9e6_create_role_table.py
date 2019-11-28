"""create role table

Revision ID: 9e7a5db8d9e6
Revises: 82e7882ec2f3
Create Date: 2016-07-28 14:55:01.420805

"""

# revision identifiers, used by Alembic.
revision = '9e7a5db8d9e6'
down_revision = '82e7882ec2f3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    role = op.create_table(
        'role',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('organization_id', sa.Integer, primary_key=True),
        sa.Column('short_name', sa.Unicode(30), nullable=True),
        sa.Column('full_name', sa.Unicode(255), nullable=True),
        sa.Column('role', sa.Unicode(30), nullable=True),
        sa.Column('type', sa.Unicode(30), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('role')

