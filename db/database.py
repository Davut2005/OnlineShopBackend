from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings
from sqlmodel import Session, SQLModel


engine = create_engine( settings.DATABASE_URL )

def get_db ():
    with Session(engine) as session:
        yield session


def create_db_tables():
    SQLModel.metadata.create_all(bind=engine)