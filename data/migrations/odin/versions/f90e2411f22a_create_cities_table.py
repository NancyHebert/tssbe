"""create_cities_table

Revision ID: f90e2411f22a
Revises: a3321747fb85
Create Date: 2016-03-30 15:40:56.338010

"""

# revision identifiers, used by Alembic.
revision = 'f90e2411f22a'
down_revision = 'a3321747fb85'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'cities',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('states_id', sa.Integer, sa.ForeignKey('states.id', name="fk_state_city"), nullable=False),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
    )


def downgrade():
    op.drop_table('cities')
