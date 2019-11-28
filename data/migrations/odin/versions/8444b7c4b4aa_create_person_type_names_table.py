"""create person_type_names tables

Revision ID: 8444b7c4b4aa
Revises: 4aa2e00610b8
Create Date: 2016-02-05 02:36:44.838192

"""

# revision identifiers, used by Alembic.
revision = '8444b7c4b4aa'
down_revision = '4aa2e00610b8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    person_type_names = op.create_table(
        'person_type_names',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('person_types_id', sa.Integer, sa.ForeignKey('person_types.id', name='fk_person_type_names_1'),
                  nullable=False),
        sa.Column('lang', sa.Unicode(2), nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False),
        sa.Column('full_path', sa.Unicode, nullable=True),
    )

    op.create_index('idx_unique_ppl_type', 'person_type_names', ['person_types_id', 'lang'], unique=True)
    op.create_index('idx_unique_ppl_type_name', 'person_type_names', ['name', 'lang'], unique=True)

    op.bulk_insert(person_type_names,
        [
            { 'person_types_id': 1, 'lang': 'EN', 'name': 'Person_type_names', 'full_path': 'full_path' },
            { 'person_types_id': 1, 'lang': 'FR', 'name': 'Personne_type_noms', 'full_path': 'plein_chemin' },
        ]
    )

def downgrade():
    op.drop_table('person_type_names')