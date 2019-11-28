"""create person_types table

Revision ID: 4aa2e00610b8
Revises: 5d3bacf017dc
Create Date: 2016-02-05 02:35:31.847315

"""

# revision identifiers, used by Alembic.
revision = '4aa2e00610b8'
down_revision = '5d3bacf017dc'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    person_types = op.create_table(
        'person_types',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('parent_id', sa.Integer, nullable=False),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('is_active', sa.Boolean, nullable=False),
    )

    op.bulk_insert(person_types,
        [
            { 'parent_id': 1, 'is_active': True },
        ]
    )

    op.create_foreign_key(
        'fk_person_types_1',
        'person_types', 'person_types',
        ['parent_id'], ['id'],
    )

def downgrade():
    op.drop_table('person_types')
