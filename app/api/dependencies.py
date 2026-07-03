from collections.abc import Generator

from app.database.connection import get_session


def get_db() -> Generator:

    session = get_session()

    try:

        yield session

    finally:

        session.close()