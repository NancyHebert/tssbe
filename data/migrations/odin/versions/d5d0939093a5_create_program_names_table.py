"""create program names table

Revision ID: d5d0939093a5
Revises: f22e0803e31b
Create Date: 2016-02-09 09:54:34.877618

"""

# revision identifiers, used by Alembic.
revision = 'd5d0939093a5'
down_revision = 'f22e0803e31b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'program_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('programs_id', sa.Integer, sa.ForeignKey('programs.id', name='fk_program_names_1'),
                  nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False)
    ),

    op.create_index('idx_unique_program', 'program_names', ['programs_id', 'lang'], unique=True),
    op.create_index('idx_unique_program_name', 'program_names', ['name', 'lang'], unique=True)

def downgrade():
    op.drop_table('program_names')
