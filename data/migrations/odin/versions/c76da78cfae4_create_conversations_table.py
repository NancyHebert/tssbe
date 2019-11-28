"""create conversations table

Revision ID: c76da78cfae4
Revises: f90a78f86dfe
Create Date: 2016-06-14 14:42:06.526656

"""

# revision identifiers, used by Alembic.
revision = 'c76da78cfae4'
down_revision = 'f90a78f86dfe'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'conversations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('researcher_uniweb_number', sa.Integer),
        sa.Column('researcher_name', sa.Unicode()), # snapshot
        sa.Column('student_username', sa.Unicode()),
        sa.Column('student_name', sa.Unicode()), # snapshot
        sa.Column('body', sa.Unicode(), nullable=False),
        sa.Column('is_from_student', sa.Boolean, nullable=False),
        sa.Column('is_draft', sa.Boolean, nullable=False),
        sa.Column('sent_date', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('read_date', sa.DateTime(timezone=True), nullable=True)
    )

def downgrade():
    op.drop_table('conversations')
