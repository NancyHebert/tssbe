"""create gs_programs table

Revision ID: e6f5b1464f9c
Revises: 3a6ae4f9501
Create Date: 2016-11-24 02:34:58.098849

"""

# revision identifiers, used by Alembic.
revision = 'e6f5b1464f9c'
down_revision = '3a6ae4f9501'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    gs_programs=op.create_table(
    'gs_programs',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('code', sa.Integer, nullable=False),
    sa.Column('name', sa.UnicodeText, nullable=False),
    sa.Column('lang', sa.Unicode(2), nullable=False)
    )


    op.bulk_insert(gs_programs,
        [
            { 'code': 1, 'name': 'Biochemistry', 'lang': 'en'},
            { 'code': 2, 'name': 'Cellular and Molecular Medicine', 'lang': 'en'},
            { 'code': 3, 'name': 'Epidemiology', 'lang': 'en'},
            { 'code': 4, 'name': 'Microbiology and Immunology', 'lang': 'en'},
            { 'code': 5, 'name': 'Neuroscience', 'lang': 'en'},
            { 'code': 1, 'name': 'Biochimie', 'lang': 'fr'},
            { 'code': 2, 'name': 'Médecine cellulaire et moléculaire', 'lang': 'fr'},
            { 'code': 3, 'name': 'Épidémiologie', 'lang': 'fr'},
            { 'code': 4, 'name': 'Microbiologie et immunologie', 'lang': 'fr'},
            { 'code': 5, 'name': 'Neurosciences', 'lang': 'fr'},
        ]
    )  

    op.create_index('idx_unique_gs_prog', 'gs_programs', ['name', 'lang'], unique=True)
    op.create_index('idx_unique_gs_prog_code', 'gs_programs', ['code', 'lang'], unique=True)
def downgrade():
    op.drop_table('gs_programs')
