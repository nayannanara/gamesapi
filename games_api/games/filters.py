from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter
from fastapi_filter.base.filter import FilterDepends, with_prefix


class PlayerFilter(Filter):
    name: Optional[str]


class GameFilter(Filter):
    player: Optional[PlayerFilter] = FilterDepends(with_prefix("player", PlayerFilter))
    