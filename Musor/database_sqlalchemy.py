from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

from sqlalchemy import (
    Column,
    Integer,
    String,
)

base = declarative_base()

class VUZ(base):
    __tablename__ = "VUZ"

    codvuz = Column(Integer, primary_key=True)
    z1 = Column(String)
    z2 = Column(String)
    region = Column(String)
    city = Column(String)
    status = Column(String)
    obl = Column(Integer)
    oblname = Column(String)
    gr_ved = Column(String)
    prof = Column(String)


engine = create_engine(
    "sqlite:///Databases/my_bd.db",
    connect_args={
        'check_same_thread': False,
    },
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


@contextmanager
def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()

session = Session()
## TEST
# with get_session() as db:
#     print(db.query(VUZ).all())
