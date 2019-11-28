"""create admin table

Revision ID: 5ee07322557b
Revises: e6f5b1464f9c
Create Date: 2016-12-22 15:01:49.320289

"""

# revision identifiers, used by Alembic.
revision = '5ee07322557b'
down_revision = 'e6f5b1464f9c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    admins = op.create_table(
        'admins',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.Unicode, nullable=False),
        sa.Column('name', sa.Unicode, nullable=False),
        sa.Column('email', sa.Unicode, nullable=False)
    )

    op.bulk_insert(admins,
                   [
                       {'username': 'klittlej', 'name': 'Karen Littlejohn', 'email': 'klittlej@uottawa.ca'},
                       {'username': 'llema2', 'name': 'Louise Lemay', 'email': 'louise.lemay@uottawa.ca'},
                       {'username': 'shamdan', 'name': 'Sadek Hamdan', 'email': 'shamdan@uottawa.ca'}
                   ]
                  )

def downgrade():
    op.drop_table('admins')
