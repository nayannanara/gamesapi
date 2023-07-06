
from pydantic import BaseModel
import pytest
import sqlalchemy

from unittest import mock

from games_api.configs.database import insert_stmt
from games_api.games.models import GameModel


@mock.patch('sqlalchemy.ext.asyncio.AsyncSession.commit')
async def test_unit_insert_stmt(mock_commit, game_model):
    mock_commit.side_effect = sqlalchemy.exc.DBAPIError(
        mock.MagicMock(), mock.MagicMock(), mock.MagicMock()
    )
    game_model.total_kills = '45'

    with pytest.raises(RuntimeError) as exc:
        await insert_stmt(game_model)

    assert isinstance(exc.value, RuntimeError)
    assert 'invalid input for query argument' in exc.value.args[0]