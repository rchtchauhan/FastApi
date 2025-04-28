"""create post table

Revision ID: a14425dbc2ee
Revises: 
Create Date: 2025-04-28 13:29:23.580730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a14425dbc2ee'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table('posts',sa.Column('id',sa.Integer(), nullable= False,primary_key = True),sa.Column('title',sa.String(),nullable = False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts')
    """Downgrade schema."""
    pass
