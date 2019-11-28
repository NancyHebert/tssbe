"""create organization table

Revision ID: 40de6ea4d344
Revises: 2f083997dcb2
Create Date: 2016-07-28 15:04:12.206654

"""

# revision identifiers, used by Alembic.
revision = '40de6ea4d344'
down_revision = '2f083997dcb2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    organization = op.create_table(
        'organization',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('address_id', sa.Integer, nullable=True),
        sa.Column('short_name', sa.Unicode(30), nullable=True),
        sa.Column('full_name', sa.Unicode(255), nullable=True),
        sa.Column('profession_name', sa.Unicode(50), nullable=True),
        sa.Column('profession_number', sa.Unicode(25), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('type', sa.Unicode(30), nullable=True),
        sa.Column('status_code', sa.Unicode(30), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('organization')

