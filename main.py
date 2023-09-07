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
async def seasons(season_name: Seasons):
    if season_name is Seasons.spring: #Если season_name равен Seasons.spring ('spring'), то сработает return
        return {"Название сезона": 'Весна', 'message': 'Поздравляю, вы попали на сезон весны'}
