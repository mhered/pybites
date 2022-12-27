from typing import Dict

from fastapi import FastAPI, Response, status
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

# write the Create endpoint
@app.post("/", status_code=200) # 
async def create_food(food: Food, response: Response):
    foods[food.id] = food
    response.status_code = status.HTTP_201_CREATED
    return foods