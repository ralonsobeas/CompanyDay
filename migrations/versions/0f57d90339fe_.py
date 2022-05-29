"""empty message

Revision ID: 0f57d90339fe
Revises: 8520e8a162e0
Create Date: 2022-05-29 12:27:57.990624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f57d90339fe'
down_revision = '8520e8a162e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('eventocharlas_ibfk_1', 'eventocharlas', type_='foreignkey')
    op.create_foreign_key(None, 'eventocharlas', 'empresas', ['empresa_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('eventoferiaempresas_ibfk_1', 'eventoferiaempresas', type_='foreignkey')
    op.create_foreign_key(None, 'eventoferiaempresas', 'empresas', ['empresa_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('eventospeedmeeting_ibfk_1', 'eventospeedmeeting', type_='foreignkey')
    op.create_foreign_key(None, 'eventospeedmeeting', 'empresas', ['empresa_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('personas_ibfk_1', 'personas', type_='foreignkey')
    op.create_foreign_key(None, 'personas', 'empresas', ['empresa_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('presentacionproyectos_ibfk_1', 'presentacionproyectos', type_='foreignkey')
    op.create_foreign_key(None, 'presentacionproyectos', 'empresas', ['empresa_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'presentacionproyectos', type_='foreignkey')
    op.create_foreign_key('presentacionproyectos_ibfk_1', 'presentacionproyectos', 'empresas', ['empresa_id'], ['id'])
    op.drop_constraint(None, 'personas', type_='foreignkey')
    op.create_foreign_key('personas_ibfk_1', 'personas', 'empresas', ['empresa_id'], ['id'])
    op.drop_constraint(None, 'eventospeedmeeting', type_='foreignkey')
    op.create_foreign_key('eventospeedmeeting_ibfk_1', 'eventospeedmeeting', 'empresas', ['empresa_id'], ['id'])
    op.drop_constraint(None, 'eventoferiaempresas', type_='foreignkey')
    op.create_foreign_key('eventoferiaempresas_ibfk_1', 'eventoferiaempresas', 'empresas', ['empresa_id'], ['id'])
    op.drop_constraint(None, 'eventocharlas', type_='foreignkey')
    op.create_foreign_key('eventocharlas_ibfk_1', 'eventocharlas', 'empresas', ['empresa_id'], ['id'])
    # ### end Alembic commands ###
