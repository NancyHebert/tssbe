"""create ***security_tokens*** table

Revision ID: f90a78f86dfe
Revises: 9512494f0a0f
Create Date: 2016-06-07 12:58:59.285485

"""

# revision identifiers, used by Alembic.
revision = 'f90a78f86dfe'
down_revision = '9512494f0a0f'
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'security_tokens',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('token', UUID()),
        sa.Column('app_name', sa.Unicode(50), unique=True, nullable=False),
        sa.Column('host', sa.Unicode(50)),
        sa.Column('is_active', sa.Boolean, nullable=False),
    )

def downgrade():
    op.drop_table('security_tokens')

