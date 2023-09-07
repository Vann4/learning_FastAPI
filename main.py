from fastapi import FastAPI
from enum import Enum

class Seasons(str, Enum):
    spring = 'spring' #весна
    summer = 'summer' #лето
    fall = 'fall' #осень
    winter = 'winter' #зима

app = FastAPI()

@app.get('/')
async def root():
    return {'Hello'}