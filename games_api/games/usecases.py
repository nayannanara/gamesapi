from games_api.contrib.dependencies import DatabaseDependency
from games_api.games.schemas import GameSchema
from games_api.games.models import GameModel

from sqlalchemy.sql import select


class GameUseCase:
    async def query(
            self: 'GameUseCase', 
            session: DatabaseDependency, 
            limit: int | None = None, 
            offset: int | None = None
        ) -> list[GameSchema]:   
        games = (await session.execute(select(GameModel).limit(limit).offset(offset))).scalars().all()

        return [GameSchema.from_orm(game) for game in games]
