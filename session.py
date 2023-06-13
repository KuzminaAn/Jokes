from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from table import Jokes

main_engine = sa.create_engine(
    'postgresql://postgres:@127.0.0.1:5432/project'
)

DBSSession = sessionmaker(
    bind=main_engine,
    expire_on_commit=False,
)


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations"""
    session = DBSSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

    