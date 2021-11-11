from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_HOST =  os.environ.get("MYSQL_HOST")
DB_USER =  os.environ.get("MYSQL_USER")
DB_PASSWORD =  os.environ.get("MYSQL_PASSWORD")
DB_NAME =  os.environ.get("MYSQL_DATABASE")

SQLALCHEMY_DATABASE_URL = "mysql://%s:%s@%s/%s?charset=utf8" % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding="utf-8"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
