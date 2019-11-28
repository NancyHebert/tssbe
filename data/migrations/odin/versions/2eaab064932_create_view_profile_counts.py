"""create view profile_counts

Revision ID: 2eaab064932
Revises: 112fd4612da
Create Date: 2016-09-20 11:47:47.722887

"""

# revision identifiers, used by Alembic.
revision = '2eaab064932'
down_revision = '112fd4612da'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # stmt = """
    #     CREATE VIEW student_profile_counts
    #       AS
    #         SELECT
    #       conversations.id as conversation_id,
    #       to_timestamp(conversations.send_date,'Mon'),
    #       count(conversations.send_date)
    #     FROM
    #       public.conversations
    #     GROUP BY
    #       to_timestamp(conversations.send_date,'Mon')
    # """
    # op.execute(stmt)
    pass


def downgrade():
    pass
