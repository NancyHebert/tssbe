"""create_states_table

Revision ID: 09f2fcdd4a4c
Revises: 5002e2c0ac25
Create Date: 2016-03-30 15:40:43.795636

"""

# revision identifiers, used by Alembic.
revision = '09f2fcdd4a4c'
down_revision = '5002e2c0ac25'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'states',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('countries_id', sa.Integer, sa.ForeignKey('countries.id', name="fk_country_state"), nullable=False),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
    )


def downgrade():
    op.drop_table('states')
