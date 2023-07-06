import asyncio

from games_api.utils.log_parser import GameProcess
from games_api.configs.database import async_session


async def main():
    async with async_session() as session:
        game_process = GameProcess(session=session)
        await game_process.create_games()

asyncio.run(main())