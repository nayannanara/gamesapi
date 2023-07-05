from typing import Type, TypeVar
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from games_api.contrib.models import BaseModel
from games_api.games.schemas import GameSchema

TYPE_GAME_MODEL = TypeVar('TYPE_GAME_MODEL', bound='GameModel')


class PlayerModel(BaseModel):
    __tablename__ = 'players'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    game: Mapped['GameModel'] = relationship(
        'GameModel', back_populates='players'
    )


class GameModel(BaseModel):
    __tablename__ = 'games'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    player_pk_id: Mapped[int] = mapped_column(ForeignKey("players.pk_id"))
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    total_kills: Mapped[int] = mapped_column(Integer, nullable=False)
    kills: Mapped[dict[str, int]] = mapped_column(JSON)
    players: Mapped[list['PlayerModel']] = relationship(back_populates='game', lazy='selectin', uselist=True)
