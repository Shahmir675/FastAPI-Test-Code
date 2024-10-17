from typing import List, Union

from fastapi import FastAPI, Query

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: List[Union[str, int]] = Query(None)):
    if q is None:
        q = []
    return {"item_id": item_id, 'q': q}

@app.post('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}