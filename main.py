from fastapi import FastAPI
from enum import Enum

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

fake_items_db = [{"Имя_элемента": "Foo"}, {"Имя_элемента": "Bar"}, {"Имя_элемента": "Baz"}] # Query-запросы
@app.get("/item_int/")
async def read_item_int(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit] # Срез, начиная с индекса skip и ограничение limit

@app.get("/item_text/")
async def read_item_text(item_text: str, q: str | None = None): # Если передать только item_text
    if q:
        return {"Первый текст": item_text, "Второй текст": q}
    return {"Текст лемента": item_text} # То сработает только этот return