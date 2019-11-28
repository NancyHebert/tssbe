"""create person_type_rel table

Revision ID: ea4671d31776
Revises: 8444b7c4b4aa
Create Date: 2016-02-05 02:47:28.487566

"""

# revision identifiers, used by Alembic.
revision = 'ea4671d31776'
down_revision = '8444b7c4b4aa'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'person_type_rel',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('person_types_id', sa.Integer, sa.ForeignKey('person_types.id', name="fk_person_type_rel_1"),
                  nullable=False),
        sa.Column('people_id', sa.Integer, sa.ForeignKey('people.id', name="fk_person_type_rel_2"),
                  nullable=False)
    )

def downgrade():
    op.drop_table('person_type_rel')