"""create_state_names_table

Revision ID: a3321747fb85
Revises: 09f2fcdd4a4c
Create Date: 2016-03-30 15:40:48.215889

"""

# revision identifiers, used by Alembic.
revision = 'a3321747fb85'
down_revision = '09f2fcdd4a4c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'state_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('states_id', sa.Integer, sa.ForeignKey('states.id', name="fk_state_names"), nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False)
    )


def downgrade():
    op.drop_table('state_names')
