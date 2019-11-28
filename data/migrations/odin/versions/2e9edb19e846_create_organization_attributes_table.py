"""create organization attributes table

Revision ID: 2e9edb19e846
Revises: 40de6ea4d344
Create Date: 2016-07-28 15:12:47.367934

"""

# revision identifiers, used by Alembic.
revision = '2e9edb19e846'
down_revision = '40de6ea4d344'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    organization_attributes = op.create_table(
        'organization_attributes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('parent_id', sa.Integer, nullable=True),
        sa.Column('language_id', sa.Integer, nullable=True),
        sa.Column('name', sa.Unicode(50), nullable=True),
        sa.Column('type', sa.Unicode(30), nullable=True),
        sa.Column('value', sa.Unicode(30), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('high', sa.Integer, nullable=True),
        sa.Column('low', sa.Integer, nullable=True),
        sa.Column('order_by', sa.Integer, nullable=True),
        sa.Column('hierarchy_level', sa.Integer, nullable=True),
        sa.Column('hierarchy_path', sa.Unicode(255), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('is_header', sa.Boolean, nullable=True),
        sa.Column('is_multilingual', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('organization_attributes')
