from games_api.configs.database import get_session
from games_api.games.schemas import GameSchema
from games_api.games.models import GameModel

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select


class GameUseCase:
    async def query(
        self: 'GameUseCase', db_session: AsyncSession = Depends(get_session)
    ) -> list[GameSchema]:
        games = (await db_session.execute(select(GameModel))).scalars().all()
        
        return [GameSchema.from_orm(game) for game in games]
