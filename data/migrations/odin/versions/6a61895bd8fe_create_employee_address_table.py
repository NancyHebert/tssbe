"""create employee address table

Revision ID: 6a61895bd8fe
Revises: a428fa64f8ce
Create Date: 2016-07-28 16:47:43.120394

"""

# revision identifiers, used by Alembic.
revision = '6a61895bd8fe'
down_revision = 'a428fa64f8ce'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    employee_address = op.create_table(
        'employee_address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address_id', sa.Integer, nullable=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('status_Code', sa.Unicode(30), nullable=True),
        sa.Column('address_type_code', sa.Unicode(30), nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('is_primary', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('employee_address')
