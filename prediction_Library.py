import mysql.connector
from mysql.connector import Error
from main_Library import *
from calculation_Library import *


def getMLBPred(*args):
    
    connection = create_connection("mlb_stats")
    
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
    
    if args[0] in teamNames:
        
        teamName = args[0]
        
        
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
    else:       
        for choice in args[2:]:
        
            userChoices.append(choice)
        
     
     
     
     
        
    # Pitcher Home Predictions
    PITCHER_PREDHOME_STRIKEOUTS = "Pitcher_PredHome_Strikeouts"
    PITCHER_PREDHOME_HITS = "Pitcher_PredHome_Hits"
    PITCHER_PREDHOME_RUNS ="Pitcher_PredHome_Runs"
    
    
    
    # Pitcher Away Predictions
    PITCHER_PREDAWAY_STRIKEOUTS = "Pitcher_PredAway_Strikeouts"
    PITCHER_PREDAWAY_HITS = "Pitcher_PredAway_Hits"
    PITCHER_PREDAWAY_RUNS = "Pitcher_PredAway_Runs"   
    
      
      
      
      
        
        
        
        
    if category == "Pitcher":
        
        pitcherStat_Count = 0
        
        for stat in userChoices:
            
            if userChoices[pitcherStat_Count] == PITCHER_PREDHOME_STRIKEOUTS:
                
                # Opp Team
                oppTeam_PerGameAway_Strikeouts = getMLBCalc(teamName, "Team", "Team_PerGameAway_Average_Strikeouts")
                oppTeam_PerGameAway_Strikeouts = float(oppTeam_PerGameAway_Strikeouts[0])
                
                #League averages
                league_PerGameAway_Average_Strikeouts = getMLBCalc("League", "League", "League_PerGameNight_Average_Strikeouts")
                league_PerGameAway_Average_Strikeouts = float(league_PerGameAway_Average_Strikeouts[0])
                
                #Pitcher Home Strikeouts
                pitcher_Home_Strikeouts = getMLBStat(playerName, "Pitcher", "Pitcher_Home_Strikeouts")
                pitcher_Home_Strikeouts = int(pitcher_Home_Strikeouts[0])
                
                #Pitcher Home Innings Pitched
                pitcher_Home_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Home_InningsPitched")
                pitcher_Home_InningsPitched = float(pitcher_Home_InningsPitched[0])
                
                #Pitcher Home Games Played
                pitcher_Home_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Home_Games")
                pitcher_Home_GamesPlayed = int(pitcher_Home_GamesPlayed[0])
                
                
                
                if game_Time == "Day":
                    
                    # Opp Team
                    oppTeam_PerGameDay_Strikeouts = getMLBCalc(teamName, "Team", "Team_PerGameDay_Average_Strikeouts")
                    oppTeam_PerGameDay_Strikeouts = float(oppTeam_PerGameDay_Strikeouts[0])
                    
                    #League averages
                    league_PerGameDay_Average_Strikeouts = getMLBCalc("League", "League", "League_PerGameDay_Average_Strikeouts")
                    league_PerGameDay_Average_Strikeouts = float(league_PerGameDay_Average_Strikeouts[0])
                    
                    #Pitcher Home Strikeouts
                    pitcher_Day_Strikeouts = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Strikeouts")
                    pitcher_Day_Strikeouts = int(pitcher_Day_Strikeouts[0])
                    
                    #Pitcher Home Innings Pitched
                    pitcher_Day_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Day_InningsPitched")
                    pitcher_Day_InningsPitched = float(pitcher_Day_InningsPitched[0])
                    
                    #Pitcher Home Games Played
                    pitcher_Day_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Games")
                    pitcher_Day_GamesPlayed = int(pitcher_Day_GamesPlayed[0])
                    
                    
                    #Calculate opp team average strikeouts between away and day
                    oppTeam_PerGame_Strikeouts = (oppTeam_PerGameAway_Strikeouts + oppTeam_PerGameDay_Strikeouts)/2
                    
                    #Calculate league average strikeouts between away and day
                    league_PerGame_Strikeouts = (league_PerGameAway_Average_Strikeouts + league_PerGameDay_Average_Strikeouts)/2
                    
                    
                    
                    #Calculate pitcher average strikeouts between home and day
                    pitcher_Strikeouts = (pitcher_Home_Strikeouts + pitcher_Day_Strikeouts)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Home_InningsPitched + pitcher_Day_InningsPitched)/2
                    
                    #Calculate pitcher average games between home and day
                    pitcher_GamesPlayed = (pitcher_Home_GamesPlayed + pitcher_Day_GamesPlayed)/2
                    
                    #Calculate opp team strikeout offset
                    teamStrikeoutDiff = league_PerGame_Strikeouts - oppTeam_PerGame_Strikeouts
                    
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                    
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_StrikeoutsPerInning = pitcher_Strikeouts/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Strikeouts = pitcher_AVG_StrikeoutsPerInning* pitcher_AVG_InningsPitched
                    
                    
                    
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredStrikeouts = pitcher_AVG_Strikeouts - teamStrikeoutDiff
                    
                    statsToReturn.append(round(pitcher_PredStrikeouts,1))
                  
                elif game_Time == "Night":
                    
                    # Opp Team
                    oppTeam_PerGameNight_Strikeouts = getMLBCalc(teamName, "Team", "Team_PerGameNight_Average_Strikeouts")
                    oppTeam_PerGameNight_Strikeouts = float(oppTeam_PerGameNight_Strikeouts[0])
                    
                    #League averages
                    league_PerGameNight_Average_Strikeouts = getMLBCalc("League", "League", "League_PerGameNight_Average_Strikeouts")
                    league_PerGameNight_Average_Strikeouts = float(league_PerGameNight_Average_Strikeouts[0])
                    
                    #Pitcher Home Strikeouts
                    pitcher_Night_Strikeouts = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Strikeouts")
                    pitcher_Night_Strikeouts = int(pitcher_Night_Strikeouts[0])
                    
                    #Pitcher Home Innings Pitched
                    pitcher_Night_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Night_InningsPitched")
                    pitcher_Night_InningsPitched = float(pitcher_Night_InningsPitched[0])
                    
                    #Pitcher Home Games Played
                    pitcher_Night_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Games")
                    pitcher_Night_GamesPlayed = int(pitcher_Night_GamesPlayed[0])
                    
                    
                    #Calculate opp team average strikeouts between away and day
                    oppTeam_PerGame_Strikeouts = (oppTeam_PerGameAway_Strikeouts + oppTeam_PerGameNight_Strikeouts)/2
                    
                    #Calculate league average strikeouts between away and day
                    league_PerGame_Strikeouts = (league_PerGameAway_Average_Strikeouts + league_PerGameNight_Average_Strikeouts)/2
                    
                    
                    
                    #Calculate pitcher average strikeouts between home and day
                    pitcher_Strikeouts = (pitcher_Home_Strikeouts + pitcher_Night_Strikeouts)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Home_InningsPitched + pitcher_Night_InningsPitched)/2
                    
                    #Calculate pitcher average games between home and day
                    pitcher_GamesPlayed = (pitcher_Home_GamesPlayed + pitcher_Night_GamesPlayed)/2
                    
                    #Calculate opp team strikeout offset
                    teamStrikeoutDiff = league_PerGame_Strikeouts - oppTeam_PerGame_Strikeouts
                    
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                    
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_StrikeoutsPerInning = pitcher_Strikeouts/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Strikeouts = pitcher_AVG_StrikeoutsPerInning* pitcher_AVG_InningsPitched
                    
                    
                    
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredStrikeouts = pitcher_AVG_Strikeouts - teamStrikeoutDiff
                    
                    statsToReturn.append(round(pitcher_PredStrikeouts,1))
                                 
            if userChoices[pitcherStat_Count] == PITCHER_PREDAWAY_STRIKEOUTS:
                
                # Opp Team
                oppTeam_PerGameHome_Strikeouts = getMLBCalc(teamName, "Team", "Team_PerGameHome_Average_Strikeouts")
                oppTeam_PerGameHome_Strikeouts = float(oppTeam_PerGameHome_Strikeouts[0])
                
                #League averages
                league_PerGameHome_Average_Strikeouts = getMLBCalc("League", "League", "League_PerGameHome_Average_Strikeouts")
                league_PerGameHome_Average_Strikeouts = float(league_PerGameHome_Average_Strikeouts[0])
                
                #Pitcher Home Strikeouts
                pitcher_Away_Strikeouts = getMLBStat(playerName, "Pitcher", "Pitcher_Away_Strikeouts")
                pitcher_Away_Strikeouts = int(pitcher_Away_Strikeouts[0])
                    
                #Pitcher Home Innings Pitched
                pitcher_Away_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Away_InningsPitched")
                pitcher_Away_InningsPitched = float(pitcher_Away_InningsPitched[0])
                    
                #Pitcher Home Games Played
                pitcher_Away_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Away_Games")
                pitcher_Away_GamesPlayed = int(pitcher_Away_GamesPlayed[0])
                    
                    
                    
                if game_Time == "Day":
                        
                    # Opp Team
                    oppTeam_PerGameDay_Strikeouts = getMLBCalc(teamName, "Team", "Team_PerGameDay_Average_Strikeouts")
                    oppTeam_PerGameDay_Strikeouts = float(oppTeam_PerGameDay_Strikeouts[0])
                        
                    #League averages
                    league_PerGameDay_Average_Strikeouts = getMLBCalc("League", "League", "League_PerGameDay_Average_Strikeouts")
                    league_PerGameDay_Average_Strikeouts = float(league_PerGameDay_Average_Strikeouts[0])
                        
                    #Pitcher Home Strikeouts
                    pitcher_Day_Strikeouts = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Strikeouts")
                    pitcher_Day_Strikeouts = int(pitcher_Day_Strikeouts[0])
                        
                    #Pitcher Home Innings Pitched
                    pitcher_Day_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Day_InningsPitched")
                    pitcher_Day_InningsPitched = float(pitcher_Day_InningsPitched[0])
                        
                    #Pitcher Home Games Played
                    pitcher_Day_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Games")
                    pitcher_Day_GamesPlayed = int(pitcher_Day_GamesPlayed[0])
                        
                        
                    #Calculate opp team average strikeouts between away and day
                    oppTeam_PerGame_Strikeouts = (oppTeam_PerGameHome_Strikeouts + oppTeam_PerGameDay_Strikeouts)/2
                        
                    #Calculate league average strikeouts between away and day
                    league_PerGame_Strikeouts = (league_PerGameHome_Average_Strikeouts + league_PerGameDay_Average_Strikeouts)/2
                        
                        
                        
                    #Calculate pitcher average strikeouts between home and day
                    pitcher_Strikeouts = (pitcher_Away_Strikeouts + pitcher_Day_Strikeouts)/2
                        
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Away_InningsPitched + pitcher_Day_InningsPitched)/2
                        
                    #Calculate pitcher average games between home and day
                    pitcher_GamesPlayed = (pitcher_Away_GamesPlayed + pitcher_Day_GamesPlayed)/2
                        
                    #Calculate opp team strikeout offset
                    teamStrikeoutDiff = league_PerGame_Strikeouts - oppTeam_PerGame_Strikeouts
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_StrikeoutsPerInning = pitcher_Strikeouts/pitcher_InningsPitched
                        
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Strikeouts = pitcher_AVG_StrikeoutsPerInning* pitcher_AVG_InningsPitched
                        
                    
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredStrikeouts = pitcher_AVG_Strikeouts - teamStrikeoutDiff
                        
                    statsToReturn.append(round(pitcher_PredStrikeouts,1))
                    
                elif game_Time == "Night":
                        
                    # Opp Team
                    oppTeam_PerGameNight_Strikeouts = getMLBCalc(teamName, "Team", "Team_PerGameNight_Average_Strikeouts")
                    oppTeam_PerGameNight_Strikeouts = float(oppTeam_PerGameNight_Strikeouts[0])
                        
                    #League averages
                    league_PerGameNight_Average_Strikeouts = getMLBCalc("League", "League", "League_PerGameNight_Average_Strikeouts")
                    league_PerGameNight_Average_Strikeouts = float(league_PerGameNight_Average_Strikeouts[0])
                        
                    #Pitcher Home Strikeouts
                    pitcher_Night_Strikeouts = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Strikeouts")
                    pitcher_Night_Strikeouts = int(pitcher_Night_Strikeouts[0])
                        
                    #Pitcher Home Innings Pitched
                    pitcher_Night_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Night_InningsPitched")
                    pitcher_Night_InningsPitched = float(pitcher_Night_InningsPitched[0])
                        
                    #Pitcher Home Games Played
                    pitcher_Night_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Games")
                    pitcher_Night_GamesPlayed = int(pitcher_Night_GamesPlayed[0])
                        
                        
                    #Calculate opp team average strikeouts between away and day
                    oppTeam_PerGame_Strikeouts = (oppTeam_PerGameHome_Strikeouts + oppTeam_PerGameNight_Strikeouts)/2
                        
                    #Calculate league average strikeouts between away and day
                    league_PerGame_Strikeouts = (league_PerGameHome_Average_Strikeouts + league_PerGameNight_Average_Strikeouts)/2
                        
                        
                        
                    #Calculate pitcher average strikeouts between home and day
                    pitcher_Strikeouts = (pitcher_Away_Strikeouts + pitcher_Night_Strikeouts)/2
                        
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Away_InningsPitched + pitcher_Night_InningsPitched)/2
                        
                    #Calculate pitcher average games between home and day
                    pitcher_GamesPlayed = (pitcher_Away_GamesPlayed + pitcher_Night_GamesPlayed)/2
                        
                    #Calculate opp team strikeout offset
                    teamStrikeoutDiff = league_PerGame_Strikeouts - oppTeam_PerGame_Strikeouts
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_StrikeoutsPerInning = pitcher_Strikeouts/pitcher_InningsPitched
                        
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Strikeouts = pitcher_AVG_StrikeoutsPerInning* pitcher_AVG_InningsPitched
                        
                    
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredStrikeouts = pitcher_AVG_Strikeouts - teamStrikeoutDiff
                        
                    statsToReturn.append(round(pitcher_PredStrikeouts,1))
                
            if userChoices[pitcherStat_Count] == PITCHER_PREDHOME_HITS:
                
                
                # Opp Team Averages
                oppTeam_Away_HitsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameAway_Average_Hits")
                oppTeam_Away_HitsPerGame = float(oppTeam_Away_HitsPerGame[0])
                
                #League Averages
                league_Away_HitsPerGame = getMLBCalc("League", "League", "League_PerGameAway_Average_Hits")
                league_Away_HitsPerGame = float(league_Away_HitsPerGame[0])
                
                #Pitcher Home Hits
                pitcher_Home_Hits = getMLBStat(playerName, "Pitcher", "Pitcher_Home_Hits")
                pitcher_Home_Hits = int(pitcher_Home_Hits[0])
                    
                #Pitcher Home Innings Pitched
                pitcher_Home_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Home_InningsPitched")
                pitcher_Home_InningsPitched = float(pitcher_Home_InningsPitched[0])
                    
                #Pitcher Home Games Played
                pitcher_Home_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Home_Games")
                pitcher_Home_GamesPlayed = int(pitcher_Home_GamesPlayed[0])
                
                if game_Time == "Day":
                    
                    # Opp Team Day Averages
                    oppTeam_Day_HitsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameDay_Average_Hits")
                    oppTeam_Day_HitsPerGame = float(oppTeam_Day_HitsPerGame[0])
                    
                    #League Day Averages
                    league_Day_HitsPerGame = getMLBCalc("League", "League", "League_PerGameDay_Average_Hits")
                    league_Day_HitsPerGame = float(league_Day_HitsPerGame[0])
                    
                    #Pitcher Day Hits
                    pitcher_Day_Hits = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Hits")
                    pitcher_Day_Hits = int(pitcher_Day_Hits[0])
                        
                    #Pitcher Day Innings Pitched
                    pitcher_Day_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Day_InningsPitched")
                    pitcher_Day_InningsPitched = float(pitcher_Day_InningsPitched[0])
                        
                    #Pitcher Day Games Played
                    pitcher_Day_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Games")
                    pitcher_Day_GamesPlayed = int(pitcher_Day_GamesPlayed[0])
                    
                    #Calculate opp team average hits between home and day
                    oppTeam_HitsPerGame = (oppTeam_Away_HitsPerGame + oppTeam_Day_HitsPerGame)/2
                    
                    
                    #Calculate opp team average hits between home and day
                    league_HitsPerGame = (league_Away_HitsPerGame + league_Day_HitsPerGame)/2
                    
                    
                    #Calculate pitcher average Hits between home and day
                    pitcher_Hits = (pitcher_Home_Hits + pitcher_Day_Hits)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Home_InningsPitched + pitcher_Day_InningsPitched)/2
                    
                    #Calculate pitcher average games played between home and day
                    pitcher_GamesPlayed = (pitcher_Home_GamesPlayed + pitcher_Day_GamesPlayed)/2
                    
                    
                    #Calculate opp team strikeout offset
                    teamHitsDiff = league_HitsPerGame - oppTeam_HitsPerGame
                    
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                    
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_HitsPerInning = pitcher_Hits/pitcher_InningsPitched
                    
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Hits = pitcher_AVG_HitsPerInning * pitcher_AVG_InningsPitched

                    #Calculate pitcher predicted strikeouts
                    pitcher_PredHits = pitcher_AVG_Hits - teamHitsDiff
                    
                        
                    statsToReturn.append(round(pitcher_PredHits,1))
                    
                    
                
                elif game_Time == "Night":
                    
                    # Opp Team Day Averages
                    oppTeam_Night_HitsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameNight_Average_Hits")
                    oppTeam_Night_HitsPerGame = float(oppTeam_Night_HitsPerGame[0])
                    
                    #League Day Averages
                    league_Night_HitsPerGame = getMLBCalc("League", "League", "League_PerGameNight_Average_Hits")
                    league_Night_HitsPerGame = float(league_Night_HitsPerGame[0])
                    
                    #Pitcher Day Hits
                    pitcher_Night_Hits = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Hits")
                    pitcher_Night_Hits = int(pitcher_Night_Hits[0])
                        
                    #Pitcher Day Innings Pitched
                    pitcher_Night_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Night_InningsPitched")
                    pitcher_Night_InningsPitched = float(pitcher_Night_InningsPitched[0])
                        
                    #Pitcher Day Games Played
                    pitcher_Night_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Games")
                    pitcher_Night_GamesPlayed = int(pitcher_Night_GamesPlayed[0])
                    
                    #Calculate opp team average hits between home and day
                    oppTeam_HitsPerGame = (oppTeam_Away_HitsPerGame + oppTeam_Night_HitsPerGame)/2
                    
                    #Calculate opp team average hits between home and day
                    league_HitsPerGame = (league_Away_HitsPerGame + league_Night_HitsPerGame)/2
                    
                    #Calculate pitcher average Hits between home and day
                    pitcher_Hits = (pitcher_Home_Hits + pitcher_Night_Hits)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Home_InningsPitched + pitcher_Night_InningsPitched)/2
                    
                    #Calculate pitcher average games played between home and day
                    pitcher_GamesPlayed = (pitcher_Home_GamesPlayed + pitcher_Night_GamesPlayed)/2
                    
                    
                    #Calculate opp team strikeout offset
                    teamHitsDiff = league_HitsPerGame - oppTeam_HitsPerGame
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_HitsPerInning = pitcher_Hits/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Hits = pitcher_AVG_HitsPerInning* pitcher_AVG_InningsPitched
                        
                    
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredHits = pitcher_AVG_Hits - teamHitsDiff
                        
                    statsToReturn.append(round(pitcher_PredHits,1))
                       
            if userChoices[pitcherStat_Count] == PITCHER_PREDAWAY_HITS:
                
                # Opp Team Averages
                oppTeam_Home_HitsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameHome_Average_Hits")
                oppTeam_Home_HitsPerGame = float(oppTeam_Home_HitsPerGame[0])
                
                #League Averages
                league_Home_HitsPerGame = getMLBCalc("League", "League", "League_PerGameHome_Average_Hits")
                league_Home_HitsPerGame = float(league_Home_HitsPerGame[0])
                
                #Pitcher Home Hits
                pitcher_Away_Hits = getMLBStat(playerName, "Pitcher", "Pitcher_Away_Hits")
                pitcher_Away_Hits = int(pitcher_Away_Hits[0])
                    
                #Pitcher Home Innings Pitched
                pitcher_Away_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Away_InningsPitched")
                pitcher_Away_InningsPitched = float(pitcher_Away_InningsPitched[0])
                    
                #Pitcher Home Games Played
                pitcher_Away_GamesPlayed = getMLBStat(playerName, "Pitcher",  "Pitcher_Away_Games")
                pitcher_Away_GamesPlayed = int(pitcher_Away_GamesPlayed[0])
                
                if game_Time == "Day":
                    
                    # Opp Team Day Averages
                    oppTeam_Day_HitsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameDay_Average_Hits")
                    oppTeam_Day_HitsPerGame = float(oppTeam_Day_HitsPerGame[0])
                    
                    #League Day Averages
                    league_Day_HitsPerGame = getMLBCalc("League", "League", "League_PerGameDay_Average_Hits")
                    league_Day_HitsPerGame = float(league_Day_HitsPerGame[0])
                    
                    #Pitcher Day Hits
                    pitcher_Day_Hits = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Hits")
                    pitcher_Day_Hits = int(pitcher_Day_Hits[0])
                        
                    #Pitcher Day Innings Pitched
                    pitcher_Day_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Day_InningsPitched")
                    pitcher_Day_InningsPitched = float(pitcher_Day_InningsPitched[0])
                        
                    #Pitcher Day Games Played
                    pitcher_Day_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Games")
                    pitcher_Day_GamesPlayed = int(pitcher_Day_GamesPlayed[0])
                    
                    #Calculate opp team average hits between home and day
                    oppTeam_HitsPerGame = (oppTeam_Home_HitsPerGame + oppTeam_Day_HitsPerGame)/2
                    
                    #Calculate opp team average hits between home and day
                    league_HitsPerGame = (league_Home_HitsPerGame + league_Day_HitsPerGame)/2
                    
                    #Calculate pitcher average Hits between home and day
                    pitcher_Hits = (pitcher_Away_Hits + pitcher_Day_Hits)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Away_InningsPitched + pitcher_Day_InningsPitched)/2
                    
                    #Calculate pitcher average games played between home and day
                    pitcher_GamesPlayed = (pitcher_Away_GamesPlayed + pitcher_Day_GamesPlayed)/2
                    
                    
                    #Calculate opp team strikeout offset
                    teamHitsDiff = league_HitsPerGame - oppTeam_HitsPerGame
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_HitsPerInning = pitcher_Hits/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Hits = pitcher_AVG_HitsPerInning* pitcher_AVG_InningsPitched
                        
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredHits = pitcher_PredHits = pitcher_AVG_Hits - teamHitsDiff
                        
                    statsToReturn.append(round(pitcher_PredHits,1))
                    
                    
                
                elif game_Time == "Night":
                    
                    # Opp Team Day Averages
                    oppTeam_Night_HitsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameNight_Average_Hits")
                    oppTeam_Night_HitsPerGame = float(oppTeam_Night_HitsPerGame[0])
                    
                    #League Day Averages
                    league_Night_HitsPerGame = getMLBCalc("League", "League", "League_PerGameNight_Average_Hits")
                    league_Night_HitsPerGame = float(league_Night_HitsPerGame[0])
                    
                    #Pitcher Day Hits
                    pitcher_Night_Hits = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Hits")
                    pitcher_Night_Hits = int(pitcher_Night_Hits[0])
                        
                    #Pitcher Day Innings Pitched
                    pitcher_Night_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Night_InningsPitched")
                    pitcher_Night_InningsPitched = float(pitcher_Night_InningsPitched[0])
                        
                    #Pitcher Day Games Played
                    pitcher_Night_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Games")
                    pitcher_Night_GamesPlayed = int(pitcher_Night_GamesPlayed[0])
                    
                    #Calculate opp team average hits between home and day
                    oppTeam_HitsPerGame = (oppTeam_Home_HitsPerGame + oppTeam_Night_HitsPerGame)/2
                    
                    #Calculate opp team average hits between home and day
                    league_HitsPerGame = (league_Home_HitsPerGame + league_Night_HitsPerGame)/2
                    
                    #Calculate pitcher average Hits between home and day
                    pitcher_Hits = (pitcher_Away_Hits + pitcher_Night_Hits)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Away_InningsPitched + pitcher_Night_InningsPitched)/2
                    
                    #Calculate pitcher average games played between home and day
                    pitcher_GamesPlayed = (pitcher_Away_GamesPlayed + pitcher_Night_GamesPlayed)/2
                    
                    
                    #Calculate opp team strikeout offset
                    teamHitsDiff = league_HitsPerGame - oppTeam_HitsPerGame
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_HitsPerInning = pitcher_Hits/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Hits = pitcher_AVG_HitsPerInning* pitcher_AVG_InningsPitched
                        
                    
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredHits = pitcher_PredHits = pitcher_AVG_Hits - teamHitsDiff
                        
                    statsToReturn.append(round(pitcher_PredHits,1))
                
            if userChoices[pitcherStat_Count] == PITCHER_PREDHOME_RUNS:
                
                # Opp Team Averages
                oppTeam_Away_RunsPerGame = getMLBCalc(teamName, "Team","Team_PerGameAway_Average_Runs")
                oppTeam_Away_RunsPerGame = float(oppTeam_Away_RunsPerGame[0])
                
                #League Averages
                league_Away_RunsPerGame = getMLBCalc("League", "League", "League_PerGameAway_Average_Runs")
                league_Away_RunsPerGame = float(league_Away_RunsPerGame[0])
                
                #Pitcher Home Hits
                pitcher_Home_Runs = getMLBStat(playerName, "Pitcher", "Pitcher_Home_Runs")
                pitcher_Home_Runs = int(pitcher_Home_Runs[0])
                    
                #Pitcher Home Innings Pitched
                pitcher_Home_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Home_InningsPitched")
                pitcher_Home_InningsPitched = float(pitcher_Home_InningsPitched[0])
                    
                #Pitcher Home Games Played
                pitcher_Home_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Home_Games")
                pitcher_Home_GamesPlayed = int(pitcher_Home_GamesPlayed[0])
            
                if game_Time == "Day":
                    
                    # Opp Team Day Averages
                    oppTeam_Day_RunsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameDay_Average_Runs")
                    oppTeam_Day_RunsPerGame = float(oppTeam_Day_RunsPerGame[0])
                    
                    #League Day Averages
                    league_Day_RunsPerGame = getMLBCalc("League", "League", "League_PerGameDay_Average_Runs")
                    league_Day_RunsPerGame = float(league_Day_RunsPerGame[0])
                    
                    #Pitcher Day Hits
                    pitcher_Day_Runs = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Runs")
                    pitcher_Day_Runs = int(pitcher_Day_Runs[0])
                        
                    #Pitcher Day Innings Pitched
                    pitcher_Day_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Day_InningsPitched")
                    pitcher_Day_InningsPitched = float(pitcher_Day_InningsPitched[0])
                        
                    #Pitcher Day Games Played
                    pitcher_Day_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Games")
                    pitcher_Day_GamesPlayed = int(pitcher_Day_GamesPlayed[0])
                    
                    #Calculate opp team average hits between home and day
                    oppTeam_RunsPerGame = (oppTeam_Away_RunsPerGame + oppTeam_Day_RunsPerGame)/2
                    
                    #Calculate opp team average hits between home and day
                    league_RunsPerGame = (league_Away_RunsPerGame + league_Day_RunsPerGame)/2
                    
                    #Calculate pitcher average Hits between home and day
                    pitcher_Runs = (pitcher_Home_Runs + pitcher_Day_Runs)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Home_InningsPitched + pitcher_Day_InningsPitched)/2
                    
                    #Calculate pitcher average games played between home and day
                    pitcher_GamesPlayed = (pitcher_Home_GamesPlayed + pitcher_Day_GamesPlayed)/2
                    
                    
                    #Calculate opp team strikeout offset
                    teamRunsDiff = league_RunsPerGame - oppTeam_RunsPerGame
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_RunsPerInning = pitcher_Runs/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Runs = pitcher_AVG_RunsPerInning* pitcher_AVG_InningsPitched
                        
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredRuns = pitcher_AVG_Runs - teamRunsDiff
                        
                    statsToReturn.append(round(pitcher_PredRuns,1))
                    
                elif game_Time == "Night":
                   
                   # Opp Team Day Averages
                    oppTeam_Night_RunsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameNight_Average_Runs")
                    oppTeam_Night_RunsPerGame = float(oppTeam_Night_RunsPerGame[0])
                    
                    #League Day Averages
                    league_Night_RunsPerGame = getMLBCalc("League", "League", "League_PerGameNight_Average_Runs")
                    league_Night_RunsPerGame = float(league_Night_RunsPerGame[0])
                    
                    #Pitcher Day Hits
                    pitcher_Night_Runs = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Runs")
                    pitcher_Night_Runs = int(pitcher_Night_Runs[0])
                        
                    #Pitcher Day Innings Pitched
                    pitcher_Night_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Night_InningsPitched")
                    pitcher_Night_InningsPitched = float(pitcher_Night_InningsPitched[0])
                        
                    #Pitcher Day Games Played
                    pitcher_Night_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Games")
                    pitcher_Night_GamesPlayed = int(pitcher_Night_GamesPlayed[0])
                    
                    #Calculate opp team average hits between home and day
                    oppTeam_RunsPerGame = (oppTeam_Away_RunsPerGame + oppTeam_Night_RunsPerGame)/2
                    
                    #Calculate opp team average hits between home and day
                    league_RunsPerGame = (league_Away_RunsPerGame + league_Night_RunsPerGame)/2
                    
                    #Calculate pitcher average Hits between home and day
                    pitcher_Runs = (pitcher_Home_Runs + pitcher_Night_Runs)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Home_InningsPitched + pitcher_Night_InningsPitched)/2
                    
                    #Calculate pitcher average games played between home and day
                    pitcher_GamesPlayed = (pitcher_Home_GamesPlayed + pitcher_Night_GamesPlayed)/2
                    
                    
                    #Calculate opp team strikeout offset
                    teamRunsDiff = league_RunsPerGame - oppTeam_RunsPerGame
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_RunsPerInning = pitcher_Runs/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Runs = pitcher_AVG_RunsPerInning* pitcher_AVG_InningsPitched
                        
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredRuns = pitcher_AVG_Runs - teamRunsDiff
                        
                    statsToReturn.append(round(pitcher_PredRuns,1)) 
                
            if userChoices[pitcherStat_Count] == PITCHER_PREDAWAY_RUNS:
                
                # Opp Team Averages
                oppTeam_Home_RunsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameHome_Average_Runs")
                oppTeam_Home_RunsPerGame = float(oppTeam_Home_RunsPerGame[0])
                
                #League Averages
                league_Home_RunsPerGame = getMLBCalc("League", "League", "League_PerGameHome_Average_Runs")
                league_Home_RunsPerGame = float(league_Home_RunsPerGame[0])
                
                #Pitcher Home Hits
                pitcher_Away_Runs = get_statData(connection, playerName, "pitcher_away_stats", "Runs")
                
                    
                #Pitcher Home Innings Pitched
                pitcher_Away_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Away_InningsPitched")
                pitcher_Away_InningsPitched = float(pitcher_Away_InningsPitched[0])
                    
                #Pitcher Home Games Played
                pitcher_Away_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Away_Games")
                pitcher_Away_GamesPlayed = int(pitcher_Away_GamesPlayed[0])
            
                if game_Time == "Day":
                    
                    # Opp Team Day Averages
                    oppTeam_Day_RunsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameDay_Average_Runs")
                    oppTeam_Day_RunsPerGame = float(oppTeam_Day_RunsPerGame[0])
                    
                    #League Day Averages
                    league_Day_RunsPerGame = getMLBCalc("League", "League", "League_PerGameDay_Average_Runs")
                    league_Day_RunsPerGame = float(league_Day_RunsPerGame[0])
                    
                    #Pitcher Day Hits
                    pitcher_Day_Runs = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Runs")
                    pitcher_Day_Runs = int(pitcher_Day_Runs[0])
                        
                    #Pitcher Day Innings Pitched
                    pitcher_Day_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Day_InningsPitched")
                    pitcher_Day_InningsPitched = float(pitcher_Day_InningsPitched[0])
                        
                    #Pitcher Day Games Played
                    pitcher_Day_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Day_Games")
                    pitcher_Day_GamesPlayed = int(pitcher_Day_GamesPlayed[0])
                    
                    #Calculate opp team average hits between home and day
                    oppTeam_RunsPerGame = (oppTeam_Home_RunsPerGame + oppTeam_Day_RunsPerGame)/2
                    
                    #Calculate opp team average hits between home and day
                    league_RunsPerGame = (league_Home_RunsPerGame + league_Day_RunsPerGame)/2
                    
                    #Calculate pitcher average Hits between home and day
                    pitcher_Runs = (pitcher_Away_Runs + pitcher_Day_Runs)/2
                    
                    #Calculate pitcher average innings pitched between home and day
                    pitcher_InningsPitched = (pitcher_Away_InningsPitched + pitcher_Day_InningsPitched)/2
                    
                    #Calculate pitcher average games played between home and day
                    pitcher_GamesPlayed = (pitcher_Away_GamesPlayed + pitcher_Day_GamesPlayed)/2
                    
                    
                    #Calculate opp team strikeout offset
                    teamRunsDiff = league_RunsPerGame - oppTeam_RunsPerGame
                        
                    #Calculate pitcher average innings pitched
                    pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                        
                    #Calculate pitcher average Strikeouts per inning
                    pitcher_AVG_RunsPerInning = pitcher_Runs/pitcher_InningsPitched
                    
                    #Calculate pitcher strikeouts per game
                    pitcher_AVG_Runs = pitcher_AVG_RunsPerInning* pitcher_AVG_InningsPitched
                        
                        
                    #Calculate pitcher predicted strikeouts
                    pitcher_PredRuns = pitcher_AVG_Runs - teamRunsDiff
                        
                    statsToReturn.append(round(pitcher_PredRuns,1))
                    
                elif game_Time == "Night":
                    try:
                    # Opp Team Day Averages
                        oppTeam_Night_RunsPerGame = getMLBCalc(teamName, "Team", "Team_PerGameNight_Average_Runs")
                        oppTeam_Night_RunsPerGame = float(oppTeam_Night_RunsPerGame[0])
                        
                        #League Day Averages
                        league_Night_RunsPerGame = getMLBCalc("League", "League", "League_PerGameNight_Average_Runs")
                        league_Night_RunsPerGame = float(league_Night_RunsPerGame[0])
                        
                        #Pitcher Day Hits
                        pitcher_Night_Runs = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Runs")
                        pitcher_Night_Runs = int(pitcher_Night_Runs[0])
                            
                        #Pitcher Day Innings Pitched
                        pitcher_Night_InningsPitched = getMLBStat(playerName, "Pitcher", "Pitcher_Night_InningsPitched")
                        pitcher_Night_InningsPitched = float(pitcher_Night_InningsPitched[0])
                            
                        #Pitcher Day Games Played
                        pitcher_Night_GamesPlayed = getMLBStat(playerName, "Pitcher", "Pitcher_Night_Games")
                        pitcher_Night_GamesPlayed = int(pitcher_Night_GamesPlayed[0])
                        
                        #Calculate opp team average hits between home and day
                        oppTeam_RunsPerGame = (oppTeam_Home_RunsPerGame + oppTeam_Night_RunsPerGame)/2
                        
                        #Calculate opp team average hits between home and day
                        league_RunsPerGame = (league_Home_RunsPerGame + league_Night_RunsPerGame)/2
                        
                        #Calculate pitcher average Hits between home and day
                        pitcher_Runs = (pitcher_Away_Runs + pitcher_Night_Runs)/2
                        
                        #Calculate pitcher average innings pitched between home and day
                        pitcher_InningsPitched = (pitcher_Away_InningsPitched + pitcher_Night_InningsPitched)/2
                        
                        #Calculate pitcher average games played between home and day
                        pitcher_GamesPlayed = (pitcher_Away_GamesPlayed + pitcher_Night_GamesPlayed)/2
                        
                        
                        #Calculate opp team strikeout offset
                        teamRunsDiff = league_RunsPerGame - oppTeam_RunsPerGame
                            
                        #Calculate pitcher average innings pitched
                        pitcher_AVG_InningsPitched = pitcher_InningsPitched / pitcher_GamesPlayed
                            
                        #Calculate pitcher average Strikeouts per inning
                        pitcher_AVG_RunsPerInning = pitcher_Runs/pitcher_InningsPitched
                        
                        #Calculate pitcher strikeouts per game
                        pitcher_AVG_Runs = pitcher_AVG_RunsPerInning* pitcher_AVG_InningsPitched
                            
                            
                        #Calculate pitcher predicted strikeouts
                        pitcher_PredRuns = pitcher_AVG_Runs - teamRunsDiff
                            
                        statsToReturn.append(round(pitcher_PredRuns,1))   
                        
                    except TypeError:
                        
                        statsToReturn.append(0)
            
                 
            pitcherStat_Count += 1
    
    elif category == "Batter":
        
        pass
    
    elif category == "Team":
        
        pass
    
    elif category == "League":
        
        
        pass
    
    

    close_connection(connection)       
    return statsToReturn

