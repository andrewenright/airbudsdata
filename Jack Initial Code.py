from ff_espn_api import League
from collections import defaultdict
import pandas as pd

league_idco = 939603
swid = '{8DB003CB-B59D-448B-B003-CBB59D948B39}'
espn_s2 = 'AEBYnsuof7DS%2FuIEltJhVhBvD1y0OCtQfGxitkOSjUs5a' \
          'TcFCI5f0O1ZcHZzeCxggpGhg86fF93xek%2FVoGVsGqVEhyI1C7x8S9na9' \
          'wiImfxAIFcuSeBowCc9baljuJtllv3A3vWhVmX8os3kxKraAVlg3mayrOu' \
          'cbGVa29SJh0XYIn5vfYCEHLN2DVEAKf4KBSYEhiyBp6VqqIcjXwS%2F8I%' \
          '2Bj8Uu%2FxgedlKrVJIl6BQivFkw8uJ8QDGfwDjRzHX1uk8sUWpZl1bpgp' \
          'nhwhCzyTqnb'

league18 = League(league_idco, 2018, espn_s2, swid)
league19 = League(league_idco, 2019, espn_s2, swid)

leagues = [league18, league19]

# =============================================================================
# aggregating points scored over 2 years
# =============================================================================

points = defaultdict(list)
for league in leagues:
    for w in range(1, league.settings.reg_season_count + 1):
        for match in range(0, int(league.settings.team_count/2)):
            m = league.scoreboard(w)[match]
            h = m.home_team.owner
            a = m.away_team.owner
            points[h].append(m.home_score)
            points[a].append(m.away_score)
dfpoints = pd.DataFrame(points)
print(dfpoints.head())
     

# =============================================================================
# aggregating power rankings over the 2 years
# =============================================================================
ranks = defaultdict(list)

for league in leagues:
    for w in range(1,16):
        for t in range(1, 13):
            rank = league.power_rankings(week = w)[t-1]
            owner = rank[1].owner
            ranks[owner].append(t)
dfranks = pd.DataFrame(ranks)
print(dfranks.head())


# =============================================================================
# finding names of whatever round pick you want for each team
# =============================================================================

l = defaultdict(list)
for league in leagues:
    for pick in range(12):
        owner = league.draft[pick].team.owner
        l[owner].append(league.draft[pick].playerName)
for key, value in l.items():
    print(key, value)


# =============================================================================
# finding category of player at year end on roster
# =============================================================================

print(league18.year)
print("\n")

for team in league18.teams:
    i = 0
    j = 0
    k = 0
    roster = team.roster
    for player in roster:
        if player.acquisitionType == 'TRADE':
            i += 1
        if player.acquisitionType == 'DRAFT':
            j += 1
        if player.acquisitionType == 'ADD':
            k += 1
    print(team.owner)
    print(str(j) + " Players from the Draft, " + str(k) + " Players off of waivers, and " + str(i) + " players from trades" + "\n")
