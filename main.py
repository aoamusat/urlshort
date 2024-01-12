from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from app.database.config import engine

Base = declarative_base()

app = FastAPI()

# Database initialization
Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


item_list = {
    "ITEM1": {"name": "abcde", "price": 42.15, "is_offer": True},
    "ITEM2": {"name": "xyzab", "price": 16.78, "is_offer": False},
    "ITEM3": {"name": "lmnop", "price": 91.23, "is_offer": True},
    "ITEM4": {"name": "qrstuv", "price": 55.67, "is_offer": False},
    "ITEM5": {"name": "wxyz", "price": 3.14, "is_offer": True},
}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_item(item_id: str, q: Union[str, None] = None) -> Item:
    item = item_list.get(item_id, None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    is_item_exist = item_list.get(item_id, None)
    if not is_item_exist:
        raise HTTPException(status_code=404, detail="Item not found")
    item_list[item_id] = item
    return item
