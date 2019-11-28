"""create person type program rel

Revision ID: 2f433a92d30f
Revises: d5d0939093a5
Create Date: 2016-02-09 09:54:50.819683

"""

# revision identifiers, used by Alembic.
revision = '2f433a92d30f'
down_revision = 'd5d0939093a5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'person_type_program_rel',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('person_types_id', sa.Integer, sa.ForeignKey('person_types.id', name='fk_person_type_program_rel_1'),
                  nullable=False),
        sa.Column('programs_id', sa.Integer, sa.ForeignKey('programs.id', name='fk_person_type_program_rel_2'),
                  nullable=False),
    )

def downgrade():
    op.drop_table('person_type_program_rel')
