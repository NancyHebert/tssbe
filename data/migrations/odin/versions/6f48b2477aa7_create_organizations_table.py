"""create organizations table

Revision ID: 6f48b2477aa7
Revises: a7fa5538c4bf
Create Date: 2016-02-05 03:11:01.374904

"""

# revision identifiers, used by Alembic.
revision = '6f48b2477aa7'
down_revision = 'a7fa5538c4bf'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    organizations = op.create_table(
        'organizations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('parent_id', sa.Integer, nullable=False),
        sa.Column('organization_types_id', sa.Integer, sa.ForeignKey('organization_types.id', name='fk_organizations_2'),
                  nullable=False),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('is_active', sa.Boolean, nullable=False),
    )
    
    op.bulk_insert(organizations,
        [
            { 'parent_id': 1, 'organization_types_id': 1, 'is_active': True },
        ]
    )

    op.create_foreign_key(
        'fk_organizations_1',
        'organizations', 'organizations',
        ['parent_id'], ['id'],
    )

def downgrade():
    op.drop_table('organizations')