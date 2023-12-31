"""your message

Revision ID: abd7c83a9772
Revises: 
Create Date: 2023-07-05 14:51:34.670529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abd7c83a9772'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('medium', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artworks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('medium', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name=op.f('fk_artworks_artist_id_artists')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_collections_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('art_collections',
    sa.Column('artwork_id', sa.Integer(), nullable=False),
    sa.Column('collection_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artwork_id'], ['artworks.id'], name=op.f('fk_art_collections_artwork_id_artworks')),
    sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], name=op.f('fk_art_collections_collection_id_collections')),
    sa.PrimaryKeyConstraint('artwork_id', 'collection_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('art_collections')
    op.drop_table('collections')
    op.drop_table('artworks')
    op.drop_table('users')
    op.drop_table('artists')
    # ### end Alembic commands ###
