from sqlalchemy import create_engine, MetaData
import os
import sys
sys.path.append(os.path.realpath(__file__ + '/../../../../'))
from config import settings

class PGModel(object):
    def __init__(self, *args, **kwargs):
        self.__conn_url__ = "postgresql+psycopg2cffi://odin:y0uguysr0ck@db/midgard"
        self.db_engine = create_engine(self.__conn_url__)
        self.db_engine.echo = False
        self.metadata = MetaData(self.db_engine)
