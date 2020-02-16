"""empty message

Revision ID: 5e45310f642b
Revises: 7f74f3ebba49
Create Date: 2020-02-16 11:11:05.572893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e45310f642b'
down_revision = '7f74f3ebba49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('art',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('creation_date', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('child_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['child.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('art')
    # ### end Alembic commands ###