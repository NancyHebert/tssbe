"""create organization person type rel table

Revision ID: d95a7a7e14a7
Revises: 0715a6b9b443
Create Date: 2016-02-09 09:53:37.488816

"""

# revision identifiers, used by Alembic.
revision = 'd95a7a7e14a7'
down_revision = '0715a6b9b443'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'organization_person_type_rel',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('person_types_id', sa.Integer, sa.ForeignKey('person_types.id', name='fk_organization_person_type_rel_1'),
                  nullable=False),
        sa.Column('organizations_id', sa.Integer, sa.ForeignKey('organizations.id', name='fk_organization_person_type_rel_2'),
                  nullable=False),
    ),
    op.create_index('idx_organization_person_type_rel_1', 'organization_person_type_rel', ['person_types_id']),
    op.create_index('idx_organization_person_type_rel_2', 'organization_person_type_rel', ['organizations_id'])


def downgrade():
    op.drop_table('organization_person_type_rel')
