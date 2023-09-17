from pydantic import BaseModel

class UserBase(BaseModel):
    surname: str

class UserCreate(UserBase):
    password: str
    surname: str
    name: str
    father_name: str
    age: int
    male: bool

class User(UserBase):
    id: int

    class Config:
        from_attributes = True #Это установка значения конфигурации, а не объявление типа.