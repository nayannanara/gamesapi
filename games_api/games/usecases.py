from sqlalchemy import func

from games_api.contrib.dependencies import DatabaseDependency

from games_api.games.schemas import GameSchema
from games_api.games.models import GameModel, PlayerModel

from sqlalchemy.sql import select
from fastapi_filter.contrib.sqlalchemy import Filter

class GameUseCase:
    async def query(
            self: 'GameUseCase', 
            session: DatabaseDependency, 
            limit: int | None = None, 
            offset: int | None = None,
            filters: Filter | None = None
        ) -> list[GameSchema]:
        query = select(GameModel).limit(limit).offset(offset)
        
        if filters:
            filters_dict = filters.dict()

            player = filters_dict.pop('player')
            player_name = player['name']
        
            query = select(GameModel).filter_by(**filters_dict)

            if player_name:
                query = query.join(PlayerModel).filter(func.lower(PlayerModel.name)==player_name)

        games = (await session.execute(query)).scalars().all()

        return [GameSchema.from_orm(game) for game in games]
