"""create role organization attributes table

Revision ID: 82e7882ec2f3
Revises: 4b037fab812c
Create Date: 2016-07-28 14:50:14.083302

"""

# revision identifiers, used by Alembic.
revision = '82e7882ec2f3'
down_revision = '4b037fab812c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    role_organization_attributes = op.create_table(
        'role_organization_attributes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Unicode(30), nullable=True),
        sa.Column('display_name', sa.Unicode(30), nullable=True),
        sa.Column('default_value', sa.Unicode(30), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('sequence_number', sa.Integer, nullable=True),
        sa.Column('parent_type', sa.Unicode(30), nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('is_display_to_user', sa.Boolean, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('role_organization_attributes')

