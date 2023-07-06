import pytest
import sqlalchemy

from unittest import mock

from games_api.contrib.exceptions import DatabaseException
from games_api.games.models import GameModel, PlayerModel
from games_api.games.schemas import GameSchema, PlayerSchema


async def test_unit_logger_game_parser_return_list(game_process):
    games = game_process.logger_game_parser()
    for game in games:
        for _, value in game.items():
            assert 'total_kills' in value
            assert value['kills'].keys() == value['players']

    assert isinstance(games, list)


async def test_unit_get_games_schema(game_process):
    games_schema = game_process.get_games_schema()

    for game in games_schema:
        assert isinstance(game, GameSchema)
        assert isinstance(game.players[0], PlayerSchema)


async def test_unit_get_games_model(game_process, get_games_schema):
    games = get_games_schema

    for game in games:
        item = game_process.get_game_model(game)
        assert isinstance(item, GameModel)
        assert isinstance(item.players[0], PlayerModel)


@mock.patch('sqlalchemy.ext.asyncio.AsyncSession.commit')
async def test_unit_create_games(mock_commit, game_process):
    await game_process.create_games()


@mock.patch('sqlalchemy.ext.asyncio.AsyncSession.commit')
async def test_unit_create_games_should_return_raise(mock_commit, game_process):
    mock_commit.side_effect = sqlalchemy.exc.DBAPIError(
        mock.MagicMock(), mock.MagicMock(), mock.MagicMock()
    )

    with pytest.raises(DatabaseException) as exc:
        await game_process.create_games()

    assert isinstance(exc.value, DatabaseException)
    assert (
        'Ocorreu um erro ao inserir o dado no banco de dados.'
        in exc.value.message
    )