from pydantic import BaseModel, Field
from yaml import FullLoader, load


class CreateItem(BaseModel):
    joke_content: str = Field(min_length=1)
    joke_author: str = Field(min_length=1)


class Database(BaseModel):
    name: str
    user: str
    host: str
    port: int
    database: str


class RandomJokes(BaseModel):
    name: str
    url: str
    timeout: int


class Settings(BaseModel):
    host: str
    port: int
    path: str
    db: Database
    random_joke: RandomJokes


conf_dict = load(open("config.example.yaml"), Loader=FullLoader)
config = Settings(**conf_dict)
