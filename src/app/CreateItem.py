from pydantic import BaseModel, Field


class CreateItem(BaseModel):
    joke_content: str = Field(min_length=1)
    joke_author: str = Field(min_length=1)
