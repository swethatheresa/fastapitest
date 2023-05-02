from fastapi import FastAPI,Query,Path
from pydantic import BaseModel
from typing import Annotated


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float 


app=FastAPI()
@app.get("/")
async def root():
    return { 'message':'hello world'}

@app.get('/items/{item_id}')
async def item(item_id : int):
    return {'item_id':item_id}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/test/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            alias="item-query",
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results