"""create_country_names_table

Revision ID: 5002e2c0ac25
Revises: 33a160b4dbc3
Create Date: 2016-03-30 15:40:37.838991

"""

# revision identifiers, used by Alembic.
revision = '5002e2c0ac25'
down_revision = '33a160b4dbc3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'country_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('countries_id', sa.Integer, sa.ForeignKey('countries.id', name="fk_country_names"), nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False)
    )


def downgrade():
    op.drop_table('country_names')
