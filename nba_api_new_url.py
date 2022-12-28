from datetime import datetime, timezone
from dateutil import parser
from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore
import pandas as pd

# String com formato do placar de hoje {Today}
f = "{gameId}: {awayTeam} vs. {homeTeam} @ {gameTimeLTZ}"

board = scoreboard.ScoreBoard()
print("ScoreBoardDate: " + board.score_board_date)

# Games de hoje
games = board.games.get_dict()

print(games)

# Retorno formatado em texto com as seguintes variáveis: ( ID do Jogo, Nome Time Visitante, Nome Time da Casa e Horário do jogo )
for game in games:
    gameTimeLTZ = parser.parse(game["gameTimeUTC"]).replace(tzinfo=timezone.utc).astimezone(tz=None)
    print(f.format(gameId=game["gameId"], awayTeam=game["awayTeam"]["teamName"], homeTeam=game["homeTeam"]["teamName"], gameTimeLTZ=gameTimeLTZ),"\n")

# Retorno formatado em tabela

gameIdEscolhido = '0022200513'

box = boxscore.BoxScore(gameIdEscolhido) # GameID

# Pontuações de cestas 
# Nota: home_team e away_team têm estrutura de dados idêntica.
players = box.away_team.get_dict()['players']
f = "{player_id}: {name}: {points} PTS"
print("##################################################################################################")
print("Jogadores e pontos do time visitante -", box.game.data['awayTeam']['teamName'],"\n")
for player in players:
    print(f.format(player_id=player['personId'],name=player['name'],points=player['statistics']['points']))

print("##################################################################################################")
print("Jogadores e pontos do time da casa -", box.game.data['homeTeam']['teamName'],"\n")
players = box.home_team.get_dict()['players']
f = "{player_id}: {name}: {points} PTS"
for player in players:
    print(f.format(player_id=player['personId'],name=player['name'],points=player['statistics']['points']))