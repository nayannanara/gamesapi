import pytest

from fastapi import status


@pytest.mark.usefixtures('database_games')
async def test_integration_query_games_return_success(client, query_url):
    response = await client.get(query_url)
    content = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert content[0] == {'name': 'game_1', 'players': [{'name': 'Isgalamido'}], 'total_kills': 0, 'kills': {'Isgalamido': 0}}


async def test_integration_query_games_return_empty_list(client, query_url):
    response = await client.get(query_url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []
