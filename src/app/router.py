from time import time

import requests
from fastapi import APIRouter, Header, Path, Response

from src.app.schemas import CreateItem
from src.db.functions import (
    create_jokes,
    delete_jokes,
    get_jokes_by_id,
    get_jokes_by_user,
    update_jokes,
)

router = APIRouter(
    prefix="/joke",
    tags=["joke"],
)


# 1. список шуток конкретного пользователя
@router.get("/")
async def get_jokes_by_user_id(
    user_id: int = Header(default=None, alias="X-User", ge=1)
):
    result = get_jokes_by_user(user_id)
    if not result:
        return Response(status_code=404)
    return result


# 2. получить конкретную шутку по id
@router.get("/{joke_id}")
async def get_jokes_by_joke_id(joke_id: int = Path(ge=1)):
    result = get_jokes_by_id(joke_id)
    if not result:
        return Response(status_code=404)
    return result


# 3. создать шутку
@router.post("/")
async def create_joke(
    item: CreateItem, user_id: int = Header(default=None, alias="X-User", ge=1)
):
    created_at = int(time())
    result = create_jokes(
        user_id, item.joke_content, item.joke_author, created_at
    )
    return result


# 4. обновить шутку
@router.put("/{joke_id}")
async def update_joke(item: CreateItem, joke_id: int = Path(ge=1)):
    result = get_jokes_by_id(joke_id)
    if not result:
        return Response(status_code=404)
    result = update_jokes(item.joke_content, item.joke_author, joke_id)
    return result


# 5. удалить выбранную шутку
@router.delete("/{joke_id}")
async def delete_item(joke_id: int = Path(ge=1)):
    result = get_jokes_by_id(joke_id)
    if not result:
        return Response(status_code=404)
    delete_jokes(joke_id)
    return Response(status_code=204)


# 6. добавить рандомную шутку
@router.post("/random")
async def create_random_joke(
    user_id: int = Header(default=None, alias="X-User", ge=1)
):
    r = requests.get("https://api.chucknorris.io/jokes/random")
    data = r.json()
    data1 = data["value"]
    created_at = int(time())
    result = create_jokes(user_id, data1, "Chuck Norris", created_at)
    return result
