"""create tables

Revision ID: 365d7ed18c6a
Revises: 
Create Date: 2020-02-23 22:04:03.654535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '365d7ed18c6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    accounts_table = op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(length=158), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_password_hash'), 'user', ['password_hash'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('oauth_client',
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('client_secret', sa.String(length=55), nullable=False),
    sa.Column('is_confidential', sa.Boolean(), nullable=True),
    sa.Column('_redirect_uris', sa.Text(), nullable=True),
    sa.Column('_default_scopes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_index(op.f('ix_oauth_client_client_secret'), 'oauth_client', ['client_secret'], unique=True)
    op.create_table('oauth_grant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('redirect_uri', sa.String(length=255), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('_scopes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['oauth_client.client_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_oauth_grant_code'), 'oauth_grant', ['code'], unique=False)
    op.create_table('oauth_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('token_type', sa.String(length=40), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('_scopes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['oauth_client.client_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token'),
    sa.UniqueConstraint('refresh_token')
    )
    # ### end Alembic commands ###
    op.bulk_insert(accounts_table, [
        {'id': 0, 'name': 'no account'}
    ])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('oauth_token')
    op.drop_index(op.f('ix_oauth_grant_code'), table_name='oauth_grant')
    op.drop_table('oauth_grant')
    op.drop_index(op.f('ix_oauth_client_client_secret'), table_name='oauth_client')
    op.drop_table('oauth_client')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_password_hash'), table_name='user')
    op.drop_table('user')
    op.drop_table('account')
    # ### end Alembic commands ###
