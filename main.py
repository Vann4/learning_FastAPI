from typing import Union
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Seasons(str, Enum): #класс сезонов природы
    spring = 'spring' #весна
    summer = 'summer' #лето
    fall = 'fall' #осень
    winter = 'winter' #зима

app = FastAPI()

@app.get('/')
async def root():
    return {'Hello'}

@app.get('/seasons/{season_name}')
async def seasons(season_name: Seasons): #Сравнение элементов перечисления
    if season_name is Seasons.spring: #Если season_name равен Seasons.spring ('spring'), то сработает return
        return {'Название сезона': 'Весна', 'Сообщение': 'Поздравляю, вы попали на сезон весны'} #Возврат элементов перечисления
    if season_name.value == 'summer': #Получение значения перечисления
        return {'Название сезона': 'Лето', 'Сообщение': 'Поздравляю, вы попали на сезон лета'} #Возврат элементов перечисления
    if season_name is Seasons.fall:
        return {'Название сезона': 'Осень', 'Сообщение': 'Поздравляю, вы попали на сезон осени'}
    if season_name.value == 'winter':
        return {'Название сезона': 'Зима', 'Сообщение': 'Поздравляю, вы попали на сезон зимы'}

@app.get("/text/{text:path}/{user_number:path}") # :path, указывает, что параметр должен соответствовать любому пути.
async def read_text(text: str, user_number: int):
    return {'Вы написали': text, 'Ваше счастливое число': user_number}

fake_items_db = [{"Имя_элемента": "Foo"}, {"Имя_элемента": "Bar"}, {"Имя_элемента": "Baz"}]
@app.get("/item_int/")
async def read_item_int(skip: int = 0, limit: int = 10):  # Query-запросы
    return fake_items_db[skip : skip + limit] # Срез, начиная с индекса skip и ограничение limit

@app.get("/item_text/{name}")
async def read_item_text(name: str, age: int, q: str | None = None, short: bool = False): # Path-запросы с Query-запросами
    text = {'Ваше имя': name, 'Ваш возраст': age}
    if q:
        text.update({'q': q})
    if not short: # Выполнится только если указать short = false
        text.update({'Описание': 'Это удивительный товар, который имеет длинное описание'})
    return text

class Body(BaseModel): #Добавление тела запроса
    name: str
    description: Union[ str, None] = None

@app.post("/request_body/")
async def body(body: Body):
    return body