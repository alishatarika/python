from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

# in-memory storage
items_db: List[Item] = []

@app.post("/items")
def add_item(item: Item):
    items_db.append(item)
    return {
        "message": "Item added successfully",
        "total_items": len(items_db),
        "items": items_db
    }

@app.get("/items")
def get_items():
    return items_db
