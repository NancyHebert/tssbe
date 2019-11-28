"""create country table

Revision ID: 1cd702276a4e
Revises: 453a9a6facd8
Create Date: 2016-07-27 18:57:11.977121

"""

# revision identifiers, used by Alembic.
revision = '1cd702276a4e'
down_revision = '453a9a6facd8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    country = op.create_table(
        'country',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('iso_code_alpha_1', sa.Unicode(3), nullable=True),
        sa.Column('iso_code_alpha_2', sa.Unicode(3), nullable=True),
        sa.Column('iso_code_alpha_3', sa.Unicode(3), nullable=True),
        sa.Column('name', sa.Unicode(50), nullable=True),
        sa.Column('ascii_name', sa.Unicode(50), nullable=True),
        sa.Column('capital_name', sa.Unicode(50), nullable=True),
        sa.Column('capital_iso_number', sa.Unicode(3), nullable=True),
        sa.Column('area', sa.Integer, nullable=True),
        sa.Column('population', sa.Integer, nullable=True),
        sa.Column('continent_name', sa.Unicode(50), nullable=True),
        sa.Column('continent_iso_number', sa.Unicode(3), nullable=True),
        sa.Column('latitude', sa.Integer, nullable=True),
        sa.Column('longtitude', sa.Integer, nullable=True),
        sa.Column('valid_date', sa.DateTime, nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_change', sa.Boolean, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('country')
