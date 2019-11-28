"""create role attributes table

Revision ID: 2f083997dcb2
Revises: 9e7a5db8d9e6
Create Date: 2016-07-28 15:00:17.546471

"""

# revision identifiers, used by Alembic.
revision = '2f083997dcb2'
down_revision = '9e7a5db8d9e6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    role_attributes = op.create_table(
        'role_attributes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('attribute_id', sa.Integer, nullable=True),
        sa.Column('role_id', sa.Integer, nullable=True),
        sa.Column('attribute_name', sa.Unicode(100), nullable=True),
        sa.Column('attribute_display_name', sa.Unicode(100), nullable=True),
        sa.Column('attribute_value', sa.Unicode(100), nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('role_attributes')

