"""create attachments table

Revision ID: ae0364975143
Revises: e976564cc28b
Create Date: 2016-07-28 18:14:23.675111

"""

# revision identifiers, used by Alembic.
revision = 'ae0364975143'
down_revision = 'e976564cc28b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    attachments = op.create_table(
        'attachments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('owner_id', sa.Integer, nullable=True),
        sa.Column('area', sa.Unicode(30), nullable=True),
        sa.Column('category', sa.Unicode(30), nullable=True),
        sa.Column('status', sa.Unicode(30), nullable=True),
        sa.Column('attachment_description', sa.Unicode(255), nullable=True),
        sa.Column('attachment_name', sa.Unicode(50), nullable=True),
        sa.Column('file_size', sa.Integer, nullable=True),
        sa.Column('file_source_path', sa.Unicode(255), nullable=True),
        sa.Column('file_revision_number', sa.Integer, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('is_private', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('attachments')
