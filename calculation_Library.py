import mysql.connector
from mysql.connector import Error
from main_Library import *

from decimal import Decimal

def getMLBCalc(*args):
    
    
    
    playerName = ""
    teamName = ""
    
    # Pitcher or Batter
    category = args[1]
    
    userChoices = []
    statsToReturn = []
    
    teamNames = ["Arizona Diamondbacks", "Atlanta Braves", "Baltimore Orioles", "Boston Red Sox", "Chicago Cubs", "Chicago White Sox", "Cincinnati Reds", "Cleveland Guardians", "Colorado Rockies",
                 "Colorado Rockies","Detroit Tigers", "Houston Astros", "Kansas City Royals", "Los Angeles Angels", "Los Angeles Dodgers", "Miami Marlins", "Milwaukee Brewers", "Minnesota Twins",
                 "New York Mets", "New York Yankees", "Oakland Athletics", "Philadelphia Phillies", "Pittsburgh Pirates", "San Diego Padres", "Seattle Mariners", "San Francisco Giants",
                 "St. Louis Cardinals", "Tampa Bay Rays", "Texas Rangers", "Toronto Blue Jays", "Washington Nationals"]
    
    game_Time_Types = ["Day", "Night"]
    game_Time = ""
    
    vsArms = ["L", "R"]
    vsArm = ""
    
    
    if args[0] in teamNames:
        
        teamName = args[0]
        
        if args[2] in game_Time_Types:
            
            game_Time = args[2]
            
            for choice in args[3:]:
                
                userChoices.append(choice)
       
        
    else:
        
        playerName = args[0]
        
    
    
    if args[2] in teamNames:
        
        teamName = args[2]
        
        
        if args[3] in game_Time_Types:
            
            game_Time = args[3]
            
            for choice in args[4:]:
                userChoices.append(choice)
        
        else:
            
            for choice in args[3:]:
    
                userChoices.append(choice)
                
    elif args[2] in game_Time_Types:
        
        game_Time = args[2]
        
        if args[3] in vsArms:
            
            vsArm = args[3]
            
            for choice in args[4:]:
        
                userChoices.append(choice)
        
        else:
            for choice in args[3:]:
        
                userChoices.append(choice)
    else:       
        for choice in args[2:]:
        
            userChoices.append(choice)
        
        
    #___________________________________________________________________________ 
    # Pitcher Calculation Options
    
    #Pitcher Total Calculations
    PITCHER_CALC_K9 = "Pitcher_Calc_K9"
    PITCHER_CALC_INNINGSPERGAME = "Pitcher_Calc_InningsPerGame"
    PITCHER_CALC_HR9 = "Pitcher_Calc_HR9"
    PITCHER_CALC_BB9 = "Pitcher_Calc_BB9"
    
    #Pitcher Home Calculations
    PITCHER_CALCHOME_K9 = "Pitcher_CalcHome_K9"
    PITCHER_CALCHOME_INNINGSPERGAME = "Pitcher_CalcHome_InningsPerGame"
    PITCHER_CALCHOME_ERA = "Pitcher_CalcHome_ERA"
    PITCHER_CALCHOME_WHIP = "Pitcher_CalcHome_WHIP"
    PITCHER_CALCHOME_HR9 = "Pitcher_CalcHome_HR9"
    PITCHER_CALCHOME_BB9 = "Pitcher_CalcHome_BB9"
    
    #Pitcher Away Calculations
    PITCHER_CALCAWAY_K9 = "Pitcher_CalcAway_K9"
    PITCHER_CALCAWAY_INNINGSPERGAME = "Pitcher_CalcAway_InningsPerGame"
    PITCHER_CALCAWAY_ERA = "Pitcher_CalcAway_ERA"
    PITCHER_CALCAWAY_WHIP = "Pitcher_CalcAway_WHIP"
    PITCHER_CALCAWAY_HR9 = "Pitcher_CalcAway_HR9"
    PITCHER_CALCAWAY_BB9 = "Pitcher_CalcAway_BB9"
    
    #Pitcher Day Calculations
    PITCHER_CALCDAY_K9 = "Pitcher_CalcDay_K9"
    PITCHER_CALCDAY_INNINGSPERGAME = "Pitcher_CalcDay_InningsPerGame"
    PITCHER_CALCDAY_HR9 = "Pitcher_CalcDay_HR9"
    PITCHER_CALCDAY_BB9 = "Pitcher_CalcDay_BB9"
    
    #Pitcher Night Calculations
    PITCHER_CALCNIGHT_K9 = "Pitcher_CalcNight_K9"
    PITCHER_CALCNIGHT_INNINGSPERGAME = "Pitcher_CalcNight_InningsPerGame"
    PITCHER_CALCNIGHT_HR9 = "Pitcher_CalcNight_HR9"
    PITCHER_CALCNIGHT_BB9 = "Pitcher_CalcNight_BB9"
    
    #Pitcher Combined Calculations
    
    
    
    
    
    #___________________________________________________________________________ 
    #--Batter Stat Calculations--
    
    #--Batter Home Calculations--
    BATTER_CALCHOME_BATTINGAVG = "Batter_CalcHome_BattingAVG"
    
    
    #--Batter away Calculations--
    BATTER_CALCAWAY_BATTINGAVG = "Batter_CalcAway_BattingAVG"
    
    #___________________________________________________________________________ 
    #--Team Stat Calculations--
    
    #Team calculated home per game stats
    TEAM_CALCHOME_RUNSPERGAME = "Team_CalcHome_RunsPerGame"
    
    #Team calculated home per game stats
    TEAM_CALCAWAY_RUNSPERGAME = "Team_CalcAway_RunsPerGame"
    
    
    #--Team Total At Bat Percentages
    TEAM_ATBAT_STRIKEOUTPERC = "Team_AtBat_StrikeoutPerc"
    TEAM_ATBAT_HITPERC = "Team_AtBat_HitPerc"
    
 
    #--Team Home At Bat Percentages
    TEAM_ATBATHOME_STRIKEOUTPERC = "Team_AtBatHome_StrikeoutPerc"
    TEAM_ATBATHOME_HITPERC = "Team_AtBatHome_HitPerc"
    
    TEAM_CALC_ATBATHOME_STRIKEOUTPERC = "Team_Calc_AtBatHome_StrikeoutPerc"
    TEAM_CALC_ATBATHOME_HITPERC = "Team_Calc_AtBatHome_HitPerc"
    
    #--Team Away At Bat Percentages
    TEAM_ATBATAWAY_STRIKEOUTPERC = "Team_AtBatAway_StrikeoutPerc"
    TEAM_ATBATAWAY_HITPERC = "Team_AtBatAway_HitPerc"
    
    TEAM_CALC_ATBATAWAY_STRIKEOUTPERC = "Team_Calc_AtBatAway_StrikeoutPerc"
    TEAM_CALC_ATBATAWAY_HITPERC = "Team_Calc_AtBatAway_HitPerc"
    
    #--Team Day At Bat Percentages
    TEAM_ATBATDAY_STRIKEOUTPERC = "Team_AtBatDay_StrikeoutPerc"
    TEAM_ATBATDAY_HITPERC = "Team_AtBatDay_HitPerc"
    
    #--Team Night At Bat Percentages
    TEAM_ATBATNIGHT_STRIKEOUTPERC = "Team_AtBatNight_StrikeoutPerc"
    TEAM_ATBATNIGHT_HITPERC = "Team_AtBatNight_HitPerc"
    
    #--Team Total Averages--
    TEAM_PERGAME_AVERAGE_STRIKEOUTS = "Team_PerGame_Average_Strikeouts"
    TEAM_PERGAME_AVERAGE_HITS = "Team_PerGame_Average_Hits"
    TEAM_PERGAME_AVERAGE_RUNS = "Team_PerGame_Average_Runs"
    
    #--Team Home Averages--
    TEAM_PERGAMEHOME_AVERAGE_STRIKEOUTS = "Team_PerGameHome_Average_Strikeouts"
    TEAM_PERGAMEHOME_AVERAGE_HITS = "Team_PerGameHome_Average_Hits"
    TEAM_PERGAMEHOME_AVERAGE_RUNS = "Team_PerGameHome_Average_Runs"
    
    TEAM_CALCHOME_BATTINGAVG = "Team_CalcHome_BattingAVG"
    
    #--Team Away Averages--
    TEAM_PERGAMEAWAY_AVERAGE_STRIKEOUTS = "Team_PerGameAway_Average_Strikeouts"
    TEAM_PERGAMEAWAY_AVERAGE_HITS = "Team_PerGameAway_Average_Hits"
    TEAM_PERGAMEAWAY_AVERAGE_RUNS = "Team_PerGameAway_Average_Runs"
    
    TEAM_CALCAWAY_BATTINGAVG = "Team_CalcAway_BattingAVG"
    
    #--Team Day Averages--
    TEAM_PERGAMEDAY_AVERAGE_STRIKEOUTS = "Team_PerGameDay_Average_Strikeouts"
    TEAM_PERGAMEDAY_AVERAGE_HITS = "Team_PerGameDay_Average_Hits"
    TEAM_PERGAMEDAY_AVERAGE_RUNS = "Team_PerGameDay_Average_Runs"
    
    #--Team Night Averages--
    TEAM_PERGAMENIGHT_AVERAGE_STRIKEOUTS = "Team_PerGameNight_Average_Strikeouts"
    TEAM_PERGAMENIGHT_AVERAGE_HITS = "Team_PerGameNight_Average_Hits"
    TEAM_PERGAMENIGHT_AVERAGE_RUNS = "Team_PerGameNight_Average_Runs"
    
    #___________________________________________________________________________ 
    #--Team Stat Calculations--
    
    #--League Total Averages--
    LEAGUE_PERGAME_AVERAGE_STRIKEOUTS = "League_PerGame_Average_Strikeouts"
    LEAGUE_PERGAME_AVERAGE_HITS = "League_PerGame_Average_Hits"
    LEAGUE_PERGAME_AVERAGE_RUNS = "League_PerGame_Average_Runs"
    
    #--League Home Averages--
    LEAGUE_PERGAMEHOME_AVERAGE_STRIKEOUTS = "League_PerGameHome_Average_Strikeouts"
    LEAGUE_PERGAMEHOME_AVERAGE_HITS = "League_PerGameHome_Average_Hits"
    LEAGUE_PERGAMEHOME_AVERAGE_RUNS = "League_PerGameHome_Average_Runs"
    
    LEAGUE_CALCHOME_RUNSPERGAME = "League_CalcHome_RunsPerGame"
    
    #--League Away Averages--
    LEAGUE_PERGAMEAWAY_AVERAGE_STRIKEOUTS = "League_PerGameAway_Average_Strikeouts"
    LEAGUE_PERGAMEAWAY_AVERAGE_HITS = "League_PerGameAway_Average_Hits"
    LEAGUE_PERGAMEAWAY_AVERAGE_RUNS = "League_PerGameAway_Average_Runs"
    
    LEAGUE_CALCAWAY_RUNSPERGAME = "League_CalcAway_RunsPerGame"
    
    #--League Day Averages--
    LEAGUE_PERGAMEDAY_AVERAGE_STRIKEOUTS = "League_PerGameDay_Average_Strikeouts"
    LEAGUE_PERGAMEDAY_AVERAGE_HITS = "League_PerGameDay_Average_Hits"
    LEAGUE_PERGAMEDAY_AVERAGE_RUNS = "League_PerGameDay_Average_Runs"
    
    #--League Night Averages--
    LEAGUE_PERGAMENIGHT_AVERAGE_STRIKEOUTS = "League_PerGameNight_Average_Strikeouts"
    LEAGUE_PERGAMENIGHT_AVERAGE_HITS = "League_PerGameNight_Average_Hits"
    LEAGUE_PERGAMENIGHT_AVERAGE_RUNS = "League_PerGameNight_Average_Runs"
    
    
    
    
    
    if category == "Pitcher":
        
        pitcherStat_Count = 0
        
        for stat in userChoices:
            connection = create_connection("mlb_stats")
            # Pitcher Total Calculations
            
            if userChoices[pitcherStat_Count] == PITCHER_CALC_K9:
                    
                    total_strikeouts = get_statData(connection, playerName, "pitcher_total_stats", "Strikeouts")
                    total_inningsPitched = get_statData(connection, playerName, "pitcher_total_stats", "Innings_Pitched")
                    
                    k9 = (total_strikeouts/total_inningsPitched)*9
                    
                    statsToReturn.append(round(k9,2))
                    
            elif userChoices[pitcherStat_Count] == PITCHER_CALC_INNINGSPERGAME:
                
                total_inningsPitched = get_statData(connection, playerName, "pitcher_total_stats", "Innings_Pitched")
                total_Games = get_statData(connection, playerName, "pitcher_total_stats", "Games_Played")
                
                inningsPerGame = total_inningsPitched/total_Games
                
                statsToReturn.append(round(inningsPerGame,2))
            
            elif userChoices[pitcherStat_Count] == PITCHER_CALC_HR9:
                
                total_inningsPitched = get_statData(connection, playerName, "pitcher_total_stats", "Innings_Pitched")
                total_HomeRuns = get_statData(connection, playerName, "pitcher_total_stats", "HomeRuns")
                
                HR9 = (total_HomeRuns/total_inningsPitched) * 9
                
                statsToReturn.append(round(HR9,2))
 
            elif userChoices[pitcherStat_Count] == PITCHER_CALC_BB9:
                
                total_inningsPitched = get_statData(connection, playerName, "pitcher_total_stats", "Innings_Pitched")
                total_Walks = get_statData(connection, playerName, "pitcher_total_stats", "Walks")
                
                BB9 = (total_Walks/total_inningsPitched) * 9
                
                statsToReturn.append(round(BB9,2))
                           
            # Pitcher Home Calculations
              
            elif userChoices[pitcherStat_Count] == PITCHER_CALCHOME_K9:
                
                total_strikeouts = get_statData(connection, playerName, "pitcher_home_stats", "Strikeouts")
                total_inningsPitched = get_statData(connection, playerName, "pitcher_home_stats", "Innings_Pitched")
                
                k9 = (total_strikeouts/total_inningsPitched)*9
                
                statsToReturn.append(round(k9,2))
                
            elif userChoices[pitcherStat_Count] == PITCHER_CALCHOME_INNINGSPERGAME:
                
                
                total_inningsPitched = get_statData(connection, playerName, "pitcher_home_stats", "Innings_Pitched")
                total_Games = get_statData(connection, playerName, "pitcher_home_stats", "Games_Played")
                
                inningsPerGame = total_inningsPitched/total_Games
                
                statsToReturn.append(round(inningsPerGame,2))
            
            elif userChoices[pitcherStat_Count] == PITCHER_CALCHOME_ERA:
                
                home_ERA = float(get_statData(connection, playerName, "pitcher_home_stats", "ERA"))
                
                if game_Time == "Day":
                    
                    day_ERA = float(get_statData(connection, playerName, "pitcher_day_stats", "ERA"))
                    
                    combined_ERA = (home_ERA + day_ERA)/2
                    
                    statsToReturn.append(round(combined_ERA,2))
                
                elif game_Time == "Night":
                    
                    night_ERA = float(get_statData(connection, playerName, "pitcher_night_stats", "ERA"))
                    
                    combined_ERA = (home_ERA + night_ERA)/2
                    
                    statsToReturn.append(round(combined_ERA,2))
            
            elif userChoices[pitcherStat_Count] == PITCHER_CALCHOME_WHIP:
                
                home_WHIP = float(get_statData(connection, playerName, "pitcher_home_stats", "WHIP"))
                
                if game_Time == "Day":
                    
                    day_WHIP = float(get_statData(connection, playerName, "pitcher_day_stats", "WHIP"))
                    
                    combined_WHIP = (home_WHIP + day_WHIP)/2
                    
                    statsToReturn.append(round(combined_WHIP,2))
                    
                elif game_Time == "Night":
                    
                    night_WHIP = float(get_statData(connection, playerName, "pitcher_night_stats", "WHIP"))
                    
                    combined_WHIP = (home_WHIP + night_WHIP)/2
                    
                    statsToReturn.append(round(combined_WHIP,2))
            
            elif userChoices[pitcherStat_Count] == PITCHER_CALCHOME_HR9:
                
                home_inningsPitched = get_statData(connection, playerName, "pitcher_home_stats", "Innings_Pitched")
                home_HomeRuns = get_statData(connection, playerName, "pitcher_home_stats", "HomeRuns")
                
                home_HR9 = (home_HomeRuns/home_inningsPitched) * 9
                
                if game_Time == "Day":
                    
                    day_inningsPitched = get_statData(connection, playerName, "pitcher_day_stats", "Innings_Pitched")
                    day_HomeRuns = get_statData(connection, playerName, "pitcher_day_stats", "HomeRuns")
                
                    day_HR9 = (day_HomeRuns/day_inningsPitched) * 9
                    
                    combined_HR9 = (home_HR9 + day_HR9)/2
                
                    statsToReturn.append(round(combined_HR9,2))
                    
                elif game_Time == "Night":
                    
                    night_inningsPitched = get_statData(connection, playerName, "pitcher_night_stats", "Innings_Pitched")
                    night_HomeRuns = get_statData(connection, playerName, "pitcher_night_stats", "HomeRuns")
                
                    night_HR9 = (night_HomeRuns/night_inningsPitched) * 9
                    
                    combined_HR9 = (home_HR9 + night_HR9)/2
                
                    statsToReturn.append(round(combined_HR9,2))
            
            elif userChoices[pitcherStat_Count] == PITCHER_CALCHOME_BB9:
                
                home_inningsPitched = get_statData(connection, playerName, "pitcher_home_stats", "Innings_Pitched")
                home_Walks = get_statData(connection, playerName, "pitcher_home_stats", "Walks")
                
                home_BB9 = (home_Walks/home_inningsPitched) * 9
                
                if game_Time == "Day":
                    
                    day_inningsPitched = get_statData(connection, playerName, "pitcher_day_stats", "Innings_Pitched")
                    day_Walks = get_statData(connection, playerName, "pitcher_day_stats", "Walks")
                    
                    day_BB9 = (day_Walks/day_inningsPitched) * 9
                    
                    combine_BB9 = (home_BB9 + day_BB9)/2
                    
                    statsToReturn.append(round(combine_BB9,2))
                    
                elif game_Time == "Night":
                    
                    night_inningsPitched = get_statData(connection, playerName, "pitcher_night_stats", "Innings_Pitched")
                    night_Walks = get_statData(connection, playerName, "pitcher_night_stats", "Walks")
                    
                    night_BB9 = (night_Walks/night_inningsPitched) * 9
                    
                    combine_BB9 = (home_BB9 + night_BB9)/2
                    
                    statsToReturn.append(round(combine_BB9,2))
            
            # Pitcher Away Calculations
                
            elif userChoices[pitcherStat_Count] == PITCHER_CALCAWAY_K9:
                
                total_strikeouts = get_statData(connection, playerName, "pitcher_away_stats", "Strikeouts")
                total_inningsPitched = get_statData(connection, playerName, "pitcher_away_stats", "Innings_Pitched")
                
                k9 = (total_strikeouts/total_inningsPitched)*9
                
                statsToReturn.append(round(k9,2))
                
            elif userChoices[pitcherStat_Count] == PITCHER_CALCAWAY_INNINGSPERGAME:
                
                
                total_inningsPitched = get_statData(connection, playerName, "pitcher_away_stats", "Innings_Pitched")
                total_Games = get_statData(connection, playerName, "pitcher_away_stats", "Games_Played")
                
                inningsPerGame = total_inningsPitched/total_Games
                
                statsToReturn.append(round(inningsPerGame,2))
             
            elif userChoices[pitcherStat_Count] == PITCHER_CALCAWAY_ERA:
                
                away_ERA = float(get_statData(connection, playerName, "pitcher_away_stats", "ERA"))
                
                if game_Time == "Day":
                    
                    day_ERA = float(get_statData(connection, playerName, "pitcher_day_stats", "ERA"))
                    
                    combined_ERA = (away_ERA + day_ERA)/2
                    
                    statsToReturn.append(round(combined_ERA,2))
                
                elif game_Time == "Night":
                    
                    night_ERA = float(get_statData(connection, playerName, "pitcher_night_stats", "ERA"))
                    
                    combined_ERA = (away_ERA + night_ERA)/2
                    
                    statsToReturn.append(round(combined_ERA,2))
                         
            elif userChoices[pitcherStat_Count] == PITCHER_CALCAWAY_WHIP:
                
                away_WHIP = float(get_statData(connection, playerName, "pitcher_away_stats", "WHIP"))
                
                if game_Time == "Day":
                    
                    day_WHIP = float(get_statData(connection, playerName, "pitcher_day_stats", "WHIP"))
                    
                    combined_WHIP = (away_WHIP + day_WHIP)/2
                    
                    statsToReturn.append(round(combined_WHIP,2))
                    
                elif game_Time == "Night":
                    
                    night_WHIP = float(get_statData(connection, playerName, "pitcher_night_stats", "WHIP"))
                    
                    combined_WHIP = (away_WHIP + night_WHIP)/2
                    
                    statsToReturn.append(round(combined_WHIP,2))
   
            elif userChoices[pitcherStat_Count] == PITCHER_CALCAWAY_HR9:
                
                away_inningsPitched = get_statData(connection, playerName, "pitcher_away_stats", "Innings_Pitched")
                away_HomeRuns = get_statData(connection, playerName, "pitcher_away_stats", "HomeRuns")
                
                away_HR9 = (away_HomeRuns/away_inningsPitched) * 9
                
                if game_Time == "Day":
                    
                    day_inningsPitched = get_statData(connection, playerName, "pitcher_day_stats", "Innings_Pitched")
                    day_HomeRuns = get_statData(connection, playerName, "pitcher_day_stats", "HomeRuns")
                
                    day_HR9 = (day_HomeRuns/day_inningsPitched) * 9
                    
                    combined_HR9 = (away_HR9 + day_HR9)/2
                
                    statsToReturn.append(round(combined_HR9,2))
                    
                elif game_Time == "Night":
                    
                    night_inningsPitched = get_statData(connection, playerName, "pitcher_night_stats", "Innings_Pitched")
                    night_HomeRuns = get_statData(connection, playerName, "pitcher_night_stats", "HomeRuns")
                
                    night_HR9 = (night_HomeRuns/night_inningsPitched) * 9
                    
                    combined_HR9 = (away_HR9 + night_HR9)/2
                
                    statsToReturn.append(round(combined_HR9,2))
                
            elif userChoices[pitcherStat_Count] == PITCHER_CALCAWAY_BB9:
                
                away_inningsPitched = get_statData(connection, playerName, "pitcher_away_stats", "Innings_Pitched")
                away_Walks = get_statData(connection, playerName, "pitcher_away_stats", "Walks")
                
                away_BB9 = (away_Walks/away_inningsPitched) * 9
                
                if game_Time == "Day":
                    
                    day_inningsPitched = get_statData(connection, playerName, "pitcher_day_stats", "Innings_Pitched")
                    day_Walks = get_statData(connection, playerName, "pitcher_day_stats", "Walks")
                    
                    day_BB9 = (day_Walks/day_inningsPitched) * 9
                    
                    combine_BB9 = (away_BB9 + day_BB9)/2
                    
                    statsToReturn.append(round(combine_BB9,2))
                    
                elif game_Time == "Night":
                    
                    night_inningsPitched = get_statData(connection, playerName, "pitcher_night_stats", "Innings_Pitched")
                    night_Walks = get_statData(connection, playerName, "pitcher_night_stats", "Walks")
                    
                    night_BB9 = (night_Walks/night_inningsPitched) * 9
                    
                    combine_BB9 = (away_BB9 + night_BB9)/2
                    
                    statsToReturn.append(round(combine_BB9,2))
                    
            # Pitcher Day Calculations
            
            elif userChoices[pitcherStat_Count] == PITCHER_CALCDAY_K9:
                
                total_strikeouts = get_statData(connection, playerName, "pitcher_day_stats", "Strikeouts")
                total_inningsPitched = get_statData(connection, playerName, "pitcher_day_stats", "Innings_Pitched")
                
                k9 = (total_strikeouts/total_inningsPitched)*9
                
                statsToReturn.append(round(k9,2))
                
            elif userChoices[pitcherStat_Count] == PITCHER_CALCDAY_INNINGSPERGAME:
                
                
                total_inningsPitched = get_statData(connection, playerName, "pitcher_day_stats", "Innings_Pitched")
                total_Games = get_statData(connection, playerName, "pitcher_day_stats", "Games_Played")
                
                inningsPerGame = total_inningsPitched/total_Games
                
                statsToReturn.append(round(inningsPerGame,2))
             
            elif userChoices[pitcherStat_Count] == PITCHER_CALCDAY_HR9:
                
                day_inningsPitched = get_statData(connection, playerName, "pitcher_day_stats", "Innings_Pitched")
                day_HomeRuns = get_statData(connection, playerName, "pitcher_day_stats", "HomeRuns")
                
                HR9 = (day_HomeRuns/day_inningsPitched) * 9
                
                statsToReturn.append(round(HR9,2))
             
            # Pitcher Night Calculations
               
            elif userChoices[pitcherStat_Count] == PITCHER_CALCNIGHT_K9:
                
                total_strikeouts = get_statData(connection, playerName, "pitcher_night_stats", "Strikeouts")
                total_inningsPitched = get_statData(connection, playerName, "pitcher_night_stats", "Innings_Pitched")
                
                k9 = (total_strikeouts/total_inningsPitched)*9
                
                statsToReturn.append(round(k9,2))
                
            elif userChoices[pitcherStat_Count] == PITCHER_CALCNIGHT_INNINGSPERGAME:
                
                
                total_inningsPitched = get_statData(connection, playerName, "pitcher_night_stats", "Innings_Pitched")
                total_Games = get_statData(connection, playerName, "pitcher_night_stats", "Games_Played")
                
                inningsPerGame = total_inningsPitched/total_Games
                
                statsToReturn.append(round(inningsPerGame,2))   
             
            elif userChoices[pitcherStat_Count] == PITCHER_CALCNIGHT_HR9:
                
                night_inningsPitched = get_statData(connection, playerName, "pitcher_night_stats", "Innings_Pitched")
                night_HomeRuns = get_statData(connection, playerName, "pitcher_night_stats", "HomeRuns")
                
                HR9 = (night_HomeRuns/night_inningsPitched) * 9
                
                statsToReturn.append(round(HR9,2))
             
             
            
                
            close_connection(connection)        
            pitcherStat_Count +=1
    
    elif category == "Batter":
        
        # Batter Home Calculations
        batterStat_Count = 0
        for stat in userChoices:
            connection = create_connection("mlb_stats")
            
            if userChoices[batterStat_Count] == BATTER_CALCHOME_BATTINGAVG:
                
                home_BattingAVG = get_statData(connection, playerName, "batter_home_stats", "Batting_AVG")
                home_BattingAVG_Decimal = home_BattingAVG
                home_BattingAVG = float(home_BattingAVG_Decimal)
                
                if game_Time == "Day":
                    
                    day_BattingAVG = get_statData(connection, playerName, "batter_day_stats", "Batting_AVG")
                    day_BattingAVG_Decimal = day_BattingAVG
                    day_BattingAVG = float(day_BattingAVG_Decimal)
                    
                    if vsArm == "L":
                        
                        vsLeft_BattingAVG = get_statData(connection, playerName, "batter_vsleft_stats", "Batting_AVG")
                        vsLeft_BattingAVG_Decimal = vsLeft_BattingAVG
                        vsLeft_BattingAVG = float(vsLeft_BattingAVG_Decimal)
                    
                        total_BattingAVG = (home_BattingAVG + day_BattingAVG + vsLeft_BattingAVG)/3
                        statsToReturn.append(round(total_BattingAVG,3))
                    
                    elif vsArm == "R":
                        
                        vsRight_BattingAVG = get_statData(connection, playerName, "batter_vsright_stats", "Batting_AVG")
                        vsRight_BattingAVG_Decimal = vsRight_BattingAVG
                        vsRight_BattingAVG = float(vsRight_BattingAVG_Decimal)
                    
                        total_BattingAVG = (home_BattingAVG + day_BattingAVG + vsRight_BattingAVG)/3
                        statsToReturn.append(round(total_BattingAVG,3))
                    
                    
                    
                elif game_Time == "Night":
                    
                    night_BattingAVG = get_statData(connection, playerName, "batter_night_stats", "Batting_AVG")
                    night_BattingAVG_Decimal = night_BattingAVG
                    night_BattingAVG = float(night_BattingAVG_Decimal)
                    
                    if vsArm == "L":
                        
                        vsLeft_BattingAVG = get_statData(connection, playerName, "batter_vsleft_stats", "Batting_AVG")
                        vsLeft_BattingAVG_Decimal = vsLeft_BattingAVG
                        vsLeft_BattingAVG = float(vsLeft_BattingAVG_Decimal)
                    
                        total_BattingAVG = (home_BattingAVG + night_BattingAVG + vsLeft_BattingAVG)/3
                        statsToReturn.append(round(total_BattingAVG,3))
                    
                    elif vsArm == "R":
                        
                        vsRight_BattingAVG = get_statData(connection, playerName, "batter_vsright_stats", "Batting_AVG")
                        vsRight_BattingAVG_Decimal = vsRight_BattingAVG
                        vsRight_BattingAVG = float(vsRight_BattingAVG_Decimal)
                    
                        total_BattingAVG = (home_BattingAVG + night_BattingAVG + vsRight_BattingAVG)/3
                        statsToReturn.append(round(total_BattingAVG,3))
    
            # Batter Away Calculations
            
            elif userChoices[batterStat_Count] == BATTER_CALCAWAY_BATTINGAVG:
                
                away_BattingAVG = get_statData(connection, playerName, "batter_home_stats", "Batting_AVG")
                away_BattingAVG_Decimal = away_BattingAVG
                away_BattingAVG = float(away_BattingAVG_Decimal)
                
                if game_Time == "Day":
                    
                    day_BattingAVG = get_statData(connection, playerName, "batter_day_stats", "Batting_AVG")
                    day_BattingAVG_Decimal = day_BattingAVG
                    day_BattingAVG = float(day_BattingAVG_Decimal)
                    
                    total_BattingAVG = (away_BattingAVG + day_BattingAVG)/2
                    
                    statsToReturn.append(round(total_BattingAVG,3))
                    
                elif game_Time == "Night":
                    
                    night_BattingAVG = get_statData(connection, playerName, "batter_night_stats", "Batting_AVG")
                    night_BattingAVG_Decimal = night_BattingAVG
                    night_BattingAVG = float(night_BattingAVG_Decimal)
                
                    total_BattingAVG = (away_BattingAVG + night_BattingAVG)/2
                    
                    statsToReturn.append(round(total_BattingAVG,3))
        
        close_connection(connection)    
        batterStat_Count += 1
    elif category == "Team":
        
        teamStat_Count = 0
        for stat in userChoices:
            connection = create_connection("mlb_stats")
            
            # Team Total Averages
            #________________________________________________________________   
            if userChoices[teamStat_Count] == TEAM_PERGAME_AVERAGE_STRIKEOUTS:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_total_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_total_stats", "Games_Played"))
                
                perGameAverage = teamTotalStrikeouts/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            elif userChoices[teamStat_Count] == TEAM_PERGAME_AVERAGE_HITS:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_total_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_total_stats", "Games_Played"))
                
                perGameAverage = teamTotalHits/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
            
            elif userChoices[teamStat_Count] == TEAM_PERGAME_AVERAGE_RUNS:
                
                teamTotalRuns = int(get_teamStatData(connection, teamName, "team_total_stats", "Runs"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_total_stats", "Games_Played"))
                
                perGameAverage = teamTotalRuns/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))    
            
            
            # Team Home Averages
            #________________________________________________________________ 
            elif userChoices[teamStat_Count] == TEAM_PERGAMEHOME_AVERAGE_STRIKEOUTS:
                
                teamTotalStrikeouts = get_teamStatData(connection, teamName, "team_home_stats", "Strikeouts")
                teamTotalStrikeouts = int(teamTotalStrikeouts)
                
                teamTotalGames = get_teamStatData(connection, teamName, "team_home_stats", "Games_Played")
                teamTotalGames = int(teamTotalGames)
                
                perGameAverage = teamTotalStrikeouts/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            elif userChoices[teamStat_Count] == TEAM_PERGAMEHOME_AVERAGE_HITS:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_home_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_home_stats", "Games_Played"))
                
                perGameAverage = teamTotalHits/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            elif userChoices[teamStat_Count] == TEAM_PERGAMEHOME_AVERAGE_RUNS:
                
                teamTotalRuns = int(get_teamStatData(connection, teamName, "team_home_stats", "Runs"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_home_stats", "Games_Played"))
                
                perGameAverage = teamTotalRuns/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            elif userChoices[teamStat_Count] == TEAM_CALCHOME_BATTINGAVG:
                
                teamHome_BattingAVG = float(get_teamStatData(connection, teamName, "team_home_stats", "Batting_AVG"))
                
            
                
                if game_Time == "Day":
                    
                    teamDay_BattingAVG = float(get_teamStatData(connection, teamName, "team_day_stats", "Batting_AVG"))
                    
                    teamCalc_BattingAVG = (teamHome_BattingAVG+teamDay_BattingAVG)/2
                    
                    statsToReturn.append(round(teamCalc_BattingAVG,3))
                        
                elif game_Time == "Night":
                    
                    teamNight_BattingAVG = float(get_teamStatData(connection, teamName, "team_night_stats", "Batting_AVG"))
                    
                    teamCalc_BattingAVG = (teamHome_BattingAVG+teamNight_BattingAVG)/2
                    
                    statsToReturn.append(round(teamCalc_BattingAVG,3))     
            
                
            #Team calculated home per game stats
            elif userChoices[teamStat_Count] == TEAM_CALCHOME_RUNSPERGAME:
                
                team_Home_RunsPerGame = getMLBCalc(teamName, "Team", game_Time, TEAM_PERGAMEHOME_AVERAGE_RUNS)
                team_Home_RunsPerGame = float(team_Home_RunsPerGame[0])
                
                if game_Time == "Day":
                    
                    team_Day_RunsPerGame = getMLBCalc(teamName, "Team", game_Time, TEAM_PERGAMEDAY_AVERAGE_RUNS)
                    team_Day_RunsPerGame = float(team_Day_RunsPerGame[0])
                    
                    team_Combined_RunsPerGame = (team_Home_RunsPerGame + team_Day_RunsPerGame)/2
                    
                    statsToReturn.append(round(team_Combined_RunsPerGame,2))
                    
                elif game_Time == "Night":
                    
                    team_Night_RunsPerGame = getMLBCalc(teamName, "Team", game_Time, TEAM_PERGAMENIGHT_AVERAGE_RUNS)
                    team_Night_RunsPerGame = float(team_Night_RunsPerGame[0])
                    
                    team_Combined_RunsPerGame = (team_Home_RunsPerGame + team_Night_RunsPerGame)/2
                    
                    statsToReturn.append(round(team_Combined_RunsPerGame,2))
                    
                    
           
                
            # Team Away Averages
            #________________________________________________________________ 
            elif userChoices[teamStat_Count] == TEAM_PERGAMEAWAY_AVERAGE_STRIKEOUTS:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_away_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_away_stats", "Games_Played"))
                
                perGameAverage = teamTotalStrikeouts/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            elif userChoices[teamStat_Count] == TEAM_PERGAMEAWAY_AVERAGE_HITS:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_away_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_away_stats", "Games_Played"))
                
                perGameAverage = teamTotalHits/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
             
            elif userChoices[teamStat_Count] == TEAM_PERGAMEAWAY_AVERAGE_RUNS:
                
                teamTotalRuns = int(get_teamStatData(connection, teamName, "team_away_stats", "Runs"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_away_stats", "Games_Played"))
                
                perGameAverage = teamTotalRuns/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))  
             
             
            elif userChoices[teamStat_Count] == TEAM_CALCAWAY_BATTINGAVG:
                
                teamAway_BattingAVG = float(get_teamStatData(connection, teamName, "team_away_stats", "Batting_AVG"))
                
            
                
                if game_Time == "Day":
                    
                    teamDay_BattingAVG = float(get_teamStatData(connection, teamName, "team_day_stats", "Batting_AVG"))
                    
                    teamCalc_BattingAVG = (teamAway_BattingAVG+teamDay_BattingAVG)/2
                    
                    statsToReturn.append(round(teamCalc_BattingAVG,3))
                        
                elif game_Time == "Night":
                    
                    teamNight_BattingAVG = float(get_teamStatData(connection, teamName, "team_night_stats", "Batting_AVG"))
                    
                    teamCalc_BattingAVG = (teamAway_BattingAVG+teamNight_BattingAVG)/2
                    
                    statsToReturn.append(round(teamCalc_BattingAVG,3))   
                    
                    
            #Team calculated away per game stats
            elif userChoices[teamStat_Count] == TEAM_CALCAWAY_RUNSPERGAME:
                
                team_Away_RunsPerGame = getMLBCalc(teamName, "Team", game_Time, TEAM_PERGAMEAWAY_AVERAGE_RUNS)
                team_Away_RunsPerGame = float(team_Away_RunsPerGame[0])
                
                if game_Time == "Day":
                    
                    team_Day_RunsPerGame = getMLBCalc(teamName, "Team", game_Time, TEAM_PERGAMEDAY_AVERAGE_RUNS)
                    team_Day_RunsPerGame = float(team_Day_RunsPerGame[0])
                    
                    team_Combined_RunsPerGame = (team_Away_RunsPerGame + team_Day_RunsPerGame)/2
                    
                    statsToReturn.append(round(team_Combined_RunsPerGame,2))
                    
                elif game_Time == "Night":
                    
                    team_Night_RunsPerGame = getMLBCalc(teamName, "Team", game_Time, TEAM_PERGAMENIGHT_AVERAGE_RUNS)
                    team_Night_RunsPerGame = float(team_Night_RunsPerGame[0])
                    
                    team_Combined_RunsPerGame = (team_Away_RunsPerGame + team_Night_RunsPerGame)/2
                    
                    statsToReturn.append(round(team_Combined_RunsPerGame,2))
                       
            # Team Day Averages
            #________________________________________________________________ 
            elif userChoices[teamStat_Count] == TEAM_PERGAMEDAY_AVERAGE_STRIKEOUTS:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_day_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_day_stats", "Games_Played"))
                
                perGameAverage = teamTotalStrikeouts/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            elif userChoices[teamStat_Count] == TEAM_PERGAMEDAY_AVERAGE_HITS:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_day_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_day_stats", "Games_Played"))
                
                perGameAverage = teamTotalHits/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
            
            elif userChoices[teamStat_Count] == TEAM_PERGAMEDAY_AVERAGE_RUNS:
                
                teamTotalRuns = int(get_teamStatData(connection, teamName, "team_day_stats", "Runs"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_day_stats", "Games_Played"))
                
                perGameAverage = teamTotalRuns/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
            
            
                   
            # Team Day Averages
            #________________________________________________________________ 
            elif userChoices[teamStat_Count] == TEAM_PERGAMENIGHT_AVERAGE_STRIKEOUTS:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_night_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_night_stats", "Games_Played"))
                
                perGameAverage = teamTotalStrikeouts/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            elif userChoices[teamStat_Count] == TEAM_PERGAMENIGHT_AVERAGE_HITS:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_night_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_night_stats", "Games_Played"))
                
                perGameAverage = teamTotalHits/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
            
            elif userChoices[teamStat_Count] == TEAM_PERGAMENIGHT_AVERAGE_RUNS:
                
                teamTotalRuns = int(get_teamStatData(connection, teamName, "team_night_stats", "Runs"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_night_stats", "Games_Played"))
                
                perGameAverage = teamTotalRuns/teamTotalGames
                
                statsToReturn.append(round(perGameAverage,2))
                
            #Team Total At Bat Percentages
            elif userChoices[teamStat_Count] == TEAM_ATBAT_STRIKEOUTPERC:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_total_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_total_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_total_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_StrikeoutAverage = teamTotalStrikeouts/teamTotalGames
                
                AtBat_StrikeoutPerc = perGame_StrikeoutAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_StrikeoutPerc,2))
                
            elif userChoices[teamStat_Count] == TEAM_ATBAT_HITPERC:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_total_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_total_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_total_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_HitsAverage = teamTotalHits/teamTotalGames
                
                AtBat_HitsPerc = perGame_HitsAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_HitsPerc,2))
                
            
                
            #Team Home At Bat Percentages
            elif userChoices[teamStat_Count] == TEAM_ATBATHOME_STRIKEOUTPERC:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_home_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_home_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_home_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_StrikeoutAverage = teamTotalStrikeouts/teamTotalGames
                
                AtBat_StrikeoutPerc = perGame_StrikeoutAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_StrikeoutPerc,2))
                
            elif userChoices[teamStat_Count] == TEAM_ATBATHOME_HITPERC:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_home_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_home_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_home_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_HitsAverage = teamTotalHits/teamTotalGames
                
                AtBat_HitsPerc = perGame_HitsAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_HitsPerc,2))
             
             
            elif userChoices[teamStat_Count] == TEAM_CALC_ATBATHOME_STRIKEOUTPERC:
                
                team_atBatHome_StrikeoutPerc = getMLBCalc(teamName, "Team", "Team_AtBatHome_StrikeoutPerc")
                team_atBatHome_StrikeoutPerc = team_atBatHome_StrikeoutPerc[0]
                
                if game_Time == "Day":
                    
                    team_AtBatDay_StrikeoutPerc = getMLBCalc(teamName, "Team", "Team_AtBatDay_StrikeoutPerc")
                    team_AtBatDay_StrikeoutPerc = team_AtBatDay_StrikeoutPerc[0]
                    
                    team_Calc_AtBat_StrikeoutPerc = (team_atBatHome_StrikeoutPerc + team_AtBatDay_StrikeoutPerc)/2
                    
                    statsToReturn.append(round(team_Calc_AtBat_StrikeoutPerc,2))
                    
                elif game_Time == "Night":
                    
                    team_AtBatNight_StrikeoutPerc = getMLBCalc(teamName, "Team", "Team_AtBatNight_StrikeoutPerc")
                    team_AtBatNight_StrikeoutPerc = team_AtBatNight_StrikeoutPerc[0]
                    
                    team_Calc_AtBat_StrikeoutPerc = (team_atBatHome_StrikeoutPerc + team_AtBatNight_StrikeoutPerc)/2
                    
                    statsToReturn.append(round(team_Calc_AtBat_StrikeoutPerc,2))
            
            elif userChoices[teamStat_Count] == TEAM_CALC_ATBATHOME_HITPERC:
                    
                team_AtBatHome_HitPerc = getMLBCalc(teamName, "Team", "Team_AtBatHome_HitPerc")
                team_AtBatHome_HitPerc = team_AtBatHome_HitPerc[0]
                    
                if game_Time == "Day":
                        
                    team_AtBatDay_HitPerc = getMLBCalc(teamName, "Team", "Team_AtBatDay_HitPerc")
                    team_AtBatDay_HitPerc = team_AtBatDay_HitPerc[0]
                        
                    team_Calc_AtBat_HitPerc = (team_AtBatHome_HitPerc + team_AtBatDay_HitPerc)/2
                        
                    statsToReturn.append(round(team_Calc_AtBat_HitPerc,2))
                        
                elif game_Time == "Night":
                        
                    team_AtBatNight_HitPerc = getMLBCalc(teamName, "Team", "Team_AtBatNight_HitPerc")
                    team_AtBatNight_HitPerc = team_AtBatNight_HitPerc[0]
                    
                    team_Calc_AtBat_HitPerc = (team_AtBatHome_HitPerc + team_AtBatNight_HitPerc)/2
                        
                    statsToReturn.append(round(team_Calc_AtBat_HitPerc,2))
                
                   
            #Team Away At Bat Percentages
            elif userChoices[teamStat_Count] == TEAM_ATBATAWAY_STRIKEOUTPERC:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_away_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_away_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_away_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_StrikeoutAverage = teamTotalStrikeouts/teamTotalGames
                
                AtBat_StrikeoutPerc = perGame_StrikeoutAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_StrikeoutPerc,2))
                
            elif userChoices[teamStat_Count] == TEAM_ATBATAWAY_HITPERC:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_away_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_away_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_away_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_HitsAverage = teamTotalHits/teamTotalGames
                
                AtBat_HitsPerc = perGame_HitsAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_HitsPerc,2))
            
            
            elif userChoices[teamStat_Count] == TEAM_CALC_ATBATAWAY_STRIKEOUTPERC:
                
                team_atBatAway_StrikeoutPerc = getMLBCalc(teamName, "Team", "Team_AtBatAway_StrikeoutPerc")
                team_atBatAway_StrikeoutPerc = team_atBatAway_StrikeoutPerc[0]
                
                if game_Time == "Day":
                    
                    team_AtBatDay_StrikeoutPerc = getMLBCalc(teamName, "Team", "Team_AtBatDay_StrikeoutPerc")
                    team_AtBatDay_StrikeoutPerc = team_AtBatDay_StrikeoutPerc[0]
                    
                    team_Calc_AtBat_StrikeoutPerc = (team_atBatAway_StrikeoutPerc + team_AtBatDay_StrikeoutPerc)/2
                    
                    statsToReturn.append(round(team_Calc_AtBat_StrikeoutPerc,2))
                    
                elif game_Time == "Night":
                    
                    team_AtBatNight_StrikeoutPerc = getMLBCalc(teamName, "Team", "Team_AtBatNight_StrikeoutPerc")
                    team_AtBatNight_StrikeoutPerc = team_AtBatNight_StrikeoutPerc[0]
                    
                    team_Calc_AtBat_StrikeoutPerc = (team_atBatAway_StrikeoutPerc + team_AtBatNight_StrikeoutPerc)/2
                    
                    statsToReturn.append(round(team_Calc_AtBat_StrikeoutPerc,2))
            
            elif userChoices[teamStat_Count] == TEAM_CALC_ATBATAWAY_HITPERC:
                    
                team_AtBatAway_HitPerc = getMLBCalc(teamName, "Team", "Team_AtBatAway_HitPerc")
                team_AtBatAway_HitPerc = team_AtBatAway_HitPerc[0]
                    
                if game_Time == "Day":
                        
                    team_AtBatDay_HitPerc = getMLBCalc(teamName, "Team", "Team_AtBatDay_HitPerc")
                    team_AtBatDay_HitPerc = team_AtBatDay_HitPerc[0]
                        
                    team_Calc_AtBat_HitPerc = (team_AtBatAway_HitPerc + team_AtBatDay_HitPerc)/2
                        
                    statsToReturn.append(round(team_Calc_AtBat_HitPerc,2))
                        
                elif game_Time == "Night":
                        
                    team_AtBatNight_HitPerc = getMLBCalc(teamName, "Team", "Team_AtBatNight_HitPerc")
                    team_AtBatNight_HitPerc = team_AtBatNight_HitPerc[0]
                    
                    team_Calc_AtBat_HitPerc = (team_AtBatAway_HitPerc + team_AtBatNight_HitPerc)/2
                        
                    statsToReturn.append(round(team_Calc_AtBat_HitPerc,2))    
                    
            #Team Day At Bat Percentages
            elif userChoices[teamStat_Count] == TEAM_ATBATDAY_STRIKEOUTPERC:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_day_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_day_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_day_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_StrikeoutAverage = teamTotalStrikeouts/teamTotalGames
                
                AtBat_StrikeoutPerc = perGame_StrikeoutAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_StrikeoutPerc,2))
                
            elif userChoices[teamStat_Count] == TEAM_ATBATDAY_HITPERC:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_day_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_day_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_day_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_HitsAverage = teamTotalHits/teamTotalGames
                
                AtBat_HitsPerc = perGame_HitsAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_HitsPerc,2))
                
            #Team Night At Bat Percentages
            elif userChoices[teamStat_Count] == TEAM_ATBATNIGHT_STRIKEOUTPERC:
                
                teamTotalStrikeouts = int(get_teamStatData(connection, teamName, "team_night_stats", "Strikeouts"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_night_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_night_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_StrikeoutAverage = teamTotalStrikeouts/teamTotalGames
                
                AtBat_StrikeoutPerc = perGame_StrikeoutAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_StrikeoutPerc,2))
                
            elif userChoices[teamStat_Count] == TEAM_ATBATNIGHT_HITPERC:
                
                teamTotalHits = int(get_teamStatData(connection, teamName, "team_night_stats", "Hits"))
                teamTotalGames = int(get_teamStatData(connection, teamName, "team_night_stats", "Games_Played"))
                teamTotalAtBats = int(get_teamStatData(connection, teamName, "team_night_stats", "AtBats"))
                
                atBats_PerGame = teamTotalAtBats/teamTotalGames
                perGame_HitsAverage = teamTotalHits/teamTotalGames
                
                AtBat_HitsPerc = perGame_HitsAverage/atBats_PerGame
                
                statsToReturn.append(round(AtBat_HitsPerc,2))
                
            
            close_connection(connection)   
            teamStat_Count +=1

        
    elif category == "League":
        
        leagueStat_Count = 0
        
        for stat in userChoices:
            connection = create_connection("mlb_stats")
            # League Total Averages
            #________________________________________________________________
            if userChoices[leagueStat_Count] == LEAGUE_PERGAME_AVERAGE_STRIKEOUTS:
                  
                teamStrikeoutsList = []
                teamGamesList = []
                strikeoutSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamStrikeoutsList.append(getMLBStat(teamNames[team_count], category, "Team_Total_Strikeouts"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_total_Games"))
                    
                    teamStrikeouts = int(teamStrikeoutsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    strikeoutSum+= teamStrikeouts/teamGames
                    
                    team_count += 1
                    
                leagueAVG = strikeoutSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
                         
            if userChoices[leagueStat_Count] == LEAGUE_PERGAME_AVERAGE_HITS:
                  
                 
                teamHitsList = []
                teamGamesList = []
                HitsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamHitsList.append(getMLBStat(teamNames[team_count], category, "Team_Total_Hits"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Total_Games"))
                    
                    teamHits = int(teamHitsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    HitsSum+= teamHits/teamGames
                    
                    team_count += 1
                    
                leagueAVG = HitsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))

            if userChoices[leagueStat_Count] == LEAGUE_PERGAME_AVERAGE_RUNS:
                  
                 
                teamRunsList = []
                teamGamesList = []
                runsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamRunsList.append(getMLBStat(teamNames[team_count], category, "Team_Total_Runs"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Total_Games"))
                    
                    teamRuns = int(teamRunsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    runsSum+= teamRuns/teamGames
                    
                    team_count += 1
                    
                leagueAVG = runsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
         
            # League Home Averages
            #________________________________________________________________
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEHOME_AVERAGE_STRIKEOUTS:
                  
                teamStrikeoutsList = []
                teamGamesList = []
                strikeoutSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamStrikeoutsList.append(getMLBStat(teamNames[team_count], category, "Team_Home_Strikeouts"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Home_Games"))
                    
                    teamStrikeouts = int(teamStrikeoutsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    strikeoutSum+= teamStrikeouts/teamGames
                    
                    team_count += 1
                    
                leagueAVG = strikeoutSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
                         
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEHOME_AVERAGE_HITS:
                  
                 
                teamHitsList = []
                teamGamesList = []
                HitsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamHitsList.append(getMLBStat(teamNames[team_count], category, "Team_Home_Hits"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Home_Games"))
                    
                    teamHits = int(teamHitsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    HitsSum+= teamHits/teamGames
                    
                    team_count += 1
                    
                leagueAVG = HitsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
             
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEHOME_AVERAGE_RUNS:
                  
                 
                teamRunsList = []
                teamGamesList = []
                runsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamRunsList.append(getMLBStat(teamNames[team_count], category, "Team_Home_Runs"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Home_Games"))
                    
                    teamRuns = int(teamRunsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    runsSum+= teamRuns/teamGames
                    
                    team_count += 1
                    
                leagueAVG = runsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
            
            
            if userChoices[leagueStat_Count] == LEAGUE_CALCHOME_RUNSPERGAME:
                
                league_Home_RunsPerGame = getMLBCalc("League", "League", "League_PerGameHome_Average_Runs")
                league_Home_RunsPerGame = float(league_Home_RunsPerGame[0])
                
                if game_Time == "Day":
                    
                    league_Day_RunsPerGame = getMLBCalc("League", "League", "League_PerGameDay_Average_Runs")
                    league_Day_RunsPerGame = float(league_Day_RunsPerGame[0])
                    
                    league_Combined_RunsPerGame = (league_Home_RunsPerGame + league_Day_RunsPerGame)/2
                    
                    statsToReturn.append(round(league_Combined_RunsPerGame,2))
                    
                elif game_Time == "Night":
                    
                    league_Night_RunsPerGame = getMLBCalc("League", "League", "League_PerGameNight_Average_Runs")
                    league_Night_RunsPerGame = float(league_Night_RunsPerGame[0])
                    
                    league_Combined_RunsPerGame = (league_Home_RunsPerGame + league_Night_RunsPerGame)/2
                    
                    statsToReturn.append(round(league_Combined_RunsPerGame,2))
                
            # League Away Averages
            #________________________________________________________________
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEAWAY_AVERAGE_STRIKEOUTS:
                  
                teamStrikeoutsList = []
                teamGamesList = []
                strikeoutSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamStrikeoutsList.append(getMLBStat(teamNames[team_count], category, "Team_Away_Strikeouts"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Away_Games"))
                    
                    teamStrikeouts = int(teamStrikeoutsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    strikeoutSum+= teamStrikeouts/teamGames
                    
                    team_count += 1
                    
                leagueAVG = strikeoutSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
                         
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEAWAY_AVERAGE_HITS:
                  
                 
                teamHitsList = []
                teamGamesList = []
                HitsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamHitsList.append(getMLBStat(teamNames[team_count], category, "Team_Away_Hits"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Away_Games"))
                    
                    teamHits = int(teamHitsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    HitsSum+= teamHits/teamGames
                    
                    team_count += 1
                    
                leagueAVG = HitsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
            
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEAWAY_AVERAGE_RUNS:
                  
                 
                teamRunsList = []
                teamGamesList = []
                runsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamRunsList.append(getMLBStat(teamNames[team_count], category, "Team_Away_Runs"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Away_Games"))
                    
                    teamRuns = int(teamRunsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    runsSum+= teamRuns/teamGames
                    
                    team_count += 1
                    
                leagueAVG = runsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
             
             
            if userChoices[leagueStat_Count] == LEAGUE_CALCAWAY_RUNSPERGAME:
                
                league_Away_RunsPerGame = getMLBCalc("League", "League", "League_PerGameAway_Average_Runs")
                league_Away_RunsPerGame = float(league_Away_RunsPerGame[0])
                
                if game_Time == "Day":
                    
                    league_Day_RunsPerGame = getMLBCalc("League", "League", "League_PerGameDay_Average_Runs")
                    league_Day_RunsPerGame = float(league_Day_RunsPerGame[0])
                    
                    league_Combined_RunsPerGame = (league_Away_RunsPerGame + league_Day_RunsPerGame)/2
                    
                    statsToReturn.append(round(league_Combined_RunsPerGame,2))
                    
                elif game_Time == "Night":
                    
                    league_Night_RunsPerGame = getMLBCalc("League", "League", "League_PerGameNight_Average_Runs")
                    league_Night_RunsPerGame = float(league_Night_RunsPerGame[0])
                    
                    league_Combined_RunsPerGame = (league_Away_RunsPerGame + league_Night_RunsPerGame)/2
                    
                    statsToReturn.append(round(league_Combined_RunsPerGame,2))
                    
                
                
                
            # League Day Averages
            #________________________________________________________________
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEDAY_AVERAGE_STRIKEOUTS:
                  
                teamStrikeoutsList = []
                teamGamesList = []
                strikeoutSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamStrikeoutsList.append(getMLBStat(teamNames[team_count], category, "Team_Day_Strikeouts"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Day_Games"))
                    
                    teamStrikeouts = int(teamStrikeoutsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    strikeoutSum+= teamStrikeouts/teamGames
                    
                    team_count += 1
                    
                leagueAVG = strikeoutSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
                       
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEDAY_AVERAGE_HITS:
                  
                 
                teamHitsList = []
                teamGamesList = []
                HitsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamHitsList.append(getMLBStat(teamNames[team_count], category, "Team_Day_Hits"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Day_Games"))
                    
                    teamHits = int(teamHitsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    HitsSum+= teamHits/teamGames
                    
                    team_count += 1
                    
                leagueAVG = HitsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
            
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMEDAY_AVERAGE_RUNS:
                  
                 
                teamRunsList = []
                teamGamesList = []
                runsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamRunsList.append(getMLBStat(teamNames[team_count], category, "Team_Day_Runs"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Day_Games"))
                    
                    teamRuns = int(teamRunsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    runsSum+= teamRuns/teamGames
                    
                    team_count += 1
                    
                leagueAVG = runsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
             
            # League Night Averages
            #________________________________________________________________
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMENIGHT_AVERAGE_STRIKEOUTS:
                  
                teamStrikeoutsList = []
                teamGamesList = []
                strikeoutSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamStrikeoutsList.append(getMLBStat(teamNames[team_count], category, "Team_Total_Strikeouts"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Total_Games"))
                    
                    teamStrikeouts = int(teamStrikeoutsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    strikeoutSum+= teamStrikeouts/teamGames
                    
                    team_count += 1
                    
                leagueAVG = strikeoutSum/30
                 
                statsToReturn.append(round(leagueAVG,2))
                      
            if userChoices[leagueStat_Count] == LEAGUE_PERGAMENIGHT_AVERAGE_HITS:
                  
                 
                teamHitsList = []
                teamGamesList = []
                HitsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamHitsList.append(getMLBStat(teamNames[team_count], category, "Team_Night_Hits"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Night_Games"))
                    
                    teamHits = int(teamHitsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    HitsSum+= teamHits/teamGames
                    
                    team_count += 1
                    
                leagueAVG = HitsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))

            if userChoices[leagueStat_Count] == LEAGUE_PERGAMENIGHT_AVERAGE_RUNS:
                  
                 
                teamRunsList = []
                teamGamesList = []
                runsSum = 0
                 
                category = "Team"
                team_count = 0
                
                for team in teamNames:
                    
                    
                    teamRunsList.append(getMLBStat(teamNames[team_count], category, "Team_Night_Runs"))
                    teamGamesList.append(getMLBStat(teamNames[team_count], category, "Team_Night_Games"))
                    
                    teamRuns = int(teamRunsList[team_count][0])
                    
                    
                    teamGames = int(teamGamesList[team_count][0])
                    
                    
                    runsSum+= teamRuns/teamGames
                    
                    team_count += 1
                    
                leagueAVG = runsSum/30
                 
                statsToReturn.append(round(leagueAVG,2))

            close_connection(connection)
    
    
    
    
    
    
    
    
    
         
    return statsToReturn


def createAnalysis(gameStats):
    
    gameAnalysis = ""
    
    gameTime = gameStats[0]
    
    awayPitcher = gameStats[1]
    homePitcher = gameStats [2]
    
    awayTeam = gameStats[3]
    homeTeam = gameStats[4]
    
    awayPitcher_ERA = gameStats[5]
    homePitcher_ERA = gameStats[6]
    
    awayPitcher_K9 = gameStats[7]
    homePitcher_K9 = gameStats[8]
    
    awayTeam_BattingAVG = gameStats[9]
    homeTeam_BattingAVG = gameStats[10]
    
    # Compare Pitcher's ERA
    if awayPitcher_ERA < homePitcher_ERA:
        
        gameAnalysis += (str(awayPitcher) + " Has a better Away/" + str(gameTime) + " ERA of " + str(awayPitcher_ERA) + " Compared to " + str(homePitcher) + "'s ERA of " + str(homePitcher_ERA) +  ".\n")
        gameAnalysis += ("We can expect " + str(awayPitcher) + " to give up less runs than " + str(homePitcher) + " in this game.\n\n")
    
    elif awayPitcher_ERA > homePitcher_ERA:
        
        gameAnalysis += (str(homePitcher) + " Has a better Home/" + str(gameTime) + "  ERA of " + str(homePitcher_ERA) + " Compared to " + str(awayPitcher) + "'s ERA of " + str(awayPitcher_ERA) + ".\n")
        gameAnalysis += ("We can expect " + str(homePitcher) + " to give up less runs than " + str(awayPitcher) + " in this game.\n\n")
        
    # Compare Pitcher's K9
    if awayPitcher_K9 > homePitcher_K9:
        
        gameAnalysis += (str(awayPitcher) + " Has a better Away/" + str(gameTime) + " K9 of " + str(awayPitcher_K9) + " Compared to " + str(homePitcher) + "'s K9 of " + str(homePitcher_K9) +  ".\n")
        gameAnalysis += ("We can expect " + str(awayPitcher) + " to throw more strikeouts than " + str(homePitcher) + " in this game.\n\n")
        
    elif awayPitcher_K9 < homePitcher_K9:
        
        gameAnalysis += (str(homePitcher) + " Has a better Home/" + str(gameTime) + " K9 of " + str(homePitcher_K9) + " Compared to " + str(awayPitcher) + "'s K9 of " + str(awayPitcher_K9) +  ".\n")
        gameAnalysis += ("We can expect " + str(homePitcher) + " to throw more strikeouts than " + str(awayPitcher) + " in this game.\n\n")
        
    if awayTeam_BattingAVG > homeTeam_BattingAVG:
        
        gameAnalysis += (str(awayTeam) + " Has a better Away/" + str(gameTime) + " batting average of " + str(awayTeam_BattingAVG) + " Compared to " + str(homeTeam) + " Batting average of " + str(homeTeam_BattingAVG) + ".\n")
        gameAnalysis += ("We can expect the " + str(awayTeam) + " To produce more hits than the " + str(homeTeam) + " This game.\n\n" )
        
    elif awayTeam_BattingAVG < homeTeam_BattingAVG:
        
        gameAnalysis += (str(homeTeam) + " have a better Home/" + str(gameTime) + " batting average of " + str(homeTeam_BattingAVG) + " Compared to " + str(awayTeam) + " Batting average of " + str(awayTeam_BattingAVG) + ".\n")
        gameAnalysis += ("We can expect the " + str(homeTeam) + " To produce more hits than the " + str(awayTeam) + " This game.\n\n" )
    
    
    
    
    if awayPitcher_ERA > homePitcher_ERA:
                
        if awayPitcher_ERA > (homePitcher_ERA * 1.3):
         
            gameAnalysis += ("MoneyLine: " + str(homeTeam))
         
        elif awayPitcher_ERA < (homePitcher_ERA*1.3):
            
            gameAnalysis += ("MoneyLine: Lean " + str(homeTeam))
           
    elif awayPitcher_ERA < homePitcher_ERA:
                
        if awayPitcher_ERA < (homePitcher_ERA * 1.3):
         
            gameAnalysis += ("MoneyLine: " + str(awayTeam))
         
        elif awayPitcher_ERA > (homePitcher_ERA*1.3):
            
            gameAnalysis += ("MoneyLine: Lean " + str(awayTeam))
            
    else:
                
        gameAnalysis += "MoneyLine: Toss up"
    
    
        
    return gameAnalysis

def calculate_PitcherOverall_Score(era, whip, k9):
    weight_era = 0.6
    weight_whip = 0.2
    weight_k9 = 0.2
    
    if era != 0 and whip!=0:
        # Adjust for ERA and WHIP (lower values are better)
        adjusted_era = 1 / era
        adjusted_whip = 1 / whip

        overall_score = (weight_era * adjusted_era) + (weight_whip * adjusted_whip) + (weight_k9 * k9)
        return overall_score

    else:
    
        return 0.00
    
    
def getNFLCalc(*args):
    
    playerName = ""
    teamName = ""
    
    
    category = args[1]
    
    userChoices = []
    statsToReturn = []
    
    teamNames = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati", "Cleveland", "Dallas", "Denver", "Detroit",
                 "Green Bay", "Houston", "Indianapolis", "Jacksonville", "Kansas City", "LA Chargers", "LA Rams", "Las Vegas", "Miami", "Minnesota",
                 "New England", "New Orleans", "NY Giants", "NY Jets", "Philadelphia", "Pittsburgh", "San Francisco", "Seattle", "Tampa Bay", "Tennessee", 
                 "Washington"]
    
    if args[0] in teamNames:
        
        teamName = args[0]
        
        userChoices = args[2:]
        
    else:
        
        playerName = args[0]
        
        if args[2] in teamNames:
            
            teamName = args[2]
            
            userChoices = args[3:]
            
        else:
            
            userChoices = args[2:]
    
    connection = create_connection("nfl_stats")
    print("connected")        
    # ----Stat Call Commands----
    
    # --Quarterback--
    
    QB_CALC_PASSYARDS_PERGAME = "QB_Calc_PassYards_PerGame"
    QB_CALC_TOUCHDOWNS_PERGAME = "QB_Calc_Touchdowns_PerGame"
    QB_CALC_COMPLETIONS_PERGAME = "QB_Calc_Completions_PerGame"
    
    # --Runningback--
    RB_CALC_RUSHYARDS_PERGAME = "RB_Calc_RushYards_PerGame"
    RB_CALC_TOUCHDOWNS_PERGAME = "RB_Calc_Touchdowns_PerGame"
    RB_CALC_ATTEMPTS_PERGAME = "RB_Calc_Attempts_PerGame"
    
    # --Wide Recievers--
    WR_CALC_RECYARDS_PERGAME = "WR_Calc_RecYards_PerGame"
    WR_CALC_TOUCHDOWNS_PERGAME = "WR_Calc_Touchdowns_PerGame"
    WR_CALC_TARGETS_PERGAME = "WR_Calc_Targets_PerGame"
    WR_CALC_COMPLETIONS_PERGAME = "WR_Calc_Completions_PerGame"
    
    # --Tight Ends--
    TE_CALC_RECYARDS_PERGAME = "TE_Calc_RecYards_PerGame"
    TE_CALC_TOUCHDOWNS_PERGAME = "TE_Calc_Touchdowns_PerGame"
    TE_CALC_TARGETS_PERGAME = "TE_Calc_Targets_PerGame"
    TE_CALC_COMPLETIONS_PERGAME = "TE_Calc_Completions_PerGame"
    
    
    for choice in userChoices:
        
        
        
        if category == "Quarterback":
            
            if choice == QB_CALC_PASSYARDS_PERGAME:
                
                QB_PassYards = get_statData(connection, playerName, "qb_total_stats", "Pass_Yards")
               
                QB_GamesPlayed = get_statData(connection, playerName, "qb_total_stats", "Games_Played")
               
                if QB_PassYards != 0 or QB_GamesPlayed != 0:
                    QB_PassYards_PerGame = (QB_PassYards/QB_GamesPlayed)
                    
                else:
                    
                    QB_PassYards_PerGame = 0
                    
                statsToReturn.append(QB_PassYards_PerGame)
            
            elif choice == QB_CALC_TOUCHDOWNS_PERGAME:
                
                QB_Touchdowns = get_statData(connection, playerName, "qb_total_stats", "Touchdowns")
               
                QB_GamesPlayed = get_statData(connection, playerName, "qb_total_stats", "Games_Played")
                
                if QB_Touchdowns != 0 or QB_GamesPlayed != 0:
                    QB_Touchdowns_PerGame = (QB_Touchdowns/QB_GamesPlayed)
                    
                else:
                    
                    QB_Touchdowns_PerGame = 0
                    
                statsToReturn.append(QB_Touchdowns_PerGame)
                
                
            elif choice == QB_CALC_COMPLETIONS_PERGAME:
                
                QB_Completions = get_statData(connection, playerName, "qb_total_stats", "Completions")
               
                QB_GamesPlayed = get_statData(connection, playerName, "qb_total_stats", "Games_Played")
                
                if QB_Completions != 0 or QB_GamesPlayed != 0:
                    QB_Completions_PerGame = (QB_Completions/QB_GamesPlayed)
                    
                else:
                    
                    QB_Completions_PerGame = 0
                    
                statsToReturn.append(QB_Completions_PerGame)
                       
        elif category == "Runningback":
            
            if choice == RB_CALC_RUSHYARDS_PERGAME:
                
                RB_RushYards = get_statData(connection, playerName, "rb_total_stats", "Yards")
               
                RB_GamesPlayed = get_statData(connection, playerName, "rb_total_stats", "Games_Played")
                
                if RB_RushYards != 0 and RB_GamesPlayed != 0:
                    RB_RushYards_PerGame = (RB_RushYards/RB_GamesPlayed)
                    
                else:
                    
                    RB_RushYards_PerGame = 0
                    
                statsToReturn.append(RB_RushYards_PerGame)
                
            elif choice == RB_CALC_TOUCHDOWNS_PERGAME:
                
                RB_Touchdowns = get_statData(connection, playerName, "rb_total_stats", "Touchdowns")
               
                RB_GamesPlayed = get_statData(connection, playerName, "rb_total_stats", "Games_Played")
                
                if RB_Touchdowns != 0 and RB_GamesPlayed != 0:
                    RB_Touchdowns_PerGame = (RB_Touchdowns/RB_GamesPlayed)
                    
                else:
                    
                    RB_Touchdowns_PerGame = 0
                    
                statsToReturn.append(RB_Touchdowns_PerGame)
                
            elif choice == RB_CALC_ATTEMPTS_PERGAME:
                
                RB_Attemts = get_statData(connection, playerName, "rb_total_stats", "Attempts")
               
                RB_GamesPlayed = get_statData(connection, playerName, "rb_total_stats", "Games_Played")
                
                if RB_Attemts != 0 and RB_GamesPlayed != 0:
                    RB_Attemts_PerGame = (RB_Attemts/RB_GamesPlayed)
                    
                else:
                    
                    RB_Attemts_PerGame = 0
                    
                statsToReturn.append(RB_Attemts_PerGame)
                    
        elif category == "WideReciever":
            
            if choice == WR_CALC_RECYARDS_PERGAME:
                
                WR_Yards = get_statData(connection, playerName, "wr_total_stats", "Yards")
               
                WR_GamesPlayed = get_statData(connection, playerName, "wr_total_stats", "Games_Played")
                
                if WR_Yards != 0 or WR_GamesPlayed != 0:
                    WR_Yards_PerGame = (WR_Yards/WR_GamesPlayed)
                    
                else:
                    
                    WR_Yards_PerGame = 0
                    
                statsToReturn.append(WR_Yards_PerGame)
                
            elif choice == WR_CALC_TOUCHDOWNS_PERGAME:
                
                WR_Touchdowns = get_statData(connection, playerName, "wr_total_stats", "Touchdowns")
               
                WR_GamesPlayed = get_statData(connection, playerName, "wr_total_stats", "Games_Played")
                
                if WR_Touchdowns != 0 or WR_GamesPlayed != 0:
                    WR_Touchdowns_PerGame = (WR_Touchdowns/WR_GamesPlayed)
                    
                else:
                    
                    WR_Touchdowns_PerGame = 0
                    
                statsToReturn.append(WR_Touchdowns_PerGame)
                
            elif choice == WR_CALC_TARGETS_PERGAME:
                
                WR_Targets = get_statData(connection, playerName, "wr_total_stats", "Targets")
               
                WR_GamesPlayed = get_statData(connection, playerName, "wr_total_stats", "Games_Played")
                
                if WR_Targets != 0 or WR_GamesPlayed != 0:
                    WR_Targets_PerGame = (WR_Targets/WR_GamesPlayed)
                    
                else:
                    
                    WR_Targets_PerGame = 0
                    
                statsToReturn.append(WR_Targets_PerGame)
                
            elif choice == WR_CALC_COMPLETIONS_PERGAME:
                
                WR_Completions = get_statData(connection, playerName, "wr_total_stats", "Catches")
               
                WR_GamesPlayed = get_statData(connection, playerName, "wr_total_stats", "Games_Played")
                
                if WR_Completions != 0 or WR_GamesPlayed != 0:
                    WR_Completions_PerGame = (WR_Completions/WR_GamesPlayed)
                    
                else:
                    
                    WR_Completions_PerGame = 0
                    
                statsToReturn.append(WR_Completions_PerGame)
                
        elif category == "TightEnd":
            
            if choice == TE_CALC_RECYARDS_PERGAME:
                
                TE_Yards = get_statData(connection, playerName, "WR_total_stats", "Yards")
               
                TE_GamesPlayed = get_statData(connection, playerName, "WR_total_stats", "Games_Played")
                
                if TE_Yards != 0 or TE_GamesPlayed != 0:
                    TE_Yards_PerGame = (TE_Yards/TE_GamesPlayed)
                    
                else:
                    
                    TE_Yards_PerGame = 0
                    
                statsToReturn.append(TE_Yards_PerGame)
                
            elif choice == TE_CALC_TARGETS_PERGAME:
                
                TE_Targets = get_statData(connection, playerName, "wr_total_stats", "Targets")
               
                TE_GamesPlayed = get_statData(connection, playerName, "wr_total_stats", "Games_Played")
                
                if TE_Targets != 0 or TE_GamesPlayed != 0:
                    TE_Targets_PerGame = (TE_Targets/TE_GamesPlayed)
                    
                else:
                    
                    TE_Targets_PerGame = 0
                    
                statsToReturn.append(TE_Targets_PerGame)
                
            elif choice == TE_CALC_TOUCHDOWNS_PERGAME:
                
                TE_Touchdowns = get_statData(connection, playerName, "wr_total_stats", "Touchdowns")
               
                TE_GamesPlayed = get_statData(connection, playerName, "wr_total_stats", "Games_Played")
                
                if TE_Touchdowns != 0 or TE_GamesPlayed != 0:
                    TE_Touchdowns_PerGame = (TE_Touchdowns/TE_GamesPlayed)
                    
                else:
                    
                    TE_Touchdowns_PerGame = 0
                    
                statsToReturn.append(TE_Touchdowns_PerGame)
                
            elif choice == TE_CALC_COMPLETIONS_PERGAME:
                
                TE_Completions = get_statData(connection, playerName, "wr_total_stats", "Catches")
               
                TE_GamesPlayed = get_statData(connection, playerName, "wr_total_stats", "Games_Played")
                
                if TE_Completions != 0 or TE_GamesPlayed != 0:
                    TE_Completions_PerGame = (TE_Completions/TE_GamesPlayed)
                    
                else:
                    
                    TE_Completions_PerGame = 0
                    
                statsToReturn.append(TE_Completions_PerGame)
            
                  
        
    connection.close()
    
    return statsToReturn   
        
def getNBACalc(*args):
    
    playerName = ""
    teamName = ""
    
    
    category = args[1]
    
    userChoices = []
    statsToReturn = []
    
    teamNames_Short = ["bos", "bkn", "ny", "phi", "tor", "gs",
                       "lac", "lal", "phx", "sac", "chi", "cle",
                       "det", "ind", "mil", "dal", "hou", "mem",
                       "no", "sa", "atl", "cha", "mia", "orl",
                       "wsh", "den", "min", "okc", "por", "utah"]
    
    if args[0] in teamNames_Short:
        
        teamName = args[0]
        
        userChoices = args[2:]
        
    else:
        
        playerName = args[0]
        
        if args[2] in teamNames_Short:
            
            teamName = args[2]
            
            userChoices = args[3:]
            
        else:
            
            userChoices = args[2:]
    
    connection = create_connection("nba_stats")
    print("connected")   
    
    # ----Stat Call Commands----
    
    # Per Minute Calculatuions
    PLAYER_POINTS_PERMINUTE = "Player_Points_PerMinute" 
    PLAYER_REBOUNDS_PERMINUTE = "Player_Rebounds_PerMinute"
    PLAYER_BLOCKS_PERMINUTE = "Player_Blocks_PerMinute"
    PLAYER_ASSISTS_PERMINUTE = "Player_Assists_PerMinute"
    
    for choice in userChoices:
         
        if category == "Player":
            
            if choice == PLAYER_POINTS_PERMINUTE:
                
                # Get players minutes per game
                player_Minutes_PerGame = getNBAStat(playerName,"Player_Misc", "Player_Minutes_PerGame")
                player_Minutes_PerGame = player_Minutes_PerGame[0]
                
                # Get Players points per game
                player_Points_PerGame = getNBAStat(playerName,"Player_Scoring", "Player_Points_PerGame")
                player_Points_PerGame = player_Points_PerGame[0]
                
                # Divide players points by minutes
                player_Points_PerMinute = player_Points_PerGame/player_Minutes_PerGame
                
                statsToReturn.append(player_Points_PerMinute)

            elif choice == PLAYER_REBOUNDS_PERMINUTE:

                # Get players minutes per game
                player_Minutes_PerGame = getNBAStat(playerName,"Player_Misc", "Player_Minutes_PerGame")
                player_Minutes_PerGame = player_Minutes_PerGame[0]

                # Get Players Rebounds per game
                player_Rebounds_PerGame = getNBAStat(playerName,"Player_Rebounds", "Player_Rebounds_PerGame")
                player_Rebounds_PerGame = player_Rebounds_PerGame[0]

                player_Rebounds_PerMinute = player_Rebounds_PerGame/player_Minutes_PerGame

                statsToReturn.append(player_Rebounds_PerMinute)

            elif choice == PLAYER_BLOCKS_PERMINUTE:

                # Get players minutes per game
                player_Minutes_PerGame = getNBAStat(playerName,"Player_Misc", "Player_Minutes_PerGame")
                player_Minutes_PerGame = player_Minutes_PerGame[0]

                # Get Players Blocks per game
                player_Blocks_PerGame = getNBAStat(playerName,"Player_Blocks", "Player_Blocks_PerGame")
                player_Blocks_PerGame = player_Blocks_PerGame[0]

                player_Blocks_PerMinute = player_Blocks_PerGame/player_Minutes_PerGame

                statsToReturn.append(player_Blocks_PerMinute)

            elif choice == PLAYER_ASSISTS_PERMINUTE:

                # Get players minutes per game
                player_Minutes_PerGame = getNBAStat(playerName,"Player_Misc", "Player_Minutes_PerGame")
                player_Minutes_PerGame = player_Minutes_PerGame[0]

                # Get Players Assists per game
                player_Assists_PerGame = getNBAStat(playerName,"Player_Assists_Turnovers", "Player_Assists_PerGame")
                player_Assists_PerGame = player_Assists_PerGame[0]

                player_Assists_PerMinute = player_Assists_PerGame/player_Minutes_PerGame

                statsToReturn.append(player_Assists_PerMinute)

            

                
                
    return statsToReturn
    
def calculate_League_Averages(*args):

    # Sport selection is at args[0]
    # Category is at args[1]
    # userChoices is at args[2]

    """
    Purpose:
        Calculates league averages of any stat in MySQL database.

    Returns:
        A league average sum as a list

    """

    statsToReturn = []
    userChoices = []

    for arg in args[2:]:
        userChoices.append(arg)
    

    if args[0] == "NFL":

        if args[1] == "Team_Defense_Passing":

            pass

        elif args[1] == "Team_Defensive_Rushing":

            pass
        
        elif args[1] == "Team_Defense_Totals":
            
            pass
        
        elif args[1] == "Team_Offense_Rushing":
            
            pass
        
        elif args[1] == "Team_Offense_Totals":
            
            pass

    elif args[0] == "NBA":

        if args[1] == "Team_Defense_Scoring":
            
            pass
        
        elif args[1] == "Team_Defense_Shooting":
            
            pass
        
        elif args[1] == "Team_Opp_Misc":
            
            pass
        
        elif args[1] == "Team_Misc":
            
            pass
        
        elif args[1] == "Team_Offensive_Scoring":
            
            pass
        
        elif args[1] == "Team_Offensive_Shooting":
            
            pass
        
        elif args[1] == "Team_Winning_Perc":
            
            pass

    elif args[0] == "MLB":

        if args[1] == "Team_Totals":
            
            pass
        
        elif args[1] == "Team_Home":
            
            pass
        
        elif args[1] == "Team_Away":
            
            pass
        
        elif args[1] == "Team_Day":
            
            pass
        
        elif args[1] == "Team_Night":
            
            pass
        
        elif args[1] == "Team_1st_Inning":
            
            pass
        

    return statsToReturn    