"""create_city_names_table

Revision ID: 8867a0a5c7c6
Revises: f90e2411f22a
Create Date: 2016-03-30 15:41:04.850543

"""

# revision identifiers, used by Alembic.
revision = '8867a0a5c7c6'
down_revision = 'f90e2411f22a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'city_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cities_id', sa.Integer, sa.ForeignKey('cities.id', name="fk_city_names"), nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False)
    )


def downgrade():
    op.drop_table('city_names')
