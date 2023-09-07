from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from src.app.schemas import config

engine = "{}://{}:@{}:{}/{}".format(
    config.db.database,
    config.db.user,
    config.db.host,
    config.db.port,
    config.db.name,
)

main_engine = sa.create_engine(engine)

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
