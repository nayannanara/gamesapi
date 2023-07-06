from pydantic import BaseModel

from sqlalchemy.ext.asyncio import AsyncSession


async def insert_model(model: BaseModel, session: AsyncSession):
    try:
        session.add(model)
        await session.commit()
    except Exception as exc:
        await session.rollback()
        raise exc
    finally:
        await session.close()