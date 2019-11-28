"""create employee notes table

Revision ID: 0a72709468f0
Revises: c830e28cc53b
Create Date: 2016-07-28 17:07:40.157928

"""

# revision identifiers, used by Alembic.
revision = '0a72709468f0'
down_revision = 'c830e28cc53b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    employee_notes = op.create_table(
        'employee_notes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('notes_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('is_primary', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('employee_notes')

