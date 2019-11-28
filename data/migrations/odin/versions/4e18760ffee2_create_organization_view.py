"""create organization_view

Revision ID: 4e18760ffee2
Revises: cfe3f3556b39
Create Date: 2016-02-16 20:22:52.594975

"""

# revision identifiers, used by Alembic.
revision = '4e18760ffee2'
down_revision = 'cfe3f3556b39'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    organization_view = """
        CREATE VIEW organization_view
          AS
            SELECT
          organizations.id as org_id,
          organizations.parent_id,
          organizations.organization_types_id,
          organizations.date_created,
          organization_names.id as org_name_id,
          organization_names.organizations_id,
          organization_names.lang,
          organization_names.name,
          organization_names.full_path
        FROM
          public.organizations,
          public.organization_names
        WHERE
          organizations.id = organization_names.organizations_id
        ORDER BY
          organizations.parent_id ASC,
          organization_names.lang ASC,
          organization_names.full_path ASC
    """
    op.execute(organization_view)

def downgrade():
    op.execute('drop view organization_view')
