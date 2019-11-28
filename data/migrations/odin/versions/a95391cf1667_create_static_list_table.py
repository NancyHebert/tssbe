"""create static list table

Revision ID: a95391cf1667
Revises: c76da78cfae4
Create Date: 2016-07-27 18:52:13.400201

"""

# revision identifiers, used by Alembic.
revision = 'a95391cf1667'
down_revision = 'c76da78cfae4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    static_list = op.create_table(
        'static_list',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('parent_id', sa.Integer, nullable=True),
        sa.Column('language_id', sa.Integer, nullable=False),
        sa.Column('type', sa.Unicode(30), nullable=True),
        sa.Column('value', sa.Unicode(30), nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('high', sa.Integer, nullable=True),
        sa.Column('low', sa.Integer, nullable=True),
        sa.Column('order_by', sa.Integer, nullable=True),
        sa.Column('hierarchical_level', sa.Integer, nullable=True),
        sa.Column('hierarchical_path', sa.Unicode(255), nullable=True),
        sa.Column('start_Date', sa.DateTime, nullable=True),
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
    op.drop_table('static_list')
