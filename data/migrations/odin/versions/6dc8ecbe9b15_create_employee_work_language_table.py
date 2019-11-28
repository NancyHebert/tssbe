"""create work language table

Revision ID: 6dc8ecbe9b15
Revises: 439f5ec23780
Create Date: 2016-07-27 18:56:17.859168

"""

# revision identifiers, used by Alembic.
revision = '6dc8ecbe9b15'
down_revision = '439f5ec23780'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    employee_work_language = op.create_table(
        'employee_work_language',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('language_id', sa.Integer, nullable=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('language_code', sa.Unicode(30), nullable=True),
        sa.Column('language_name', sa.Unicode(30), nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('is_primary', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('employee_work_language')

