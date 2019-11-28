"""create person table

Revision ID: ffdbb1969ab6
Revises: a95391cf1667
Create Date: 2016-07-27 18:54:13.280151

"""

# revision identifiers, used by Alembic.
revision = 'ffdbb1969ab6'
down_revision = 'a95391cf1667'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    person = op.create_table(
        'person',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('primary_address_id', sa.Integer, nullable=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('country_id', sa.Integer, nullable=True),
        sa.Column('work_language_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('title', sa.Unicode(15), nullable=True),
        sa.Column('first_name', sa.Unicode(50), nullable=True),
        sa.Column('last_name', sa.Unicode(50), nullable=True),
        sa.Column('middle_name', sa.Unicode(50), nullable=True),
        sa.Column('maiden_name', sa.Unicode(50), nullable=True),
        sa.Column('alias_name', sa.Unicode(50), nullable=True),
        sa.Column('title_suffix', sa.Unicode(50), nullable=True),
        sa.Column('date_of_birth', sa.DateTime, nullable=True),
        sa.Column('country_of_birth', sa.Unicode(100), nullable=True),
        sa.Column('citizenship', sa.Unicode(30), nullable=True),
        sa.Column('age', sa.Integer, nullable=True),
        sa.Column('gender', sa.Unicode(30), nullable=True),
        sa.Column('marital_status', sa.Unicode(30), nullable=True),
        sa.Column('fax_number', sa.Unicode(20), nullable=True),
        sa.Column('home_number', sa.Unicode(20), nullable=True),
        sa.Column('cell_number', sa.Unicode(20), nullable=True),
        sa.Column('email', sa.Unicode(50), nullable=True),
        sa.Column('preferred_communication_method', sa.Unicode(30), nullable=True),
        sa.Column('preferred_language', sa.Unicode(30), nullable=True),
        sa.Column('status_in_canada', sa.Unicode(30), nullable=True),
        sa.Column('foreign_national_status', sa.Unicode(50), nullable=True),
        sa.Column('visa_type', sa.Unicode(30), nullable=True),
        sa.Column('visa_number', sa.Integer, nullable=True),
        sa.Column('visa_start_date', sa.DateTime, nullable=True),
        sa.Column('visa_end_date', sa.DateTime, nullable=True),
        sa.Column('job_title', sa.Unicode(75), nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('comment', sa.Unicode(255), nullable=True),
        sa.Column('is_employee', sa.Boolean, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('person')
