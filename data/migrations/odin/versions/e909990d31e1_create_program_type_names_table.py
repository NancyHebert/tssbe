"""create program type names table

Revision ID: e909990d31e1
Revises: e9ede2797c48
Create Date: 2016-02-09 09:54:12.265947

"""

# revision identifiers, used by Alembic.
revision = 'e909990d31e1'
down_revision = 'e9ede2797c48'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'program_type_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('program_types_id', sa.Integer, sa.ForeignKey('program_types.id', name='fk_program_type_names_1'),
                  nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False),
        sa.Column('full_path', sa.Unicode, nullable=True),
    ),

    op.create_index('idx_unique_program_type', 'program_type_names', ['program_types_id', 'lang'], unique=True),
    op.create_index('idx_unique_program_type_name', 'program_type_names', ['name', 'lang'], unique=True)

def downgrade():
    op.drop_table('program_type_names')
