from pstats import Stats
from requests import get

base_url = "http://data.nba.net"
all_json = "/prod/v1/today.json"

## Jogos de hoje
def get_links():
    response = get(base_url+all_json).json()
    return response["links"]

# print(get_links())

## Placar atual
def get_currentScoreboard():
    response = get(base_url+get_links()["currentScoreboard"]).json()
    games = response["games"]

    for games in games:
        time_de_casa = games["hTeam"]
        time_de_fora = games["vTeam"]
        clock = games["clock"]
        period = games["period"]

        print("##############################################\n")
        print(f"{time_de_casa['triCode']} vs {time_de_fora['triCode']}")
        print(f" SCORE: {time_de_casa['score']} x {time_de_fora['score']}")
        print(f"{clock} - {period['current']}\n")
    

#  print(get_currentScoreboard())


## Placar atual
def get_todayScoreboard():
    response = get(base_url+get_links()["todayScoreboard"]).json()
    games = response["games"]

    for games in games:
        time_de_casa = games["hTeam"]
        time_de_fora = games["vTeam"]
        clock = games["clock"]
        period = games["period"]

        print("##############################################\n")
        print(f"{time_de_casa['triCode']} vs {time_de_fora['triCode']}")
        print(f" SCORE: {time_de_casa['score']} x {time_de_fora['score']}")
        print(f"{clock} - {period['current']}\n")

# print(get_todayScoreboard())


## Status do time
def get_teams_status():
    stats = get_links()["leagueTeamStatsLeaders"]
    data = get(base_url+stats).json()
    teams = data["league"]["standard"]["regularSeason"]["teams"]

    teams =list(filter(lambda x: x["name"] != "team", teams))
    teams.sort(key = lambda x: x["ppg"]["rank"])

    for team in teams:
        team_name = team["name"]
        nickname = team["nickname"]
        ppg = team["ppg"]

        print(f"{team_name} - {nickname} | PPG: {ppg}")

print(get_teams_status())