def getNFLPred(*args):
    
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
        
        for arg in args[2:]:
            userChoices.append(arg)
        
    else:
        
        playerName = args[0]
        
        if args[2] in teamNames:
            
            teamName = args[2]
            
            for arg in args[3:]:
                userChoices.append(arg)
            
        else:
            
            for arg in args[2:]:
                userChoices.append(arg)
    
    connection = create_connection("nfl_stats")
    
               
    # ----Stat Call Commands----
    
    # --Quarterback--
    
    QB_PRED_PASSYARDS = "QB_Pred_PassYards"
    QB_PRED_TOUCHDOWNS = "QB_Pred_Touchdowns"
    QB_PRED_COMPLETIONS = "QB_Pred_Completions"
    QB_PRED_RUSHYARDS = "QB_Pred_RushYard"
    QB_PRED_RUSHATTEMPTS = "QB_Pred_RushAttempts"
    
    # --Runningback--
    RB_PRED_RUSHYARDS = "RB_Pred_RushYards"
    RB_PRED_TOUCHDOWNS = "RB_Pred_Touchdowns"
    RB_PRED_ATTEMPTS = "RB_Pred_Attempts"
    RB_PRED_YPA = "RB_Pred_YPA"
    RB_PRED_RECYARDS = "RB_Pred_RecYards"
    
    # --Wide Recievers--
    WR_PRED_RECYARDS = "WR_Pred_RecYards"
    WR_PRED_TOUCHDOWNS = "WR_Pred_Touchdowns"
    WR_PRED_COMPLETIONS = "WR_Pred_Completions"
    WR_PRED_YPC = "WR_Pred_YPC"
    
    # --Tight Ends--
    TE_PRED_RECYARDS = "TE_Pred_RecYards"
    TE_PRED_TOUCHDOWNS = "TE_Pred_Touchdowns"
    TE_PRED_COMPLETIONS = "TE_Pred_Completions"
    
    # --Team---
    TEAM_PRED_POINTS = "Team_Pred_Points"
            
    for choice in userChoices:
        
        
        
        if category == "Quarterback":
        
            if choice == QB_PRED_PASSYARDS:
                
                # Get QB's Pass Yards Per Game
                QB_PassYards_PerGame = getNFLCalc(playerName, "Quarterback", "QB_Calc_PassYards_PerGame")
                QB_PassYards_PerGame = float(QB_PassYards_PerGame[0])
                
                # Get versus team's pass yards allowed per game
                vsTeam_PassYards_Allowed_PerGame =  get_statData(connection, teamName, "defteam_passing_stats", "PassYards_PerGame")
                vsTeam_PassYards_Allowed_PerGame = float(vsTeam_PassYards_Allowed_PerGame)
                
                # Get everyteam's pass yards allowed per game
                league_PassYards_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_PassYards_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
        
                    league_PassYards_PerGame_List.append(stat[0])
                
                # Sum All team's pass yards allowed per game
                league_PassYards_PerGame_Sum = 0   
                for yard in league_PassYards_PerGame_List:
                    
                    league_PassYards_PerGame_Sum += float(yard)
                    
                # Calculate the league average of pass yards allowed per game
                league_PassYards_PerGame_AVG = (league_PassYards_PerGame_Sum/len(league_PassYards_PerGame_List))
                
                # Calculate pass Yards allowed difference between versus team and league average as a percentage
                percentage_passYards_Diff = ((vsTeam_PassYards_Allowed_PerGame - league_PassYards_PerGame_AVG) / league_PassYards_PerGame_AVG) * 100
                percentage_passYards_Diff = percentage_passYards_Diff/2
                
                # Calculate predicted QB's pass touchdowns as a percentage change from QB's average
                pred_QB_PassingYards = QB_PassYards_PerGame * (1 + percentage_passYards_Diff / 100)
                
                statsToReturn.append(round(pred_QB_PassingYards,1))
                
            elif choice == QB_PRED_TOUCHDOWNS:
                
                QB_Touchdowns_PerGame = getNFLCalc(playerName, "Quarterback", "QB_Calc_Touchdowns_PerGame")
                QB_Touchdowns_PerGame = float(QB_Touchdowns_PerGame[0])
                
                vsTeam_PassTouchdowns_Allowed_PerGame =  get_statData(connection, teamName, "defteam_passing_stats", "PassTouchdowns_PerGame")
                vsTeam_PassTouchdowns_Allowed_PerGame = float(vsTeam_PassTouchdowns_Allowed_PerGame)
                
                # Get everyteam's Pass Touchdowns allowed per game
                league_PassTouchdowns_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_PassTouchdowns_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
        
                    league_PassTouchdowns_PerGame_List.append(stat[0])
                
                # Sum All team's Pass Touchdowns allowed per game
                league_PassTouchdowns_PerGame_Sum = 0   
                for touchdowns in league_PassTouchdowns_PerGame_List:
                    
                    league_PassTouchdowns_PerGame_Sum += float(touchdowns)
                   
                # Calculate the league average of pass Touchdowns allowed per game
                league_PassTouchdowns_PerGame_AVG = (league_PassTouchdowns_PerGame_Sum/len(league_PassTouchdowns_PerGame_List))
                
                # Calculate pass touchdowns allowed difference between versus team and league average as a percentage
                percentage_passTouchdowns_Diff = ((vsTeam_PassTouchdowns_Allowed_PerGame - league_PassTouchdowns_PerGame_AVG) / league_PassTouchdowns_PerGame_AVG) * 100
                percentage_passTouchdowns_Diff = percentage_passTouchdowns_Diff/2
                
                # Calculate predicted QB's pass touchdowns as a percentage change from QB's average
                pred_QB_PassingTouchdowns = QB_Touchdowns_PerGame * (1 + percentage_passTouchdowns_Diff / 100)
                
                statsToReturn.append(round(pred_QB_PassingTouchdowns,1))
                
            elif choice == QB_PRED_COMPLETIONS:
                
                QB_Completions_PerGame = getNFLCalc(playerName, "Quarterback", "QB_Calc_Completions_PerGame")
                QB_Completions_PerGame = float(QB_Completions_PerGame[0])
                
                vsTeam_Completions_Allowed_PerGame =  get_statData(connection, teamName, "defteam_passing_stats", "Completions_PerGame")
                vsTeam_Completions_Allowed_PerGame = float(vsTeam_Completions_Allowed_PerGame)
                
                
                # Get everyteam's Pass Touchdowns allowed per game
                league_Completions_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_Completions_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
        
                    league_Completions_PerGame_List.append(stat[0])
                
                # Sum All team's Pass Touchdowns allowed per game
                league_Completions_PerGame_Sum = 0   
                for completions in league_Completions_PerGame_List:
                    
                    league_Completions_PerGame_Sum += float(completions)
                   
                # Calculate the league average of pass Touchdowns allowed per game
                league_Completions_PerGame_AVG = (league_Completions_PerGame_Sum/len(league_Completions_PerGame_List))
                
                # Calculate pass completions allowed difference between versus team and league average as a percentage
                percentage_passCompletions_Diff = ((vsTeam_Completions_Allowed_PerGame - league_Completions_PerGame_AVG) / league_Completions_PerGame_AVG) * 100
                percentage_passCompletions_Diff = percentage_passCompletions_Diff/2
                
                # Calculate predicted QB's pass touchdowns as a percentage change from QB's average
                pred_QB_PassingCompletions = QB_Completions_PerGame * (1 + percentage_passCompletions_Diff / 100)
                
                statsToReturn.append(round(pred_QB_PassingCompletions,1))
                
        elif category == "Runningback":
            
            if choice == RB_PRED_RUSHYARDS:
                
                RB_RushYards_PerGame = getNFLCalc(playerName, "Runningback", "RB_Calc_RushYards_PerGame")
                RB_RushYards_PerGame = float(RB_RushYards_PerGame[0])
                
                vsTeam_RushYards_Allowed_PerGame =  get_statData(connection, teamName, "defteam_rushing_stats", "RushYards_PerGame")
                vsTeam_RushYards_Allowed_PerGame = float(vsTeam_RushYards_Allowed_PerGame)
                
                # Get everyteam's Rush Yards allowed per game
                league_RushYards_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_RushYards_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Rushing", statToGet)
        
                    league_RushYards_PerGame_List.append(stat[0])
                
                # Sum All team's Pass Touchdowns allowed per game
                league_RushYards_PerGame_Sum = 0   
                for yards in league_RushYards_PerGame_List:
                    
                    league_RushYards_PerGame_Sum += float(yards)
                   
                # Calculate the league average of pass Touchdowns allowed per game
                league_RushYards_PerGame_AVG = (league_RushYards_PerGame_Sum/len(league_RushYards_PerGame_List))
                
                # Calculate Rush Yards allowed difference between versus team and league average as a percentage
                percentage_RushYards_Diff = ((vsTeam_RushYards_Allowed_PerGame - league_RushYards_PerGame_AVG) / league_RushYards_PerGame_AVG) * 100
                percentage_RushYards_Diff = percentage_RushYards_Diff/2
                
                # Calculate predicted RB's Rush Yards as a percentage change from QB's average
                pred_RB_RushingYards = RB_RushYards_PerGame * (1 + percentage_RushYards_Diff / 100)
                
                statsToReturn.append(round(pred_RB_RushingYards,1))
                
            elif choice == RB_PRED_TOUCHDOWNS:
                
                RB_RushTouchdowns_PerGame = getNFLCalc(playerName, "Runningback", "RB_Calc_Touchdowns_PerGame")
                RB_RushTouchdowns_PerGame = float(RB_RushTouchdowns_PerGame[0])
                
                vsTeam_RushTouchdowns_Allowed_PerGame =  get_statData(connection, teamName, "defteam_rushing_stats", "RushTouchdowns_PerGame")
                vsTeam_RushTouchdowns_Allowed_PerGame = float(vsTeam_RushTouchdowns_Allowed_PerGame)
                
                # Get everyteam's rush touchdowns allowed per game
                league_RushTouchdowns_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_RushTouchdowns_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Rushing", statToGet)
        
                    league_RushTouchdowns_PerGame_List.append(stat[0])
                
                # Sum All team's Rush Touchdowns allowed per game
                league_RushTouchdowns_PerGame_Sum = 0   
                for touchdowns in league_RushTouchdowns_PerGame_List:
                    
                    league_RushTouchdowns_PerGame_Sum += float(touchdowns)
                   
                # Calculate the league average of Rush Touchdowns allowed per game
                league_RushTouchdowns_PerGame_AVG = (league_RushTouchdowns_PerGame_Sum/len(league_RushTouchdowns_PerGame_List))
                
                # Calculate Rush Touchdowns allowed difference between versus team and league average as a percentage
                percentage_RushTouchdowns_Diff = ((vsTeam_RushTouchdowns_Allowed_PerGame - league_RushTouchdowns_PerGame_AVG) / league_RushTouchdowns_PerGame_AVG) * 100
                percentage_RushTouchdowns_Diff = percentage_RushTouchdowns_Diff/2
                
                # Calculate predicted RB's Rushing touchdowns as a percentage change from QB's average
                pred_RB_RushTouchdowns = RB_RushTouchdowns_PerGame * (1 + percentage_RushTouchdowns_Diff / 100)
                
                
                statsToReturn.append(round(pred_RB_RushTouchdowns,1))
                
            elif choice == RB_PRED_ATTEMPTS:
                
                RB_Attempts_PerGame = getNFLCalc(playerName, "Runningback", "RB_Calc_Attempts_PerGame")
                RB_Attempts_PerGame = float(RB_Attempts_PerGame[0])
                
                vsTeam_Attempts_Allowed_PerGame =  get_statData(connection, teamName, "defteam_rushing_stats", "RushAttempts_PerGame")
                vsTeam_Attempts_Allowed_PerGame = float(vsTeam_Attempts_Allowed_PerGame)
                
                # Get everyteam's rush Attempts allowed per game
                league_Attempts_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_RushAttempts_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Rushing", statToGet)
        
                    league_Attempts_PerGame_List.append(stat[0])
                
                # Sum All team's Rush Attempts allowed per game
                league_Attempts_PerGame_Sum = 0   
                for attempts in league_Attempts_PerGame_List:
                    
                    league_Attempts_PerGame_Sum += float(attempts)
                   
                # Calculate the league average of Rush Attempts allowed per game
                league_Attempts_PerGame_AVG = (league_Attempts_PerGame_Sum/len(league_Attempts_PerGame_List))
                
                # Calculate Rush Attempts allowed difference between versus team and league average as a percentage
                percentage_RushAttempts_Diff = ((vsTeam_Attempts_Allowed_PerGame - league_Attempts_PerGame_AVG) / league_Attempts_PerGame_AVG) * 100
                percentage_RushAttempts_Diff = percentage_RushAttempts_Diff/2
                
                # Calculate predicted RB's Rushing touchdowns as a percentage change from QB's average
                pred_RB_RushAttempts = RB_Attempts_PerGame * (1 + percentage_RushAttempts_Diff / 100)
                
                
                statsToReturn.append(round(pred_RB_RushAttempts,1))
                
            elif choice == RB_PRED_YPA:
                
                RB_YPA_AVG = get_statData(connection, playerName, "rb_total_stats", "Yards_PerAttempt")
                RB_YPA_AVG = float(RB_YPA_AVG)
                
                vsTeam_YPA_Allowed =  getNFLStat(teamName, "Defense_Team_Rushing", "DefTeam_RushYards_PerAttempt")
                vsTeam_YPA_Allowed = float(vsTeam_YPA_Allowed[0])
                
                # Get everyteam's rush yards per attempt allowed
                league_YPA_List = []
                for team in teamNames:
                    
                    statToGet = "DefTeam_RushYards_PerAttempt"
                    stat = getNFLStat(team, "Defense_Team_Rushing", statToGet)
        
                    league_YPA_List.append(stat[0])
                    
                # Sum All team's Rush Yards allowed per attempt
                league_YPA_Sum = 0   
                for Yards in league_YPA_List:
                    
                    league_YPA_Sum += float(Yards)
                    
                # Calculate the league average of YPA allowed 
                league_YPA_AVG = (league_YPA_Sum/len(league_YPA_List))
                
                # Calculate YPA allowed difference between versus team and league average as a percentage
                percentage_YPA_Diff = ((vsTeam_YPA_Allowed - league_YPA_AVG) / league_YPA_AVG) * 100
                percentage_YPA_Diff = percentage_YPA_Diff/2
                
                # Calculate predicted RB's Rushing touchdowns as a percentage change from QB's average
                pred_RB_YPA = RB_YPA_AVG * (1 + percentage_YPA_Diff / 100)
                
                statsToReturn.append(round(pred_RB_YPA,1))
                
                
        
        elif category == "WideReciever":
            
            if choice == WR_PRED_RECYARDS:
                
                WR_RecYards_PerGame = getNFLCalc(playerName, "WideReciever", "WR_Calc_RecYards_PerGame")
                WR_RecYards_PerGame = float(WR_RecYards_PerGame[0])
                
                vsTeam_PassYards_Allowed_PerGame =  get_statData(connection, teamName, "defteam_passing_stats", "PassYards_PerGame")
                vsTeam_PassYards_Allowed_PerGame = float(vsTeam_PassYards_Allowed_PerGame)
                
                # Get everyteam's Pass Yards allowed per game
                league_PassYards_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_PassYards_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
        
                    league_PassYards_PerGame_List.append(stat[0])
                    
                # Sum All team's Pass Yards allowed per game
                league_PassYards_PerGame_Sum = 0   
                for yards in league_PassYards_PerGame_List:
                    
                    league_PassYards_PerGame_Sum += float(yards)
                    
                # Calculate the league average of Pass Yards allowed per game
                league_PassYards_PerGame_AVG = (league_PassYards_PerGame_Sum/len(league_PassYards_PerGame_List))
                
                # Calculate Pass Yards allowed difference between versus team and league average as a percentage
                percentage_PassYards_Diff = ((vsTeam_PassYards_Allowed_PerGame - league_PassYards_PerGame_AVG) / league_PassYards_PerGame_AVG) * 100
                percentage_PassYards_Diff = percentage_PassYards_Diff/2
                
                # Calculate predicted WR Rec Yards as a percentage change from QB's average
                pred_WR_RecYards = WR_RecYards_PerGame * (1 + percentage_PassYards_Diff / 100)
                
                statsToReturn.append(round(pred_WR_RecYards,1))
            
            elif choice == WR_PRED_TOUCHDOWNS:
                
                WR_RecTouchdowns_PerGame = getNFLCalc(playerName, "WideReciever", "WR_Calc_Touchdowns_PerGame")
                WR_RecTouchdowns_PerGame = float(WR_RecTouchdowns_PerGame[0])
                
                vsTeam_PassTouchdowns_Allowed_PerGame =  get_statData(connection, teamName, "defteam_passing_stats", "PassTouchdowns_PerGame")
                vsTeam_PassTouchdowns_Allowed_PerGame = float(vsTeam_PassTouchdowns_Allowed_PerGame)
                
                # Get everyteam's Touchdowns allowed per game
                league_PassTouchdowns_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_PassTouchdowns_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
        
                    league_PassTouchdowns_PerGame_List.append(stat[0])
                    
                # Sum All team's Pass Touchdowns allowed per game
                league_PassTouchdowns_PerGame_Sum = 0   
                for yards in league_PassTouchdowns_PerGame_List:
                    
                    league_PassTouchdowns_PerGame_Sum += float(yards)
                    
                # Calculate the league average of Pass Touchdowns allowed per game
                league_PassTouchdowns_PerGame_AVG = (league_PassTouchdowns_PerGame_Sum/len(league_PassTouchdowns_PerGame_List))
                
                # Calculate Pass Touchdowns allowed difference between versus team and league average as a percentage
                percentage_PassTouchdowns_Diff = ((vsTeam_PassTouchdowns_Allowed_PerGame - league_PassTouchdowns_PerGame_AVG) / league_PassTouchdowns_PerGame_AVG) * 100
                percentage_PassTouchdowns_Diff = percentage_PassTouchdowns_Diff/2
                
                # Calculate predicted WR Rec Touchdowns as a percentage change from QB's average
                pred_WR_RecTouchdowns = WR_RecTouchdowns_PerGame * (1 + percentage_PassTouchdowns_Diff / 100)
                
                statsToReturn.append(round(pred_WR_RecTouchdowns,1))
            
            elif choice == WR_PRED_COMPLETIONS:
                
                WR_Completions_PerGame = getNFLCalc(playerName, "WideReciever", "WR_Calc_Completions_PerGame")
                WR_Completions_PerGame = float(WR_Completions_PerGame[0])
                
                vsTeam_Completions_Allowed_PerGame = get_statData(connection, teamName, "defteam_passing_stats", "Completions_PerGame")
                vsTeam_Completions_Allowed_PerGame = float(vsTeam_Completions_Allowed_PerGame)
                

                # Get every team's completions allowed per game
                league_Completions_PerGame_List = []
                for team in teamNames:
                    
                    statToGet = "DefTeam_Completions_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
                    league_Completions_PerGame_List.append(float(stat[0]))

                # Sum All team's completions allowed per game
                league_Completions_PerGame_Sum = sum(league_Completions_PerGame_List)

                # Calculate the league average of completions allowed per game
                league_Completions_PerGame_AVG = league_Completions_PerGame_Sum / len(league_Completions_PerGame_List)

                # Calculate completions allowed difference between versus team and league average as a percentage
                percentage_Completions_Diff = ((vsTeam_Completions_Allowed_PerGame - league_Completions_PerGame_AVG) / league_Completions_PerGame_AVG) * 100
                percentage_Completions_Diff = percentage_Completions_Diff/2

                # Calculate predicted WR completions as a percentage change from WR's average
                pred_WR_Completions = WR_Completions_PerGame * (1 + percentage_Completions_Diff / 100)

                statsToReturn.append(round(pred_WR_Completions, 1))
                
            elif choice == WR_PRED_YPC:
                
                # Yards Per Catch
                WR_YPC = get_statData(connection, playerName, "wr_total_stats", "Yards_PerReception")
                WR_YPC = float(WR_YPC)
                
                if WR_YPC <= 0.0:
                    WR_YPC = 1.0
                
                vsTeam_YPC_Allowed_PerGame = getNFLStat(teamName, "Defense_Team_Passing", "DefTeam_PassYards_PerCompletion")
                vsTeam_YPC_Allowed_PerGame = float(vsTeam_YPC_Allowed_PerGame[0])
                

                # Get every team's completions allowed per game
                league_YPC_List = []
                for team in teamNames:
                    
                    statToGet = "DefTeam_PassYards_PerCompletion"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
                    league_YPC_List.append(float(stat[0]))

                # Sum All team's completions allowed per game
                league_YPC_Sum = sum(league_YPC_List)

                # Calculate the league average of completions allowed per game
                league_YPC_AVG = league_YPC_Sum / len(league_YPC_List)

                # Calculate completions allowed difference between versus team and league average as a percentage
                percentage_YPC_Diff = ((vsTeam_YPC_Allowed_PerGame - league_YPC_AVG) / league_YPC_AVG) * 100
                percentage_YPC_Diff = percentage_YPC_Diff/2

                # Calculate predicted WR completions as a percentage change from WR's average
                pred_WR_YPC = WR_YPC * (1 + percentage_YPC_Diff / 100)

                statsToReturn.append(round(pred_WR_YPC, 1))
        
        elif category == "TightEnd":
            
            if choice == TE_PRED_RECYARDS:
                
                TE_RecYards_PerGame = getNFLCalc(playerName, "TightEnd", "TE_Calc_RecYards_PerGame")
                TE_RecYards_PerGame = float(TE_RecYards_PerGame[0])
                
                vsTeam_PassYards_Allowed_PerGame =  get_statData(connection, teamName, "defteam_passing_stats", "PassYards_PerGame")
                vsTeam_PassYards_Allowed_PerGame = float(vsTeam_PassYards_Allowed_PerGame)
                
                # Get everyteam's Pass Yards allowed per game
                league_PassYards_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_PassYards_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
        
                    league_PassYards_PerGame_List.append(stat[0])
                    
                # Sum All team's Pass Yards allowed per game
                league_PassYards_PerGame_Sum = 0   
                for yards in league_PassYards_PerGame_List:
                    
                    league_PassYards_PerGame_Sum += float(yards)
                    
                # Calculate the league average of Pass Yards allowed per game
                league_PassYards_PerGame_AVG = (league_PassYards_PerGame_Sum/len(league_PassYards_PerGame_List))
                
                # Calculate Pass Yards allowed difference between versus team and league average as a percentage
                percentage_PassYards_Diff = ((vsTeam_PassYards_Allowed_PerGame - league_PassYards_PerGame_AVG) / league_PassYards_PerGame_AVG) * 100
                percentage_PassYards_Diff = percentage_PassYards_Diff/2
                
                # Calculate predicted TE Rec Yards as a percentage change from QB's average
                pred_TE_RecYards = TE_RecYards_PerGame * (1 + percentage_PassYards_Diff / 100)
                
                statsToReturn.append(round(pred_TE_RecYards,1))
            
            elif choice == TE_PRED_TOUCHDOWNS:
                
                TE_RecTouchdowns_PerGame = getNFLCalc(playerName, "TightEnd", "TE_Calc_Touchdowns_PerGame")
                TE_RecTouchdowns_PerGame = float(TE_RecTouchdowns_PerGame[0])
                
                vsTeam_PassTouchdowns_Allowed_PerGame =  get_statData(connection, teamName, "defteam_passing_stats", "PassTouchdowns_PerGame")
                vsTeam_PassTouchdowns_Allowed_PerGame = float(vsTeam_PassTouchdowns_Allowed_PerGame)
                
                # Get everyteam's Touchdowns allowed per game
                league_PassTouchdowns_PerGame_List= []
                for team in teamNames:
                    
                    statToGet = "DefTeam_PassTouchdowns_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
        
                    league_PassTouchdowns_PerGame_List.append(stat[0])
                    
                # Sum All team's Pass Touchdowns allowed per game
                league_PassTouchdowns_PerGame_Sum = 0   
                for yards in league_PassTouchdowns_PerGame_List:
                    
                    league_PassTouchdowns_PerGame_Sum += float(yards)
                    
                # Calculate the league average of Pass Touchdowns allowed per game
                league_PassTouchdowns_PerGame_AVG = (league_PassTouchdowns_PerGame_Sum/len(league_PassTouchdowns_PerGame_List))
                
                # Calculate Pass Touchdowns allowed difference between versus team and league average as a percentage
                percentage_PassTouchdowns_Diff = ((vsTeam_PassTouchdowns_Allowed_PerGame - league_PassTouchdowns_PerGame_AVG) / league_PassTouchdowns_PerGame_AVG) * 100
                percentage_PassTouchdowns_Diff = percentage_PassTouchdowns_Diff/2
                
                # Calculate predicted TE Rec Touchdowns as a percentage change from QB's average
                pred_TE_RecTouchdowns = TE_RecTouchdowns_PerGame * (1 + percentage_PassTouchdowns_Diff / 100)
                
                statsToReturn.append(round(pred_TE_RecTouchdowns,1))    
    
            elif choice == TE_PRED_COMPLETIONS:
                
                TE_Completions_PerGame = getNFLCalc(playerName, "TightEnd", "TE_Calc_Completions_PerGame")
                TE_Completions_PerGame = float(TE_Completions_PerGame[0])
                
                vsTeam_Completions_Allowed_PerGame = get_statData(connection, teamName, "defteam_passing_stats", "Completions_PerGame")
                vsTeam_Completions_Allowed_PerGame = float(vsTeam_Completions_Allowed_PerGame)
                

                # Get every team's completions allowed per game
                league_Completions_PerGame_List = []
                for team in teamNames:
                    
                    statToGet = "DefTeam_Completions_PerGame"
                    stat = getNFLStat(team, "Defense_Team_Passing", statToGet)
                    league_Completions_PerGame_List.append(float(stat[0]))

                # Sum All team's completions allowed per game
                league_Completions_PerGame_Sum = sum(league_Completions_PerGame_List)

                # Calculate the league average of completions allowed per game
                league_Completions_PerGame_AVG = league_Completions_PerGame_Sum / len(league_Completions_PerGame_List)

                # Calculate completions allowed difference between versus team and league average as a percentage
                percentage_Completions_Diff = ((vsTeam_Completions_Allowed_PerGame - league_Completions_PerGame_AVG) / league_Completions_PerGame_AVG) * 100
                percentage_Completions_Diff = percentage_Completions_Diff/2

                # Calculate predicted TE completions as a percentage change from TE's average
                pred_TE_Completions = TE_Completions_PerGame * (1 + percentage_Completions_Diff / 100)

                statsToReturn.append(round(pred_TE_Completions, 1))
 
        
               
    connection.close()  
     
    return statsToReturn 

