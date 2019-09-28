from ff_espn_api import League

league_id = 939603
year = 2019
swid = '{6AB2CECC-9BA9-484A-8AD1-665122725A9F}'
espn_s2 = 'AEC1KU4z9AZ45%2BTMBhcPxCNUsILOcXsytMiYivHRGn' \
          '%2FEOSExocT8FdCfIrtcoLcrY7j98wxQPSBuGmOa%2BzZVy0ndGisCqPHt' \
          '%2B2lzDRDjuiBQKGStfnd54WYqIiFVSwi%2FIKGT0GwMyeWD9BPkLcee9T' \
          '%2BY5z1wZXjGxQuoNKCIlAPWdQIxBcPw2FkQX2G9NcZMnGLnNjn7PxlcIB' \
          'HVms71uGsFXnNHCCB9LZMgmcbRFEPwSkd9spgoS%2FS6jb5askfDE4SAyF' \
          'DOEfUjJecXYMkWQy3AE%2FwsJd66QK1YsV7uBV5iwA%3D%3D'

league = League(league_id, year, espn_s2, swid)

weekly_highest_team_score = 0
weekly_lowest_team_score = 0
weekly_highest_player_score = 0
biggest_blowout = 0
longest_win_streak = 0
longest_losing_streak = 0
highest_points_for = 0
lowest_points_for = 0
highest_points_against = 0
lowest_points_against = 0
greatest_season_point_differential = 0
lowest_season_point_differential = 0
most_waiver_wire_pickups = 0
most_transactions = 0
most_trades = 0
sixty_nine_club = 0
year_weekly_highest_team_score = 0
year_weekly_lowest_team_score = 0
year_weekly_highest_player_score = 0
year_biggest_blowout = 0
year_longest_win_streak = 0
year_longest_losing_streak = 0
year_highest_points_for = 0
year_lowest_points_for = 0
year_highest_points_against = 0
year_lowest_points_against = 0
year_greatest_season_point_differential = 0
year_lowest_season_point_differential = 0
year_most_waiver_wire_pickups = 0
year_most_transactions = 0
year_most_trades = 0


f = open("stats.txt", "w+")

output = "All Time Records\n" \
         "Weekly Highest Team Score - {weekly_highest_team_score}\n\n" \
         "Weekly Lowest Team Score - {weekly_lowest_team_score}\n\n" \
         "Weekly Highest Player Score - {weekly_highest_player_score}\n\n" \
         "Biggest Blowout - {biggest_blowout}\n\n" \
         "Longest Win Streak - {longest_win_streak}\n\n" \
         "Longest Losing Streak - {longest_losing_streak}\n\n" \
         "Highest Points For - {highest_points_for}\n\n" \
         "Lowest Points For - {lowest_points_for}\n\n" \
         "Highest Points Against - {highest_points_against}\n\n" \
         "Lowest Points Against - {lowest_points_against}\n\n" \
         "Greatest Season Point Differential - {greatest_season_point_differential}\n\n" \
         "Lowest Season Point Differential - {lowest_season_point_differential}\n\n" \
         "Most Waiver Wire Pickups - {most_waiver_wire_pickups}\n\n" \
         "Most Transactions - {most_transactions}\n\n" \
         "Most Trades - {most_trades}\n\n" \
         "69 Club - {sixty_nine_club}\n\n" \
         "2019 Records\n" \
         "Weekly Highest Team Score - {year_weekly_highest_team_score}\n\n" \
         "Weekly Lowest Team Score - {year_weekly_lowest_team_score}\n\n" \
         "Weekly Highest Player Score - {year_weekly_highest_player_score}\n\n" \
         "Biggest Blowout - {year_biggest_blowout}\n\n" \
         "Longest Win Streak - {year_longest_win_streak}\n\n" \
         "Longest Losing Streak - {year_longest_losing_streak}\n\n" \
         "Highest Points For - {year_highest_points_for}\n\n" \
         "Lowest Points For - {year_lowest_points_for}\n\n" \
         "Highest Points Against - {year_highest_points_against}\n\n" \
         "Lowest Points Against - {year_lowest_points_against}\n\n" \
         "Greatest Season Point Differential - {year_greatest_season_point_differential}\n\n" \
         "Lowest Season Point Differential - {year_lowest_season_point_differential}\n\n" \
         "Most Waiver Wire Pickups - {year_most_waiver_wire_pickups}\n\n" \
         "Most Transactions - {year_most_transactions}\n\n" \
         "Most Trades - {year_most_trades}\n\n" \
         "".format(weekly_highest_team_score=weekly_highest_team_score,
                   weekly_lowest_team_score=weekly_lowest_team_score,
                   weekly_highest_player_score=weekly_highest_player_score,
                   biggest_blowout=biggest_blowout,
                   longest_win_streak=longest_win_streak,
                   longest_losing_streak=longest_losing_streak,
                   highest_points_for=highest_points_for,
                   lowest_points_for=lowest_points_for,
                   highest_points_against=highest_points_against,
                   lowest_points_against=lowest_points_against,
                   greatest_season_point_differential=greatest_season_point_differential,
                   lowest_season_point_differential=lowest_season_point_differential,
                   most_waiver_wire_pickups=most_waiver_wire_pickups,
                   most_transactions=most_transactions,
                   most_trades=most_trades,
                   sixty_nine_club=sixty_nine_club,
                   year_weekly_highest_team_score=year_weekly_highest_team_score,
                   year_weekly_lowest_team_score=year_weekly_lowest_team_score,
                   year_weekly_highest_player_score=year_weekly_highest_player_score,
                   year_biggest_blowout=year_biggest_blowout,
                   year_longest_win_streak=year_longest_win_streak,
                   year_longest_losing_streak=year_longest_losing_streak,
                   year_highest_points_for=year_highest_points_for,
                   year_lowest_points_for=year_lowest_points_for,
                   year_highest_points_against=year_highest_points_against,
                   year_lowest_points_against=year_lowest_points_against,
                   year_greatest_season_point_differential=year_greatest_season_point_differential,
                   year_lowest_season_point_differential=year_lowest_season_point_differential,
                   year_most_waiver_wire_pickups=year_most_waiver_wire_pickups,
                   year_most_transactions=year_most_transactions,
                   year_most_trades=year_most_trades)


f.write(output)
