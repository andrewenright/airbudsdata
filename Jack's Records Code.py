from ff_espn_api import League
from collections import defaultdict

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
# Biggest Blowout and PPG
# =============================================================================

margin = 0
winner = ''
loser = ''
winnerscore = 0
loserscore = 0

points = defaultdict(list)

for league in leagues:
    for w in range(1, league.settings.reg_season_count + 1):
        for match in range(0, int(league.settings.team_count/2)):
            m = league.scoreboard(w)[match]
            if m.home_score != 0:
                h = m.home_team.owner
                a = m.away_team.owner
                points[h].append(m.home_score)
                points[a].append(m.away_score)
                if abs(m.home_score - m.away_score) > margin:
                    margin = abs(m.home_score - m.away_score)
                    if m.home_score > m.away_score:
                        winner = m.home_team.owner
                        loser = m.away_team.owner
                        winnerscore = m.home_score
                        loserscore = m.away_score
                    else:
                        winner = m.away_team.owner
                        loser = m.home_team.owner
                        winnerscore = m.away_score
                        loserscore = m.home_score

# variables to use: winner, loser, winnerscore, loserscore, margin

# below is for PPG calculations:

game_averages = defaultdict(float)
for key, value in points.items():
    game_averages[key] = sum(value)/len(value)

# max points per game
maxppgowner = max(game_averages, key=game_averages.get)
maxppg = game_averages[maxppgowner]

# min points per game
minppgowner = min(game_averages, key=game_averages.get)
minppg = game_averages[minppgowner]

# variables to use: maxppgowner, maxppg, minppgowner, minppg

# =============================================================================
# Finding Max, Min for Points For, Points Against, and Differential
# =============================================================================

season_points_for = defaultdict(list)
season_points_against = defaultdict(list)
season_point_diff = defaultdict(list)

for league in leagues:
    yr = league.year
    for team in league.teams:
        pf = team.points_for
        pa = team.points_against
        diff = pf - pa
        owner = team.owner
        season_points_for[owner].append([yr,pf])
        season_points_against[owner].append([yr,pa])
        season_point_diff[owner].append([yr,diff])
        
# max points for in a season
maxpfsowner = ''
maxpfs = 0
maxpfsyr = 0
# min points for in a season
minpfsowner = ''
minpfs = 10000
minpfsyr = 0
# max points against in a season
maxpasowner = ''
maxpas = 0
maxpasyr = 0
# min points against in a season
minpasowner = ''
minpas = 10000
minpasyr = 0
# max differential in a season
maxdiffowner = ''
maxdiff = 0
maxdiffyr = 0
# min differential in a season
mindiffowner = ''
mindiff = 0
mindiffyr = 0

for key, value in season_points_for.items():
    if value[1] > maxpfs:
        maxpfsowner = key
        maxpfs = value[1]
        maxpfsyr = value[0]
    if value[1] < minpfs:
        minpfsowner = key
        minpfs = value[1]
        minpfsyr = value[0]

for key, value in season_points_against.items():
    if value[1] > maxpas:
        maxpasowner = key
        maxpas = value[1]
        maxpasyr = value[0]
    if value[1] < minpas:
        minpasowner - key
        minpas = value[1]
        minpasyr = value[0]

for key, value in season_point_diff.items():
    if value[1] > maxdiff:
        maxdiffowner = key
        maxdiff = value[1]
        maxdiffyr = value[0]
    if value[1] < mindiff:
        mindiffowner = key
        mindiff = value[1]
        mindiffyr = value[0]
       
# variables to use (max/min)(pfs/pas/diff)(owner/ /yr)
