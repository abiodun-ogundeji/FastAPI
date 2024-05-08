from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World Again"}

@app.get("/users/{user_id}")
def reader_user(user_id: str):
    """
    user_id is accepted here, and return  a json-blob containing it.
    """
    return {"user_id": user_id}

from pydantic import BaseModel, validator

class Item(BaseModel):
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0: 
            raise ValueError(f"the price is expected to be >= 0, it is given {value}")
        return value

@app.post("/items/")
def create_item(item: Item):
    return item

import time
import asyncio

@app.get("/sleep_slow")
def sleep_slow():
    r = time.sleep(1)
    return {"satatus": "done"}

@app.get("/sleep_fast")
async def sleep_fast():
    r = await asyncio.sleep(1)
    return {"satatus": "done"}

