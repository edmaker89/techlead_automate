from collections.abc import Generator

from teachlead.db.session import SessionLocal


def get_db() -> Generator:
    with SessionLocal() as session:
        yield session
