"""create person profession table

Revision ID: e2a69e85fc83
Revises: 2e9edb19e846
Create Date: 2016-07-28 15:32:47.352006

"""

# revision identifiers, used by Alembic.
revision = 'e2a69e85fc83'
down_revision = '2e9edb19e846'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    person_profession = op.create_table(
        'person_profession',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('person_id', sa.Integer, nullable=True),
        sa.Column('employee_id', sa.Integer, nullable=True),
        sa.Column('organization_id', sa.Integer, nullable=True),
        sa.Column('short_name', sa.Unicode(30), nullable=True),
        sa.Column('full_name', sa.Unicode(255), nullable=True),
        sa.Column('profession_name', sa.Unicode(30), nullable=True),
        sa.Column('profession_number', sa.Integer, nullable=True),
        sa.Column('description', sa.Unicode(255), nullable=True),
        sa.Column('type', sa.Unicode(30), nullable=True),
        sa.Column('status', sa.Unicode(30), nullable=True),
        sa.Column('start_date', sa.DateTime, nullable=True),
        sa.Column('end_date', sa.DateTime, nullable=True),
        sa.Column('is_active', sa.Boolean, nullable=True),
        sa.Column('created_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('last_updated_date', sa.TIMESTAMP, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('last_updated_by', sa.Integer, nullable=True),
    )


def downgrade():
    op.drop_table('person_profession')
