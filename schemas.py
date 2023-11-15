from pydantic import BaseModel


class FoodResponse(BaseModel):
    name: str
    category: str
    price: float
