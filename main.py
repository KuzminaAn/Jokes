from fastapi import FastAPI, Header
from fastapi import Response
from pydantic import BaseModel
from time import time
from functions import get_jokes_by_user, get_jokes_by_id, create_jokes, update_jokes, delete_jokes
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, my friend!"}


# 1. список шуток конкретного пользователя
@app.get("/joke/")
async def get_jokes_by_user_id(user_id: int = Header(default=None, alias='X-User')):
    result = get_jokes_by_user(user_id)
    return result


# 2. получить конкретную шутку по id
@app.get("/joke/{joke_id}")
async def get_jokes_by_joke_id(joke_id: int):
    result = get_jokes_by_id(joke_id)
    return result


# 3. создать шутку
class CreateItem(BaseModel):
    joke_content: str
    joke_author: str


@app.post("/joke/")
async def create_joke(item: CreateItem, user_id: int = Header(default=None, alias='X-User')):
    created_at = int(time())
    result = create_jokes(user_id, item.joke_content, item.joke_author, created_at)
    return result


# 4. обновить шутку
class UpdateItem(BaseModel):
    joke_content: str
    joke_author: str


@app.put("/joke/{joke_id}")
async def update_joke(item: UpdateItem, joke_id: int):
    result = update_jokes(item.joke_content, item.joke_author, joke_id)
    return result


# 5. удалить выбранную шутку
@app.delete("/joke/{joke_id}")
async def delete_item(joke_id: int):
    delete_jokes(joke_id)
    return Response(status_code=204)


# 6. добавить рандомную шутку
@app.post("/joke/random")
async def create_random_joke(user_id: int = Header(default=None, alias='X-User')):
    r = requests.get("https://api.chucknorris.io/jokes/random")
    data = r.json()
    data1 = data['value']
    created_at = int(time())
    result = create_jokes(user_id, data1, "Chuck Norris", created_at)
    return result
