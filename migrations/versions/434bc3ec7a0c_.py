"""empty message

Revision ID: 434bc3ec7a0c
Revises: 41e9fc7bb5a9
Create Date: 2023-04-05 10:56:39.355536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '434bc3ec7a0c'
down_revision = '41e9fc7bb5a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topic_content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topic_content', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
