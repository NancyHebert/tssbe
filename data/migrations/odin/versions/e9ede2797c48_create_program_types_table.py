"""create program types table

Revision ID: e9ede2797c48
Revises: d95a7a7e14a7
Create Date: 2016-02-09 09:54:00.907227

"""

# revision identifiers, used by Alembic.
revision = 'e9ede2797c48'
down_revision = 'd95a7a7e14a7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'program_types',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('is_active', sa.Boolean, nullable=False),
    )

def downgrade():
    op.drop_table('program_types')
