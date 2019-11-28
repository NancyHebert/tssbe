"""create employee table

Revision ID: f158c0cd35ab
Revises: ffdbb1969ab6
Create Date: 2016-07-27 18:54:39.593320

"""

# revision identifiers, used by Alembic.
revision = 'f158c0cd35ab'
down_revision = 'ffdbb1969ab6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    employee = op.create_table(
        'employee',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('contact_address_id', sa.Integer, nullable=True),
        sa.Column('home_address_id', sa.Integer, nullable=True),
        sa.Column('alternate_email_id', sa.Integer, nullable=True),
        sa.Column('phone_id', sa.Integer, nullable=True),
        sa.Column('alternate_phone_id', sa.Integer, nullable=True),
        sa.Column('account_or_organization_id', sa.Integer, nullable=True),
        sa.Column('facility_id', sa.Integer, nullable=True),
        sa.Column('position_id', sa.Integer, nullable=True),
        sa.Column('role_id', sa.Integer, nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('comments', sa.Unicode(255), nullable=True),
        sa.Column('employment_status_Code', sa.Unicode(30), nullable=True),
        sa.Column('employee_number', sa.Unicode(30), nullable=True),
        sa.Column('employee_work_location', sa.Unicode(50), nullable=True),
        sa.Column('job_title', sa.Unicode(75), nullable=True),
        sa.Column('marital_status_code', sa.Unicode(30), nullable=True),
        sa.Column('position_type_code', sa.Unicode(30), nullable=True),
        sa.Column('pratice_type', sa.Unicode(30), nullable=True),
        sa.Column('last_insurance_date', sa.DateTime, nullable=True),
        sa.Column('last_cpso_date', sa.DateTime, nullable=True),
        sa.Column('last_credit_date', sa.DateTime, nullable=True),
        sa.Column('is_orientation_complete', sa.Boolean, nullable=True),
        sa.Column('is_employee', sa.Boolean, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('employee')
