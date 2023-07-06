import pytest


@pytest.mark.usefixtures('database_games')
async def test_usecases_query_games_should_return_success(gameusecase, db_session):
    result = await gameusecase.query(db_session)