from typing import AsyncGenerator
import sqlalchemy

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from games_api.configs.settings import settings

engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


async def insert_stmt(stmt):
    async with async_session() as session:
        try:
            async with session.begin():
                session.add(stmt)
                await session.flush()
                await session.refresh(stmt)
        except sqlalchemy.exc.DBAPIError as exc:
            error = str(exc.__cause__)
            await session.rollback()
            raise RuntimeError(error) from exc
        finally:
            await session.close()