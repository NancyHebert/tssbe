"""create hospital affiliation table

Revision ID: 7d3870fd3166
Revises: 0a72709468f0
Create Date: 2016-07-28 17:17:08.699881

"""

# revision identifiers, used by Alembic.
revision = '7d3870fd3166'
down_revision = '0a72709468f0'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    hospital_affiliation = op.create_table(
        'hospital_affiliation',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('parent_id', sa.Integer, nullable=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('hospital_name', sa.Unicode(255), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('affiliation_type', sa.Unicode(30), nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('is_primary', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('hospital_affiliation')

