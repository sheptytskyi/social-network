import typing as t
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from database.config import async_postgres_settings


DATABASE_URL = async_postgres_settings.db_url
engine = create_async_engine(
    DATABASE_URL
)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base: DeclarativeMeta = declarative_base()


async def get_async_session() -> t.AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
