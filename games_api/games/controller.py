from games_api.contrib.dependencies import DatabaseDependency

from games_api.games.usecases import GameUseCase
from games_api.games.schemas import GameSchema

from fastapi import APIRouter, Depends, Query, status
from fastapi_pagination import LimitOffsetPage, paginate
 
router = APIRouter()

@router.get('/', response_model=LimitOffsetPage[GameSchema], status_code=status.HTTP_200_OK)
async def query(
    session: DatabaseDependency,
    use_case: GameUseCase = Depends(),
    limit: int = Query(100, ge=0),
    offset: int = Query(0, ge=0)
) -> LimitOffsetPage[GameSchema]:
    games = await use_case.query(session=session, limit=limit, offset=offset)
    
    return paginate(games)