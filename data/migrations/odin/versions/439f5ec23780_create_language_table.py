"""create language table

Revision ID: 439f5ec23780
Revises: 62752b992cf5
Create Date: 2016-07-27 18:55:59.053631

"""

# revision identifiers, used by Alembic.
revision = '439f5ec23780'
down_revision = '62752b992cf5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    language = op.create_table(
        'language',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('iso_693_code_1', sa.Unicode(3), nullable=True),
        sa.Column('iso_693_code_2', sa.Unicode(3), nullable=True),
        sa.Column('iso_693_code_3', sa.Unicode(3), nullable=True),
        sa.Column('name', sa.Unicode(50), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('language')

