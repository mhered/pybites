from pydantic import BaseModel
from typing import Optional

# write a Food pydantic model




class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: Optional[float] = 0.0
    

if __name__ == "__main__":
    food = Food(id = 3, name ="spaghetti", serving_size = "100g", kcal_per_serving=500, protein_grams =5.1)
    print(food.name)
    print(food.kcal_per_serving)
    print(food.fibre_grams)