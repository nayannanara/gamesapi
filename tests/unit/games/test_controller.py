import pytest

from fastapi import status


@pytest.mark.usefixtures('mock_usecase_query_games')
async def test_unit_query_games_return_success(client, query_url):
    response = await client.get(query_url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "name":"game_1",
            "players":[
                {
                    "name":"Isgalamido"
                }
            ],
            "total_kills": 1,
            "kills":{
                "Isgalamido":0
            }
        }
    ]


async def test_unit_query_games_return_empty_list(client, query_url):
    response = await client.get(query_url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []