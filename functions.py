from sqlalchemy import select, update, delete
from session import session_scope
from table import Jokes


def get_jokes_by_user(user_id):
    stmt = select(Jokes).where(Jokes.user_id == user_id)
    with session_scope() as s:
        result = s.execute(stmt).scalars().all()
    return result


def get_jokes_by_id(joke_id):
    stmt = select(Jokes).where(Jokes.joke_id == joke_id)
    with session_scope() as s:
        result = s.execute(stmt).scalar()
    return result


def create_jokes(user_id, joke_content, joke_author, created_at):
    joke = Jokes(user_id=user_id, content=joke_content, author=joke_author, created_at=created_at)
    with session_scope() as s:
        s.add(joke)
        s.flush()
        result = s.execute(select(Jokes).where(Jokes.joke_id == joke.joke_id)).scalar()
    return result


def update_jokes(joke_content, joke_author, joke_id):
    stmt = update(Jokes).values(content=joke_content, author=joke_author).where(Jokes.joke_id == joke_id)
    with session_scope() as s:
        s.execute(stmt)
    return get_jokes_by_id(joke_id)


def delete_jokes(joke_id):
    stmt = delete(Jokes).where(Jokes.joke_id == joke_id)
    with session_scope() as s:
        result = s.execute(stmt)
    return result
