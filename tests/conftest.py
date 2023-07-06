import asyncio
import pytest

from typing import AsyncGenerator, Callable, Generator

from fastapi import FastAPI
from httpx import AsyncClient
from pytest_mock import MockerFixture
from sqlalchemy.ext.asyncio.session import AsyncSession

from games_api.configs.database import async_session, engine, get_session
from games_api.contrib.models import BaseModel
from games_api.utils.log_parser import GameProcess
from games_api.games.models import GameModel, PlayerModel
from games_api.games.usecases import GameUseCase

from tests.factories import minimal_game

from .fixture_package.routers import routers as fixture_routers


@pytest.fixture(scope='session')
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def db_session() -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.drop_all)
        await connection.run_sync(BaseModel.metadata.create_all)

        async with async_session(bind=connection) as session:
            yield session
            await session.flush()
            await session.rollback()


@pytest.fixture
def database(db_session: AsyncSession) -> Callable:
    async def _database():
        yield db_session

    return _database


@pytest.fixture
def app(database: Callable) -> FastAPI:
    from games_api.main import app

    app.dependency_overrides[get_session] = database

    return app


@pytest.fixture
async def client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url='http://games') as ac:
        yield ac


@pytest.fixture
def routers():
    return fixture_routers


@pytest.fixture
def query_url():
    return 'api/v0/games/'


@pytest.fixture
def game_process():
    return GameProcess()


@pytest.fixture
def gameusecase():
    return GameUseCase()


@pytest.fixture
async def database_games(game_process, db_session):
    await game_process.create_games(session=db_session)


@pytest.fixture
async def mock_get_games_schema(mocker: MockerFixture):
    return mocker.patch.object(
        GameProcess, 'logger_game_parser', return_value=minimal_game()
    )


@pytest.fixture
def get_games_schema(mock_get_games_schema, game_process):
    return game_process.get_games_schema()


@pytest.fixture
async def game_model(get_games_schema):    
    game = get_games_schema[0]
    
    return GameModel(**game.dict(exclude={'players'}), 
            players=[
                PlayerModel(**player.dict())
                for player in game.players
            ]
        )


@pytest.fixture
async def mock_usecase_query_games(mocker: MockerFixture, get_games_schema):
    return mocker.patch.object(GameUseCase, 'query', return_value=get_games_schema)