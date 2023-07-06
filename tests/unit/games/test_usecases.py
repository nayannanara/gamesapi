import pytest

from games_api.games.schemas import GameSchema


@pytest.mark.usefixtures('database_games')
async def test_usecases_query_games_should_return_success(gameusecase, db_session):
    result = await gameusecase.query(db_session)
    
    assert isinstance(result[0], GameSchema)
    assert len(result) > 1


async def test_usecases_query_games_should_empty_list(gameusecase, db_session):
    result = await gameusecase.query(db_session)
    
    assert result == []