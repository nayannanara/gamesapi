from pydantic import Field

from games_api.contrib.schemas import BaseSchema


class PlayerSchema(BaseSchema):
    name: str = Field(title='Player name', example='Isgalamido')


class GameSchema(BaseSchema):
    name: str = Field(..., title='Game Name', example='game_1')
    players: list[PlayerSchema] = Field(
        ..., title='Game players', example=["Dono da bola", "Isgalamido", "Zeh"]
    )
    total_kills: int = Field(..., title='Kills count', example=45)
    kills: dict[str, int] = Field(..., title='Kills', example={
        "Dono da bola": 5,
        "Isgalamido": 18,
        "Zeh": 20
    })
