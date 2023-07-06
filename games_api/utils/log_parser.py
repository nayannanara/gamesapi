import re
import sqlalchemy

from games_api.configs.transaction import insert_model
from games_api.contrib.dependencies import DatabaseDependency

from games_api.contrib.exceptions import DatabaseException
from games_api.games.models import GameModel, PlayerModel
from games_api.games.schemas import GameSchema, PlayerSchema


class GameProcess:
    def __init__(self: 'GameProcess', session: DatabaseDependency = DatabaseDependency) -> None:
        self.session = session


    def logger_game_parser(self: 'GameProcess'):
        with open("games.log") as f:
            lines = f.readlines()

            game_n = 0
            games = {}

            for line in lines:
                if "InitGame" in line:
                    game_n += 1
                    games[f"game_{game_n}"] = {"total_kills": 0, 'players': set(), 'kills': {}}
                
                players = re.search(r'n\\(.*?)\\t', line)

                if players:
                    games[f"game_{game_n}"]["players"].add(players.string.split('\\')[1])
                
                    for player in games[f"game_{game_n}"]["players"]:
                        if player not in games[f"game_{game_n}"]["kills"]:
                            games[f"game_{game_n}"]["kills"][player] = 0

                if "Kill" in line:
                    games[f"game_{game_n}"]["total_kills"] += 1
                    players_split = line.split('killed')

                    player_win = players_split[0].split(':')[-1].strip()
                    player_lose = players_split[1].split('by')[0].strip()

                    if player_win != '<world>':
                        games[f"game_{game_n}"]["kills"][player_win] += 1
                    
                    games[f"game_{game_n}"]["kills"][player_lose] -= 1

        return [games]

    
    def get_games_schema(self: 'GameProcess'):
        games = self.logger_game_parser()
        games_schema = []

        for game in games:
            games_schema = [
                GameSchema(
                    name=key, 
                    total_kills=value['total_kills'], 
                    kills=value['kills'], 
                    players=[PlayerSchema(name=player) for player in value['players']]
                ) 
                for key, value in game.items()
            ]
        
        return games_schema

    
    def get_game_model(self: 'GameProcess', game):
        return GameModel(**game.dict(exclude={'players'}), 
            players=[
                PlayerModel(**player.dict())
                for player in game.players
            ]
        )


    async def create_games(self: 'GameProcess'):
        games_schema = self.get_games_schema()

        try:
            for game in games_schema:
                await insert_model(model=self.get_game_model(game), session=self.session)
        except sqlalchemy.exc.DBAPIError:
            raise DatabaseException(
                message='Ocorreu um erro ao inserir o dado no banco de dados.'
            )