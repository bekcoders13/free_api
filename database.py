# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import pymysql
#
# engine = create_engine('mysql+pymysql://root:root@localhost/tamaddi_db')
# SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
# Base = declarative_base()
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///./test.db",
                       connect_args={"check_same_thread": False})

SessionLocal = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
