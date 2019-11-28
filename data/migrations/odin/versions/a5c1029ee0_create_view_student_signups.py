"""create view student_signups

Revision ID: a5c1029ee0
Revises: 2eaab064932
Create Date: 2016-09-20 11:48:35.431922

"""

# revision identifiers, used by Alembic.
revision = 'a5c1029ee0'
down_revision = '2eaab064932'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    stmt = """
        CREATE VIEW researcher_student_signups
          AS
            SELECT
          conversations.id as conversation_id
        FROM
          public.conversations
    """
    op.execute(stmt)


def downgrade():
    op.execute('drop view researcher_student_signups')

