"""create students table

Revision ID: 9512494f0a0f
Revises: 8867a0a5c7c6
Create Date: 2016-05-30 17:23:43.418394

"""

# revision identifiers, used by Alembic.
revision = '9512494f0a0f'
down_revision = '8867a0a5c7c6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.Unicode, unique=True, nullable=False),
        sa.Column('name', sa.Unicode, nullable=False),
        sa.Column('email', sa.Unicode, nullable=False),
        sa.Column('program_code', sa.Integer, nullable=True),
        sa.Column('admitted', sa.Unicode, nullable=True),
        sa.Column('level_of_instruction', sa.Unicode(3), nullable=True),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('is_active', sa.Boolean, nullable=False, server_default="true")
    )
def downgrade():
    op.drop_table('students')
