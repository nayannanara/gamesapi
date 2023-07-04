from games_api.configs.database import get_session

from games_api.games.usecases import GameUseCase
from games_api.games.schemas import GameSchema

from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def query(
    use_case: GameUseCase = Depends(),
    db_session: AsyncSession = Depends(get_session),
) -> list[GameSchema]:
    games = await use_case.query(db_session=db_session)

    return games