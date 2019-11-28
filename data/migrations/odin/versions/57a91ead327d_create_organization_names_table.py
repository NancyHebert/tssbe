"""create organization_names table

Revision ID: 57a91ead327d
Revises: 6f48b2477aa7
Create Date: 2016-02-05 03:16:27.288318

"""

# revision identifiers, used by Alembic.
revision = '57a91ead327d'
down_revision = '6f48b2477aa7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    organization_names = op.create_table(
        'organization_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('organizations_id', sa.Integer, sa.ForeignKey('organizations.id', name='fk_organization_names_1'),
                  nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False),
        sa.Column('full_path', sa.Unicode, nullable=True),
    )

    op.create_index('idx_unique_org', 'organization_names', ['organizations_id', 'lang'], unique=True)
    op.create_index('idx_unique_org_name', 'organization_names', ['name', 'lang'], unique=True)

    op.bulk_insert(organization_names,
        [
            { 'organizations_id': 1, 'lang': 'EN', 'name': 'Organization_names', 'full_path': 'full_path' },
            { 'organizations_id': 1, 'lang': 'FR', 'name': 'Organisation_noms', 'full_path': 'plein_chemin' },
        ]
    )

def downgrade():
    op.execute('drop table organization_names CASCADE')
