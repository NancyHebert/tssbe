"""create view researcher_response

Revision ID: 138682536e7
Revises: a5c1029ee0
Create Date: 2016-09-20 11:48:49.643670

"""

# revision identifiers, used by Alembic.
revision = '138682536e7'
down_revision = 'a5c1029ee0'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    stmt = """
        CREATE VIEW researcher_response_view
          AS
            SELECT
          conversations.id as conversation_id
        FROM
          public.conversations
        
    """
    op.execute(stmt)


def downgrade():
    pass
