"""create faculty appointment table

Revision ID: f83b85ec8321
Revises: e2a69e85fc83
Create Date: 2016-07-28 15:37:47.023922

"""

# revision identifiers, used by Alembic.
revision = 'f83b85ec8321'
down_revision = 'e2a69e85fc83'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    faculty_appointment = op.create_table(
        'faculty_appointment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('short_name', sa.Unicode(30), nullable=True),
        sa.Column('full_name', sa.Unicode(255), nullable=True),
        sa.Column('faculty', sa.Unicode(30), nullable=True),
        sa.Column('division', sa.Unicode(30), nullable=True),
        sa.Column('department', sa.Unicode(30), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('type', sa.Unicode(30), nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_current', sa.Boolean, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('faculty_appointment')

