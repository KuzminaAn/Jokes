from yaml import load, FullLoader
from pydantic import BaseModel, Field


class CreateItem(BaseModel):
    joke_content: str = Field(min_length=1)
    joke_author: str = Field(min_length=1)


class Database(BaseModel):
    name: str
    user: str
    host: str
    port: int
    database: str


class Settings(BaseModel):
    host: str
    port: int
    path: str
    db: Database


conf_dict = load(open("config.example.yaml"), Loader=FullLoader)
config = Settings(**conf_dict)
