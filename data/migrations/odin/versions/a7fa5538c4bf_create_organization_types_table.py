"""create organization_types table

Revision ID: a7fa5538c4bf
Revises: ea4671d31776
Create Date: 2016-02-05 03:08:32.210996

"""

# revision identifiers, used by Alembic.
revision = 'a7fa5538c4bf'
down_revision = 'ea4671d31776'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


def upgrade():
    organization_types = op.create_table(
        'organization_types',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('is_active', sa.Boolean, nullable=False),
    )

    op.bulk_insert(organization_types,
        [
            { 'is_active': True },
        ]
    )

def downgrade():
    op.drop_table('organization_types')
