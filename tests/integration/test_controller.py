import pytest

from fastapi import status


@pytest.mark.usefixtures('database_games')
async def test_query_games_return_success(client, query_url):
    response = await client.get(query_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []
