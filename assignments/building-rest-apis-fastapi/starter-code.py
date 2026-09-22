from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Items API")

items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
]


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Items API"}


# TODO: Add CRUD endpoints for items
# - GET /items
# - GET /items/{item_id}
# - POST /items
# - PUT /items/{item_id}
# - DELETE /items/{item_id}
