from games_api.contrib.dependencies import DatabaseDependency

from games_api.games.usecases import GameUseCase
from games_api.games.schemas import GameSchema
from games_api.games.filters import GameFilter

from fastapi import APIRouter, Depends, Query, status
from fastapi_pagination import LimitOffsetPage, paginate
from fastapi_filter.base.filter import FilterDepends

router = APIRouter()

@router.get('/', response_model=LimitOffsetPage[GameSchema], status_code=status.HTTP_200_OK)
async def query(
    session: DatabaseDependency,
    use_case: GameUseCase = Depends(),
    limit: int = Query(100, ge=0),
    offset: int = Query(0, ge=0),
    filters: GameFilter = FilterDepends(GameFilter)
) -> LimitOffsetPage[GameSchema]:
    games = await use_case.query(
        session=session, 
        limit=limit, 
        offset=offset, 
        filters=filters
    )
    
    return paginate(games)