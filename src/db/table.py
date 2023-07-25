from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Jokes(Base):

    __tablename__ = 'jokes'
    
    joke_id = Column('id', Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, nullable=False, unique=True, primary_key=True)
    content = Column('content', String, nullable=False)
    author = Column('author', String, nullable=False)
    created_at = Column('created_at', DateTime)

    def __int__(self, user_id: int, content: str, author: str, created_at: int):
        self.user_id = user_id
        self.content = content
        self.author = author
        self.created_at = created_at

    def dict(self):
        return dict(
            user_id=self.user_id,
            content=self.content,
            author=self.author,
            created_at=self.created_at,
            joke_id=self.joke_id
        )


a = Jokes()
a.dict()
