"""create notes table

Revision ID: c830e28cc53b
Revises: 6a61895bd8fe
Create Date: 2016-07-28 17:02:32.253097

"""

# revision identifiers, used by Alembic.
revision = 'c830e28cc53b'
down_revision = '6a61895bd8fe'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    notes = op.create_table(
        'notes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('area_code', sa.Unicode(30), nullable=True),
        sa.Column('category_code', sa.Unicode(30), nullable=True),
        sa.Column('note', sa.Unicode(255), nullable=True),
        sa.Column('note_type', sa.Unicode(30), nullable=True),
        sa.Column('priority', sa.Unicode(30), nullable=True),
        sa.Column('action', sa.Unicode(30), nullable=True),
        sa.Column('duration', sa.Integer, nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('is_current', sa.Boolean, nullable=True),
        sa.Column('is_private', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('notes')
