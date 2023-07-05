from games_api.contrib.dependencies import DatabaseDependency
from games_api.games.usecases import GameUseCase
from games_api.games.schemas import GameSchema

from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def query(
    db_session: DatabaseDependency,
    use_case: GameUseCase = Depends(),
) -> list[GameSchema]:
    games = await use_case.query(db_session=db_session)

    return games