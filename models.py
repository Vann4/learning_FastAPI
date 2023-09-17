from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users" #имя таблицы

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    father_name = Column(String)
    hashed_password = Column(String)
    age = Column(Integer)
    male = Column(Boolean, default=True)