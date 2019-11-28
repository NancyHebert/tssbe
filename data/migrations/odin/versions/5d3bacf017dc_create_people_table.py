"""create people table

Revision ID: 5d3bacf017dc
Revises: 
Create Date: 2016-02-05 02:32:20.573976

"""

# revision identifiers, used by Alembic.
revision = '5d3bacf017dc'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'people',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.Unicode(50), nullable=False),
        sa.Column('middle_initial', sa.Unicode(50), nullable=False),
        sa.Column('last_name', sa.Unicode(50), nullable=False),
        sa.Column('date_of_birth', sa.Date, nullable=False),
    )

def downgrade():
    op.drop_table('people')