"""create table verification

Revision ID: 112fd4612da
Revises: ae0364975143
Create Date: 2016-09-19 20:54:41.118945

"""

# revision identifiers, used by Alembic.
revision = '112fd4612da'
down_revision = 'ae0364975143'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'verifications',
        # sa.Column('id', sa.Integer, primary_key=True),
        # sa.Column('guid', sa.Integer, nullable=False),
        # sa.Column('code', sa.UnicodeText, nullable=False),
        # sa.Column('email', sa.String, nullable=True),
        # sa.Column('send_date', sa.UnicodeText, nullable = True),
        # sa.Column('expired_date', sa.UnicodeText, nullable=False)
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.Unicode, nullable=False),
        sa.Column('code', sa.Unicode, nullable=False)
    )


def downgrade():
    op.drop_table('verifications')
