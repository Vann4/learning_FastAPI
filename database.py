from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost/my_first_db_fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL) #создание «движка» SQLAlchemy.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #Каждый экземпляр класса SessionLocalбудет сеансом базы данных.

Base = declarative_base()