def getNBAPred(*args):
    
    playerName = ""
    teamName = ""
    
    
    category = args[1]
    
    userChoices = []
    statsToReturn = []
    
    teamNames = ["Boston", "Brooklyn", "New York", "Philadelphia", "Toronto", "Chicago", "Cleveland", "Detroit", "Indiana", "Milwaukee",
                 "Atlanta", "Charlotte", "Miami", "Orlando", "Washington", "Denver", "Minnesota", "Okla City", "Portland", "Utah",
                 "Golden State", "LA Clippers", "LA Lakers", "Phoenix", "Sacramento", "Dallas", "Houston", "Memphis", "New Orleans", "San Antonio"]
    
    if args[0] in teamNames:
        
        teamName = args[0]
        
        if args[2] in teamNames:
            
            teamName2 = args[2]
            
            for arg in args[3:]:
                
                userChoices.append(arg)
        
        else:        
            for arg in args[2:]:
                userChoices.append(arg)
        
    else:
        
        playerName = args[0]
        
        if args[2] in teamNames:
            
            teamName = args[2]
            
            for arg in args[3:]:
                userChoices.append(arg)
            
        else:
            
            for arg in args[2:]:
                userChoices.append(arg)
    
    connection = create_connection("nba_stats")
    
               
    # ----Stat Call Commands----
    
    # Offensive scoring
    PLAYER_PRED_POINTS = "Player_Pred_Points"
    #Test Model
    PLAYER_PRED_POINTS2 = "Player_Pred_Points2"
    PLAYER_PRED_POINTS3 = "Player_Pred_Points3"
    
    PLAYER_PRED_ASSISTS = "Player_Pred_Assists"
    PLAYER_PRED_THREES = "Player_Pred_Threes"
    #Test Model
    PLAYER_PRED_THREES2 = "Player_Pred_Threes2"
    PLAYER_PRED_THREES3 = "Player_Pred_Threes3"
    PLAYER_PRED_FIELDGOALS = "Player_Pred_FieldGoals"
    #Test Model
    PLAYER_PRED_FIELDGOALS2 = "Player_Pred_FieldGoals2"
    PLAYER_PRED_FIELDGOALS3 = "Player_Pred_FieldGoals3"
    
    PLAYER_PRED_REBOUNDS = "Player_Pred_Rebounds"
    # DEFENSE
    PLAYER_PRED_STEALS = "Player_Pred_Steals"
    PLAYER_PRED_BLOCKS = "Player_Pred_Blocks"
    PLAYER_PRED_DEFTURNOVERS = "Player_Pred_DefTurnovers"
    
    # TEAM MISC
    TEAM_PRED_POINTS = "Team_Pred_Points"
    TEAM_PRED_POINTS_Test = "Team_Pred_Points_Test"
    TEAM_PRED_POINTS_Test2 = "Team_Pred_Points_Test2"
    TEAM_PRED_POINTS_Test3 = "Team_Pred_Points_Test3"
    TEAM_PRED_POINTS_Test4 = "Team_Pred_Points_Test4"
    TEAM_PRED_POINTS_Test5 = "Team_Pred_Points_Test5"
    TEAM_PRED_POINTS_Test6 = "Team_Pred_Points_Test6"
    TEAM_PRED_OVERUNDER = "Team_Pred_OverUnder"
    TEAM_PRED_MONEYLINE = "Team_Pred_MoneyLine"
    
    for choice in userChoices:
        
        if category == "Offense":
            
            if choice == PLAYER_PRED_POINTS:
                
                player_Pred_FieldGoals = getNBAPred(playerName, "Offense",teamName, "Player_Pred_FieldGoals")
                player_Pred_FieldGoals = player_Pred_FieldGoals[0]
                
                player_Pred_Threes = getNBAPred(playerName, "Offense",teamName, "Player_Pred_Threes")
                player_Pred_Threes = player_Pred_Threes[0]
                
                player_Pred_Points = (player_Pred_FieldGoals * 2) + (player_Pred_Threes * 3)
                
                statsToReturn.append(player_Pred_Points)
                
            elif choice == PLAYER_PRED_POINTS2:
                
                player_Pred_FieldGoals = getNBAPred(playerName, "Offense",teamName, "Player_Pred_FieldGoals2")
                player_Pred_FieldGoals = player_Pred_FieldGoals[0]
                
                player_Pred_Threes = getNBAPred(playerName, "Offense",teamName, "Player_Pred_Threes2")
                player_Pred_Threes = player_Pred_Threes[0]
                
                player_Pred_Points = (player_Pred_FieldGoals * 2) + (player_Pred_Threes * 3)
                
                statsToReturn.append(player_Pred_Points)
                
            elif choice == PLAYER_PRED_POINTS3:
                
                player_Pred_FieldGoals = getNBAPred(playerName, "Offense",teamName, "Player_Pred_FieldGoals3")
                player_Pred_FieldGoals = player_Pred_FieldGoals[0]
                
                player_Pred_Threes = getNBAPred(playerName, "Offense",teamName, "Player_Pred_Threes3")
                player_Pred_Threes = player_Pred_Threes[0]
                
                player_Pred_Points = (player_Pred_FieldGoals * 2) + (player_Pred_Threes * 3)
                
                statsToReturn.append(player_Pred_Points)
                
            elif choice == PLAYER_PRED_ASSISTS:
                
                teams_Avg_Assists_PerGameAllowed = []
                
                player_Assists_PerGame = getNBAStat(playerName, "Player_Assists_Turnovers", "Player_Assists_PerGame")
                player_Assists_PerGame = player_Assists_PerGame[0]
                
                vs_team_AssistsAllowed_PerGame = getNBAStat(teamName, "Team_Opp_Misc", "Team_Opp_Assists_PerGame")
                vs_team_AssistsAllowed_PerGame = vs_team_AssistsAllowed_PerGame[0]
                
                for team in teamNames:
                    
                    team_AssistsAllowed = getNBAStat(team, "Team_Opp_Misc", "Team_Opp_Assists_PerGame")
                    team_AssistsAllowed = team_AssistsAllowed[0]
                    teams_Avg_Assists_PerGameAllowed.append(team_AssistsAllowed)
                    
                league_Avg_AssistsAllowed = sum(teams_Avg_Assists_PerGameAllowed) / len(teams_Avg_Assists_PerGameAllowed)
                
                if league_Avg_AssistsAllowed != 0:
                    
                    if vs_team_AssistsAllowed_PerGame < league_Avg_AssistsAllowed:
                    
                        percentage_difference = (vs_team_AssistsAllowed_PerGame / league_Avg_AssistsAllowed) -1
                        
                    elif vs_team_AssistsAllowed_PerGame >= league_Avg_AssistsAllowed:
                        
                        percentage_difference = (vs_team_AssistsAllowed_PerGame / league_Avg_AssistsAllowed)
                  
                adjusted_player_Assists_PerGame = player_Assists_PerGame * (1 + (2 * percentage_difference)/100)
                
                statsToReturn.append(adjusted_player_Assists_PerGame)
        
            elif choice == PLAYER_PRED_THREES:
                
                teams_Avg_ThreesAttempted_PerGameAllowed_List = []
                teams_Avg_ThreesPerc_PerGameAllowed_List = []
                
                player_threeAttempts_Total = getNBAStat(playerName,"Player_Scoring", "Player_ThreePointers_Attempted")
                player_threeAttempts_Total = player_threeAttempts_Total[0]
                
                player_GamesPlayed = getNBAStat(playerName,"Player_Misc", "Player_GamesPlayed")
                player_GamesPlayed = player_GamesPlayed[0]
                
                if player_threeAttempts_Total != 0 and player_GamesPlayed != 0:
                    player_threeAttempts_PerGame = player_threeAttempts_Total/player_GamesPlayed
                    
                else:
                    
                    player_threeAttempts_PerGame = 1
                    
                player_threePoint_Perc = getNBAStat(playerName,"Player_Scoring", "Player_ThreePointers_Perc")
                player_threePoint_Perc = player_threePoint_Perc[0]
                
                vs_Team_ThreePointers_Attempted_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_ThreePointer_Attempts_PerGame")
                vs_Team_ThreePointers_Attempted_PerGame = vs_Team_ThreePointers_Attempted_PerGame[0]
                
                for team in teamNames:
                    
                    team_ThreePointers_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_ThreePointer_Attempts_PerGame")
                    team_ThreePointers_Attempted_PerGame = team_ThreePointers_Attempted_PerGame[0]
                    
                    teams_Avg_ThreesAttempted_PerGameAllowed_List.append(team_ThreePointers_Attempted_PerGame)
                    
                league_Avg_Threes_PerGameAllowedSum = sum(teams_Avg_ThreesAttempted_PerGameAllowed_List) / len(teams_Avg_ThreesAttempted_PerGameAllowed_List)
                
                if league_Avg_Threes_PerGameAllowedSum != 0:
                    
                    if vs_Team_ThreePointers_Attempted_PerGame < league_Avg_Threes_PerGameAllowedSum:
                    
                        percentage_difference_Attempts = ((vs_Team_ThreePointers_Attempted_PerGame - league_Avg_Threes_PerGameAllowedSum) / league_Avg_Threes_PerGameAllowedSum) -1
                        
                    elif vs_Team_ThreePointers_Attempted_PerGame >= league_Avg_Threes_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = ((vs_Team_ThreePointers_Attempted_PerGame - league_Avg_Threes_PerGameAllowedSum) / league_Avg_Threes_PerGameAllowedSum)
                    
                adjusted_player_ThreesAttempts_PerGame = player_threeAttempts_PerGame * (1 + (5 * percentage_difference_Attempts)/100)
                
                
                vs_Team_ThreePointers_Perc_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_ThreePoint_Perc")
                vs_Team_ThreePointers_Perc_PerGame = vs_Team_ThreePointers_Perc_PerGame[0]
                
                for team in teamNames:
                    
                    team_ThreePointersPerc_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_ThreePoint_Perc")
                    team_ThreePointersPerc_PerGame = team_ThreePointersPerc_PerGame[0]
                    
                    teams_Avg_ThreesPerc_PerGameAllowed_List.append(team_ThreePointersPerc_PerGame)
                    
                league_Avg_ThreesPerc_PerGameAllowedSum = sum(teams_Avg_ThreesPerc_PerGameAllowed_List) / len(teams_Avg_ThreesPerc_PerGameAllowed_List)
                
                if league_Avg_ThreesPerc_PerGameAllowedSum != 0:
                    
                    if vs_Team_ThreePointers_Perc_PerGame < league_Avg_ThreesPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = (vs_Team_ThreePointers_Perc_PerGame / league_Avg_ThreesPerc_PerGameAllowedSum) -1
                        
                    elif vs_Team_ThreePointers_Perc_PerGame > league_Avg_ThreesPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = (vs_Team_ThreePointers_Perc_PerGame / league_Avg_ThreesPerc_PerGameAllowedSum)
                    
                adjusted_player_ThreesPerc_PerGame = player_threePoint_Perc * (1 + (5 * percentage_difference_Perc)/100)
                
                player_Pred_Threes = adjusted_player_ThreesAttempts_PerGame * (adjusted_player_ThreesPerc_PerGame/100)
                
                statsToReturn.append(player_Pred_Threes)
            
            elif choice == PLAYER_PRED_THREES2:
                
                teams_Avg_ThreesAttempted_PerGameAllowed_List = []
                teams_Avg_ThreesPerc_PerGameAllowed_List = []
                
                player_threeAttempts_Total = getNBAStat(playerName,"Player_Scoring", "Player_ThreePointers_Attempted")
                player_threeAttempts_Total = player_threeAttempts_Total[0]
                
                player_GamesPlayed = getNBAStat(playerName,"Player_Misc", "Player_GamesPlayed")
                player_GamesPlayed = player_GamesPlayed[0]
                
                if player_threeAttempts_Total != 0 and player_GamesPlayed != 0:
                    player_threeAttempts_PerGame = player_threeAttempts_Total/player_GamesPlayed
                    
                else:
                    
                    player_threeAttempts_PerGame = 1
                    
                player_threePoint_Perc = getNBAStat(playerName,"Player_Scoring", "Player_ThreePointers_Perc")
                player_threePoint_Perc = player_threePoint_Perc[0]
                
                vs_Team_ThreePointers_Attempted_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_ThreePointer_Attempts_PerGame")
                vs_Team_ThreePointers_Attempted_PerGame = vs_Team_ThreePointers_Attempted_PerGame[0]
                
                for team in teamNames:
                    
                    team_ThreePointers_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_ThreePointer_Attempts_PerGame")
                    team_ThreePointers_Attempted_PerGame = team_ThreePointers_Attempted_PerGame[0]
                    
                    teams_Avg_ThreesAttempted_PerGameAllowed_List.append(team_ThreePointers_Attempted_PerGame)
                    
                league_Avg_Threes_PerGameAllowedSum = sum(teams_Avg_ThreesAttempted_PerGameAllowed_List) / len(teams_Avg_ThreesAttempted_PerGameAllowed_List)
                
                if league_Avg_Threes_PerGameAllowedSum != 0:
                    
                    if vs_Team_ThreePointers_Attempted_PerGame < league_Avg_Threes_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_ThreePointers_Attempted_PerGame / league_Avg_Threes_PerGameAllowedSum) - 1
                
                    elif vs_Team_ThreePointers_Attempted_PerGame >= league_Avg_Threes_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_ThreePointers_Attempted_PerGame / league_Avg_Threes_PerGameAllowedSum)
                
                adjusted_player_ThreesAttempts_PerGame = player_threeAttempts_PerGame * (1 + (10 * percentage_difference_Attempts)/100)
                
                
                vs_Team_ThreePointers_Perc_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_ThreePoint_Perc")
                vs_Team_ThreePointers_Perc_PerGame = vs_Team_ThreePointers_Perc_PerGame[0]
                
                for team in teamNames:
                    
                    team_ThreePointersPerc_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_ThreePoint_Perc")
                    team_ThreePointersPerc_PerGame = team_ThreePointersPerc_PerGame[0]
                    
                    teams_Avg_ThreesPerc_PerGameAllowed_List.append(team_ThreePointersPerc_PerGame)
                    
                league_Avg_ThreesPerc_PerGameAllowedSum = sum(teams_Avg_ThreesPerc_PerGameAllowed_List) / len(teams_Avg_ThreesPerc_PerGameAllowed_List)
                
                if league_Avg_ThreesPerc_PerGameAllowedSum != 0:
                    
                    if vs_Team_ThreePointers_Perc_PerGame < league_Avg_ThreesPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_ThreePointers_Perc_PerGame - league_Avg_ThreesPerc_PerGameAllowedSum) / league_Avg_ThreesPerc_PerGameAllowedSum)-1
                        
                    elif vs_Team_ThreePointers_Perc_PerGame >= league_Avg_ThreesPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_ThreePointers_Perc_PerGame - league_Avg_ThreesPerc_PerGameAllowedSum) / league_Avg_ThreesPerc_PerGameAllowedSum)
                
                adjusted_player_ThreesPerc_PerGame = player_threePoint_Perc * (1 + (10 * percentage_difference_Perc)/100)
                
                player_Pred_Threes = adjusted_player_ThreesAttempts_PerGame * (adjusted_player_ThreesPerc_PerGame/100)
                
                statsToReturn.append(player_Pred_Threes)
            
            elif choice == PLAYER_PRED_THREES3:
                
                teams_Avg_ThreesAttempted_PerGameAllowed_List = []
                teams_Avg_ThreesPerc_PerGameAllowed_List = []
                
                player_threeAttempts_Total = getNBAStat(playerName,"Player_Scoring", "Player_ThreePointers_Attempted")
                player_threeAttempts_Total = player_threeAttempts_Total[0]
                
                player_GamesPlayed = getNBAStat(playerName,"Player_Misc", "Player_GamesPlayed")
                player_GamesPlayed = player_GamesPlayed[0]
                
                if player_threeAttempts_Total != 0 and player_GamesPlayed != 0:
                    player_threeAttempts_PerGame = player_threeAttempts_Total/player_GamesPlayed
                    
                else:
                    
                    player_threeAttempts_PerGame = 1
                    
                player_threePoint_Perc = getNBAStat(playerName,"Player_Scoring", "Player_ThreePointers_Perc")
                player_threePoint_Perc = player_threePoint_Perc[0]
                
                vs_Team_ThreePointers_Attempted_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_ThreePointer_Attempts_PerGame")
                vs_Team_ThreePointers_Attempted_PerGame = vs_Team_ThreePointers_Attempted_PerGame[0]
                
                for team in teamNames:
                    
                    team_ThreePointers_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_ThreePointer_Attempts_PerGame")
                    team_ThreePointers_Attempted_PerGame = team_ThreePointers_Attempted_PerGame[0]
                    
                    teams_Avg_ThreesAttempted_PerGameAllowed_List.append(team_ThreePointers_Attempted_PerGame)
                    
                league_Avg_Threes_PerGameAllowedSum = sum(teams_Avg_ThreesAttempted_PerGameAllowed_List) / len(teams_Avg_ThreesAttempted_PerGameAllowed_List)
                
                if league_Avg_Threes_PerGameAllowedSum != 0:
                    
                    if vs_Team_ThreePointers_Attempted_PerGame < league_Avg_Threes_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_ThreePointers_Attempted_PerGame / league_Avg_Threes_PerGameAllowedSum)-1
                        
                    elif vs_Team_ThreePointers_Attempted_PerGame >= league_Avg_Threes_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_ThreePointers_Attempted_PerGame / league_Avg_Threes_PerGameAllowedSum)
                
                
                adjusted_player_ThreesAttempts_PerGame = player_threeAttempts_PerGame * (1 + (30 * percentage_difference_Attempts)/100)
                
                
                vs_Team_ThreePointers_Perc_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_ThreePoint_Perc")
                vs_Team_ThreePointers_Perc_PerGame = vs_Team_ThreePointers_Perc_PerGame[0]
                
                for team in teamNames:
                    
                    team_ThreePointersPerc_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_ThreePoint_Perc")
                    team_ThreePointersPerc_PerGame = team_ThreePointersPerc_PerGame[0]
                    
                    teams_Avg_ThreesPerc_PerGameAllowed_List.append(team_ThreePointersPerc_PerGame)
                    
                league_Avg_ThreesPerc_PerGameAllowedSum = sum(teams_Avg_ThreesPerc_PerGameAllowed_List) / len(teams_Avg_ThreesPerc_PerGameAllowed_List)
                
                if league_Avg_ThreesPerc_PerGameAllowedSum != 0:
                    
                    if vs_Team_ThreePointers_Perc_PerGame < league_Avg_ThreesPerc_PerGameAllowedSum:
                    
                        percentage_difference_Perc = ((vs_Team_ThreePointers_Perc_PerGame - league_Avg_ThreesPerc_PerGameAllowedSum) / league_Avg_ThreesPerc_PerGameAllowedSum)-1
                        
                    elif vs_Team_ThreePointers_Perc_PerGame >= league_Avg_ThreesPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_ThreePointers_Perc_PerGame - league_Avg_ThreesPerc_PerGameAllowedSum) / league_Avg_ThreesPerc_PerGameAllowedSum)
                
                
                
                adjusted_player_ThreesPerc_PerGame = player_threePoint_Perc * (1+(30 * percentage_difference_Perc)/100)
                
                player_Pred_Threes = adjusted_player_ThreesAttempts_PerGame * (adjusted_player_ThreesPerc_PerGame/100)
                
                statsToReturn.append(player_Pred_Threes)
            
            elif choice == PLAYER_PRED_FIELDGOALS:
                
                # Assign Lists for teams average Field Goals Attempted
                teams_Avg_FieldGoalsAttempted_PerGameAllowed_List = []
                teams_Avg_FieldGoalPerc_PerGameAllowed_List = []
                
                # Get Player's Field Goals Attempted Total
                player_FieldGoalAttempts_Total = getNBAStat(playerName,"Player_Scoring", "Player_FieldGoals_Attempted")
                player_FieldGoalAttempts_Total = player_FieldGoalAttempts_Total[0]
                
                # Get Player's total played games
                player_GamesPlayed = getNBAStat(playerName,"Player_Misc", "Player_GamesPlayed")
                player_GamesPlayed = player_GamesPlayed[0]
                
                # Calculate Player's Field goal attempts per game
                if player_FieldGoalAttempts_Total != 0 and player_FieldGoalAttempts_Total != 0:
                    player_FieldGoalAttempts_PerGame = player_FieldGoalAttempts_Total/player_GamesPlayed
                    
                else:
                    
                    player_FieldGoalAttempts_PerGame = 1
                
                # Get Player's field goal percentage 
                player_FieldGoal_Perc = getNBAStat(playerName,"Player_Scoring", "Player_FieldGoal_Perc")
                player_FieldGoal_Perc = player_FieldGoal_Perc[0]
                
                # Get versus team's allowed field goal attempts per game
                vs_Team_FieldGoals_Attempted_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                vs_Team_FieldGoals_Attempted_PerGame = vs_Team_FieldGoals_Attempted_PerGame[0]
                
                # Get and calculate the league average for field goal attempts per game
                for team in teamNames:
                    
                    team_FieldGoals_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                    team_FieldGoals_Attempted_PerGame = team_FieldGoals_Attempted_PerGame[0]
                    
                    teams_Avg_FieldGoalsAttempted_PerGameAllowed_List.append(team_FieldGoals_Attempted_PerGame)
                    
                league_Avg_FieldGoals_PerGameAllowedSum = sum(teams_Avg_FieldGoalsAttempted_PerGameAllowed_List) / len(teams_Avg_FieldGoalsAttempted_PerGameAllowed_List)
                
                # Calculate adjusted player's attempted field goals per game
                if league_Avg_FieldGoals_PerGameAllowedSum != 0:
                    
                    if vs_Team_FieldGoals_Attempted_PerGame <  league_Avg_FieldGoals_PerGameAllowedSum:
                        percentage_difference_Attempts = (vs_Team_FieldGoals_Attempted_PerGame / league_Avg_FieldGoals_PerGameAllowedSum) - 1
                        
                    elif vs_Team_FieldGoals_Attempted_PerGame >=  league_Avg_FieldGoals_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_FieldGoals_Attempted_PerGame / league_Avg_FieldGoals_PerGameAllowedSum)
                    
                adjusted_player_FieldGoalsAttempts_PerGame = player_FieldGoalAttempts_PerGame * (1 + (5 * percentage_difference_Attempts)/100)
                
                # Get versus team's Field Goals allowed per game
                vs_Team_FieldGoals_Allowed_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_FieldGoals_PerGame")
                vs_Team_FieldGoals_Allowed_PerGame = vs_Team_FieldGoals_Allowed_PerGame[0]
                
                # Calculate versus team's field goal percentage allowed per game
                vs_Team_FieldGoals_Perc_PerGame = vs_Team_FieldGoals_Allowed_PerGame/vs_Team_FieldGoals_Attempted_PerGame
                
                # Get and calculate the league's average field goals allowed per game
                for team in teamNames:
                    
                    team_FieldGoals_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoals_PerGame")
                    team_FieldGoals_PerGame = team_FieldGoals_PerGame[0]
                    
                    team_FieldGoals_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                    team_FieldGoals_Attempted_PerGame = team_FieldGoals_Attempted_PerGame[0]
                    
                    team_FieldGoal_Perc_PerGame = team_FieldGoals_PerGame/team_FieldGoals_Attempted_PerGame
                    
                    teams_Avg_FieldGoalPerc_PerGameAllowed_List.append(team_FieldGoal_Perc_PerGame)
                    
                league_Avg_FieldGoalsPerc_PerGameAllowedSum = sum(teams_Avg_FieldGoalPerc_PerGameAllowed_List) / len(teams_Avg_FieldGoalPerc_PerGameAllowed_List)
                
                # Calculate adjusted player's attempted field goals per game
                if league_Avg_FieldGoalsPerc_PerGameAllowedSum != 0:
                    
                    if vs_Team_FieldGoals_Perc_PerGame < league_Avg_FieldGoalsPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_FieldGoals_Perc_PerGame - league_Avg_FieldGoalsPerc_PerGameAllowedSum) / league_Avg_FieldGoalsPerc_PerGameAllowedSum) - 1
                        
                    elif  vs_Team_FieldGoals_Perc_PerGame >= league_Avg_FieldGoalsPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_FieldGoals_Perc_PerGame - league_Avg_FieldGoalsPerc_PerGameAllowedSum) / league_Avg_FieldGoalsPerc_PerGameAllowedSum)
                    
                adjusted_player_FieldGoalPerc_PerGame = player_FieldGoal_Perc * (1 + (5 * percentage_difference_Perc)/100)
                
                # Calculate Player's predicted field goals 
                player_Pred_FieldGoals = adjusted_player_FieldGoalsAttempts_PerGame * (adjusted_player_FieldGoalPerc_PerGame/100)
                
                statsToReturn.append(player_Pred_FieldGoals)
             
            elif choice == PLAYER_PRED_FIELDGOALS2:
                
                # Assign Lists for teams average Field Goals Attempted
                teams_Avg_FieldGoalsAttempted_PerGameAllowed_List = []
                teams_Avg_FieldGoalPerc_PerGameAllowed_List = []
                
                # Get Player's Field Goals Attempted Total
                player_FieldGoalAttempts_Total = getNBAStat(playerName,"Player_Scoring", "Player_FieldGoals_Attempted")
                player_FieldGoalAttempts_Total = player_FieldGoalAttempts_Total[0]
                
                # Get Player's total played games
                player_GamesPlayed = getNBAStat(playerName,"Player_Misc", "Player_GamesPlayed")
                player_GamesPlayed = player_GamesPlayed[0]
                
                # Calculate Player's Field goal attempts per game
                if player_FieldGoalAttempts_Total != 0 and player_FieldGoalAttempts_Total != 0:
                    player_FieldGoalAttempts_PerGame = player_FieldGoalAttempts_Total/player_GamesPlayed
                    
                else:
                    
                    player_FieldGoalAttempts_PerGame = 1
                
                # Get Player's field goal percentage 
                player_FieldGoal_Perc = getNBAStat(playerName,"Player_Scoring", "Player_FieldGoal_Perc")
                player_FieldGoal_Perc = player_FieldGoal_Perc[0]
                
                # Get versus team's allowed field goal attempts per game
                vs_Team_FieldGoals_Attempted_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                vs_Team_FieldGoals_Attempted_PerGame = vs_Team_FieldGoals_Attempted_PerGame[0]
                
                # Get and calculate the league average for field goal attempts per game
                for team in teamNames:
                    
                    team_FieldGoals_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                    team_FieldGoals_Attempted_PerGame = team_FieldGoals_Attempted_PerGame[0]
                    
                    teams_Avg_FieldGoalsAttempted_PerGameAllowed_List.append(team_FieldGoals_Attempted_PerGame)
                    
                league_Avg_FieldGoals_PerGameAllowedSum = sum(teams_Avg_FieldGoalsAttempted_PerGameAllowed_List) / len(teams_Avg_FieldGoalsAttempted_PerGameAllowed_List)
                
                # Calculate adjusted player's attempted field goals per game
                if league_Avg_FieldGoals_PerGameAllowedSum != 0:
                    
                    if vs_Team_FieldGoals_Attempted_PerGame < league_Avg_FieldGoals_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_FieldGoals_Attempted_PerGame / league_Avg_FieldGoals_PerGameAllowedSum) - 1
                        
                    elif vs_Team_FieldGoals_Attempted_PerGame >= league_Avg_FieldGoals_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_FieldGoals_Attempted_PerGame / league_Avg_FieldGoals_PerGameAllowedSum)
                    
                adjusted_player_FieldGoalsAttempts_PerGame = player_FieldGoalAttempts_PerGame * (1 + (10 * percentage_difference_Attempts)/100)
                
                # Get versus team's Field Goals allowed per game
                vs_Team_FieldGoals_Allowed_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_FieldGoals_PerGame")
                vs_Team_FieldGoals_Allowed_PerGame = vs_Team_FieldGoals_Allowed_PerGame[0]
                
                # Calculate versus team's field goal percentage allowed per game
                vs_Team_FieldGoals_Perc_PerGame = vs_Team_FieldGoals_Allowed_PerGame/vs_Team_FieldGoals_Attempted_PerGame
                
                # Get and calculate the league's average field goals allowed per game
                for team in teamNames:
                    
                    team_FieldGoals_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoals_PerGame")
                    team_FieldGoals_PerGame = team_FieldGoals_PerGame[0]
                    
                    team_FieldGoals_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                    team_FieldGoals_Attempted_PerGame = team_FieldGoals_Attempted_PerGame[0]
                    
                    team_FieldGoal_Perc_PerGame = team_FieldGoals_PerGame/team_FieldGoals_Attempted_PerGame
                    
                    teams_Avg_FieldGoalPerc_PerGameAllowed_List.append(team_FieldGoal_Perc_PerGame)
                    
                league_Avg_FieldGoalsPerc_PerGameAllowedSum = sum(teams_Avg_FieldGoalPerc_PerGameAllowed_List) / len(teams_Avg_FieldGoalPerc_PerGameAllowed_List)
                
                # Calculate adjusted player's attempted field goals per game
                if league_Avg_FieldGoalsPerc_PerGameAllowedSum != 0:
                    
                    if vs_Team_FieldGoals_Perc_PerGame < league_Avg_FieldGoalsPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_FieldGoals_Perc_PerGame - league_Avg_FieldGoalsPerc_PerGameAllowedSum) / league_Avg_FieldGoalsPerc_PerGameAllowedSum) - 1
                        
                    elif vs_Team_FieldGoals_Perc_PerGame >= league_Avg_FieldGoalsPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_FieldGoals_Perc_PerGame - league_Avg_FieldGoalsPerc_PerGameAllowedSum) / league_Avg_FieldGoalsPerc_PerGameAllowedSum)
                    
                adjusted_player_FieldGoalPerc_PerGame = player_FieldGoal_Perc * (1 + (10 * percentage_difference_Perc)/100)
                
                # Calculate Player's predicted field goals 
                player_Pred_FieldGoals = adjusted_player_FieldGoalsAttempts_PerGame * (adjusted_player_FieldGoalPerc_PerGame/100)
                
                statsToReturn.append(player_Pred_FieldGoals) 
            
            elif choice == PLAYER_PRED_FIELDGOALS3:
                
                # Assign Lists for teams average Field Goals Attempted
                teams_Avg_FieldGoalsAttempted_PerGameAllowed_List = []
                teams_Avg_FieldGoalPerc_PerGameAllowed_List = []
                
                # Get Player's Field Goals Attempted Total
                player_FieldGoalAttempts_Total = getNBAStat(playerName,"Player_Scoring", "Player_FieldGoals_Attempted")
                player_FieldGoalAttempts_Total = player_FieldGoalAttempts_Total[0]
                
                # Get Player's total played games
                player_GamesPlayed = getNBAStat(playerName,"Player_Misc", "Player_GamesPlayed")
                player_GamesPlayed = player_GamesPlayed[0]
                
                # Calculate Player's Field goal attempts per game
                if player_FieldGoalAttempts_Total != 0 and player_FieldGoalAttempts_Total != 0:
                    player_FieldGoalAttempts_PerGame = player_FieldGoalAttempts_Total/player_GamesPlayed
                    
                else:
                    
                    player_FieldGoalAttempts_PerGame = 1
                
                # Get Player's field goal percentage 
                player_FieldGoal_Perc = getNBAStat(playerName,"Player_Scoring", "Player_FieldGoal_Perc")
                player_FieldGoal_Perc = player_FieldGoal_Perc[0]
                
                # Get versus team's allowed field goal attempts per game
                vs_Team_FieldGoals_Attempted_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                vs_Team_FieldGoals_Attempted_PerGame = vs_Team_FieldGoals_Attempted_PerGame[0]
                
                # Get and calculate the league average for field goal attempts per game
                for team in teamNames:
                    
                    team_FieldGoals_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                    team_FieldGoals_Attempted_PerGame = team_FieldGoals_Attempted_PerGame[0]
                    
                    teams_Avg_FieldGoalsAttempted_PerGameAllowed_List.append(team_FieldGoals_Attempted_PerGame)
                    
                league_Avg_FieldGoals_PerGameAllowedSum = sum(teams_Avg_FieldGoalsAttempted_PerGameAllowed_List) / len(teams_Avg_FieldGoalsAttempted_PerGameAllowed_List)
                
                # Calculate adjusted player's attempted field goals per game
                if league_Avg_FieldGoals_PerGameAllowedSum != 0:
                    
                    if vs_Team_FieldGoals_Attempted_PerGame < league_Avg_FieldGoals_PerGameAllowedSum:
                    
                        percentage_difference_Attempts = (vs_Team_FieldGoals_Attempted_PerGame / league_Avg_FieldGoals_PerGameAllowedSum) -1
                        
                    elif vs_Team_FieldGoals_Attempted_PerGame >= league_Avg_FieldGoals_PerGameAllowedSum:
                        
                        percentage_difference_Attempts = (vs_Team_FieldGoals_Attempted_PerGame / league_Avg_FieldGoals_PerGameAllowedSum)
                    
                adjusted_player_FieldGoalsAttempts_PerGame = player_FieldGoalAttempts_PerGame * (1 + (20 * percentage_difference_Attempts)/100)
                
                # Get versus team's Field Goals allowed per game
                vs_Team_FieldGoals_Allowed_PerGame = getNBAStat(teamName, "Team_Defensive_Shooting", "Team_Opp_FieldGoals_PerGame")
                vs_Team_FieldGoals_Allowed_PerGame = vs_Team_FieldGoals_Allowed_PerGame[0]
                
                # Calculate versus team's field goal percentage allowed per game
                vs_Team_FieldGoals_Perc_PerGame = vs_Team_FieldGoals_Allowed_PerGame/vs_Team_FieldGoals_Attempted_PerGame
                
                # Get and calculate the league's average field goals allowed per game
                for team in teamNames:
                    
                    team_FieldGoals_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoals_PerGame")
                    team_FieldGoals_PerGame = team_FieldGoals_PerGame[0]
                    
                    team_FieldGoals_Attempted_PerGame = getNBAStat(team, "Team_Defensive_Shooting", "Team_Opp_FieldGoal_Attempts_PerGame")
                    team_FieldGoals_Attempted_PerGame = team_FieldGoals_Attempted_PerGame[0]
                    
                    team_FieldGoal_Perc_PerGame = team_FieldGoals_PerGame/team_FieldGoals_Attempted_PerGame
                    
                    teams_Avg_FieldGoalPerc_PerGameAllowed_List.append(team_FieldGoal_Perc_PerGame)
                    
                league_Avg_FieldGoalsPerc_PerGameAllowedSum = sum(teams_Avg_FieldGoalPerc_PerGameAllowed_List) / len(teams_Avg_FieldGoalPerc_PerGameAllowed_List)
                
                # Calculate adjusted player's attempted field goals per game
                if league_Avg_FieldGoalsPerc_PerGameAllowedSum != 0:
                    
                    if vs_Team_FieldGoals_Perc_PerGame < league_Avg_FieldGoalsPerc_PerGameAllowedSum: 
                    
                        percentage_difference_Perc = ((vs_Team_FieldGoals_Perc_PerGame - league_Avg_FieldGoalsPerc_PerGameAllowedSum) / league_Avg_FieldGoalsPerc_PerGameAllowedSum) -1
                        
                    elif vs_Team_FieldGoals_Perc_PerGame >= league_Avg_FieldGoalsPerc_PerGameAllowedSum:
                        
                        percentage_difference_Perc = ((vs_Team_FieldGoals_Perc_PerGame - league_Avg_FieldGoalsPerc_PerGameAllowedSum) / league_Avg_FieldGoalsPerc_PerGameAllowedSum)
                    
                adjusted_player_FieldGoalPerc_PerGame = player_FieldGoal_Perc * (1 + (20 * percentage_difference_Perc)/100)
                
                # Calculate Player's predicted field goals 
                player_Pred_FieldGoals = adjusted_player_FieldGoalsAttempts_PerGame * (adjusted_player_FieldGoalPerc_PerGame/100)
                
                statsToReturn.append(player_Pred_FieldGoals)
               
            elif choice == PLAYER_PRED_REBOUNDS:
                
                league_Avg_OffRebounds_PerGameAllowed_List = []
                league_Avg_DefRebounds_PerGameAllowed_List = []
                
                # Get Player Offensive Rebounds
                player_OffRebounds = getNBAStat(playerName,"Player_Rebounds", "Player_Offensive_Rebounds")
                player_OffRebounds = player_OffRebounds[0]
                
                # Get Player Defensive Rebounds
                player_DefRebounds = getNBAStat(playerName,"Player_Rebounds", "Player_Defensive_Rebounds")
                player_DefRebounds = player_DefRebounds[0]
                
                #Get Player Games Played
                player_GamesPlayed = getNBAStat(playerName,"Player_Misc", "Player_GamesPlayed")
                player_GamesPlayed = player_GamesPlayed[0]
                
                # Get Opposing Team's Offensive Rebounds Allowed Per Game
                team_Opp_OffRebounds_AllowedPerGame = getNBAStat(teamName, "Team_Opp_Misc", "Team_Opp_OffRebounds_PerGame")
                team_Opp_OffRebounds_AllowedPerGame = team_Opp_OffRebounds_AllowedPerGame[0]
                
                # Get Opposing Team's Defensive Rebounds Allowed Per Game
                team_Opp_DefRebounds_AllowedPerGame = getNBAStat(teamName, "Team_Opp_Misc", "Team_Opp_DefRebounds_PerGame")
                team_Opp_DefRebounds_AllowedPerGame = team_Opp_DefRebounds_AllowedPerGame[0]
                
                # Calculate league average for offensive rebounds
                for team in teamNames:
                    
                    league_Opp_OffRebounds_AllowedPerGame = getNBAStat(team, "Team_Opp_Misc", "Team_Opp_OffRebounds_PerGame")
                    league_Opp_OffRebounds_AllowedPerGame = team_Opp_OffRebounds_AllowedPerGame
                    
                    league_Avg_OffRebounds_PerGameAllowed_List.append(league_Opp_OffRebounds_AllowedPerGame)
                    
                league_Avg_OffRebounds_PerGameAllowedSum = sum(league_Avg_OffRebounds_PerGameAllowed_List) / len(league_Avg_OffRebounds_PerGameAllowed_List)
                
                # Calculate Offensive Rebounds percentage difference from opp team and league
                if league_Avg_OffRebounds_PerGameAllowedSum != 0:
                    
                    if team_Opp_OffRebounds_AllowedPerGame < league_Avg_OffRebounds_PerGameAllowedSum:
                    
                        percentage_difference_OffRebounds = (team_Opp_OffRebounds_AllowedPerGame / league_Avg_OffRebounds_PerGameAllowedSum) - 1
                        
                    elif team_Opp_OffRebounds_AllowedPerGame >= league_Avg_OffRebounds_PerGameAllowedSum:
                        
                        percentage_difference_OffRebounds = (team_Opp_OffRebounds_AllowedPerGame / league_Avg_OffRebounds_PerGameAllowedSum)
                    
                # Calculate league average for defensive rebounds
                for team in teamNames:
                    
                    league_Opp_DefRebounds_AllowedPerGame = getNBAStat(team, "Team_Opp_Misc", "Team_Opp_DefRebounds_PerGame")
                    league_Opp_DefRebounds_AllowedPerGame = team_Opp_DefRebounds_AllowedPerGame
                    
                    league_Avg_DefRebounds_PerGameAllowed_List.append(league_Opp_DefRebounds_AllowedPerGame)
                    
                league_Avg_DefRebounds_PerGameAllowedSum = sum(league_Avg_DefRebounds_PerGameAllowed_List) / len(league_Avg_DefRebounds_PerGameAllowed_List)
                
                # Calculate Defensive Rebounds percentage difference from opp team and league
                if league_Avg_DefRebounds_PerGameAllowedSum != 0:
                    
                    if team_Opp_DefRebounds_AllowedPerGame < league_Avg_DefRebounds_PerGameAllowedSum:
                    
                        percentage_difference_DefRebounds = (team_Opp_DefRebounds_AllowedPerGame / league_Avg_DefRebounds_PerGameAllowedSum) - 1
                        
                    elif team_Opp_DefRebounds_AllowedPerGame >= league_Avg_DefRebounds_PerGameAllowedSum:
                        
                        percentage_difference_DefRebounds = (team_Opp_DefRebounds_AllowedPerGame / league_Avg_DefRebounds_PerGameAllowedSum)
                
                # Calculate player offensive rebounds per game
                player_OffRebounds_PerGame = player_OffRebounds/player_GamesPlayed
                
                # Calculate player defensive rebounds per game
                player_DefRebounds_PerGame = player_DefRebounds/player_GamesPlayed
                
                # Calculate adjusted player offensive rebounds
                adjusted_Player_OffRebounds_PerGame = player_OffRebounds_PerGame * (1 + (5 * percentage_difference_OffRebounds)/100)
                
                # Calculate adjusted player defensive rebounds
                adjusted_Player_DefRebounds_PerGame = player_DefRebounds_PerGame * (1 + (5 * percentage_difference_DefRebounds)/100)
                
                # Calculate player's predicted total rebounds
                pred_Player_TotalRebounds = adjusted_Player_OffRebounds_PerGame + adjusted_Player_DefRebounds_PerGame
                
                # Append stat to statsToReturn
                statsToReturn.append(pred_Player_TotalRebounds)
                
        elif category == "Defense":
            
            if choice == PLAYER_PRED_STEALS:

                pass
                
                # Database does not have player steals, only turnovers

            elif choice == PLAYER_PRED_BLOCKS:

                league_Avg_Blocks_PerGameAllowed_List = []

                # Get Player Blocks
                player_Blocks_PerGame = getNBAStat(playerName,"Player_Blocks", "Player_Blocks_PerGame")
                player_Blocks_PerGame = player_Blocks_PerGame[0]

                # Get Opposing Team's Blocks Allowed Per Game
                team_Opp_Blocks_AllowedPerGame = getNBAStat(teamName, "Team_Opp_Misc", "Team_Opp_Blocks_PerGame")
                team_Opp_Blocks_AllowedPerGame = team_Opp_Blocks_AllowedPerGame[0]

                # Calculate league average for offensive rebounds
                for team in teamNames:
                    
                    league_Opp_Blocks_AllowedPerGame = getNBAStat(team, "Team_Opp_Misc", "Team_Opp_Blocks_PerGame")
                    league_Opp_Blocks_AllowedPerGame = team_Opp_Blocks_AllowedPerGame
                    
                    league_Avg_Blocks_PerGameAllowed_List.append(league_Opp_Blocks_AllowedPerGame)
                    
                league_Avg_Blocks_PerGameAllowedSum = sum(league_Avg_Blocks_PerGameAllowed_List) / len(league_Avg_Blocks_PerGameAllowed_List)
        
                # Calculate Offensive Rebounds percentage difference from opp team and league
                if league_Avg_Blocks_PerGameAllowedSum != 0:
                    
                    if team_Opp_Blocks_AllowedPerGame < league_Avg_Blocks_PerGameAllowedSum:
                    
                        percentage_difference_Blocks = (team_Opp_Blocks_AllowedPerGame / league_Avg_Blocks_PerGameAllowedSum) - 1
                        
                    elif team_Opp_Blocks_AllowedPerGame >= league_Avg_Blocks_PerGameAllowedSum:
                        
                        percentage_difference_Blocks = (team_Opp_Blocks_AllowedPerGame / league_Avg_Blocks_PerGameAllowedSum)

                # Calculate adjusted player offensive rebounds
                adjusted_Player_Blocks_PerGame = player_Blocks_PerGame * (1 + (30 * percentage_difference_Blocks)/100)

                statsToReturn.append(adjusted_Player_Blocks_PerGame)

            elif choice == PLAYER_PRED_DEFTURNOVERS:

                pass

        elif category == "Team":
            
            if choice == TEAM_PRED_POINTS:
                
                league_Avg_PointsPerGame_List = []
                
                # Get Teams points per game
                team_Points_PerGame = getNBAStat(teamName, "Team_Offensive_Scoring", "Team_Points_PerGame")
                team_Points_PerGame = team_Points_PerGame[0]
                
                # Get opposing teams points per game
                opp_team_Points_PerGame = getNBAStat(teamName2, "Team_Defensive_Scoring", "Team_Opp_Points_PerGame")
                opp_team_Points_PerGame = opp_team_Points_PerGame[0]
                
                # Calculate league average points per game
                for team in teamNames:
                    
                    league_Team_PointsPerGame = getNBAStat(team, "Team_Defensive_Scoring", "Team_Opp_Points_PerGame")
                    league_Team_PointsPerGame = league_Team_PointsPerGame[0]
                    
                    league_Avg_PointsPerGame_List.append(league_Team_PointsPerGame)

                league_Avg_PointsPerGameSum = sum(league_Avg_PointsPerGame_List)/len(league_Avg_PointsPerGame_List)
                
                # Calculate percentage difference from opposing team and league average
                if league_Avg_PointsPerGameSum != 0:
                    percentage_difference_PointsPerGame = (opp_team_Points_PerGame / league_Avg_PointsPerGameSum)
                
                # Calculate adjusted team points per game   
                adjusted_Team_PointsPerGame = team_Points_PerGame * (1 + (5 * percentage_difference_PointsPerGame)/100)
                
                # Append adjusted team points per game to stats to return
                statsToReturn.append(adjusted_Team_PointsPerGame)

            elif choice == TEAM_PRED_POINTS_Test:
                
                team_Roster = []
                team_Points_List = []
                
                team_Roster = get_NamesFrom_NBARoster(teamName)
                injured_Players = check_NBA_InjuryStatus(teamName)
                
                # Remove any player in team_roster that is also in injured_players
                team_Roster = [player for player in team_Roster if player not in injured_Players]
                
                if len(team_Roster) >=17:
                    
                    minute_Cutoff = 17.5
                    
                elif len(team_Roster) >=15 and len(team_Roster) < 17 :
                    
                    minute_Cutoff = 15.5
                    
                elif len(team_Roster) >=12 and len(team_Roster) < 15:
                    
                    minute_Cutoff = 12.5
                    
                elif len(team_Roster) >=9 and len(team_Roster) < 12:
                    
                    minute_Cutoff = 9.5
                    
                else:
                    
                    minute_Cutoff = 5
                
                for player in team_Roster:
                    
                    result = checkNBA_PlayerHasStats(player)
                    
                    if result:
                    
                        player_Minutes_Played = getNBAStat(player, "Player_Misc", "Player_GamesPlayed")
                        player_Minutes_Played = player_Minutes_Played[0]
                        
                        if player_Minutes_Played > minute_Cutoff:
                        
                            player_Pred_Points = getNBAPred(player, "Offense",teamName2, "Player_Pred_Points")
                            player_Pred_Points = player_Pred_Points[0]
                            
                            team_Points_List.append(player_Pred_Points)
                        
                    else:
                        
                        continue
                    
                team_Points = sum(team_Points_List)
                
                statsToReturn.append(team_Points)
   
            elif choice == TEAM_PRED_POINTS_Test2:
                
                # Connect to your MySQL database
                db_host = '127.0.0.1'  # Replace with your database host
                db_user = 'root'  # Replace with your database username
                db_password = 'root'  # Replace with your database password
                db_name = 'nba_stats'  # Replace with your database name

                conn = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name
                )
                
                cursor = conn.cursor()
                
                if teamName == "Boston":
        
                    team1_short = "bos"
                    
                
                elif teamName == "Brooklyn":
                    
                    team1_short = "bkn"
                    team_short = "brooklyn-nets"
                    
                elif teamName == "New York":
                    
                    team1_short = "ny"
                    
                    
                elif teamName == "Philadelphia":
                    
                    team1_short = "phi"
                    
                    
                elif teamName == "Toronto":
                    
                    team1_short = "tor"
                    

                elif teamName == "Golden State":
                    
                    team1_short = "gs"
                    
                    
                elif teamName == "LA Clippers":
                    
                    team1_short = "lac"
                    
                    
                elif teamName == "LA Lakers":
                    
                    team1_short = "lal"
                    
                    
                elif teamName == "Phoenix": 
                    
                    team1_short = "phx"  
                     
                    
                elif teamName == "Sacramento":
                
                    team1_short = "sac"
                    
                    
                elif teamName == "Chicago":
                    
                    team1_short = "chi"
                    
                    
                elif teamName == "Cleveland":
                    
                    team1_short = "cle"
                    
                    
                elif teamName == "Detroit":
                    
                    team1_short = "det"
                    
                    
                elif teamName == "Indiana":
                    
                    team1_short = "ind"
                    
                
                elif teamName == "Milwaukee":
                    
                    team1_short = "mil"
                    
                    
                elif teamName == "Dallas":
                    
                    team1_short = "dal"
                    
                    
                elif teamName == "Houston":
                    
                    team1_short = "hou"
                    
                    
                elif teamName == "Memphis":
                    
                    team1_short = "mem"
                    
                    
                elif teamName == "New Orleans":
                    
                    team1_short = "no"
                    
                    
                elif teamName == "San Antonio":
                    
                    team1_short = "sa"
                    
                    
                elif teamName == "Atlanta":
                    
                    team1_short = "atl"
                    
                    
                elif teamName == "Charlotte":
                    
                    team1_short = "cha"
                    
                    
                elif teamName == "Miami":
                    
                    team1_short = "mia"   
                     
                    
                elif teamName == "Orlando":
                    
                    team1_short = "orl"
                    
                
                elif teamName == "Washington":
                    
                    team1_short = "wsh"
                    
                    
                elif teamName == "Denver":
                    
                    team1_short = "den"
                    
                    
                elif teamName == "Minnesota":
                    
                    team1_short = "min"
                    
                    
                elif teamName == "Okla City":
                    
                    team1_short = "okc"
                    
                    
                elif teamName == "Portland":
                    
                    team1_short = "por"
                    
                    
                elif teamName == "Utah":
                    
                    team1_short = "utah"
                
                team_Roster = []
                team_Points_List = [] 
                playing_Roster = []  
            
                team_Roster = get_NamesFrom_NBARoster(teamName)
                injured_Players = check_NBA_InjuryStatus(teamName)
                
                # Remove any player in team_roster that is also in injured_players
                team_Roster = [player for player in team_Roster if player not in injured_Players]
                
                playing_Roster = team_Roster.copy()
                
                fourth_String_Players = []
                fifth_String_Players = []
                
                for player in playing_Roster:
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 4"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fourth_String_Players.append(player)
                        
                    else:
                        
                        continue
                    
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 5"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fifth_String_Players.append(player)
                        
                    else:
                        
                        continue
                    
                playing_Roster = [player for player in playing_Roster if player not in fourth_String_Players]
                playing_Roster = [player for player in playing_Roster if player not in fifth_String_Players]
                
                playing_Roster = list(set(playing_Roster))
                
                player_Points_AlreadyAdded = []
                
                for player in injured_Players:
                    
                    query = f"SELECT position, string FROM {team1_short}_roster WHERE Name = %s"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        
                        position, string = result[0]
                        
                        
                        query = f"SELECT Name FROM {team1_short}_roster WHERE Position = '{position}' AND String = '{string+1}'"
                        cursor.execute(query)
                        result = cursor.fetchone()
                        
                        if result:
                            underStudy_Player = result[0]
                            
                            player_Points_AlreadyAdded.append(underStudy_Player)
                            
                            # Get injured Players minutes per game
                            
                            injuredPlayer_MinutesPerGame = getNBAStat(player,"Player_Misc", "Player_Minutes_PerGame")
                            injuredPlayer_MinutesPerGame = injuredPlayer_MinutesPerGame[0]
                            
                            underStudy_PointsPerMinute = getNBACalc(underStudy_Player, "Player", "Player_Points_PerMinute")
                            underStudy_PointsPerMinute = underStudy_PointsPerMinute[0]
                            
                            underStudy_Player_PredPoints = underStudy_PointsPerMinute * injuredPlayer_MinutesPerGame
                            
                            team_Points_List.append(underStudy_Player_PredPoints)
                        
                    else:
                        
                        continue
                        
                playing_Roster = [player for player in playing_Roster if player not in player_Points_AlreadyAdded]
                
                for player in playing_Roster:
                    
                    result = checkNBA_PlayerHasStats(player)
                    
                    if result:
                    
                        
                        
                        player_Pred_Points = getNBAPred(player, "Offense",teamName2, "Player_Pred_Points")
                        player_Pred_Points = player_Pred_Points[0]
                            
                        team_Points_List.append(player_Pred_Points)
                        
                    else:
                        
                        continue
                print(team_Points_List)   
                team_Points = sum(team_Points_List)
                
                # Close the cursor and connection
                cursor.close()
                connection.close()
                
                statsToReturn.append(team_Points)
                    
            elif choice == TEAM_PRED_POINTS_Test3:
                
                # Connect to your MySQL database
                db_host = '127.0.0.1'  # Replace with your database host
                db_user = 'root'  # Replace with your database username
                db_password = 'root'  # Replace with your database password
                db_name = 'nba_stats'  # Replace with your database name

                conn = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name
                )
                
                cursor = conn.cursor()
                
                if teamName == "Boston":
        
                    team1_short = "bos"
                    
                
                elif teamName == "Brooklyn":
                    
                    team1_short = "bkn"
                    team_short = "brooklyn-nets"
                    
                elif teamName == "New York":
                    
                    team1_short = "ny"
                    
                    
                elif teamName == "Philadelphia":
                    
                    team1_short = "phi"
                    
                    
                elif teamName == "Toronto":
                    
                    team1_short = "tor"
                    

                elif teamName == "Golden State":
                    
                    team1_short = "gs"
                    
                    
                elif teamName == "LA Clippers":
                    
                    team1_short = "lac"
                    
                    
                elif teamName == "LA Lakers":
                    
                    team1_short = "lal"
                    
                    
                elif teamName == "Phoenix": 
                    
                    team1_short = "phx"  
                     
                    
                elif teamName == "Sacramento":
                
                    team1_short = "sac"
                    
                    
                elif teamName == "Chicago":
                    
                    team1_short = "chi"
                    
                    
                elif teamName == "Cleveland":
                    
                    team1_short = "cle"
                    
                    
                elif teamName == "Detroit":
                    
                    team1_short = "det"
                    
                    
                elif teamName == "Indiana":
                    
                    team1_short = "ind"
                    
                
                elif teamName == "Milwaukee":
                    
                    team1_short = "mil"
                    
                    
                elif teamName == "Dallas":
                    
                    team1_short = "dal"
                    
                    
                elif teamName == "Houston":
                    
                    team1_short = "hou"
                    
                    
                elif teamName == "Memphis":
                    
                    team1_short = "mem"
                    
                    
                elif teamName == "New Orleans":
                    
                    team1_short = "no"
                    
                    
                elif teamName == "San Antonio":
                    
                    team1_short = "sa"
                    
                    
                elif teamName == "Atlanta":
                    
                    team1_short = "atl"
                    
                    
                elif teamName == "Charlotte":
                    
                    team1_short = "cha"
                    
                    
                elif teamName == "Miami":
                    
                    team1_short = "mia"   
                     
                    
                elif teamName == "Orlando":
                    
                    team1_short = "orl"
                    
                
                elif teamName == "Washington":
                    
                    team1_short = "wsh"
                    
                    
                elif teamName == "Denver":
                    
                    team1_short = "den"
                    
                    
                elif teamName == "Minnesota":
                    
                    team1_short = "min"
                    
                    
                elif teamName == "Okla City":
                    
                    team1_short = "okc"
                    
                    
                elif teamName == "Portland":
                    
                    team1_short = "por"
                    
                    
                elif teamName == "Utah":
                    
                    team1_short = "utah"
                
                team_Roster = []
                team_Points_List = [] 
                playing_Roster = []  
            
                team_Roster = get_NamesFrom_NBARoster(teamName)
                injured_Players = check_NBA_InjuryStatus(teamName)
                
                # Remove any player in team_roster that is also in injured_players
                team_Roster = [player for player in team_Roster if player not in injured_Players]
                
                playing_Roster = team_Roster.copy()
                
                fourth_String_Players = []
                fifth_String_Players = []
                
                for player in playing_Roster:
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 4"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fourth_String_Players.append(player)
                        
                    else:
                        
                        continue
                    
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 5"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fifth_String_Players.append(player)
                        
                    else:
                        
                        continue
                    
                playing_Roster = [player for player in playing_Roster if player not in fourth_String_Players]
                playing_Roster = [player for player in playing_Roster if player not in fifth_String_Players]
                
                playing_Roster = list(set(playing_Roster))
                
                player_Points_AlreadyAdded = []
                
                for player in injured_Players:
                    
                    query = f"SELECT position, string FROM {team1_short}_roster WHERE Name = %s"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        
                        position, string = result[0]
                        
                        
                        query = f"SELECT Name FROM {team1_short}_roster WHERE Position = '{position}' AND String = '{string+1}'"
                        cursor.execute(query)
                        result = cursor.fetchone()
                        
                        if result:
                            underStudy_Player = result[0]
                            
                            player_Points_AlreadyAdded.append(underStudy_Player)
                            
                            # Get injured Players minutes per game
                            
                            injuredPlayer_MinutesPerGame = getNBAStat(player,"Player_Misc", "Player_Minutes_PerGame")
                            injuredPlayer_MinutesPerGame = injuredPlayer_MinutesPerGame[0]
                            
                            underStudy_PointsPerMinute = getNBACalc(underStudy_Player, "Player", "Player_Points_PerMinute")
                            underStudy_PointsPerMinute = underStudy_PointsPerMinute[0]
                            
                            underStudy_Player_PredPoints = underStudy_PointsPerMinute * injuredPlayer_MinutesPerGame
                            
                            team_Points_List.append(underStudy_Player_PredPoints)
                        
                    else:
                        
                        continue
                        
                playing_Roster = [player for player in playing_Roster if player not in player_Points_AlreadyAdded]
                
                for player in playing_Roster:
                    
                    result = checkNBA_PlayerHasStats(player)
                    
                    if result:
                    
                        
                        
                        player_Pred_Points = getNBAPred(player, "Offense",teamName2, "Player_Pred_Points2")
                        player_Pred_Points = player_Pred_Points[0]
                            
                        team_Points_List.append(player_Pred_Points)
                        
                    else:
                        
                        continue
                print(team_Points_List)   
                team_Points = sum(team_Points_List)
                
                # Close the cursor and connection
                cursor.close()
                connection.close()
                
                statsToReturn.append(team_Points)        
             
            elif choice == TEAM_PRED_POINTS_Test4:
                
                # Connect to your MySQL database
                db_host = '127.0.0.1'  # Replace with your database host
                db_user = 'root'  # Replace with your database username
                db_password = 'root'  # Replace with your database password
                db_name = 'nba_stats'  # Replace with your database name

                conn = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name
                )
                
                cursor = conn.cursor()
                
                if teamName == "Boston":
        
                    team1_short = "bos"
                    
                
                elif teamName == "Brooklyn":
                    
                    team1_short = "bkn"
                    team_short = "brooklyn-nets"
                    
                elif teamName == "New York":
                    
                    team1_short = "ny"
                    
                    
                elif teamName == "Philadelphia":
                    
                    team1_short = "phi"
                    
                    
                elif teamName == "Toronto":
                    
                    team1_short = "tor"
                    

                elif teamName == "Golden State":
                    
                    team1_short = "gs"
                    
                    
                elif teamName == "LA Clippers":
                    
                    team1_short = "lac"
                    
                    
                elif teamName == "LA Lakers":
                    
                    team1_short = "lal"
                    
                    
                elif teamName == "Phoenix": 
                    
                    team1_short = "phx"  
                     
                    
                elif teamName == "Sacramento":
                
                    team1_short = "sac"
                    
                    
                elif teamName == "Chicago":
                    
                    team1_short = "chi"
                    
                    
                elif teamName == "Cleveland":
                    
                    team1_short = "cle"
                    
                    
                elif teamName == "Detroit":
                    
                    team1_short = "det"
                    
                    
                elif teamName == "Indiana":
                    
                    team1_short = "ind"
                    
                
                elif teamName == "Milwaukee":
                    
                    team1_short = "mil"
                    
                    
                elif teamName == "Dallas":
                    
                    team1_short = "dal"
                    
                    
                elif teamName == "Houston":
                    
                    team1_short = "hou"
                    
                    
                elif teamName == "Memphis":
                    
                    team1_short = "mem"
                    
                    
                elif teamName == "New Orleans":
                    
                    team1_short = "no"
                    
                    
                elif teamName == "San Antonio":
                    
                    team1_short = "sa"
                    
                    
                elif teamName == "Atlanta":
                    
                    team1_short = "atl"
                    
                    
                elif teamName == "Charlotte":
                    
                    team1_short = "cha"
                    
                    
                elif teamName == "Miami":
                    
                    team1_short = "mia"   
                     
                    
                elif teamName == "Orlando":
                    
                    team1_short = "orl"
                    
                
                elif teamName == "Washington":
                    
                    team1_short = "wsh"
                    
                    
                elif teamName == "Denver":
                    
                    team1_short = "den"
                    
                    
                elif teamName == "Minnesota":
                    
                    team1_short = "min"
                    
                    
                elif teamName == "Okla City":
                    
                    team1_short = "okc"
                    
                    
                elif teamName == "Portland":
                    
                    team1_short = "por"
                    
                    
                elif teamName == "Utah":
                    
                    team1_short = "utah"
                
                team_Roster = []
                team_Points_List = [] 
                playing_Roster = []  
            
                team_Roster = get_NamesFrom_NBARoster(teamName)
                injured_Players = check_NBA_InjuryStatus(teamName)
                
                # Remove any player in team_roster that is also in injured_players
                team_Roster = [player for player in team_Roster if player not in injured_Players]
                
                playing_Roster = team_Roster.copy()
                
                fourth_String_Players = []
                fifth_String_Players = []
                
                for player in playing_Roster:
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 4"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fourth_String_Players.append(player)
                        
                    else:
                        
                        continue
                    
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 5"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fifth_String_Players.append(player)
                        
                    else:
                        
                        continue
                    
                playing_Roster = [player for player in playing_Roster if player not in fourth_String_Players]
                playing_Roster = [player for player in playing_Roster if player not in fifth_String_Players]
                
                playing_Roster = list(set(playing_Roster))
                
                player_Points_AlreadyAdded = []
                
                for player in injured_Players:
                    
                    query = f"SELECT position, string FROM {team1_short}_roster WHERE Name = %s"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        
                        position, string = result[0]
                        
                        
                        query = f"SELECT Name FROM {team1_short}_roster WHERE Position = '{position}' AND String = '{string+1}'"
                        cursor.execute(query)
                        result = cursor.fetchone()
                        
                        if result:
                            underStudy_Player = result[0]
                            
                            player_Points_AlreadyAdded.append(underStudy_Player)
                            
                            # Get injured Players minutes per game
                            
                            injuredPlayer_MinutesPerGame = getNBAStat(player,"Player_Misc", "Player_Minutes_PerGame")
                            injuredPlayer_MinutesPerGame = injuredPlayer_MinutesPerGame[0]
                            
                            underStudy_PointsPerMinute = getNBACalc(underStudy_Player, "Player", "Player_Points_PerMinute")
                            underStudy_PointsPerMinute = underStudy_PointsPerMinute[0]
                            
                            underStudy_Player_PredPoints = underStudy_PointsPerMinute * injuredPlayer_MinutesPerGame
                            
                            team_Points_List.append(underStudy_Player_PredPoints)
                        
                    else:
                        
                        continue
                        
                playing_Roster = [player for player in playing_Roster if player not in player_Points_AlreadyAdded]
                
                for player in playing_Roster:
                    
                    result = checkNBA_PlayerHasStats(player)
                    
                    if result:
                    
                        
                        
                        player_Pred_Points = getNBAPred(player, "Offense",teamName2, "Player_Pred_Points3")
                        player_Pred_Points = player_Pred_Points[0]
                            
                        team_Points_List.append(player_Pred_Points)
                        
                    else:
                        
                        continue
                print(team_Points_List)   
                team_Points = sum(team_Points_List)
                
                # Close the cursor and connection
                cursor.close()
                connection.close()
                
                statsToReturn.append(team_Points) 

            elif choice == TEAM_PRED_POINTS_Test5:

                league_Avg_PointsPerGame_List = []
                
                # Get Teams points per game
                team_Points_PerGame = getNBAStat(teamName, "Team_Offensive_Scoring", "Team_Points_PerGame")
                team_Points_PerGame = team_Points_PerGame[0]
                
                # Get opposing teams points per game
                opp_team_Points_PerGame = getNBAStat(teamName2, "Team_Defensive_Scoring", "Team_Opp_Points_PerGame")
                opp_team_Points_PerGame = opp_team_Points_PerGame[0]
                
                # Calculate league average points per game
                for team in teamNames:
                    
                    league_Team_PointsPerGame = getNBAStat(team, "Team_Defensive_Scoring", "Team_Opp_Points_PerGame")
                    league_Team_PointsPerGame = league_Team_PointsPerGame[0]
                    
                    league_Avg_PointsPerGame_List.append(league_Team_PointsPerGame)

                league_Avg_PointsPerGameSum = sum(league_Avg_PointsPerGame_List)/len(league_Avg_PointsPerGame_List)
                
                # Calculate percentage difference from opposing team and league average
                if league_Avg_PointsPerGameSum != 0:
                    
                    if opp_team_Points_PerGame < league_Avg_PointsPerGameSum:
                    
                        percentage_difference_PointsPerGame = (opp_team_Points_PerGame / league_Avg_PointsPerGameSum) -1
                        
                    elif opp_team_Points_PerGame >= league_Avg_PointsPerGameSum:
                        
                        percentage_difference_PointsPerGame = (opp_team_Points_PerGame / league_Avg_PointsPerGameSum)
                
                # Calculate adjusted team points per game   
                adjusted_Team_PointsPerGame = team_Points_PerGame * (1 + (20 * percentage_difference_PointsPerGame)/100)
                
                # Append adjusted team points per game to stats to return
                statsToReturn.append(adjusted_Team_PointsPerGame)
                
            elif choice == TEAM_PRED_POINTS_Test6:

                league_Avg_PointsPerGame_List = []
                
                # Get Teams points per game
                team_Points_PerGame = getNBAStat(teamName, "Team_Offensive_Scoring", "Team_Points_PerGame")
                team_Points_PerGame = team_Points_PerGame[0]
                
                # Get opposing teams points per game
                opp_team_Points_PerGame = getNBAStat(teamName2, "Team_Defensive_Scoring", "Team_Opp_Points_PerGame")
                opp_team_Points_PerGame = opp_team_Points_PerGame[0]
                
                # Calculate league average points per game
                for team in teamNames:
                    
                    league_Team_PointsPerGame = getNBAStat(team, "Team_Defensive_Scoring", "Team_Opp_Points_PerGame")
                    league_Team_PointsPerGame = league_Team_PointsPerGame[0]
                    
                    league_Avg_PointsPerGame_List.append(league_Team_PointsPerGame)

                league_Avg_PointsPerGameSum = sum(league_Avg_PointsPerGame_List)/len(league_Avg_PointsPerGame_List)
                
                # Calculate percentage difference from opposing team and league average
                if league_Avg_PointsPerGameSum != 0:
                    
                    if opp_team_Points_PerGame < league_Avg_PointsPerGameSum:
                    
                        percentage_difference_PointsPerGame = (opp_team_Points_PerGame / league_Avg_PointsPerGameSum) -1
                        
                    elif opp_team_Points_PerGame >= league_Avg_PointsPerGameSum:
                        
                        percentage_difference_PointsPerGame = (opp_team_Points_PerGame / league_Avg_PointsPerGameSum)
                
                # Calculate adjusted team points per game   
                adjusted_Team_PointsPerGame = team_Points_PerGame * (1 + (10 * percentage_difference_PointsPerGame)/100)
                
                # Append adjusted team points per game to stats to return
                statsToReturn.append(adjusted_Team_PointsPerGame)

            elif choice == TEAM_PRED_OVERUNDER:
                
                team1_Points = getNBAPred(teamName, "Team", teamName2, "Team_Pred_Points")
                team1_Points = team1_Points[0]
                
                team2_Points = getNBAPred(teamName2, "Team", teamName, "Team_Pred_Points")
                team2_Points = team2_Points[0]
                
                total_Points = team1_Points + team2_Points
                
                statsToReturn.append(total_Points)

            elif choice == TEAM_PRED_MONEYLINE:

                rebounds_Equiv_Points = 1.7
                assists_Equiv_Points = 2.2
                
                blocks_Equiv_Points = 6.1
                steals_Equiv_Points = 9.1

                team_Overall_Score = []

                # Connect to your MySQL database
                db_host = '127.0.0.1'  # Replace with your database host
                db_user = 'root'  # Replace with your database username
                db_password = 'root'  # Replace with your database password
                db_name = 'nba_stats'  # Replace with your database name

                conn = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name
                )
                
                cursor = conn.cursor()
                
                if teamName == "Boston":
        
                    team1_short = "bos"
                    
                
                elif teamName == "Brooklyn":
                    
                    team1_short = "bkn"
                    
                    
                elif teamName == "New York":
                    
                    team1_short = "ny"
                    
                    
                elif teamName == "Philadelphia":
                    
                    team1_short = "phi"
                    
                    
                elif teamName == "Toronto":
                    
                    team1_short = "tor"
                    

                elif teamName == "Golden State":
                    
                    team1_short = "gs"
                    
                    
                elif teamName == "LA Clippers":
                    
                    team1_short = "lac"
                    
                    
                elif teamName == "LA Lakers":
                    
                    team1_short = "lal"
                    
                    
                elif teamName == "Phoenix": 
                    
                    team1_short = "phx"  
                     
                    
                elif teamName == "Sacramento":
                
                    team1_short = "sac"
                    
                    
                elif teamName == "Chicago":
                    
                    team1_short = "chi"
                    
                    
                elif teamName == "Cleveland":
                    
                    team1_short = "cle"
                    
                    
                elif teamName == "Detroit":
                    
                    team1_short = "det"
                    
                    
                elif teamName == "Indiana":
                    
                    team1_short = "ind"
                    
                
                elif teamName == "Milwaukee":
                    
                    team1_short = "mil"
                    
                    
                elif teamName == "Dallas":
                    
                    team1_short = "dal"
                    
                    
                elif teamName == "Houston":
                    
                    team1_short = "hou"
                    
                    
                elif teamName == "Memphis":
                    
                    team1_short = "mem"
                    
                    
                elif teamName == "New Orleans":
                    
                    team1_short = "no"
                    
                    
                elif teamName == "San Antonio":
                    
                    team1_short = "sa"
                    
                    
                elif teamName == "Atlanta":
                    
                    team1_short = "atl"
                    
                    
                elif teamName == "Charlotte":
                    
                    team1_short = "cha"
                    
                    
                elif teamName == "Miami":
                    
                    team1_short = "mia"   
                     
                    
                elif teamName == "Orlando":
                    
                    team1_short = "orl"
                    
                
                elif teamName == "Washington":
                    
                    team1_short = "wsh"
                    
                    
                elif teamName == "Denver":
                    
                    team1_short = "den"
                    
                    
                elif teamName == "Minnesota":
                    
                    team1_short = "min"
                    
                    
                elif teamName == "Okla City":
                    
                    team1_short = "okc"
                    
                    
                elif teamName == "Portland":
                    
                    team1_short = "por"
                    
                    
                elif teamName == "Utah":
                    
                    team1_short = "utah"
                
                team_Roster = []
                team_Points_List = [] 
                team_Rebounds_List = []
                team_Assists_List = []
                team_Blocks_List = []

                playing_Roster = []  

                team_Roster = get_NamesFrom_NBARoster(teamName)
                injured_Players = check_NBA_InjuryStatus(teamName)
                
                # Remove any player in team_roster that is also in injured_players
                team_Roster = [player for player in team_Roster if player not in injured_Players]
                
                playing_Roster = team_Roster.copy()
                
                fourth_String_Players = []
                fifth_String_Players = []
                
                for player in playing_Roster:
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 4"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fourth_String_Players.append(player)
                        
                    else:
                        
                        continue
                    
                    
                    query = f"SELECT * FROM {team1_short}_roster WHERE Name = %s AND String = 5"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        fifth_String_Players.append(player)
                        
                    else:
                        
                        continue

                playing_Roster = [player for player in playing_Roster if player not in fourth_String_Players]
                playing_Roster = [player for player in playing_Roster if player not in fifth_String_Players]
                
                playing_Roster = list(set(playing_Roster))
                
                player_Points_AlreadyAdded = []
                
                for player in injured_Players:
                    
                    query = f"SELECT position, string FROM {team1_short}_roster WHERE Name = %s"
                    cursor.execute(query, (player,))
                    result = cursor.fetchall()
                    
                    if result:
                        
                        position, string = result[0]
                        
                        
                        query = f"SELECT Name FROM {team1_short}_roster WHERE Position = '{position}' AND String = '{string+1}'"
                        cursor.execute(query)
                        result = cursor.fetchone()
                        
                        if result:
                            underStudy_Player = result[0]
                            
                            player_Points_AlreadyAdded.append(underStudy_Player)
                            
                            # Get injured Players minutes per game
                            
                            injuredPlayer_MinutesPerGame = getNBAStat(player,"Player_Misc", "Player_Minutes_PerGame")
                            injuredPlayer_MinutesPerGame = injuredPlayer_MinutesPerGame[0]
                            
                            underStudy_PointsPerMinute = getNBACalc(underStudy_Player, "Player", "Player_Points_PerMinute")
                            underStudy_PointsPerMinute = underStudy_PointsPerMinute[0]

                            underStudy_ReboundsPerMinute = getNBACalc(underStudy_Player, "Player", "Player_Rebounds_PerMinute")
                            underStudy_ReboundsPerMinute = underStudy_ReboundsPerMinute[0]

                            underStudy_BlocksPerMinute = getNBACalc(underStudy_Player, "Player", "Player_Blocks_PerMinute")
                            underStudy_BlocksPerMinute = underStudy_BlocksPerMinute[0]

                            underStudy_AssistsPerMinute = getNBACalc(underStudy_Player, "Player", "Player_Assists_PerMinute")
                            underStudy_AssistsPerMinute = underStudy_AssistsPerMinute[0]

                            underStudy_Player_PredPoints = underStudy_PointsPerMinute * injuredPlayer_MinutesPerGame
                            
                            team_Points_List.append(underStudy_Player_PredPoints)
                            team_Rebounds_List.append(underStudy_ReboundsPerMinute)
                            team_Assists_List.append(underStudy_AssistsPerMinute)
                            team_Blocks_List.append(underStudy_BlocksPerMinute)
                        
                    else:
                        
                        continue
                        
                playing_Roster = [player for player in playing_Roster if player not in player_Points_AlreadyAdded]

                for player in playing_Roster:
                    
                    result = checkNBA_PlayerHasStats(player)
                    
                    if result:
                    
                        
                        
                        player_Pred_Points = getNBAPred(player, "Offense",teamName2, "Player_Pred_Points3")
                        player_Pred_Points = player_Pred_Points[0]

                        player_Pred_Rebounds = getNBAPred(player,"Offense",teamName2,"Player_Pred_Rebounds")
                        player_Pred_Rebounds = player_Pred_Rebounds[0]

                        player_Pred_Blocks = getNBAPred(player,"Defense",teamName2,"Player_Pred_Blocks")
                        player_Pred_Blocks = player_Pred_Blocks[0]

                        player_Pred_Assists = getNBAPred(player,"Offense",teamName2,"Player_Pred_Assists")
                        player_Pred_Assists = player_Pred_Assists[0]

        
                            
                        team_Points_List.append(player_Pred_Points)
                        team_Rebounds_List.append(player_Pred_Rebounds)
                        team_Assists_List.append(player_Pred_Assists)
                        team_Blocks_List.append(player_Pred_Blocks)
                        
                    else:
                        
                        continue
                  
                team_Points = sum(team_Points_List)
                team_Rebound_Score = (sum(team_Rebounds_List)) * rebounds_Equiv_Points
                team_Assists_Score = (sum(team_Assists_List)) * assists_Equiv_Points
                team_Blocks_Score = (sum(team_Blocks_List)) * blocks_Equiv_Points

                team_Overall_Score = team_Points + team_Rebound_Score + team_Assists_Score + team_Blocks_Score

                # Close the cursor and connection
                cursor.close()
                connection.close()
                
                statsToReturn.append(team_Overall_Score)

    connection.close()  
     
    return statsToReturn