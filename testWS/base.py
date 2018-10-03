from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import orm

engine = create_engine('mysql+pymysql://root@localhost:3306/test_projet')
Session = sessionmaker(bind=engine)

sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
    expire_on_commit=True)
session = orm.scoped_session(sm)
session2 = Session()

Base = declarative_base()