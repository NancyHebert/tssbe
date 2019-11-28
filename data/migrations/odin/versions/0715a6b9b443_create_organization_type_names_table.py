"""create organization_type_names table

Revision ID: 0715a6b9b443
Revises: 57a91ead327d
Create Date: 2016-02-05 03:21:02.889638

"""

# revision identifiers, used by Alembic.
revision = '0715a6b9b443'
down_revision = '57a91ead327d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    organization_type_names = op.create_table(
        'organization_type_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('organization_types_id', sa.Integer, sa.ForeignKey('organization_types.id',
                                                                     name='fk_organization_type_names'),
                  nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False)
    )

    op.create_index('idx_unique_org_type', 'organization_type_names', ['organization_types_id', 'lang'], unique=True)
    op.create_index('idx_unique_org_type_name', 'organization_type_names', ['name', 'lang'], unique=True)

    op.bulk_insert(organization_type_names,
        [
            { 'organization_types_id': 1, 'lang': 'EN', 'name': 'Organization_type_names' },
            { 'organization_types_id': 1, 'lang': 'FR', 'name': 'Organisation_type_noms' },
        ]
    )

def downgrade():
    op.drop_table('organization_type_names')
