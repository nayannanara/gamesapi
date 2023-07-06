from games_api.contrib.dependencies import DatabaseDependency
from games_api.games.schemas import GameSchema
from games_api.games.models import GameModel

from sqlalchemy.sql import select


class GameUseCase:
    async def query(self: 'GameUseCase', db_session: DatabaseDependency) -> list[GameSchema]:   
        games = (await db_session.execute(select(GameModel))).scalars().all()

        return [GameSchema.from_orm(game) for game in games]
