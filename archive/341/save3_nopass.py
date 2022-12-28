from datetime import datetime
from typing import Any

from passlib.context import CryptContext
from pydantic import BaseModel

from pydantic.dataclasses import dataclass


# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# which we'll further explore in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    """Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0

# Write the User and FoodEntry models here ...

@dataclass
class User(BaseModel):
    id: int
    username: str
    password: str  # (needed for authentication later)

    # For password override the constructor (__init__.py) to hash the password upon creation of the module. 
    # You can use the provided get_password_hash() function for this.
    
    def __post_init__(self):
        self.password = get_password_hash(self.password)


class FoodEntry(BaseModel):
    id: int  # (what in a DB would be the primary key)
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    # add a property to calculate the total calories of a food entry 
    
    @property
    def total_calories(self):
        return self.food.kcal_per_serving * self.number_servings
        
