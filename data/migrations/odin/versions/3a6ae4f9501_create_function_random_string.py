"""create function random_string

Revision ID: 3a6ae4f9501
Revises: 138682536e7
Create Date: 2016-09-20 17:09:49.744593

"""

# revision identifiers, used by Alembic.
revision = '3a6ae4f9501'
down_revision = '138682536e7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    stmt = """
      create or replace function random_string(length integer) returns text as 
      $$
      declare
        chars text[] := '{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z}';
        result text := '';
        i integer := 0;
      begin
        if length < 0 then
          raise exception 'Given length cannot be less than 0';
        end if;
        for i in 1..length loop
          result := result || chars[1+random()*(array_length(chars, 1)-1)];
        end loop;
        return result;
      end;
      $$ language plpgsql;
    """
    op.execute(stmt)


def downgrade():
    op.execute('drop function random_string')
