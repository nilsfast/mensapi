from typing import Union

from fastapi import FastAPI


from menu_service import MenuService
from schemas import FoodResponse


app = FastAPI()

menu_service = MenuService()


@app.get("/")
def read_root():
    return "MensAPI by Nils"


@app.get("/menu", response_model=list[FoodResponse])
def read_root():
    return menu_service.get_menu()
