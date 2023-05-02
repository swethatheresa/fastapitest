from fastapi import FastAPI
from pydantic import BaseModel


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