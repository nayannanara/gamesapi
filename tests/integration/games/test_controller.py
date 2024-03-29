import pytest

from fastapi import status


@pytest.mark.usefixtures('database_games')
async def test_integration_query_games_return_success(client, query_url):
    response = await client.get(query_url)
    content = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert content['items'][0] == {'name': 'game_1', 'players': [{'name': 'Isgalamido'}], 'total_kills': 0, 'kills': {'Isgalamido': 0}}


async def test_integration_query_games_return_empty_list(client, query_url):
    response = await client.get(query_url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'items': [], 'total': 0, 'limit': 50, 'offset': 0}


@pytest.mark.usefixtures('database_games')
async def test_integration_query_with_query_params_games_return_success(client, query_url):
    response = await client.get(query_url, params={'player__name': 'zeh', 'limit': 2})
    content = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert content['total'] > 1