from fastapi import APIRouter

from games_api.games import controller as games

api_router = APIRouter()

api_router.include_router(
    games.router, prefix='/games', tags=['games']
)
