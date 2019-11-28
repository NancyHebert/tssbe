"""create address table

Revision ID: 847ec131c7b0
Revises: f158c0cd35ab
Create Date: 2016-07-27 18:55:05.759582

"""

# revision identifiers, used by Alembic.
revision = '847ec131c7b0'
down_revision = 'f158c0cd35ab'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    address = op.create_table(
        'address',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('address_line_1', sa.Unicode(100), nullable=True),
        sa.Column('address_line_2', sa.Unicode(100), nullable=True),
        sa.Column('address_line_3', sa.Unicode(100), nullable=True),
        sa.Column('address_line_4', sa.Unicode(100), nullable=True),
        sa.Column('address_line_5', sa.Unicode(100), nullable=True),
        sa.Column('address_name', sa.Unicode(100), nullable=True),
        sa.Column('address_number', sa.Integer, nullable=True),
        sa.Column('address_type_code', sa.Unicode(30), nullable=True),
        sa.Column('city', sa.Unicode(50), nullable=True),
        sa.Column('postal_Code', sa.Unicode(30), nullable=True),
        sa.Column('country', sa.Unicode(30), nullable=True),
        sa.Column('county', sa.Unicode(50), nullable=True),
        sa.Column('state', sa.Unicode(10), nullable=True),
        sa.Column('district', sa.Unicode(50), nullable=True),
        sa.Column('province', sa.Unicode(50), nullable=True),
        sa.Column('latitude', sa.Integer, nullable=True),
        sa.Column('longtitude', sa.Integer, nullable=True),
        sa.Column('misc_address_line', sa.Unicode(100), nullable=True),
        sa.Column('rural_route_number', sa.Unicode(10), nullable=True),
        sa.Column('time_zone_code', sa.Unicode(30), nullable=True),
        sa.Column('comments', sa.Unicode(255), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('info_record_date', sa.DateTime, nullable=True),
        sa.Column('is_primary_address', sa.Boolean, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('address')

