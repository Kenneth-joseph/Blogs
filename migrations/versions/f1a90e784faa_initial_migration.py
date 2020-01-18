"""Initial Migration

Revision ID: f1a90e784faa
Revises: 
Create Date: 2020-01-18 23:44:17.367344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1a90e784faa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password_hash'),
    sa.UniqueConstraint('username')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('blog')
    op.drop_table('users')
    # ### end Alembic commands ###
