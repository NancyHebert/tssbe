"""create programs table

Revision ID: f22e0803e31b
Revises: e909990d31e1
Create Date: 2016-02-09 09:54:25.522149

"""

# revision identifiers, used by Alembic.
revision = 'f22e0803e31b'
down_revision = 'e909990d31e1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'programs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('program_types_id', sa.Integer,  sa.ForeignKey('program_types.id', name="fk_program_type")),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('is_active', sa.Boolean, nullable=False),
    )

def downgrade():
    op.drop_table('programs')
