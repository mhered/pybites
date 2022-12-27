from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


@app.post("/", status_code=201)
async def create_food(food: Food):
    """Endpoint from Bite 03"""
    foods[food.id] = food
    return food


# write the two Read endpoints
@app.get("/", status_code=200)
async def read_foods():
    """Endpoint to read all foods"""
    return foods

@app.get("/", status_code=200)
async def read_food(id):
    """Endpoint to read a given food item"""
    return foods[id]
