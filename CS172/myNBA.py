from nba_api.stats.static import teams, players
from nba_api.stats.endpoints import CommonTeamRoster

players_dict = players.get_players()
teams_dict = teams.get_teams()



for player in players_dict:
    if player['is_active'] is True:
            print("\nPlayer: ", player['full_name'])
    


###
''''

for team in teams_dict:
    print("\n", team['full_name'], "in", team['city'])
'''

###


