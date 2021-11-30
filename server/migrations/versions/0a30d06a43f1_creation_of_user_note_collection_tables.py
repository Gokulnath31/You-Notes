"""Creation of User,Note,Collection tables

Revision ID: 0a30d06a43f1
Revises: 
Create Date: 2021-09-25 09:13:30.238300

"""
from alembic import op
from pydantic.tools import T
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision = '0a30d06a43f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False,autoincrement=True),
        sa.Column('first_name', sa.String(length=255), nullable=False),
        sa.Column('last_name', sa.String(length=255), nullable=True),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.Column('modified', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


    op.create_table('collections',
        sa.Column('id', sa.Integer(), nullable=False,autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),  
        sa.Column('created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.Column('modified', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('notes',
        sa.Column('id', sa.Integer(), nullable=False,autoincrement=True),
        sa.Column('title', sa.String(length=255), nullable=False), 
        sa.Column('tags', sa.JSON(), nullable=True), 
        sa.Column('markdown_text', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('collection_id', sa.Integer(), nullable=  True),
        sa.Column('source', mysql.ENUM("YOUTUBE","ARTICLES","DOCUMENTATION","OTHERS"), nullable=False),
        sa.Column('visibility', sa.Boolean(), nullable=False),
        sa.Column('created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.Column('modified', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['collection_id'], ['collections.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    )

def downgrade():
    op.drop_table('users')
    op.drop_table('collections')
    op.drop_table('notes')
