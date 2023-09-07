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