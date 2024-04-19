from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from main_Library import *
import mysql.connector
from bs4 import BeautifulSoup
import time
from datetime import datetime
from datetime import date
import datetime
import math
import re

# Update all tables
def updateAllNFLTables():
    
    supplyTable_QB_Home()
    supplyTable_QB_Away()
    supplyTable_QB_Totals()
    
    
    supplyTable_RB_Home()
    supplyTable_RB_Away()
    supplyTable_RB_Totals()
    
    
    supplyTable_WR_Home()
    supplyTable_WR_Away()
    supplyTable_WR_Totals()
    
    supplyTable_TeamDef_Totals()
    supplyTable_TeamOff_Totals()
    
    supplyTable_Team_OffenseRoster()
    
# Supply Quarterback Tables
def supplyTable_QB_Totals():
    
    QB_Names = []
    gamesPlayed = []
    pass_Yards = []
    yards_Per_Attempt = []
    attempts = []
    completions = []
    completions_Perc = []
    touchdowns = []
    interceptions = []
    twentyPlus_Passes = []
    longest_Pass = []
    sacks = []
    sacks_LostYards = []
    qb_Ranking = []
    
    database_Name = "nfl_stats"
    
    qb_Away_Names = get_NamesFromDatabase(database_Name, "qb_away_stats")
    qb_Home_Names = get_NamesFromDatabase(database_Name, "qb_home_stats")
    
    qb_Names = list(set(qb_Away_Names + qb_Home_Names))
    qb_Names = list(qb_Names)
    connection = create_connection("nfl_stats")
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    for name in qb_Names:
        
        # Calculate QB Total Games Played
        qb_home_GamesPlayed = get_statData(connection, name,"qb_home_stats", "Games_Played")
        
        if qb_home_GamesPlayed == None:
            qb_home_GamesPlayed = 0
            
        qb_away_GamesPlayed = get_statData(connection, name,"qb_away_stats", "Games_Played")
        
        if qb_away_GamesPlayed == None:
            qb_away_GamesPlayed = 0
            
        qb_total_GamesPlayed = (qb_home_GamesPlayed + qb_away_GamesPlayed)
        
        # Calculate QB Total Passing Yards
        qb_home_PassYards = get_statData(connection, name,"qb_home_stats", "Pass_Yards")
        
        if qb_home_PassYards == None:
            qb_home_PassYards = 0
            
        qb_away_PassYards = get_statData(connection, name,"qb_away_stats", "Pass_Yards")
        
        if qb_away_PassYards == None:
            qb_away_PassYards = 0
            
        qb_total_PassYards = (qb_home_PassYards + qb_away_PassYards)
        
        # Calculate QB Total Yards Per Attempt
        qb_home_YPA = get_statData(connection, name,"qb_home_stats", "Yards_Per_Attempt")
        
        if qb_home_YPA == None:
            qb_home_YPA = 0
            
        qb_away_YPA = get_statData(connection, name,"qb_away_stats", "Yards_Per_Attempt")
        
        if qb_away_YPA == None:
            qb_away_YPA = 0
            
        if qb_away_GamesPlayed + qb_home_GamesPlayed == 0:
            qb_total_YPA = 0.0  # or any default value you prefer
        else:
            qb_total_YPA = ((qb_away_YPA * qb_away_GamesPlayed) + (qb_home_YPA * qb_home_GamesPlayed)) / (qb_away_GamesPlayed + qb_home_GamesPlayed)
        
        # Calculate QB Total Attempts
        qb_home_Attempts = get_statData(connection, name,"qb_home_stats", "Attempts")
        
        if qb_home_Attempts == None:
            qb_home_Attempts = 0
            
        qb_away_Attempts = get_statData(connection, name,"qb_away_stats", "Attempts")
        
        if qb_away_Attempts == None:
            qb_away_Attempts = 0
            
        qb_total_Attempts = (qb_home_Attempts + qb_away_Attempts)
        
        # Calculate QB Total Completions
        qb_home_Completions = get_statData(connection, name,"qb_home_stats", "Completions")
        
        if qb_home_Completions == None:
            qb_home_Completions = 0
            
        qb_away_Completions = get_statData(connection, name,"qb_away_stats", "Completions")
        
        if qb_away_Completions == None:
            qb_away_Completions = 0
            
        qb_total_Completions = (qb_home_Completions + qb_away_Completions)
         
        # Calculate QB Total Completion Percentage
        qb_total_Completions = (qb_home_Completions + qb_away_Completions)
        
        if qb_total_Attempts == 0:
            qb_total_Completion_Perc = 0.00
        else:
            qb_total_Completion_Perc = qb_total_Completions / qb_total_Attempts
            
    
        # Calculate QB Total Touchdowns
        qb_home_Touchdowns = get_statData(connection, name,"qb_home_stats", "Touchdowns")
        
        if qb_home_Touchdowns == None:
            qb_home_Touchdowns = 0
            
        qb_away_Touchdowns = get_statData(connection, name,"qb_away_stats", "Touchdowns")
        
        if qb_away_Touchdowns == None:
            qb_away_Touchdowns = 0
            
        qb_total_Touchdowns = (qb_home_Touchdowns + qb_away_Touchdowns)
        
        # Calculate QB Total Interceptions
        qb_home_Interceptions = get_statData(connection, name,"qb_home_stats", "Interceptions")
        
        if qb_home_Interceptions == None:
            qb_home_Interceptions = 0
            
        qb_away_Interceptions = get_statData(connection, name,"qb_away_stats", "Interceptions")
        
        if qb_away_Interceptions == None:
            qb_away_Interceptions = 0
            
        qb_total_Interceptions = (qb_home_Interceptions + qb_away_Interceptions)
        
        # Calculate QB Total Sacks
        qb_home_Sacks = get_statData(connection, name,"qb_home_stats", "Sacks")
        
        if qb_home_Sacks == None:
            qb_home_Sacks = 0
            
        qb_away_Sacks = get_statData(connection, name,"qb_away_stats", "Sacks")
        
        if qb_away_Sacks == None:
            qb_away_Sacks = 0
            
        qb_total_Sacks = (qb_home_Sacks + qb_away_Sacks)
          
        # Calculate QB Total Lost of Yards Due to Sacks
        qb_home_SLY = get_statData(connection, name,"qb_home_stats", "Sacks_LostYards")
        
        if qb_home_SLY == None:
            qb_home_SLY = 0
            
        qb_away_SLY = get_statData(connection, name,"qb_away_stats", "Sacks_LostYards")
        
        if qb_away_SLY == None:
            qb_away_SLY = 0
            
        qb_total_SLY = (qb_home_SLY + qb_away_SLY)
        
        
        
        
        # Calculate QB Total rating
        
        qb_home_rating = get_statData(connection, name,"qb_home_stats", "Rating")
        
        if qb_home_rating == None:
            qb_home_rating = 0.0
            
        else: 
             qb_home_rating = float( qb_home_rating)
            
        qb_away_rating = get_statData(connection, name,"qb_away_stats", "Rating")
        
        if qb_away_rating == None:
            qb_away_rating = 0
            
        else: 
             qb_away_rating = float( qb_away_rating)
        
        if qb_away_rating == 0 or qb_home_rating == 0 or qb_away_GamesPlayed == 0 or qb_home_GamesPlayed == 0:
            
            continue
        
        else:     
            qb_total_Rating = ((qb_home_rating * qb_home_GamesPlayed) + (qb_away_rating * qb_away_GamesPlayed))/(qb_home_GamesPlayed + qb_away_GamesPlayed)
            qb_total_Rating = (round(qb_total_Rating,2))
        
        
        insert_query = "INSERT INTO qb_total_stats (Name, Games_Played, Pass_Yards, Yards_Per_Attempt, Attempts, Completions, Completion_Perc, Touchdowns, Interceptions, Sacks, Sacks_LostYards, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Pass_Yards=VALUES(Pass_Yards), Yards_Per_Attempt=VALUES(Yards_Per_Attempt), Attempts=VALUES(Attempts), Completions=VALUES(Completions), Completion_Perc=VALUES(Completion_Perc), Touchdowns=VALUES(Touchdowns), Interceptions=VALUES(Interceptions), Sacks=VALUES(Sacks), Sacks_LostYards=VALUES(Sacks_LostYards), Rating=VALUES(Rating)"
        
        qb_data = [
                (name, qb_total_GamesPlayed, qb_total_PassYards, qb_total_YPA, qb_total_Attempts, qb_total_Completions, qb_total_Completion_Perc, qb_total_Touchdowns, qb_total_Interceptions, qb_total_Sacks, qb_total_SLY, qb_total_Rating),
        # Add more rows if needed
                ]
        
        cursor.executemany(insert_query,qb_data)
        conn.commit()  
        
    connection.close()
    print("Updated Quarterback Total Stats")                  
   
def supplyTable_QB_Home():
    
    QB_Names = []
    gamesPlayed = []
    pass_Yards = []
    yards_Per_Attempt = []
    attempts = []
    completions = []
    completions_Perc = []
    touchdowns = []
    interceptions = []
    sacks = []
    sacks_LostYards = []
    qb_Ranking = []
    
    today = datetime.date.today()

    current_month = today.month
    
    current_year = today.year
    
    if current_month in [1, 2]:  # January is 1, February is 2
        current_year -= 1
    
    
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    # Get the website that has the Quarterback's stats
    
    driver.get("https://stathead.com/football/player_split_finder.cgi?request=1&order_by=pass_td&year_min="+str(current_year)+"&split_list=Game+Location&sub_game_location=Home&stat_ratio=season&type=player")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    statTable = soup.find('div', id = 'div_game_location_splits')
    
    #--Quarterback Names--
    
    name_elements = statTable.find_all('td', class_='left', attrs={'data-stat': 'player'})
    
    
    for name_element in name_elements:
        a_element = name_element.find('a')
        player_name = a_element.text
        QB_Names.append(player_name)


    #--Quarterback Games Played--
    
   
    gamesPlayed_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'g'})

    for gamesPlayed_elements in gamesPlayed_elements:
        Games_Played = gamesPlayed_elements.text
        if Games_Played != '':
            gamesPlayed.append(int(Games_Played))
            
        else: 
            Games_Played = '0'
            gamesPlayed.append(int(Games_Played))
            
            
    #--Quarterback Passing Yards--
    
   
    pass_yds_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_yds'})

    
    for pass_yds_element in pass_yds_elements:
        pass_yds = pass_yds_element.text
        if pass_yds != '':
            pass_Yards.append(int(pass_yds))
            
        else: 
            pass_yds = '0'
            pass_yds.append(int(pass_yds))
        
    #--Quarterback Yards Per Passing Attempt--
  
    pass_yds_Attempt_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_yds_per_att'})

    for pass_yds_Attempt_elements in pass_yds_Attempt_elements:
        pass_yds_Attempt = pass_yds_Attempt_elements.text
        if pass_yds_Attempt != '':
            yards_Per_Attempt.append(float(pass_yds_Attempt))
            
        else:
            pass_yds_Attempt = '0.0'
            yards_Per_Attempt.append(float(pass_yds_Attempt))
            
    #--Quarterback Passing Attempts--
  
    Attempts_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_att'})

    for Attempts_elements in Attempts_elements:
        Attempts = Attempts_elements.text
        if Attempts != '':
            attempts.append(int(Attempts))
            
        else:
            Attempts = '0.0'
            attempts.append(int(Attempts))
            
    #--Quarterback Passing Completions--
  
    Completions_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_cmp'})

    for Completions_elements in Completions_elements:
        Completions = Completions_elements.text
        if Completions != '':
            completions.append(int(Completions))
            
        else:
            Completions = '0'
            completions.append(int(Completions))
            
            
    #--Quarterback Passing Completion Percentage--
  
    Completions_Perc_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_cmp_perc'})

    for Completions_Perc_elements in Completions_Perc_elements:
        Completions_Perc = Completions_Perc_elements.text
        if Completions_Perc != '' or Completions_Perc != "":
            completions_Perc.append(float(Completions_Perc))
            
        else:
            Completions_Perc = "00.0"
            completions_Perc.append(float(Completions_Perc))
            
            
     #--Quarterback Passing Touchdowns--
  
    touchdowns_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_td'})

    for touchdowns_elements in touchdowns_elements:
        Touchdowns = touchdowns_elements.text
        if Touchdowns != '':
            touchdowns.append(int(Touchdowns))
            
        else:
            Touchdowns = '0'
            touchdowns.append(int(Touchdowns))
            
            
    #--Quarterback Passing Interceptions--
  
    interceptions_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_int'})

    for interceptions_elements in interceptions_elements:
        Interceptions = interceptions_elements.text
        if Interceptions != '':
            interceptions.append(int(Interceptions))
            
        else:
            Interceptions = '0'
            interceptions.append(int(Interceptions))
            
        
    #--Quarterback Sacks--
  
    Sacks_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_sacked'})

    for Sacks_elements in Sacks_elements:
        Sacks = Sacks_elements.text
        if Sacks != '':
            sacks.append(int(Sacks))
            
        else:
            Sacks = '0'
            sacks.append(int(Sacks))
               
            
    #--Quarterback Lost Yards Due To Sacks--
  
    Sacks_LostYards_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_sacked_yds'})

    for Sacks_LostYards_elements in Sacks_LostYards_elements:
        Sacks_LostYards = Sacks_LostYards_elements.text.strip('-')
        if Sacks_LostYards != '':
            sacks_LostYards.append(int(Sacks_LostYards))
            
        else:
            Sacks_LostYards = '0'
            sacks_LostYards.append(int(Sacks_LostYards))
      
    #--Quarterback Rating--
  
    qbRating_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_rating'})

    for qbRating_elements in qbRating_elements:
        QB_Ranking = qbRating_elements.text
        if QB_Ranking != '':
            qb_Ranking.append(float(QB_Ranking))
            
            
        else:
            QB_Ranking = '0'
            qb_Ranking.append(float(QB_Ranking))  
                

    driver.quit()
    
    data_tuples = []

    for QB_Names, Games_Played, pass_Yards, yards_Per_Attempt, attempts, completions, completions_Perc, touchdowns, interceptions, sacks, sacks_LostYards, qb_Ranking in zip(
        QB_Names, gamesPlayed, pass_Yards, yards_Per_Attempt, attempts,
        completions, completions_Perc, touchdowns, interceptions,
        sacks, sacks_LostYards, qb_Ranking
    ):
        
        data_tuple = (
            QB_Names, Games_Played, pass_Yards, yards_Per_Attempt, attempts, completions, completions_Perc,
            touchdowns, interceptions, sacks, sacks_LostYards, qb_Ranking
        )
        data_tuples.append(data_tuple)
            
        
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO qb_home_stats (Name, Games_Played, Pass_Yards, Yards_Per_Attempt, Attempts, Completions, Completion_Perc, Touchdowns, Interceptions, Sacks, Sacks_LostYards, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Pass_Yards=VALUES(Pass_Yards), Yards_Per_Attempt=VALUES(Yards_Per_Attempt), Attempts=VALUES(Attempts), Completions=VALUES(Completions), Completion_Perc=VALUES(Completion_Perc), Touchdowns=VALUES(Touchdowns), Interceptions=VALUES(Interceptions), Sacks=VALUES(Sacks), Sacks_LostYards=VALUES(Sacks_LostYards), Rating=VALUES(Rating)"

    sorted_data_tuples = sorted(data_tuples, key=lambda x: x[0])
    
    cursor.executemany(insert_query, sorted_data_tuples)
    conn.commit()  
    print("Updated Quarterback Home Stats") 
    
def supplyTable_QB_Away():
    
    QB_Names = []
    gamesPlayed = []
    pass_Yards = []
    yards_Per_Attempt = []
    attempts = []
    completions = []
    completions_Perc = []
    touchdowns = []
    interceptions = []
    sacks = []
    sacks_LostYards = []
    qb_Ranking = []
    
    today = datetime.date.today()

    current_month = today.month
    
    current_year = today.year
    
    if current_month in [1, 2]:  # January is 1, February is 2
        current_year -= 1
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    # Get the website that has the Quarterback's stats
    
    driver.get("https://stathead.com/football/player_split_finder.cgi?request=1&order_by=pass_td&year_min="+str(current_year)+"&split_list=Game+Location&sub_game_location=Away&stat_ratio=season&type=player")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    statTable = soup.find('div', id = 'div_game_location_splits')
    
    #--Quarterback Names--
    
    name_elements = statTable.find_all('td', class_='left', attrs={'data-stat': 'player'})
    
    
    for name_element in name_elements:
        a_element = name_element.find('a')
        player_name = a_element.text
        QB_Names.append(player_name)


    #--Quarterback Games Played--
    
   
    gamesPlayed_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'g'})

    for gamesPlayed_elements in gamesPlayed_elements:
        Games_Played = gamesPlayed_elements.text
        if Games_Played != '':
            gamesPlayed.append(int(Games_Played))
            
        else: 
            Games_Played = '0'
            gamesPlayed.append(int(Games_Played))
            
            
    #--Quarterback Passing Yards--
    
   
    pass_yds_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_yds'})

    
    for pass_yds_element in pass_yds_elements:
        pass_yds = pass_yds_element.text
        if pass_yds != '':
            pass_Yards.append(int(pass_yds))
            
        else: 
            pass_yds = '0'
            pass_yds.append(int(pass_yds))
        
    #--Quarterback Yards Per Passing Attempt--
  
    pass_yds_Attempt_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_yds_per_att'})

    for pass_yds_Attempt_elements in pass_yds_Attempt_elements:
        pass_yds_Attempt = pass_yds_Attempt_elements.text
        if pass_yds_Attempt != '':
            yards_Per_Attempt.append(float(pass_yds_Attempt))
            
        else:
            pass_yds_Attempt = '0.0'
            yards_Per_Attempt.append(float(pass_yds_Attempt))
            
    #--Quarterback Passing Attempts--
  
    Attempts_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_att'})

    for Attempts_elements in Attempts_elements:
        Attempts = Attempts_elements.text
        if Attempts != '':
            attempts.append(int(Attempts))
            
        else:
            Attempts = '0.0'
            attempts.append(int(Attempts))
            
    #--Quarterback Passing Completions--
  
    Completions_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_cmp'})

    for Completions_elements in Completions_elements:
        Completions = Completions_elements.text
        if Completions != '':
            completions.append(int(Completions))
            
        else:
            Completions = '0'
            completions.append(int(Completions))
            
            
    #--Quarterback Passing Completion Percentage--
  
    Completions_Perc_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_cmp_perc'})

    for Completions_Perc_elements in Completions_Perc_elements:
        Completions_Perc = Completions_Perc_elements.text
        if Completions_Perc != '' or Completions_Perc != "":
            completions_Perc.append(float(Completions_Perc))
            
        else:
            Completions_Perc = "00.0"
            completions_Perc.append(float(Completions_Perc))
            
            
     #--Quarterback Passing Touchdowns--
  
    touchdowns_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_td'})

    for touchdowns_elements in touchdowns_elements:
        Touchdowns = touchdowns_elements.text
        if Touchdowns != '':
            touchdowns.append(int(Touchdowns))
            
        else:
            Touchdowns = '0'
            touchdowns.append(int(Touchdowns))
            
            
    #--Quarterback Passing Interceptions--
  
    interceptions_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_int'})

    for interceptions_elements in interceptions_elements:
        Interceptions = interceptions_elements.text
        if Interceptions != '':
            interceptions.append(int(Interceptions))
            
        else:
            Interceptions = '0'
            interceptions.append(int(Interceptions))
            
        
    #--Quarterback Sacks--
  
    Sacks_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_sacked'})

    for Sacks_elements in Sacks_elements:
        Sacks = Sacks_elements.text
        if Sacks != '':
            sacks.append(int(Sacks))
            
        else:
            Sacks = '0'
            sacks.append(int(Sacks))
               
            
    #--Quarterback Lost Yards Due To Sacks--
  
    Sacks_LostYards_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_sacked_yds'})

    for Sacks_LostYards_elements in Sacks_LostYards_elements:
        Sacks_LostYards = Sacks_LostYards_elements.text.strip('-')
        if Sacks_LostYards != '':
            sacks_LostYards.append(int(Sacks_LostYards))
            
        else:
            Sacks_LostYards = '0'
            sacks_LostYards.append(int(Sacks_LostYards))
      
    #--Quarterback Rating--
  
    qbRating_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'pass_rating'})

    for qbRating_elements in qbRating_elements:
        QB_Ranking = qbRating_elements.text
        if QB_Ranking != '':
            qb_Ranking.append(float(QB_Ranking))
            
            
        else:
            QB_Ranking = '0'
            qb_Ranking.append(float(QB_Ranking))  
                

    driver.quit()
    
    data_tuples = []

    for QB_Names, Games_Played, pass_Yards, yards_Per_Attempt, attempts, completions, completions_Perc, touchdowns, interceptions, sacks, sacks_LostYards, qb_Ranking in zip(
        QB_Names, gamesPlayed, pass_Yards, yards_Per_Attempt, attempts,
        completions, completions_Perc, touchdowns, interceptions,
        sacks, sacks_LostYards, qb_Ranking
    ):
        
        data_tuple = (
            QB_Names, Games_Played, pass_Yards, yards_Per_Attempt, attempts, completions, completions_Perc,
            touchdowns, interceptions, sacks, sacks_LostYards, qb_Ranking
        )
        data_tuples.append(data_tuple)
            
        
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO qb_away_stats (Name, Games_Played, Pass_Yards, Yards_Per_Attempt, Attempts, Completions, Completion_Perc, Touchdowns, Interceptions, Sacks, Sacks_LostYards, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Pass_Yards=VALUES(Pass_Yards), Yards_Per_Attempt=VALUES(Yards_Per_Attempt), Attempts=VALUES(Attempts), Completions=VALUES(Completions), Completion_Perc=VALUES(Completion_Perc), Touchdowns=VALUES(Touchdowns), Interceptions=VALUES(Interceptions), Sacks=VALUES(Sacks), Sacks_LostYards=VALUES(Sacks_LostYards), Rating=VALUES(Rating)"

    sorted_data_tuples = sorted(data_tuples, key=lambda x: x[0])
    
    cursor.executemany(insert_query, sorted_data_tuples)
    conn.commit()  
    print("Updated Quarterback Away Stats") 


# Supply Running Back Tables
def supplyTable_RB_Totals():
    
    database_Name = "nfl_stats"
    
    RB_Away_Names = get_NamesFromDatabase(database_Name, "rb_away_stats")
    RB_Home_Names = get_NamesFromDatabase(database_Name, "rb_home_stats")
    
    RB_Names = list(set(RB_Away_Names + RB_Home_Names))
    RB_Names = list(RB_Names)
    
    connection = create_connection("nfl_stats")
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    for name in RB_Names:
        
        #Calculate RB Games Played
        rb_Away_GamesPlayed = get_statData(connection, name, "rb_away_stats", "Games_Played")
        
        if rb_Away_GamesPlayed == None:
            rb_Away_GamesPlayed = 0
        
        rb_Home_GamesPlayed = get_statData(connection, name, "rb_home_stats", "Games_Played")
        
        if rb_Home_GamesPlayed == None:
            rb_Home_GamesPlayed = 0
            
        rb_total_GamesPlayed = rb_Away_GamesPlayed + rb_Home_GamesPlayed
        
        #Calculate RB Attempts
        rb_Away_Attempts = get_statData(connection, name, "rb_away_stats", "Attempts")
        
        if rb_Away_Attempts == None:
            rb_Away_Attempts = 0
        
        rb_Home_Attempts = get_statData(connection, name, "rb_home_stats", "Attempts")
        
        if rb_Home_Attempts == None:
            rb_Home_Attempts = 0
            
        rb_total_Attempts = rb_Away_Attempts + rb_Home_Attempts
        
        #Calculate RB Yards
        rb_Away_Yards = get_statData(connection, name, "rb_away_stats", "Yards")
        
        if rb_Away_Yards == None:
            rb_Away_Yards = 0
        
        rb_Home_Yards = get_statData(connection, name, "rb_home_stats", "Yards")
        
        if rb_Home_Yards == None:
            rb_Home_Yards = 0
            
        rb_total_Yards = rb_Away_Yards + rb_Home_Yards
        
        #Calculate RB Yards Per Attempt
        rb_Away_YPA = get_statData(connection, name, "rb_away_stats", "Yards_PerAttempt")
        
        if rb_Away_YPA == None:
            rb_Away_YPA = 0
        
        rb_Home_YPA = get_statData(connection, name, "rb_home_stats", "Yards_PerAttempt")
        
        if rb_Home_YPA == None:
            rb_Home_YPA = 0
        
        if rb_Away_GamesPlayed + rb_Home_GamesPlayed != 0:  
            rb_total_YPA = ((rb_Away_YPA * rb_Away_GamesPlayed) + (rb_Home_YPA * rb_Home_GamesPlayed))/ (rb_Away_GamesPlayed + rb_Home_GamesPlayed)
            
        else:
            # Handle the case where the denominator is zero (division by zero)
            rb_total_YPA = 0
        
        rb_total_YPA = round(rb_total_YPA,1)
        
        #Calculate RB Touchdowns
        rb_Away_Touchdowns = get_statData(connection, name, "rb_away_stats", "Touchdowns")
        
        if rb_Away_Touchdowns == None:
            rb_Away_Touchdowns = 0
        
        rb_Home_Touchdowns = get_statData(connection, name, "rb_home_stats", "Touchdowns")
        
        if rb_Home_Touchdowns == None:
            rb_Home_Touchdowns = 0
            
        rb_total_Touchdowns = rb_Away_Touchdowns + rb_Home_Touchdowns
    
        #Calculate RB First down runs
        rb_Away_FDR = get_statData(connection, name, "rb_away_stats", "FirstDown_Runs")
        
        if rb_Away_FDR == None:
            rb_Away_FDR = 0
        
        rb_Home_FDR = get_statData(connection, name, "rb_home_stats", "FirstDown_Runs")
        
        if rb_Home_FDR == None:
            rb_Home_FDR = 0
            
        rb_total_FDR = rb_Away_FDR + rb_Home_FDR
        
        
        # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
        insert_query = "INSERT INTO rb_total_stats (Name, Games_Played, Attempts, Yards, Yards_PerAttempt, Touchdowns, FirstDown_Runs) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Attempts=VALUES(Attempts), Yards=VALUES(Yards), Yards_PerAttempt=VALUES(Yards_PerAttempt), Touchdowns=VALUES(Touchdowns), FirstDown_Runs=VALUES(FirstDown_Runs)"

        
        rb_data = [
            (name, rb_total_GamesPlayed, rb_total_Attempts, rb_total_Yards, rb_total_YPA, rb_total_Touchdowns, rb_Away_FDR),
        # Add more rows if needed
                ]
        
        cursor.executemany(insert_query, rb_data)
        conn.commit()  
    connection.close()
    print("Updated RunningBack Total Stats")

def supplyTable_RB_Home():
    
    RB_Names = []
    games_Played = []
    attempts = []
    yards = []
    yards_PerAttempt = []
    touchdowns = []
    firstDown_Runs = []
    
    

    today = datetime.date.today()

    current_month = today.month
    
    current_year = today.year
    
    if current_month in [1, 2]:  # January is 1, February is 2
        current_year -= 1
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    # Get the website that has the Quarterback's stats
    
    driver.get("https://stathead.com/football/player_split_finder.cgi?request=1&year_min="+str(current_year)+"&split_list=Game+Location&sub_game_location=Home&stat_ratio=season&show%5B%5D=rush&type=player")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    statTable = soup.find('div', id = 'div_game_location_splits')
    
    #--Running Back Names--
    
    name_elements = statTable.find_all('td', class_='left', attrs={'data-stat': 'player'})
    
    
    for name_element in name_elements:
        a_element = name_element.find('a')
        player_name = a_element.text
        RB_Names.append(player_name)
        
    #--Running Back Games Played--
    gamesPlayed_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'g'})

    for gamesPlayed_elements in gamesPlayed_elements:
        Games_Played = gamesPlayed_elements.text
        if Games_Played != '':
            games_Played.append(int(Games_Played))
            
        else: 
            Games_Played = '0'
            games_Played.append(int(Games_Played))
    
    
    #--Running Back Rush Attempts--
    rushAttempts_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_att'})

    for rushAttempts_elements in rushAttempts_elements:
        rushAttempts = rushAttempts_elements.text
        if rushAttempts != '':
            attempts.append(int(rushAttempts))
            
        else: 
            rushAttempts = '0'
            attempts.append(int(rushAttempts))
            
    #--Running Back Yards--
    Yards_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_yds'})

    for Yards_elements in Yards_elements:
        Yards = Yards_elements.text
        if Yards != '':
            yards.append(int(Yards))
            
        else: 
            Yards = '0'
            yards.append(int(Yards))
            
    #--Running Back Yards Per Attempt--
    Yards_PerAttempt_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_yds_per_att'})

    for Yards_PerAttempt_elements in Yards_PerAttempt_elements:
        Yards_PerAttempt = Yards_PerAttempt_elements.text
        if Yards_PerAttempt != '':
            yards_PerAttempt.append(float(Yards_PerAttempt))
            
        else: 
            Yards_PerAttempt = '0.0'
            yards_PerAttempt.append(float(Yards_PerAttempt))
            
    #--Running Back Touchdowns--
    Touchdowns_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_td'})

    for Touchdowns_elements in Touchdowns_elements:
        Touchdowns = Touchdowns_elements.text
        if Touchdowns != '':
            touchdowns.append(int(Touchdowns))
            
        else: 
            Touchdowns = '0'
            touchdowns.append(int(Touchdowns))
            
    #--Running Back First Down Runs--
    FirstDown_Runs_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_first_down'})

    for FirstDown_Runs_elements in FirstDown_Runs_elements:
        FirstDown_Runs = FirstDown_Runs_elements.text
        if FirstDown_Runs != '':
            firstDown_Runs.append(int(FirstDown_Runs))
            
        else: 
            FirstDown_Runs = '0'
            firstDown_Runs.append(int(FirstDown_Runs))
            
    driver.quit()
    
    data_tuples = []

    for RB_Names, games_Played, attempts, yards, yards_PerAttempt, touchdowns, firstDown_Runs in zip(
        RB_Names, games_Played, attempts, yards, yards_PerAttempt, touchdowns, firstDown_Runs
    ):
        
        data_tuple = (
            
            RB_Names, games_Played, attempts, yards, yards_PerAttempt, touchdowns, firstDown_Runs
        )
        data_tuples.append(data_tuple)
            
        
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO rb_home_stats (Name, Games_Played, Attempts, Yards, Yards_PerAttempt, Touchdowns, FirstDown_Runs) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Attempts=VALUES(Attempts), Yards=VALUES(Yards), Yards_PerAttempt=VALUES(Yards_PerAttempt), Touchdowns=VALUES(Touchdowns), FirstDown_Runs=VALUES(FirstDown_Runs)"

    sorted_data_tuples = sorted(data_tuples, key=lambda x: x[0])
    
    cursor.executemany(insert_query, sorted_data_tuples)
    conn.commit()  
    print("Updated RunningBack Home Stats")

def supplyTable_RB_Away():
    
    RB_Names = []
    games_Played = []
    attempts = []
    yards = []
    yards_PerAttempt = []
    touchdowns = []
    firstDown_Runs = []
    
    today = datetime.date.today()

    current_month = today.month
    
    current_year = today.year
    
    if current_month in [1, 2]:  # January is 1, February is 2
        current_year -= 1
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    # Get the website that has the Quarterback's stats
    
    driver.get("https://stathead.com/football/player_split_finder.cgi?request=1&year_min="+str(current_year)+"&split_list=Game+Location&sub_game_location=Away&stat_ratio=season&show%5B%5D=rush&type=player")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    statTable = soup.find('div', id = 'div_game_location_splits')
    
    #--Running Back Names--
    
    name_elements = statTable.find_all('td', class_='left', attrs={'data-stat': 'player'})
    
    
    for name_element in name_elements:
        a_element = name_element.find('a')
        player_name = a_element.text
        RB_Names.append(player_name)
        
    #--Running Back Games Played--
    gamesPlayed_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'g'})

    for gamesPlayed_elements in gamesPlayed_elements:
        Games_Played = gamesPlayed_elements.text
        if Games_Played != '':
            games_Played.append(int(Games_Played))
            
        else: 
            Games_Played = '0'
            games_Played.append(int(Games_Played))
    
    
    #--Running Back Rush Attempts--
    rushAttempts_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_att'})

    for rushAttempts_elements in rushAttempts_elements:
        rushAttempts = rushAttempts_elements.text
        if rushAttempts != '':
            attempts.append(int(rushAttempts))
            
        else: 
            rushAttempts = '0'
            attempts.append(int(rushAttempts))
            
    #--Running Back Yards--
    Yards_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_yds'})

    for Yards_elements in Yards_elements:
        Yards = Yards_elements.text
        if Yards != '':
            yards.append(int(Yards))
            
        else: 
            Yards = '0'
            yards.append(int(Yards))
            
    #--Running Back Yards Per Attempt--
    Yards_PerAttempt_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_yds_per_att'})

    for Yards_PerAttempt_elements in Yards_PerAttempt_elements:
        Yards_PerAttempt = Yards_PerAttempt_elements.text
        if Yards_PerAttempt != '':
            yards_PerAttempt.append(float(Yards_PerAttempt))
            
        else: 
            Yards_PerAttempt = '0.0'
            yards_PerAttempt.append(float(Yards_PerAttempt))
            
    #--Running Back Touchdowns--
    Touchdowns_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_td'})

    for Touchdowns_elements in Touchdowns_elements:
        Touchdowns = Touchdowns_elements.text
        if Touchdowns != '':
            touchdowns.append(int(Touchdowns))
            
        else: 
            Touchdowns = '0'
            touchdowns.append(int(Touchdowns))
            
    #--Running Back First Down Runs--
    FirstDown_Runs_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rush_first_down'})

    for FirstDown_Runs_elements in FirstDown_Runs_elements:
        FirstDown_Runs = FirstDown_Runs_elements.text
        if FirstDown_Runs != '':
            firstDown_Runs.append(int(FirstDown_Runs))
            
        else: 
            FirstDown_Runs = '0'
            firstDown_Runs.append(int(FirstDown_Runs))
            
    driver.quit()
    
    data_tuples = []

    for RB_Names, games_Played, attempts, yards, yards_PerAttempt, touchdowns, firstDown_Runs in zip(
        RB_Names, games_Played, attempts, yards, yards_PerAttempt, touchdowns, firstDown_Runs
    ):
        
        data_tuple = (
            
            RB_Names, games_Played, attempts, yards, yards_PerAttempt, touchdowns, firstDown_Runs
        )
        data_tuples.append(data_tuple)
            
        
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO rb_away_stats (Name, Games_Played, Attempts, Yards, Yards_PerAttempt, Touchdowns, FirstDown_Runs) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Attempts=VALUES(Attempts), Yards=VALUES(Yards), Yards_PerAttempt=VALUES(Yards_PerAttempt), Touchdowns=VALUES(Touchdowns), FirstDown_Runs=VALUES(FirstDown_Runs)"

    sorted_data_tuples = sorted(data_tuples, key=lambda x: x[0])
    
    cursor.executemany(insert_query, sorted_data_tuples)
    conn.commit()  
    print("Updated RunningBack Away Stats")


# Supply Wide Reciever Tables
def supplyTable_WR_Totals():
    
    WR_Names = []
    gamesPlayed = []
    yards = []
    yards_PerReception = []
    yards_PerTarget = []
    targets = []
    touchdowns = []
    catch_Perc = []
    catches = []
    firstDown_Catches = []
    
    database_Name = "nfl_stats"
    
    WR_Away_Names = get_NamesFromDatabase(database_Name, "WR_away_stats")
    WR_Home_Names = get_NamesFromDatabase(database_Name, "WR_home_stats")
    
    WR_Names = list(set(WR_Away_Names + WR_Home_Names))
    WR_Names = list(WR_Names)
    
    connection = create_connection("nfl_stats")
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    for name in WR_Names:
        
        #Calculate WR Games Played
        WR_Away_GamesPlayed = get_statData(connection, name, "WR_away_stats", "Games_Played")
        
        if WR_Away_GamesPlayed == None or WR_Away_GamesPlayed == 0:
            WR_Away_GamesPlayed = 1
            
        else:
             WR_Away_GamesPlayed = int( WR_Away_GamesPlayed)
            
        
        WR_Home_GamesPlayed = get_statData(connection, name, "WR_home_stats", "Games_Played")
        
        if WR_Home_GamesPlayed == None or WR_Home_GamesPlayed == 0:
            WR_Home_GamesPlayed = 1
            
        else:
             WR_Home_GamesPlayed = int( WR_Home_GamesPlayed)
            
        WR_total_GamesPlayed = int(WR_Away_GamesPlayed) + int(WR_Home_GamesPlayed)
        
        #Calculate WR Yards
        WR_Away_Yards = get_statData(connection, name, "WR_away_stats", "Yards")
        
        if WR_Away_Yards == None:
            WR_Away_Yards = 0
        
        WR_Home_Yards = get_statData(connection, name, "WR_home_stats", "Yards")
        
        if WR_Home_Yards == None:
            WR_Home_Yards = 0
            
        WR_total_Yards = WR_Away_Yards + WR_Home_Yards
        
        #Calculate WR Yards Per Catch
        WR_Away_YPC = get_statData(connection, name, "WR_away_stats", "Yards_perReception")
        
        if WR_Away_YPC == None:
            WR_Away_YPC = 0.0
            
        elif WR_Away_YPC > 0.0:
            
            WR_Away_YPC = float(WR_Away_YPC)
            
        else:
            
            WR_Away_YPC = 0.0
               
        WR_Home_YPC = get_statData(connection, name, "WR_home_stats", "Yards_perReception")
        
        if WR_Home_YPC == None:
            WR_Home_YPC = 1.0
            
        elif WR_Home_YPC > 0.0:
            
            WR_Home_YPC = float(WR_Away_YPC)
            
        else:
            
            WR_Home_YPC = 1.0
            
        WR_total_YPC = ((WR_Away_YPC * WR_Away_GamesPlayed) + (WR_Home_YPC * WR_Home_GamesPlayed))/(WR_Home_GamesPlayed+WR_Away_GamesPlayed)
        WR_total_YPC = round(WR_total_YPC,1)
        
        
        
        #Calculate WR Yards Per Target
        WR_Away_YPT = get_statData(connection, name, "WR_away_stats", "Yards_perTarget")
        
        if WR_Away_YPT == None:
            WR_Away_YPT = 0.0
            
        elif WR_Away_YPT > 0.0:
            
            WR_Away_YPT = float(WR_Away_YPT)
            
        else:
            
            WR_Away_YPT = 0.0
               
        WR_Home_YPT = get_statData(connection, name, "WR_home_stats", "Yards_perTarget")
        
        if WR_Home_YPT == None:
            WR_Home_YPT = 1.0
            
        elif WR_Home_YPT > 0.0:
            
            WR_Home_YPT = float(WR_Away_YPT)
            
        else:
            
            WR_Home_YPT = 1.0

        WR_total_YPT = ((WR_Away_YPT * WR_Away_GamesPlayed) + (WR_Home_YPT * WR_Home_GamesPlayed))/(WR_Home_GamesPlayed+WR_Away_GamesPlayed)
        WR_total_YPT = round(WR_total_YPT,1)
        
        
        
        #Calculate WR Targets
        WR_Away_Targets = get_statData(connection, name, "WR_away_stats", "Targets")
        
        if WR_Away_Targets == None:
            WR_Away_Targets = 0
        
        WR_Home_Targets = get_statData(connection, name, "WR_home_stats", "Targets")
        
        if WR_Home_Targets == None:
            WR_Home_Targets = 0
            
        WR_total_Targets = WR_Away_Targets + WR_Home_Targets
        
        
        
        
        #Calculate WR Touchdowns
        WR_Away_Touchdowns = get_statData(connection, name, "WR_away_stats", "Touchdowns")
        
        if WR_Away_Touchdowns == None:
            WR_Away_Touchdowns = 0
        
        WR_Home_Touchdowns = get_statData(connection, name, "WR_home_stats", "Touchdowns")
        
        if WR_Home_Touchdowns == None:
            WR_Home_Touchdowns = 0
            
        WR_total_Touchdowns = WR_Away_Touchdowns + WR_Home_Touchdowns
        
        
        
        #Calculate WR Catch Percentage
        WR_Away_CatchPercent = get_statData(connection, name, "WR_away_stats", "Catch_Perc")
        
        if WR_Away_CatchPercent == None:
            WR_Away_CatchPercent = 0.0
            
        elif WR_Away_CatchPercent > 0.0:
            
            WR_Away_CatchPercent = float(WR_Away_CatchPercent)
            
        else:
            
            WR_Away_CatchPercent = 0.0
               
        WR_Home_CatchPercent = get_statData(connection, name, "WR_home_stats", "Catch_Perc")
        
        if WR_Home_CatchPercent == None:
            WR_Home_CatchPercent = 1.0
            
        elif WR_Home_CatchPercent > 0.0:
            
            WR_Home_CatchPercent = float(WR_Away_CatchPercent)
            
        else:
            
            WR_Home_CatchPercent = 1.0

        WR_total_CatchPercent = ((WR_Away_CatchPercent * WR_Away_GamesPlayed) + (WR_Home_CatchPercent * WR_Home_GamesPlayed))/(WR_Home_GamesPlayed+WR_Away_GamesPlayed)
        WR_total_CatchPercent = round(WR_total_CatchPercent,1)
        
        #Calculate WR Catches
        WR_Away_Catches = get_statData(connection, name, "WR_away_stats", "Catches")
        
        if WR_Away_Catches == None:
            WR_Away_Catches = 0
        
        WR_Home_Catches = get_statData(connection, name, "WR_home_stats", "Catches")
        
        if WR_Home_Catches == None:
            WR_Home_Catches = 0
            
        WR_total_Catches = WR_Away_Catches + WR_Home_Catches
        
        #Calculate WR First Down Catches
        WR_Away_FDC = get_statData(connection, name, "WR_away_stats", "FirstDown_Catches")
        
        if WR_Away_FDC == None:
            WR_Away_FDC = 0
        
        WR_Home_FDC = get_statData(connection, name, "WR_home_stats", "FirstDown_Catches")
        
        if WR_Home_FDC == None:
            WR_Home_FDC = 0
            
        WR_total_FDC = WR_Away_FDC + WR_Home_FDC
        
        
        
        
        # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
        insert_query = "INSERT INTO wr_total_stats (Name, Games_Played, Yards, Yards_PerReception, Yards_PerTarget, Targets, Touchdowns, Catch_Perc, Catches, FirstDown_Catches) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Yards=VALUES(Yards), Yards_PerReception=VALUES(Yards_PerReception), Yards_PerTarget=VALUES(Yards_PerTarget), Targets=VALUES(Targets), Touchdowns=VALUES(Touchdowns), Catch_Perc=VALUES(Catch_Perc), Catches=VALUES(Catches)"

        WR_data = [
            (name, WR_total_GamesPlayed, WR_total_Yards, WR_total_YPC, WR_total_YPT, WR_total_Targets, WR_total_Touchdowns, WR_total_CatchPercent, WR_total_Catches, WR_Away_FDC),
        # Add more rows if needed
                ]
    
        cursor.executemany(insert_query, WR_data)
        conn.commit()  
    connection.close()
    print("Updated Wide Receiver Total Stats")
        
def supplyTable_WR_Home():
    
    WR_Names = []
    gamesPlayed = []
    yards = []
    yards_PerReception = []
    yards_PerTarget = []
    targets = []
    touchdowns = []
    catch_Perc = []
    catches = []
    firstDown_Catches = []
    
    today = datetime.date.today()

    current_month = today.month
    
    current_year = today.year
    
    if current_month in [1, 2]:  # January is 1, February is 2
        current_year -= 1
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    # Get the website that has the Quarterback's stats
    
    driver.get("https://stathead.com/football/player_split_finder.cgi?request=1&order_by=pass_td&year_min="+str(current_year)+"&split_list=Game+Location&sub_game_location=Home&stat_ratio=season&show%5B%5D=rec&type=player")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    statTable = soup.find('div', id = 'div_game_location_splits')
    
    
    #--Wide Receiver Names--
    
    name_elements = statTable.find_all('td', class_='left', attrs={'data-stat': 'player'})
    
    
    for name_element in name_elements:
        a_element = name_element.find('a')
        player_name = a_element.text
        WR_Names.append(player_name)
        
    #--Wide Receiver Games Played--
    gamesPlayed_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'g'})

    for gamesPlayed_elements in gamesPlayed_elements:
        Games_Played = gamesPlayed_elements.text
        if Games_Played != '':
            gamesPlayed.append(int(Games_Played))
            
        else: 
            Games_Played = '0'
            gamesPlayed.append(int(Games_Played))
          
    #--Wide Receiver Yards--
    Yards_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_yds'})

    for Yards_elements in Yards_elements:
        
        Yards = Yards_elements.text
        
        if Yards != '':
            yards.append(float(Yards))
            
        else: 
            Yards = '0.0'
            yards.append(float(Yards))
    
    
    #--Wide Receiver Yards Per Reception--
    Yards_PerReception_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_yds_per_rec'})

    for Yards_PerReception_elements in Yards_PerReception_elements:
        
        Yards_PerReception = Yards_PerReception_elements.text
        
        if Yards_PerReception != '':
            yards_PerReception.append(float(Yards_PerReception))
            
        else: 
            Yards_PerReception = '0.0'
            yards_PerReception.append(float(Yards_PerReception))  
            
    #--Wide Receiver Yards Per Target--
    Yards_PerTarget_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_yds_per_tgt'})

    for Yards_PerTarget_elements in Yards_PerTarget_elements:
        
        Yards_PerTarget = Yards_PerTarget_elements.text
        
        if Yards_PerTarget != '':
            yards_PerTarget.append(float(Yards_PerTarget))
            
        else: 
            Yards_PerTarget = '0.0'
            yards_PerTarget.append(float(Yards_PerTarget))
            
      
    #--Wide Receiver Targets --
    Targets_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'targets'})

    for Targets_elements in Targets_elements:
        
        Targets = Targets_elements.text
        
        if Targets != '':
            targets.append(int(Targets))
            
        else: 
            Targets = '0'
            targets.append(int(Targets)) 
    
    #--Wide Receiver Touchdowns --
    Touchdowns_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_td'})

    for Touchdowns_elements in Touchdowns_elements:
        
        Touchdowns = Touchdowns_elements.text
        
        if Touchdowns != '':
            touchdowns.append(int(Touchdowns))
            
        else: 
            Touchdowns = '0'
            touchdowns.append(int(Touchdowns))
            
    #--Wide Receiver Catch Percentage --
    Catch_Perc_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'catch_pct'})

    for Catch_Perc_elements in Catch_Perc_elements:
        
        Catch_Perc = Catch_Perc_elements.text.strip('%')
        
        if Catch_Perc != '':
            catch_Perc.append(float(Catch_Perc))
            
        else: 
            Catch_Perc = '0.0'
            catch_Perc.append(float(Catch_Perc))
            
    #--Wide Receiver Catches --
    Catches_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec'})

    for Catches_elements in Catches_elements:
        
        Catches = Catches_elements.text.strip('%')
        
        if Catches != '':
            catches.append(int(Catches))
            
        else: 
            Catches = '0'
            catches.append(int(Catches))
    
    #--Wide Receiver First Down Catches --
    FirstDown_Catches_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_first_down'})

    for FirstDown_Catches_elements in  FirstDown_Catches_elements:
        
        FirstDown_Catches =  FirstDown_Catches_elements.text
        
        if FirstDown_Catches != '':
            firstDown_Catches.append(int(FirstDown_Catches))
            
        else: 
            FirstDown_Catches = '0'
            FirstDown_Catches.append(int(FirstDown_Catches))
            
    driver.quit()
    
    data_tuples = []

    for WR_Names, gamesPlayed, yards, yards_PerReception, yards_PerTarget, targets, touchdowns, catch_Perc, catches, firstDown_Catches in zip(
        WR_Names, gamesPlayed, yards, yards_PerReception, yards_PerTarget, targets, touchdowns, catch_Perc, catches, firstDown_Catches
    ):
        
        data_tuple = (
            
            WR_Names, gamesPlayed, yards, yards_PerReception, yards_PerTarget, targets, touchdowns, catch_Perc, catches, firstDown_Catches
        )
        data_tuples.append(data_tuple)
            
        
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO wr_home_stats (Name, Games_Played, Yards, Yards_PerReception, Yards_PerTarget, Targets, Touchdowns, Catch_Perc, Catches, FirstDown_Catches) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Yards=VALUES(Yards), Yards_PerReception=VALUES(Yards_PerReception), Yards_PerTarget=VALUES(Yards_PerTarget), Targets=VALUES(Targets), Touchdowns=VALUES(Touchdowns), Catch_Perc=VALUES(Catch_Perc), Catches=VALUES(Catches)"

    sorted_data_tuples = sorted(data_tuples, key=lambda x: x[0])
    
    cursor.executemany(insert_query, sorted_data_tuples)
    conn.commit()  
    
    print("Updated Wide Receiver Home Stats")
    
def supplyTable_WR_Away():
    
    WR_Names = []
    gamesPlayed = []
    yards = []
    yards_PerReception = []
    yards_PerTarget = []
    targets = []
    touchdowns = []
    catch_Perc = []
    catches = []
    firstDown_Catches = []
    
    today = datetime.date.today()

    current_month = today.month
    
    current_year = today.year
    
    if current_month in [1, 2]:  # January is 1, February is 2
        current_year -= 1
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    # Get the website that has the Quarterback's stats
    
    driver.get("https://stathead.com/football/player_split_finder.cgi?request=1&order_by=pass_td&year_min="+str(current_year)+"&split_list=Game+Location&sub_game_location=Away&stat_ratio=season&show%5B%5D=rec&type=player")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    statTable = soup.find('div', id = 'div_game_location_splits')
    
    
    #--Wide Receiver Names--
    
    name_elements = statTable.find_all('td', class_='left', attrs={'data-stat': 'player'})
    
    
    for name_element in name_elements:
        a_element = name_element.find('a')
        player_name = a_element.text
        WR_Names.append(player_name)
        
    #--Wide Receiver Games Played--
    gamesPlayed_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'g'})

    for gamesPlayed_elements in gamesPlayed_elements:
        Games_Played = gamesPlayed_elements.text
        if Games_Played != '':
            gamesPlayed.append(int(Games_Played))
            
        else: 
            Games_Played = '0'
            gamesPlayed.append(int(Games_Played))
          
    #--Wide Receiver Yards--
    Yards_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_yds'})

    for Yards_elements in Yards_elements:
        
        Yards = Yards_elements.text
        
        if Yards != '':
            yards.append(float(Yards))
            
        else: 
            Yards = '0.0'
            yards.append(float(Yards))
    
    
    #--Wide Receiver Yards Per Reception--
    Yards_PerReception_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_yds_per_rec'})

    for Yards_PerReception_elements in Yards_PerReception_elements:
        
        Yards_PerReception = Yards_PerReception_elements.text
        
        if Yards_PerReception != '':
            yards_PerReception.append(float(Yards_PerReception))
            
        else: 
            Yards_PerReception = '0.0'
            yards_PerReception.append(float(Yards_PerReception))  
            
    #--Wide Receiver Yards Per Target--
    Yards_PerTarget_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_yds_per_tgt'})

    for Yards_PerTarget_elements in Yards_PerTarget_elements:
        
        Yards_PerTarget = Yards_PerTarget_elements.text
        
        if Yards_PerTarget != '':
            yards_PerTarget.append(float(Yards_PerTarget))
            
        else: 
            Yards_PerTarget = '0.0'
            yards_PerTarget.append(float(Yards_PerTarget))
            
      
    #--Wide Receiver Targets --
    Targets_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'targets'})

    for Targets_elements in Targets_elements:
        
        Targets = Targets_elements.text
        
        if Targets != '':
            targets.append(int(Targets))
            
        else: 
            Targets = '0'
            targets.append(int(Targets)) 
    
    #--Wide Receiver Touchdowns --
    Touchdowns_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_td'})

    for Touchdowns_elements in Touchdowns_elements:
        
        Touchdowns = Touchdowns_elements.text
        
        if Touchdowns != '':
            touchdowns.append(int(Touchdowns))
            
        else: 
            Touchdowns = '0'
            touchdowns.append(int(Touchdowns))
            
    #--Wide Receiver Catch Percentage --
    Catch_Perc_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'catch_pct'})

    for Catch_Perc_elements in Catch_Perc_elements:
        
        Catch_Perc = Catch_Perc_elements.text.strip('%')
        
        if Catch_Perc != '':
            catch_Perc.append(float(Catch_Perc))
            
        else: 
            Catch_Perc = '0.0'
            catch_Perc.append(float(Catch_Perc))
            
    #--Wide Receiver Catches --
    Catches_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec'})

    for Catches_elements in Catches_elements:
        
        Catches = Catches_elements.text.strip('%')
        
        if Catches != '':
            catches.append(int(Catches))
            
        else: 
            Catches = '0'
            catches.append(int(Catches))
    
    #--Wide Receiver First Down Catches --
    FirstDown_Catches_elements = statTable.find_all('td', class_='right', attrs={'data-stat': 'rec_first_down'})

    for FirstDown_Catches_elements in  FirstDown_Catches_elements:
        
        FirstDown_Catches =  FirstDown_Catches_elements.text
        
        if FirstDown_Catches != '':
            firstDown_Catches.append(int(FirstDown_Catches))
            
        else: 
            FirstDown_Catches = '0'
            FirstDown_Catches.append(int(FirstDown_Catches))
            
    driver.quit()
    
    data_tuples = []

    for WR_Names, gamesPlayed, yards, yards_PerReception, yards_PerTarget, targets, touchdowns, catch_Perc, catches, firstDown_Catches in zip(
        WR_Names, gamesPlayed, yards, yards_PerReception, yards_PerTarget, targets, touchdowns, catch_Perc, catches, firstDown_Catches
    ):
        
        data_tuple = (
            
            WR_Names, gamesPlayed, yards, yards_PerReception, yards_PerTarget, targets, touchdowns, catch_Perc, catches, firstDown_Catches
        )
        data_tuples.append(data_tuple)
            
        
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO wr_away_stats (Name, Games_Played, Yards, Yards_PerReception, Yards_PerTarget, Targets, Touchdowns, Catch_Perc, Catches, FirstDown_Catches) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Yards=VALUES(Yards), Yards_PerReception=VALUES(Yards_PerReception), Yards_PerTarget=VALUES(Yards_PerTarget), Targets=VALUES(Targets), Touchdowns=VALUES(Touchdowns), Catch_Perc=VALUES(Catch_Perc), Catches=VALUES(Catches)"

    sorted_data_tuples = sorted(data_tuples, key=lambda x: x[0])
    
    cursor.executemany(insert_query, sorted_data_tuples)
    conn.commit()  
    print("Updated Wide Receiver Away Stats")



# Supply Defensive Player Tables
def supplyTable_DefPlayer_Totals():
    
    pass

def supplyTable_DefPlayer_Home():
    
    pass

def supplyTable_DefPlayer_Away():
    
    pass



# Supply Team Defense Tables
def supplyTable_TeamDef_Totals():
    
    teamNames = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati", "Cleveland", "Dallas", "Denver", "Detroit",
                 "Green Bay", "Houston", "Indianapolis", "Jacksonville", "Kansas City", "LA Chargers", "LA Rams", "Las Vegas", "Miami", "Minnesota",
                 "New England", "New Orleans", "NY Giants", "NY Jets", "Philadelphia", "Pittsburgh", "San Francisco", "Seattle", "Tampa Bay", "Tennessee", 
                 "Washington"]
    
    # Rushing Lists
    rushAttempts_PerGame = []
    rushYards_PerGame = []
    rushYards_PerAttempt = []
    rushFirstdowns_PerGame = []
    rushTouchdowns_PerGame = []
    
    #Passing Lists
    passAttempts_PerGame = []
    completions_PerGame = []
    completion_Perc = []
    passYards_PerGame = []
    passYards_PerAttempt = []
    passYards_PerCompletion = []
    passTouchdowns_PerGame = []
    passFirstdowns_PerGame = []
    sacks_PerGame = []
    
    yards_PerGame = []
    plays_PerGame = []
    yards_PerPlay = []
    firstdowns_PerGame = []
    thirddowns_PerGame = []
    thirddownConversions_PerGame = []
    thirddownConversion_Perc = []
    fourthdowns_PerGame = []
    fourthdownConversions_PerGame = []
    fourthdownConversion_Perc = []
    avgTimePossession = []
    pointsAllowed_PerGame = []
    touchdowns_PerGame = []
    redzoneScoring_Attempts_PerGame = []
    redzoneScores_PerGame = []
    redzoneScoring_Perc = []
    
    
    database_Name = "nfl_stats"
    
    connection = create_connection("nfl_stats")
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    
    # Get Teams Defense Rush Attempts Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-rushing-attempts-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushAttempt_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushAttempt_Elements) >= 3:
                        
                        rushAttempts_PerGame_element = rushAttempt_Elements[0]
                        
                        rushAttempts_PerGame_Stat = rushAttempts_PerGame_element.text.strip()
                        
                        rushAttempts_PerGame.append(rushAttempts_PerGame_Stat)
                        


    # Get Team Defense Rushing Yards Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-rushing-yards-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushYards_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushYards_PerGame_Elements) >= 3:
                        
                        rushYards_PerGame_element = rushYards_PerGame_Elements[0]
                        
                        rushYards_PerGame_Stat = rushYards_PerGame_element.text.strip()
                        
                        rushYards_PerGame.append(rushYards_PerGame_Stat)
                        
                        

    # Get Team Defense Rushing Yards Per Attempt
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-yards-per-rush-attempt")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushYards_PerAttempt_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushYards_PerAttempt_Elements) >= 3:
                        
                        rushYards_PerAttempt_element = rushYards_PerAttempt_Elements[0]
                        
                        rushYards_PerAttempt_Stat = rushYards_PerAttempt_element.text.strip()
                        
                        rushYards_PerAttempt.append(rushYards_PerAttempt_Stat)
                        
                        
                        
                        
                        
                        
    # Get Team Defense Rushing Firstdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-rushing-first-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushFirstDowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushFirstDowns_PerGame_Elements) >= 3:
                        
                        rushFirstDowns_PerGame_element = rushFirstDowns_PerGame_Elements[0]
                        
                        rushFirstDowns_PerGame_Stat = rushFirstDowns_PerGame_element.text.strip()
                        
                        rushFirstdowns_PerGame.append(rushFirstDowns_PerGame_Stat)
                        
                        
                        
                        
    # Get Team Defense Rushing Touchdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-rushing-touchdowns-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushTouchdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushTouchdowns_PerGame_Elements) >= 3:
                        
                        rushTouchdowns_PerGame_element = rushTouchdowns_PerGame_Elements[0]
                        
                        rushTouchdowns_PerGame_Stat = rushTouchdowns_PerGame_element.text.strip()
                        
                        rushTouchdowns_PerGame.append(rushTouchdowns_PerGame_Stat)
                        
                        
                        
    # Get Team Defense Pass Attempts Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-pass-attempts-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passAttempts_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passAttempts_PerGame_Elements) >= 3:
                        
                        passAttempts_PerGame_element = passAttempts_PerGame_Elements[0]
                        
                        passAttempts_PerGame_Stat = passAttempts_PerGame_element.text.strip()
                        
                        passAttempts_PerGame.append(passAttempts_PerGame_Stat)
                        
                        
                        
    # Get Team Defense Pass Completions Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-completions-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passCompletions_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passCompletions_PerGame_Elements) >= 3:
                        
                        passCompletions_PerGame_element = passCompletions_PerGame_Elements[0]
                        
                        passCompletions_PerGame_Stat = passCompletions_PerGame_element.text.strip()
                        
                        completions_PerGame.append(passCompletions_PerGame_Stat)
                        
                        
                        
    # Get Team Defense Pass Completions Percentage
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-completion-pct")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passCompletions_Perc_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passCompletions_Perc_Elements) >= 3:
                        
                        passCompletions_Perc_element = passCompletions_Perc_Elements[0]
                        
                        passCompletions_Perc_Stat = passCompletions_Perc_element.text.strip().rstrip('%')
                        
                        completion_Perc.append(passCompletions_Perc_Stat)
                        
                        
                        
    # Get Team Defense Pass Yards Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-passing-yards-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passYards_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passYards_PerGame_Elements) >= 3:
                        
                        passYards_PerGame_element = passYards_PerGame_Elements[0]
                        
                        passYards_PerGame_Stat = passYards_PerGame_element.text.strip()
                        
                        passYards_PerGame.append(passYards_PerGame_Stat)
                        
                        
                        
    # Get Team Defense Pass Yards Per Pass Attempt
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-yards-per-pass-attempt")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passYards_PerAttempt_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passYards_PerAttempt_Elements) >= 3:
                        
                        passYards_PerAttempt_element = passYards_PerAttempt_Elements[0]
                        
                        passYards_PerAttempt_Stat = passYards_PerAttempt_element.text.strip()
                        
                        passYards_PerAttempt.append(passYards_PerAttempt_Stat)
                        
                        
                        
    # Get Team Defense Pass Yards Per Pass Completion
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-yards-per-completion")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passYards_PerCompletion_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passYards_PerCompletion_Elements) >= 3:
                        
                        passYards_PerCompletion_element = passYards_PerCompletion_Elements[0]
                        
                        passYards_PerCompletion_Stat = passYards_PerCompletion_element.text.strip()
                        
                        passYards_PerCompletion.append(passYards_PerCompletion_Stat)
                        
                        
                        
    # Get Team Defense Pass Touchdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-passing-touchdowns-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passTouchdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passTouchdowns_PerGame_Elements) >= 3:
                        
                        passTouchdowns_PerGame_element = passTouchdowns_PerGame_Elements[0]
                        
                        passTouchdowns_PerGame_Stat = passTouchdowns_PerGame_element.text.strip()
                        
                        passTouchdowns_PerGame.append(passTouchdowns_PerGame_Stat)
                        
                        
    # Get Team Defense Pass Touchdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-passing-first-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passFirstdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passFirstdowns_PerGame_Elements) >= 3:
                        
                        passFirstdowns_PerGame_element = passFirstdowns_PerGame_Elements[0]
                        
                        passFirstdowns_PerGame_Stat = passFirstdowns_PerGame_element.text.strip()
                        
                        passFirstdowns_PerGame.append(passFirstdowns_PerGame_Stat)
    
                        
    # Get Team Defense Sacks Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/sacks-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    sacks_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(sacks_PerGame_Elements) >= 3:
                        
                        sacks_PerGame_element = sacks_PerGame_Elements[0]
                        
                        sacks_PerGame_Stat = sacks_PerGame_element.text.strip()
                        
                        sacks_PerGame.append(sacks_PerGame_Stat)
                        
    # Get Team Defense Yards Allowed Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-yards-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    yards_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(yards_PerGame_Elements) >= 3:
                        
                        yards_PerGame_element = yards_PerGame_Elements[0]
                        
                        yards_PerGame_Stat = yards_PerGame_element.text.strip()
                        
                        yards_PerGame.append(yards_PerGame_Stat)
                        
    # Get Team Defense Plays Allowed Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-plays-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    plays_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(plays_PerGame_Elements) >= 3:
                        
                        plays_PerGame_element = plays_PerGame_Elements[0]
                        
                        plays_PerGame_Stat = plays_PerGame_element.text.strip()
                        
                        plays_PerGame.append(plays_PerGame_Stat)
                        
    # Get Team Defense Yards Allowed Per Play
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-yards-per-play")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    yards_PerPlay_Elements = row.find_all('td', class_='text-right')
                    
                    if len(yards_PerPlay_Elements) >= 3:
                        
                        yards_PerPlay_element = yards_PerPlay_Elements[0]
                        
                        yards_PerPlay_Stat = yards_PerPlay_element.text.strip()
                        
                        yards_PerPlay.append(yards_PerPlay_Stat)
                        
    # Get Team Defense Firstdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-first-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    firstdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(firstdowns_PerGame_Elements) >= 3:
                        
                        firstdowns_PerGame_element = firstdowns_PerGame_Elements[0]
                        
                        firstdowns_PerGame_Stat = firstdowns_PerGame_element.text.strip()
                        
                        firstdowns_PerGame.append(firstdowns_PerGame_Stat)
                        
    # Get Team Defense Third Downs Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-third-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    thirddowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(thirddowns_PerGame_Elements) >= 3:
                        
                        thirddowns_PerGame_element = thirddowns_PerGame_Elements[0]
                        
                        thirddowns_PerGame_Stat = thirddowns_PerGame_element.text.strip()
                        
                        thirddowns_PerGame.append(thirddowns_PerGame_Stat)
                        
    # Get Team Defense Third Down Conversions Per Game Allowed
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-third-down-conversions-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    thirddownConversions_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(thirddownConversions_PerGame_Elements) >= 3:
                        
                        thirddownConversions_PerGame_element = thirddownConversions_PerGame_Elements[0]
                        
                        thirddownConversions_PerGame_Stat = thirddownConversions_PerGame_element.text.strip()
                        
                        thirddownConversions_PerGame.append(thirddownConversions_PerGame_Stat)
                        
    # Get Team Defense Third Down Conversion Perc
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-third-down-conversion-pct")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    thirddownConversion_Perc_Elements = row.find_all('td', class_='text-right')
                    
                    if len(thirddownConversion_Perc_Elements) >= 3:
                        
                        thirddownConversion_Perc_element = thirddownConversion_Perc_Elements[0]
                        
                        thirddownConversion_Perc_Stat = thirddownConversion_Perc_element.text.strip().rstrip('%')
                        
                        if thirddownConversion_Perc_Stat == "--":
                            
                            thirddownConversion_Perc_Stat = 0.0
                        
                        thirddownConversion_Perc.append(thirddownConversion_Perc_Stat)
                        
    # Get Team Defense Fourth Downs Per Game 
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-fourth-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    fourthdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(fourthdowns_PerGame_Elements) >= 3:
                        
                        fourthdowns_PerGame_element = fourthdowns_PerGame_Elements[0]
                        
                        fourthdowns_PerGame_Stat = fourthdowns_PerGame_element.text.strip()
                        
                        fourthdowns_PerGame.append(fourthdowns_PerGame_Stat)
                        
    # Get Team Defense Fourth Down Conversions Per Game Allowed
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-fourth-down-conversions-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    fourthdownConversions_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(fourthdownConversions_PerGame_Elements) >= 3:
                        
                        fourthdownConversions_PerGame_element = fourthdownConversions_PerGame_Elements[0]
                        
                        fourthdownConversions_PerGame_Stat = fourthdownConversions_PerGame_element.text.strip()
                        
                        fourthdownConversions_PerGame.append(fourthdownConversions_PerGame_Stat)
                        
    # Get Team Defense Fourth Down Conversion Perc
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-fourth-down-conversion-pct")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    fourthdownConversion_Perc_Elements = row.find_all('td', class_='text-right')
                    
                    if len(fourthdownConversion_Perc_Elements) >= 3:
                        
                        fourthdownConversion_Perc_element = fourthdownConversion_Perc_Elements[0]
                        
                        fourthdownConversion_Perc_Stat = fourthdownConversion_Perc_element.text.strip().rstrip('%')
                        
                        if fourthdownConversion_Perc_Stat == "--":
                            
                            fourthdownConversion_Perc_Stat = 0.0
                        
                        fourthdownConversion_Perc.append(fourthdownConversion_Perc_Stat)
                        
    # Get Team Defense Average Time of Possession Allowed
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-average-time-of-possession-net-of-ot")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    avgTimePossession_Elements = row.find_all('td', class_='text-right')
                    
                    if len(avgTimePossession_Elements) >= 3:
                        
                        avgTimePossession_element = avgTimePossession_Elements[0]
                        
                        avgTimePossession_Stat = avgTimePossession_element.text.strip()
                        
                        avgTimePossession.append(avgTimePossession_Stat)
                        
    # Get Team Defense Points Allowed Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-points-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    pointsAllowed_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(pointsAllowed_PerGame_Elements) >= 3:
                        
                        pointsAllowed_PerGame_element = pointsAllowed_PerGame_Elements[0]
                        
                        pointsAllowed_PerGame_Stat = pointsAllowed_PerGame_element.text.strip()
                        
                        pointsAllowed_PerGame.append(pointsAllowed_PerGame_Stat)
                        
    # Get Team Defense Touchdowns Allowed Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-touchdowns-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    touchdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(touchdowns_PerGame_Elements) >= 3:
                        
                        touchdowns_PerGame_element = touchdowns_PerGame_Elements[0]
                        
                        touchdowns_PerGame_Stat = touchdowns_PerGame_element.text.strip()
                        
                        touchdowns_PerGame.append(touchdowns_PerGame_Stat)
                        
    # Get Team Defense RedZone Scoring Attempts Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-red-zone-scoring-attempts-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    redzoneScoring_Attempts_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(redzoneScoring_Attempts_PerGame_Elements) >= 3:
                        
                        redzoneScoring_Attempts_PerGame_element = redzoneScoring_Attempts_PerGame_Elements[0]
                        
                        redzoneScoring_Attempts_PerGame_Stat = redzoneScoring_Attempts_PerGame_element.text.strip()
                        
                        redzoneScoring_Attempts_PerGame.append(redzoneScoring_Attempts_PerGame_Stat)
                        
    # Get Team Defense RedZone Scores Allowed Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-red-zone-scores-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    redzoneScores_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(redzoneScores_PerGame_Elements) >= 3:
                        
                        redzoneScores_PerGame_element = redzoneScores_PerGame_Elements[0]
                        
                        redzoneScores_PerGame_Stat = redzoneScores_PerGame_element.text.strip()
                        
                        redzoneScores_PerGame.append(redzoneScores_PerGame_Stat)
                        
    # Get Team Defense RedZone Scoring Percentage
    driver.get("https://www.teamrankings.com/nfl/stat/opponent-red-zone-scoring-pct")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    redzoneScoring_Perc_Elements = row.find_all('td', class_='text-right')
                    
                    if len(redzoneScoring_Perc_Elements) >= 3:
                        
                        redzoneScoring_Perc_element = redzoneScoring_Perc_Elements[0]
                        
                        redzoneScoring_Perc_Stat = redzoneScoring_Perc_element.text.strip().rstrip('%')
                        
                        redzoneScoring_Perc.append(redzoneScoring_Perc_Stat)
                        
    driver.quit() 
    
                       
    # Iterate through the lists and insert/update data in the database
    count = 0
    for i in range(len(teamNames)):
        team_Name_entry = teamNames[i]
        rush_attempts_entry = rushAttempts_PerGame[count]
        rush_yards_entry = rushYards_PerGame[count]
        rushYards_PerAttempt_entry = rushYards_PerAttempt[count]
        rushFirstdowns_PerGame_entry = rushFirstdowns_PerGame[count]
        rushTouchdowns_PerGame_entry = rushTouchdowns_PerGame[count]
        
        passAttempts_PerGame_entry = passAttempts_PerGame[count]
        completions_PerGame_entry = completions_PerGame[count]
        completion_Perc_entry = completion_Perc[count]
        passYards_PerGame_entry = passYards_PerGame[count]
        passYards_PerAttempt_entry = passYards_PerAttempt[count]
        passYards_PerCompletion_entry = passYards_PerCompletion[count]
        passFirstdowns_PerGame_entry = passFirstdowns_PerGame[count]
        passTouchdowns_PerGame_entry = passTouchdowns_PerGame[count]
        sacks_PerGame_entry = sacks_PerGame[count]
        
        yards_PerGame_entry = yards_PerGame[count]
        plays_PerGame_entry = plays_PerGame[count]
        yards_PerPlay_entry = yards_PerPlay[count]
        firstdowns_PerGame_entry = firstdowns_PerGame[count]
        thirddowns_PerGame_entry = thirddowns_PerGame[count]
        thirddownConversions_PerGame_entry = thirddownConversions_PerGame[count]
        thirddownConversion_Perc_entry = thirddownConversion_Perc[count]
        fourthdowns_PerGame_entry = fourthdowns_PerGame[count]
        fourthdownConversions_PerGame_entry = fourthdownConversions_PerGame[count]
        fourthdownConversion_Perc_entry = fourthdownConversion_Perc[count]
        avgTimePossession_entry = avgTimePossession[count]
        pointsAllowed_PerGame_entry = pointsAllowed_PerGame[count]
        touchdowns_PerGame_entry = touchdowns_PerGame[count]
        redzoneScoring_Attempts_PerGame_entry = redzoneScoring_Attempts_PerGame[count]
        redzoneScores_PerGame_entry = redzoneScores_PerGame[count]
        redzoneScoring_Perc_entry = redzoneScoring_Perc[count]
        
        
        
        # Define the SQL INSERT query with ON DUPLICATE KEY UPDATE
        insert_query = """
        INSERT INTO defteam_rushing_stats(Name, RushAttempts_PerGame, RushYards_PerGame, RushYards_PerAttempt, RushFirstDowns_PerGame, RushTouchdowns_PerGame) 
        VALUES(%s, %s, %s, %s, %s, %s) 
        ON DUPLICATE KEY UPDATE
        RushAttempts_PerGame = VALUES(RushAttempts_PerGame),
        RushYards_PerGame = VALUES(RushYards_PerGame),
        RushYards_PerAttempt = VALUES(RushYards_PerAttempt),
        RushFirstDowns_PerGame = VALUES(RushFirstDowns_PerGame),
        RushTouchdowns_PerGame = VALUES(RushTouchdowns_PerGame);
        """
        
        insert_query2 = """
        INSERT INTO defteam_passing_stats(Name, PassAttempts_PerGame, Completions_PerGame, Completion_Perc, PassYards_PerGame, PassYards_PerAttempt, PassYards_PerCompletion,
        PassFirstDown_PerGame, PassTouchdowns_PerGame, Sacks_PerGame)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        PassAttempts_PerGame = VALUES(PassAttempts_PerGame),
        Completions_PerGame = VALUES(Completions_PerGame),
        Completion_Perc = VALUES(Completion_Perc),
        PassYards_PerGame = VALUES(PassYards_PerGame),
        PassYards_PerAttempt = VALUES(PassYards_PerAttempt),
        PassYards_PerCompletion = VALUES(PassYards_PerCompletion),
        PassFirstDown_PerGame = VALUES(PassFirstDown_PerGame),
        PassTouchdowns_PerGame = VALUES(PassTouchdowns_PerGame),
        Sacks_PerGame = VALUES(Sacks_PerGame);
        """
        
        insert_query3 = """
        INSERT INTO team_total_defense(Name, yards_PerGame, plays_PerGame, yards_PerPlay, firstdowns_PerGame, thirddowns_PerGame, thirddownConversions_PerGame, thirddownConversion_Perc,
        fourthdowns_PerGame, fourthdownConversions_PerGame, fourthdownConversion_Perc, avgTimePossession, pointsAllowed_PerGame, touchdowns_PerGame, redzoneScoring_Attempts_PerGame, 
        redzoneScores_PerGame, redzoneScoring_Perc)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        yards_PerGame = VALUES(yards_PerGame),
        plays_PerGame = VALUES(plays_PerGame),
        yards_PerPlay = VALUES(yards_PerPlay),
        firstdowns_PerGame = VALUES(firstdowns_PerGame),
        thirddowns_PerGame = VALUES(thirddowns_PerGame),
        thirddownConversions_PerGame = VALUES(thirddownConversions_PerGame),
        thirddownConversion_Perc = VALUES(thirddownConversion_Perc),
        fourthdowns_PerGame = VALUES(fourthdowns_PerGame),
        fourthdownConversions_PerGame = VALUES(fourthdownConversions_PerGame),
        fourthdownConversion_Perc = VALUES(fourthdownConversion_Perc),
        avgTimePossession = VALUES(avgTimePossession),
        pointsAllowed_PerGame = VALUES(pointsAllowed_PerGame),
        touchdowns_PerGame = VALUES(touchdowns_PerGame),
        redzoneScoring_Attempts_PerGame = VALUES(redzoneScoring_Attempts_PerGame),
        redzoneScores_PerGame = VALUES(redzoneScores_PerGame),
        redzoneScoring_Perc = VALUES(redzoneScoring_Perc);
        """

        # Execute the SQL query
        cursor.execute(insert_query, (team_Name_entry, rush_attempts_entry, rush_yards_entry, rushYards_PerAttempt_entry, rushFirstdowns_PerGame_entry, rushTouchdowns_PerGame_entry))
        cursor.execute(insert_query2, (team_Name_entry, passAttempts_PerGame_entry, completions_PerGame_entry, completion_Perc_entry, passYards_PerGame_entry, passYards_PerAttempt_entry, passYards_PerCompletion_entry, passFirstdowns_PerGame_entry, passTouchdowns_PerGame_entry, sacks_PerGame_entry))
        cursor.execute(insert_query3, (team_Name_entry, yards_PerGame_entry, plays_PerGame_entry, yards_PerPlay_entry, firstdowns_PerGame_entry, thirddowns_PerGame_entry, thirddownConversions_PerGame_entry, thirddownConversion_Perc_entry, fourthdowns_PerGame_entry, fourthdownConversions_PerGame_entry, fourthdownConversion_Perc_entry, avgTimePossession_entry, pointsAllowed_PerGame_entry, touchdowns_PerGame_entry, redzoneScoring_Attempts_PerGame_entry, redzoneScores_PerGame_entry, redzoneScoring_Perc_entry))
        # Commit the changes to the database
        conn.commit()

        count += 1
    # Close the database connection
    cursor.close()
    conn.close()

def supplyTable_TeamDef_Home():
    
    pass
                        

def supplyTable_TeamDef_Away():
    
    pass

# Supply Team Offense Tables
def supplyTable_TeamOff_Totals():
    
    teamNames = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati", "Cleveland", "Dallas", "Denver", "Detroit",
                 "Green Bay", "Houston", "Indianapolis", "Jacksonville", "Kansas City", "LA Chargers", "LA Rams", "Las Vegas", "Miami", "Minnesota",
                 "New England", "New Orleans", "NY Giants", "NY Jets", "Philadelphia", "Pittsburgh", "San Francisco", "Seattle", "Tampa Bay", "Tennessee", 
                 "Washington"]
    
    rushAttempts_PerGame = []
    rushYards_PerGame = []
    rushFirstDowns_PerGame = []
    rushTouchdowns_PerGame = []
    rushYards_PerAttempt = []
    
    passAttempts_PerGame = []
    completions_PerGame = []
    completion_Perc = []
    passYards_PerGame = []
    passYards_PerAttempt = []
    passYards_PerCompletion = []
    passTouchdowns_PerGame = []
    sacks_PerGame = []
    
    yards_PerGame = []
    plays_PerGame = []
    yards_PerPlay = []
    firstdowns_PerGame = []
    thirddowns_PerGame = []
    thirddownConversions_PerGame = []
    forthdowns_PerGame = []
    forthdownConversions_PerGame = []
    avgTimePossession = []
    points_PerGame = []
    avgScoreMargin = []
    touchdowns_PerGame = []
    redzoneScoring_Attempts_PerGame = []
    redzoneScores_PerGame = []
    redzoneScoring_Perc = []
    
    
    
    
    database_Name = "nfl_stats"
    
    connection = create_connection("nfl_stats")
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    
    # Get Teams Offense Rush Attempts Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/rushing-attempts-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
    
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushAttempt_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushAttempt_Elements) >= 3:
                        
                        rushAttempts_PerGame_element = rushAttempt_Elements[0]
                        
                        rushAttempt_PerGame_Stat = rushAttempts_PerGame_element.text.strip()
                        
                        rushAttempts_PerGame.append(rushAttempt_PerGame_Stat)
                        
                        
    
    # Get Teams Offense Rush Yards Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/rushing-yards-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushYards_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushYards_PerGame_Elements) >= 3:
                        
                        rushYards_PerGame_element = rushYards_PerGame_Elements[0]
                        
                        rushYards_PerGame_Stat = rushYards_PerGame_element.text.strip()
                        
                        rushYards_PerGame.append(rushYards_PerGame_Stat)
                        
                        
                        
    # Get Teams Offense Rush First Downs Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/rushing-first-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushFirstDowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushFirstDowns_PerGame_Elements) >= 3:
                        
                        rushFirstDowns_PerGame_element = rushFirstDowns_PerGame_Elements[0]
                        
                        rushFirstDowns_PerGame_Stat = rushFirstDowns_PerGame_element.text.strip()
                        
                        rushFirstDowns_PerGame.append(rushFirstDowns_PerGame_Stat)
                        
                        
                        
    # Get Teams Offense Rush Touchdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/rushing-touchdowns-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushTouchdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushTouchdowns_PerGame_Elements) >= 3:
                        
                        rushTouchdowns_PerGame_element = rushTouchdowns_PerGame_Elements[0]
                        
                        rushTouchdowns_PerGame_Stat = rushTouchdowns_PerGame_element.text.strip()
                        
                        rushTouchdowns_PerGame.append(rushTouchdowns_PerGame_Stat)
                        
                        
                        
    # Get Teams Offense Rush Yards Per Attempt
    driver.get("https://www.teamrankings.com/nfl/stat/yards-per-rush-attempt")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    rushYards_PerAttempt_Elements = row.find_all('td', class_='text-right')
                    
                    if len(rushYards_PerAttempt_Elements) >= 3:
                        
                        rushYards_PerAttempt_element = rushYards_PerAttempt_Elements[0]
                        
                        rushYards_PerAttempt_Stat = rushYards_PerAttempt_element.text.strip()
                        
                        rushYards_PerAttempt.append(rushYards_PerAttempt_Stat)
                        
                        

    # Get Teams Offense Pass Attempts Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/pass-attempts-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passAttempts_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passAttempts_PerGame_Elements) >= 3:
                        
                        passAttempts_PerGame_element = passAttempts_PerGame_Elements[0]
                        
                        passAttempts_PerGame_Stat = passAttempts_PerGame_element.text.strip()
                        
                        passAttempts_PerGame.append(passAttempts_PerGame_Stat)
                        
                        
                        
    # Get Teams Offense Pass Completions Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/completions-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passCompletions_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passCompletions_PerGame_Elements) >= 3:
                        
                        passCompletions_PerGame_element = passCompletions_PerGame_Elements[0]
                        
                        passCompletions_PerGame_Stat = passCompletions_PerGame_element.text.strip()
                        
                        completions_PerGame.append(passCompletions_PerGame_Stat)
                        
                        
                        
    # Get Teams Offense Pass Completions Percentage
    driver.get("https://www.teamrankings.com/nfl/stat/completion-pct")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passCompletions_Perc_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passCompletions_Perc_Elements) >= 3:
                        
                        passCompletions_Perc_element = passCompletions_Perc_Elements[0]
                        
                        passCompletions_Perc_Stat = passCompletions_Perc_element.text.strip().rstrip('%')
                        
                        completion_Perc.append(passCompletions_Perc_Stat)
                        
                        
                        
    # Get Teams Offense Pass Yards Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/passing-yards-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passYards_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passYards_PerGame_Elements) >= 3:
                        
                        passYards_PerGame_element = passYards_PerGame_Elements[0]
                        
                        passYards_PerGame_Stat = passYards_PerGame_element.text.strip()
                        
                        passYards_PerGame.append(passYards_PerGame_Stat)
                        
                        
                        
    # Get Teams Offense Pass Yards Per Attempt
    driver.get("https://www.teamrankings.com/nfl/stat/yards-per-pass-attempt")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passYards_PerAttempt_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passYards_PerAttempt_Elements) >= 3:
                        
                        passYards_PerAttempt_element = passYards_PerAttempt_Elements[0]
                        
                        passYards_PerAttempt_Stat = passYards_PerAttempt_element.text.strip()
                        
                        passYards_PerAttempt.append(passYards_PerAttempt_Stat)
                        
                        
                        
    # Get Teams Offense Pass Yards Per Completion
    driver.get("https://www.teamrankings.com/nfl/stat/yards-per-completion")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passYards_PerCompletion_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passYards_PerAttempt_Elements) >= 3:
                        
                        passYards_PerCompletion_element = passYards_PerCompletion_Elements[0]
                        
                        passYards_PerCompletion_Stat = passYards_PerCompletion_element.text.strip()
                        
                        passYards_PerCompletion.append(passYards_PerCompletion_Stat)
                        
                        
                        
    # Get Teams Offense Pass Touchdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/passing-touchdowns-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    passTouchdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(passTouchdowns_PerGame_Elements) >= 3:
                        
                        passTouchdowns_PerGame_element = passTouchdowns_PerGame_Elements[0]
                        
                        passTouchdowns_PerGame_Stat = passTouchdowns_PerGame_element.text.strip()
                        
                        passTouchdowns_PerGame.append(passTouchdowns_PerGame_Stat)
                        
                        
                        
    # Get Teams Offense Sacks Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/qb-sacked-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    sacks_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(sacks_PerGame_Elements) >= 3:
                        
                        sacks_PerGame_element = sacks_PerGame_Elements[0]
                        
                        sacks_PerGame_Stat = sacks_PerGame_element.text.strip()
                        
                        sacks_PerGame.append(sacks_PerGame_Stat)
                        
    # Get Teams Offense Yards Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/yards-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    yards_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(yards_PerGame_Elements) >= 3:
                        
                        yards_PerGame_element = yards_PerGame_Elements[0]
                        
                        yards_PerGame_Stat = yards_PerGame_element.text.strip()
                        
                        yards_PerGame.append(yards_PerGame_Stat)
                        
    # Get Teams Offense Plays Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/plays-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    plays_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(plays_PerGame_Elements) >= 3:
                        
                        plays_PerGame_element = plays_PerGame_Elements[0]
                        
                        plays_PerGame_Stat = plays_PerGame_element.text.strip()
                        
                        plays_PerGame.append(plays_PerGame_Stat)
                        
    # Get Teams Offense Yards Per Play
    driver.get("https://www.teamrankings.com/nfl/stat/yards-per-play")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    yards_PerPlay_Elements = row.find_all('td', class_='text-right')
                    
                    if len(yards_PerPlay_Elements) >= 3:
                        
                        yards_PerPlay_element = yards_PerPlay_Elements[0]
                        
                        yards_PerPlay_Stat = yards_PerPlay_element.text.strip()
                        
                        yards_PerPlay.append(yards_PerPlay_Stat)
                        
                        
    # Get Teams Offense Firstdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/first-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    firstdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(firstdowns_PerGame_Elements) >= 3:
                        
                        firstdowns_PerGame_element = firstdowns_PerGame_Elements[0]
                        
                        firstdowns_PerGame_Stat = firstdowns_PerGame_element.text.strip()
                        
                        firstdowns_PerGame.append(firstdowns_PerGame_Stat)
                        
    # Get Teams Offense Thirddowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/third-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    thirddowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(thirddowns_PerGame_Elements) >= 3:
                        
                        thirddowns_PerGame_element = thirddowns_PerGame_Elements[0]
                        
                        thirddowns_PerGame_Stat = thirddowns_PerGame_element.text.strip()
                        
                        thirddowns_PerGame.append(thirddowns_PerGame_Stat)
                        
    # Get Teams Offense Thirddown Conversions Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/third-down-conversions-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    thirddownConversions_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(thirddownConversions_PerGame_Elements) >= 3:
                        
                        thirddownConversions_PerGame_element = thirddownConversions_PerGame_Elements[0]
                        
                        thirddownConversions_PerGame_Stat = thirddownConversions_PerGame_element.text.strip()
                        
                        thirddownConversions_PerGame.append(thirddownConversions_PerGame_Stat)
                        
    # Get Teams Offense Forthdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/fourth-downs-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    forthdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(forthdowns_PerGame_Elements) >= 3:
                        
                        forthdowns_PerGame_element = forthdowns_PerGame_Elements[0]
                        
                        forthdowns_PerGame_Stat = forthdowns_PerGame_element.text.strip()
                        
                        forthdowns_PerGame.append(forthdowns_PerGame_Stat)
                        
    # Get Teams Offense Forthdown conversions Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/fourth-down-conversions-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    forthdownConversions_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(forthdownConversions_PerGame_Elements) >= 3:
                        
                        forthdownConversions_PerGame_element = forthdownConversions_PerGame_Elements[0]
                        
                        forthdownConversions_PerGame_Stat = forthdownConversions_PerGame_element.text.strip()
                        
                        forthdownConversions_PerGame.append(forthdownConversions_PerGame_Stat)
                        
    # Get Teams Offense Average Time of Possession
    driver.get("https://www.teamrankings.com/nfl/stat/average-time-of-possession-net-of-ot")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    avgTimePossession_Elements = row.find_all('td', class_='text-right')
                    
                    if len(avgTimePossession_Elements) >= 3:
                        
                        avgTimePossession_element = avgTimePossession_Elements[0]
                        
                        avgTimePossession_Stat = avgTimePossession_element.text.strip()
                        
                        avgTimePossession.append(avgTimePossession_Stat)
                        
    # Get Teams Offense Points Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/points-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    points_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(points_PerGame_Elements) >= 3:
                        
                        points_PerGame_element = points_PerGame_Elements[0]
                        
                        points_PerGame_Stat = points_PerGame_element.text.strip()
                        
                        points_PerGame.append(points_PerGame_Stat)
                        
    # Get Teams Offense Average Score Margin Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/average-scoring-margin")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    avgScoreMargin_Elements = row.find_all('td', class_='text-right')
                    
                    if len(avgScoreMargin_Elements) >= 3:
                        
                        avgScoreMargin_element = avgScoreMargin_Elements[0]
                        
                        avgScoreMargin_Stat = avgScoreMargin_element.text.strip()
                        
                        avgScoreMargin.append(avgScoreMargin_Stat)
                        
    # Get Teams Offense Touchdowns Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/touchdowns-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    touchdowns_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(touchdowns_PerGame_Elements) >= 3:
                        
                        touchdowns_PerGame_element = touchdowns_PerGame_Elements[0]
                        
                        touchdowns_PerGame_Stat = touchdowns_PerGame_element.text.strip()
                        
                        touchdowns_PerGame.append(touchdowns_PerGame_Stat)
                
    # Get Teams Offense RedZone Scoring Attempts Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/red-zone-scoring-attempts-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    redzoneScoring_Attempts_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(redzoneScoring_Attempts_PerGame_Elements) >= 3:
                        
                        redzoneScoring_Attempts_PerGame_element = redzoneScoring_Attempts_PerGame_Elements[0]
                        
                        redzoneScoring_Attempts_PerGame_Stat = redzoneScoring_Attempts_PerGame_element.text.strip()
                        
                        redzoneScoring_Attempts_PerGame.append(redzoneScoring_Attempts_PerGame_Stat)
                        
    # Get Teams Offense RedZone scores Per Game
    driver.get("https://www.teamrankings.com/nfl/stat/red-zone-scores-per-game")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    redzoneScores_PerGame_Elements = row.find_all('td', class_='text-right')
                    
                    if len(redzoneScores_PerGame_Elements) >= 3:
                        
                        redzoneScores_PerGame_element = redzoneScores_PerGame_Elements[0]
                        
                        redzoneScores_PerGame_Stat = redzoneScores_PerGame_element.text.strip()
                        
                        redzoneScores_PerGame.append(redzoneScores_PerGame_Stat)
                        
    # Get Teams Offense RedZone scoring Percentage
    driver.get("https://www.teamrankings.com/nfl/stat/red-zone-scoring-pct")
    
    time.sleep(2)
            # Set up BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                        
    for team in teamNames:
        
        rows = scrollWrapper.find_all('tr', role='row')
        
        for row in rows:
            team_name_element = row.find('td', class_='text-left nowrap')
            if team_name_element:
                team_name = team_name_element.text.strip()

                if team_name == team:
                    
                    redzoneScoring_Perc_Elements = row.find_all('td', class_='text-right')
                    
                    if len(redzoneScoring_Perc_Elements) >= 3:
                        
                        redzoneScoring_Perc_element = redzoneScoring_Perc_Elements[0]
                        
                        redzoneScoring_Perc_Stat = redzoneScoring_Perc_element.text.strip().rstrip('%')
                        
                        redzoneScoring_Perc.append(redzoneScoring_Perc_Stat)
                        
                        

    driver.quit() 
                       
    # Iterate through the lists and insert/update data in the database
    count = 0
    for i in range(len(teamNames)):
        team_Name_entry = teamNames[i]
        rush_attempts_entry = rushAttempts_PerGame[count]
        rush_yards_entry = rushYards_PerGame[count]
        rushYards_PerAttempt_entry = rushYards_PerAttempt[count]
        rushFirstdowns_PerGame_entry = rushFirstDowns_PerGame[count]
        rushTouchdowns_PerGame_entry = rushTouchdowns_PerGame[count]
        
        passAttempts_PerGame_entry = passAttempts_PerGame[count]
        completions_PerGame_entry = completions_PerGame[count]
        completion_Perc_entry = completion_Perc[count]
        passYards_PerGame_entry = passYards_PerGame[count]
        passYards_PerAttempt_entry = passYards_PerAttempt[count]
        passYards_PerCompletion_entry = passYards_PerCompletion[count]
        passTouchdowns_PerGame_entry = passTouchdowns_PerGame[count]
        sacks_PerGame_entry = sacks_PerGame[count]
        
        yards_PerGame_entry = yards_PerGame[count]
        plays_PerGame_entry = plays_PerGame[count]
        yards_PerPlay_entry = yards_PerPlay[count]
        firstdowns_PerGame_entry = firstdowns_PerGame[count]
        thirddowns_PerGame_entry = thirddowns_PerGame[count]
        thirddownConversions_PerGame_entry = thirddownConversions_PerGame[count]
        forthdowns_PerGame_entry = forthdowns_PerGame[count]
        forthdownConversions_PerGame_entry = forthdownConversions_PerGame[count]
        avgTimePossession_entry = avgTimePossession[count]
        points_PerGame_entry = points_PerGame[count]
        avgScoreMargin_entry = avgScoreMargin[count]
        touchdowns_PerGame_entry = touchdowns_PerGame[count]
        redzoneScoring_Attempts_PerGame_entry = redzoneScoring_Attempts_PerGame[count]
        redzoneScores_PerGame_entry = redzoneScores_PerGame[count]
        redzoneScoring_Perc_entry = redzoneScoring_Perc[count]
        
        
        
        # Define the SQL INSERT query with ON DUPLICATE KEY UPDATE
        insert_query = """
        INSERT INTO offteam_rushing_stats(Name, RushAttempts_PerGame, RushYards_PerGame, RushYards_PerAttempt, RushFirstDowns_PerGame, RushTouchdowns_PerGame) 
        VALUES(%s, %s, %s, %s, %s, %s) 
        ON DUPLICATE KEY UPDATE
        RushAttempts_PerGame = VALUES(RushAttempts_PerGame),
        RushYards_PerGame = VALUES(RushYards_PerGame),
        RushYards_PerAttempt = VALUES(RushYards_PerAttempt),
        RushFirstDowns_PerGame = VALUES(RushFirstDowns_PerGame),
        RushTouchdowns_PerGame = VALUES(RushTouchdowns_PerGame);
        """
        
        insert_query2 = """
        INSERT INTO offteam_passing_stats(Name, PassAttempts_PerGame, Completions_PerGame, Completion_Perc, PassYards_PerGame, PassYards_PerAttempt, PassYards_PerCompletion,
        PassTouchdowns_PerGame, Sacks_PerGame)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        PassAttempts_PerGame = VALUES(PassAttempts_PerGame),
        Completions_PerGame = VALUES(Completions_PerGame),
        Completion_Perc = VALUES(Completion_Perc),
        PassYards_PerGame = VALUES(PassYards_PerGame),
        PassYards_PerAttempt = VALUES(PassYards_PerAttempt),
        PassYards_PerCompletion = VALUES(PassYards_PerCompletion),
        PassTouchdowns_PerGame = VALUES(PassTouchdowns_PerGame),
        Sacks_PerGame = VALUES(Sacks_PerGame);
        """
        
        insert_query3 = """
        INSERT INTO team_total_offense(Name, yards_PerGame, plays_PerGame, yards_PerPlay, firstdowns_PerGame, thirddowns_PerGame, thirddownConversions_PerGame,
        forthdowns_PerGame, forthdownConversions_PerGame, avgTimePossession, points_PerGame, avgScoreMargin, touchdowns_PerGame, redzoneScoring_Attempts_PerGame, redzoneScores_PerGame,
        redzoneScoring_Perc)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        yards_PerGame = VALUES(yards_PerGame),
        plays_PerGame = VALUES(plays_PerGame),
        yards_PerPlay = VALUES(yards_PerPlay),
        firstdowns_PerGame = VALUES(firstdowns_PerGame),
        thirddowns_PerGame = VALUES(thirddowns_PerGame),
        thirddownConversions_PerGame = VALUES(thirddownConversions_PerGame),
        forthdowns_PerGame = VALUES(forthdowns_PerGame),
        forthdownConversions_PerGame = VALUES(forthdownConversions_PerGame),
        avgTimePossession = VALUES(avgTimePossession),
        points_PerGame = VALUES(points_PerGame),
        avgScoreMargin = VALUES(avgScoreMargin),
        touchdowns_PerGame = VALUES(touchdowns_PerGame),
        redzoneScoring_Attempts_PerGame = VALUES(redzoneScoring_Attempts_PerGame),
        redzoneScores_PerGame = VALUES(redzoneScores_PerGame),
        redzoneScoring_Perc = VALUES(redzoneScoring_Perc);
        """

        # Execute the SQL query
        cursor.execute(insert_query, (team_Name_entry, rush_attempts_entry, rush_yards_entry, rushYards_PerAttempt_entry, rushFirstdowns_PerGame_entry, rushTouchdowns_PerGame_entry))
        cursor.execute(insert_query2, (team_Name_entry, passAttempts_PerGame_entry, completions_PerGame_entry, completion_Perc_entry, passYards_PerGame_entry, passYards_PerAttempt_entry, passYards_PerCompletion_entry, passTouchdowns_PerGame_entry, sacks_PerGame_entry))
        cursor.execute(insert_query3, (team_Name_entry, yards_PerGame_entry, plays_PerGame_entry, yards_PerPlay_entry, firstdowns_PerGame_entry, thirddowns_PerGame_entry, thirddownConversions_PerGame_entry, forthdowns_PerGame_entry, forthdownConversions_PerGame_entry, avgTimePossession_entry, points_PerGame_entry, avgScoreMargin_entry, touchdowns_PerGame_entry, redzoneScoring_Attempts_PerGame_entry, redzoneScores_PerGame_entry, redzoneScoring_Perc_entry))
        # Commit the changes to the database
        conn.commit()

        count += 1
    # Close the database connection
    cursor.close()
    conn.close()



# Supply Teams Defensive Roster
def supplyTable_Team_DefenseRoster():
    
    pass

# Supply Teams Offensive Roster
def supplyTable_Team_OffenseRoster():
    team_ABR = ["buf", "mia", "ne", "nyj", "bal", "cin", "cle", "pit", "hou", "ind", "jax", "ten", "den", "kc", "lv", 
                "lac", "dal", "nyg", "phi", "wsh", "chi", "det", "gb", "min", "atl", "car", "no", "tb", "ari", "lar", "sf", "sea"]
    
    teamNames = ["bills", "dolphins", "patriots", "jets", "ravens", "bengals", "browns", "steelers", "texans", "colts", "jaguars", "titans",
                 "broncos", "chiefs", "raiders", "chargers", "cowboys", "giants", "eagles", "commanders", "bears",
                 "lions", "packers", "vikings", "falcons", "panthers", "saints", "buccaneers", "cardinals", "rams", "sanfrancisco", "seahawks"]
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = connection.cursor()
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1080, 1200)
    wait = WebDriverWait(driver, 10)
    
    for teamCount, team in enumerate(team_ABR):
        QB = ""
        RB1 = ""
        RB2 = ""
        WR1 = ""
        WR2 = ""
        WR3 = ""
        TE = ""
        
        driver.get("https://www.espn.com/nfl/team/depth/_/name/" + str(team))
        time.sleep(2)
        
        # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
    
        table = soup.find_all('div', class_ = 'Table__Scroller')
        tableBody = table[0].find('tbody', class_='Table__TBODY')
        rows = tableBody.find_all('tr', class_='Table__TR Table__TR--sm Table__even')
        
        qb_element = rows[0].find('td', class_='Table__TD')
        qb_a_element = qb_element.find('a', class_='AnchorLink')
        qb_name = qb_a_element.text
        QB = qb_name
        
        rb_elements = rows[1].find_all('td', class_='Table__TD')
        rb1_a_element = rb_elements[0].find('a', class_='AnchorLink')
        rb2_a_element = rb_elements[1].find('a', class_='AnchorLink')
        rb1_name = rb1_a_element.text
        rb2_name = rb2_a_element.text
        RB1 = rb1_name
        RB2 = rb2_name
        
        wr1_element = rows[2].find('td', class_='Table__TD')
        wr1_a_element = wr1_element.find('a', class_='AnchorLink')
        wr1_name = wr1_a_element.text
        WR1 = wr1_name
        
        wr2_element = rows[3].find('td', class_='Table__TD')
        wr2_a_element = wr2_element.find('a', class_='AnchorLink')
        wr2_name = wr2_a_element.text
        WR2 = wr2_name
        
        wr3_element = rows[4].find('td', class_='Table__TD')
        wr3_a_element = wr3_element.find('a', class_='AnchorLink')
        wr3_name = wr3_a_element.text
        WR3 = wr3_name
        
        te_element = rows[5].find('td', class_='Table__TD')
        te_a_element = te_element.find('a', class_='AnchorLink')
        te_name = te_a_element.text
        TE = te_name

        # Define the table name for the team's offense roster
        table_name = f'{teamNames[teamCount].lower()}_offense_roster'

        # Define player names for QB, RB1, RB2, WR1, WR2, WR3, and TE
        player_names = [QB, RB1, RB2, WR1, WR2, WR3, TE]

        # Define SQL INSERT statement
        insert_sql = f"INSERT IGNORE INTO {table_name} (Name, Position) VALUES (%s, %s) ON DUPLICATE KEY UPDATE Name = VALUES(Name)"

        # Insert player names into the respective table
        for Name, Position in zip(player_names, ["QB", "RB1", "RB2", "WR1", "WR2", "WR3", "TE"]):
            cursor.execute(insert_sql, (Name, Position))

    # Commit the changes to the database
    connection.commit()

    # Close the database connection
    connection.close()
        
    driver.quit()

# Update NFL Player Gamelogs. (QB, RB, WR, TE, Needs Team)  
def update_NFL_GameLogs():
    
    today = datetime.date.today()

    current_month = today.month
    
    current_year = today.year
    
    if current_month in [1, 2]:  # January is 1, February is 2
        current_year -= 1
    
    conn = create_connection("nfl_stats")
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'nfl_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    
    
    teamNames = ["bills", "dolphins", "patriots", "jets", "ravens", "bengals", "browns", "steelers", "texans", "colts", "jaguars", "titans",
                 "broncos", "chiefs", "raiders", "chargers", "cowboys", "giants", "eagles", "commanders", "bears",
                 "lions", "packers", "vikings", "falcons", "panthers", "saints", "buccaneers", "cardinals", "rams", "sanfrancisco", "seahawks"]
    
    
    playerNames_QBs = []
    playerNames_RB1 = []
    playerNames_RB2 = []
    playerNames_WR1 = []
    playerNames_WR2 = []
    playerNames_WR3 = []
    playerNames_TE = []
    
    cursor = conn.cursor()
    
    for team in teamNames:
        
        
        column = "Name"
        
        team_TableName = str(team + "_offense_roster")
        
        # Define the positions you want to fetch
        positions = ['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'WR3', 'TE']
        
        # Build the query using the IN clause
        mysql_query = f"SELECT {column} FROM {team_TableName} WHERE position IN ({', '.join(['%s']*len(positions))}) ORDER BY position"
        cursor.execute(mysql_query, positions)

        # Fetch all the results at once
        results = cursor.fetchall()

        # Process the results
        QB, RB1, RB2, WR1, WR2, WR3, TE = [clean_PlayerName(result[0]) for result in results]
        
        playerNames_QBs.append(QB)
        playerNames_RB1.append (RB1)
        playerNames_RB2.append(RB2)
        playerNames_WR1.append(WR1)
        playerNames_WR2.append (WR2)
        playerNames_WR3.append(WR3)
        playerNames_TE.append(TE)
        
    cursor.close()
    
    
    
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver2 = webdriver.Chrome(options=chrome_options)
    driver3 = webdriver.Chrome(options=chrome_options)
    
    
    # List of drivers
    drivers = [driver, driver2, driver3]  
    
    index_size = 3
    
    cursor = conn.cursor()
    
    for i in range(0, len(playerNames_QBs), index_size):
        chunk = playerNames_QBs[i:i + index_size]
        pass
        # Your code to process the current chunk goes here
        for j, QB in enumerate(chunk):
            # Your processing code for each QB in the current chunk
            formatted_name = QB.replace(" ", "-").replace("'", "-")
            SQLformatted_name = QB.replace(" ", "").replace("'", "-")
            if formatted_name == "josh-allen" or formatted_name == "Josh-Allen":
                
                formatted_name = "Josh-Allen-4"
                
            elif formatted_name == "c.j.-stroud" or formatted_name == "C.J.-Stroud":
                
                formatted_name = "c-j-stroud"
                
            
                
            

            # Use the corresponding driver instance for each QB
            current_driver = drivers[j]
            
            url = "https://www.nfl.com/players/" + str(formatted_name) + "/stats/logs/"
            
            
            # Open the URL
            current_driver.get(url)
            
            WeekList = []
            QB_CompletionsList = []
            QB_AttemptsList = []
            QB_PassYardsList = []
            QB_Yards_PerCompletionList = []
            QB_TouchdownsList = []
            QB_InterceptionsList = []
            QB_SacksList = []
            QB_RushAttemptsList = []
            QB_RushYardsList = []
            QB_RushTouchdownsList = []
            
            html_content = current_driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the table element by class name
            statTable_element = soup.find_all("table", class_="d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]]}")
            
            if len(statTable_element) < 2:
                rows = statTable_element[0].find_all("tr")
                
            else:
                rows = statTable_element[1].find_all("tr")
            
            i = 0
            for row in rows[1:]:
                
                td_elements = row.find_all("td", class_="nfl-t-stats__col-18")

                WeekList.append(int(td_elements[0].text.strip()))
                
                if td_elements[4].text.strip() == '':
                    QB_CompletionsList.append(0)
                else:
                    QB_CompletionsList.append(int(td_elements[4].text.strip()))
                    
                if td_elements[5].text.strip() == '':
                    QB_AttemptsList.append(0)
                else:
                    QB_AttemptsList.append(int(td_elements[5].text.strip()))
                    
                if td_elements[6].text.strip() == '':
                    QB_PassYardsList.append(0)
                else:
                    QB_PassYardsList.append(int(td_elements[6].text.strip()))
                    
                if td_elements[7].text.strip() == '':
                    QB_Yards_PerCompletionList.append(0)
                else:
                    QB_Yards_PerCompletionList.append(float(td_elements[7].text.strip()))
                    
                if td_elements[8].text.strip() == '':
                    QB_TouchdownsList.append(0)
                else:
                    QB_TouchdownsList.append(int(td_elements[8].text.strip()))
                    
                if td_elements[9].text.strip() == '':
                    QB_InterceptionsList.append(0)
                else:
                    QB_InterceptionsList.append(int(td_elements[9].text.strip()))
                    
                if td_elements[10].text.strip() == '':
                    QB_SacksList.append(0)
                else:
                    QB_SacksList.append(int(td_elements[10].text.strip()))
                
                if td_elements[13].text.strip() == '':
                    QB_RushAttemptsList.append(0)
                else:
                    QB_RushAttemptsList.append(int(td_elements[13].text.strip()))
                    
                if td_elements[14].text.strip() == '':
                    QB_RushYardsList.append(0)
                else:
                    QB_RushYardsList.append(int(td_elements[14].text.strip()))
                    
                if td_elements[16].text.strip() == '':
                    QB_RushTouchdownsList.append(0)  
                else:
                    QB_RushTouchdownsList.append(int(td_elements[16].text.strip()))
            
            # SQL query to check if the table exists
            check_table_query = f"SHOW TABLES LIKE '{SQLformatted_name}_GameLogs';"
            cursor.execute(check_table_query)

            # Fetch the result
            result = cursor.fetchone()
            
            if not result:
                # SQL query to create the table
                create_table_query = f"""
                CREATE TABLE `{SQLformatted_name}_GameLogs` (
                    Week INT PRIMARY KEY,
                    Completions INT,
                    Attempts INT,
                    Pass_Yards INT,
                    Yards_PerCompletion DECIMAL(3, 1),
                    Touchdowns INT,
                    Interceptions INT,
                    Sacks INT,
                    Rush_Attempts INT,
                    Rush_Yards INT,
                    Rush_Touchdowns INT
                );
                """
                
                
                
                # Execute the query to create the table
                cursor.execute(create_table_query)

                # Commit the changes
                conn.commit()
            
            for i in range(len(WeekList)):
                # Check if the row with the same Week already exists
                check_duplicate_query = f"SELECT COUNT(*) FROM `{SQLformatted_name}_GameLogs` WHERE Week = %s;"
                cursor.execute(check_duplicate_query, (WeekList[i],))
                count = cursor.fetchone()[0]

                if count == 0:
                    # The row doesn't exist, proceed with the insert
                    insert_query = f"""
                    INSERT INTO `{SQLformatted_name}_GameLogs` (
                        Week,
                        Completions,
                        Attempts,
                        Pass_Yards,
                        Yards_PerCompletion,
                        Touchdowns,
                        Interceptions,
                        Sacks,
                        Rush_Attempts,
                        Rush_Yards,
                        Rush_Touchdowns
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        Completions = VALUES(Completions),
                        Attempts = VALUES(Attempts),
                        Pass_Yards = VALUES(Pass_Yards),
                        Yards_PerCompletion = VALUES(Yards_PerCompletion),
                        Touchdowns = VALUES(Touchdowns),
                        Interceptions = VALUES(Interceptions),
                        Sacks = VALUES(Sacks),
                        Rush_Attempts = VALUES(Rush_Attempts),
                        Rush_Yards = VALUES(Rush_Yards),
                        Rush_Touchdowns = VALUES(Rush_Touchdowns);
                    """
                    current_values = (
                        WeekList[i],
                        QB_CompletionsList[i],
                        QB_AttemptsList[i],
                        QB_PassYardsList[i],
                        QB_Yards_PerCompletionList[i],
                        QB_TouchdownsList[i],
                        QB_InterceptionsList[i],
                        QB_SacksList[i],
                        QB_RushAttemptsList[i],
                        QB_RushYardsList[i],
                        QB_RushTouchdownsList[i]
                    )
                    cursor.execute(insert_query, current_values)

            # Commit the changes
            conn.commit()

        # Close the cursor and connection
    cursor.close()
    
       
    cursor = conn.cursor() 
   
    for i in range(0, len(playerNames_RB1), index_size):
        chunk = playerNames_RB1[i:i + index_size]
       
         # Your code to process the current chunk goes here
        for j, RB in enumerate(chunk):
            # Your processing code for each QB in the current chunk
            formatted_name = RB.replace(" ", "-").replace("'", "-")
            SQLformatted_name = RB.replace(" ", "").replace("'", "-")
            
            if formatted_name == "james-cook" or formatted_name == "James-Cook":
                
                formatted_name = "James-Cook-2"
                
            if formatted_name == "najee-harris" or formatted_name == "Najee-Harris":
                
                formatted_name = "najee-harris-x2665"
                
            if formatted_name == "kenneth-walker" or formatted_name == "Kenneth-Walker":
                
                formatted_name = "kenneth-walker-iii"
                
            
                
            # Use the corresponding driver instance for each QB
            current_driver = drivers[j]
            
            url = "https://www.nfl.com/players/" + str(formatted_name) + "/stats/logs/"
            
            
            current_driver.get(url)
            
            WeekList = []
            RB_RushAttemptsList = []
            RB_RushYardsList = []
            RB_RushYards_PerAttemptList = []
            RB_RushTouchdownsList = []
            RB_RecsList = []
            RB_RecYardsList = []
            RB_RecYards_PerRecList = []
            RB_RecTouchdownsList = []
            
            html_content = current_driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the table element by class name
            statTable_element = soup.find_all("table", class_="d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]]}")
            
            if len(statTable_element) < 2:
                rows = statTable_element[0].find_all("tr")
                
            else:
                rows = statTable_element[1].find_all("tr")
                
            i = 0
            for row in rows[1:]:
                
                td_elements = row.find_all("td", class_="nfl-t-stats__col-15")

                WeekList.append(int(td_elements[0].text.strip()))
                
                if td_elements[4].text.strip() == '':
                    RB_RushAttemptsList.append(0)
                else:
                    RB_RushAttemptsList.append(int(td_elements[4].text.strip()))
                    
                if td_elements[5].text.strip() == '':
                    RB_RushYardsList.append(0)
                else:
                    RB_RushYardsList.append(int(td_elements[5].text.strip()))
                    
                if td_elements[6].text.strip() == '':
                    RB_RushYards_PerAttemptList.append(0)
                else:
                    RB_RushYards_PerAttemptList.append(float(td_elements[6].text.strip()))
                    
                if td_elements[8].text.strip() == '':
                    RB_RushTouchdownsList.append(0)
                else:
                    RB_RushTouchdownsList.append(int(td_elements[8].text.strip()))
                    
                if td_elements[9].text.strip() == '':
                    RB_RecsList.append(0)
                else:
                    RB_RecsList.append(int(td_elements[9].text.strip()))
                    
                if td_elements[10].text.strip() == '':
                    RB_RecYardsList.append(0)
                else:
                    RB_RecYardsList.append(int(td_elements[10].text.strip()))
                    
                if td_elements[11].text.strip() == '':
                    RB_RecYards_PerRecList.append(0)
                else:
                    RB_RecYards_PerRecList.append(float(td_elements[11].text.strip()))
                    
                if td_elements[13].text.strip() == '':
                    RB_RecTouchdownsList.append(0)
                else:
                    RB_RecTouchdownsList.append(int(td_elements[13].text.strip()))
            
                
                # SQL query to check if the table exists
                check_table_query = f"SHOW TABLES LIKE '{SQLformatted_name}_GameLogs';"
                cursor.execute(check_table_query)

                # Fetch the result
                result = cursor.fetchone()
                
                if not result:
                    # SQL query to create the table
                    create_table_query = f"""
                    CREATE TABLE `{SQLformatted_name}_GameLogs` (
                        Week INT PRIMARY KEY,
                        Rush_Attempts INT,
                        Rush_Yards INT,
                        Rush_Yards_PA DECIMAL(3,1),
                        Rush_Touchdowns INT,
                        Receptions INT,
                        Rec_Yards INT,
                        Rec_Yards_PR DECIMAL(3,1),
                        Rec_Touchdowns INT
                    );
                    """
                    
                    
                    
                    # Execute the query to create the table
                    cursor.execute(create_table_query)

                    # Commit the changes
                    conn.commit()
                
                for i in range(len(WeekList)):
                    # Check if the row with the same Week already exists
                    check_duplicate_query = f"SELECT COUNT(*) FROM `{SQLformatted_name}_GameLogs` WHERE Week = %s;"
                    cursor.execute(check_duplicate_query, (WeekList[i],))
                    count = cursor.fetchone()[0]

                    if count == 0:
                        # The row doesn't exist, proceed with the insert
                        insert_query = f"""
                        INSERT INTO `{SQLformatted_name}_GameLogs` (
                            Week,
                            Rush_Attempts,
                            Rush_Yards,
                            Rush_Yards_PA,
                            Rush_Touchdowns,
                            Receptions,
                            Rec_Yards,
                            Rec_Yards_PR,
                            Rec_Touchdowns
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            Rush_Attempts = VALUES(Rush_Attempts),
                            Rush_Yards = VALUES(Rush_Yards),
                            Rush_Yards_PA = VALUES(Rush_Yards_PA),
                            Rush_Touchdowns = VALUES(Rush_Touchdowns),
                            Receptions = VALUES(Receptions),
                            Rec_Yards = VALUES(Rec_Yards),
                            Rec_Yards_PR = VALUES(Rec_Yards_PR),
                            Rec_Touchdowns = VALUES(Rec_Touchdowns);
                            
                        """
                        current_values = (
                            WeekList [i],
                            RB_RushAttemptsList [i],
                            RB_RushYardsList [i],
                            RB_RushYards_PerAttemptList [i],
                            RB_RushTouchdownsList [i],
                            RB_RecsList [i],
                            RB_RecYardsList [i],
                            RB_RecYards_PerRecList [i],
                            RB_RecTouchdownsList [i]
                            )
                        cursor.execute(insert_query, current_values)
                
            # Commit the changes
            conn.commit()

    # Close the cursor and connection
    cursor.close()
    
    cursor = conn.cursor()
       
    for i in range(0, len(playerNames_RB2), index_size):
        chunk = playerNames_RB2[i:i + index_size]
       
         # Your code to process the current chunk goes here
        for j, RB in enumerate(chunk):
            # Your processing code for each QB in the current chunk
            formatted_name = RB.replace(" ", "-").replace("'", "-")
            SQLformatted_name = RB.replace(" ", "").replace("'", "-")
                
            if formatted_name == "de-von-achane" or formatted_name == "De-Von-Achane":
                
                formatted_name = "devon-achane"
                SQLformatted_name = "devonachane"
                
            if formatted_name == "antonio-gibson" or formatted_name == "Antonio-Gibson":
                
                formatted_name = "antonio-gibson-2"
                SQLformatted_name = "antoniogibson"
                
            if formatted_name == "aj-dillon" or formatted_name == "AJ-Dillon":
                
                formatted_name = "a-j-dillon"
                SQLformatted_name = "ajdillon"
                
            if formatted_name == "elijah-mitchell" or formatted_name == "Elijah-Mitchell":
                
                formatted_name = "elijah-mitchell-2"
                SQLformatted_name = "elijahmitchell"
                
                
            # Use the corresponding driver instance for each QB
            current_driver = drivers[j]
            
            url = "https://www.nfl.com/players/" + str(formatted_name) + "/stats/logs/"
            
            
            current_driver.get(url)
            
            WeekList = []
            RB_RushAttemptsList = []
            RB_RushYardsList = []
            RB_RushYards_PerAttemptList = []
            RB_RushTouchdownsList = []
            RB_RecsList = []
            RB_RecYardsList = []
            RB_RecYards_PerRecList = []
            RB_RecTouchdownsList = []
            
            html_content = current_driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the table element by class name
            statTable_element = soup.find_all("table", class_="d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]]}")
            
            if len(statTable_element) < 2:
                rows = statTable_element[0].find_all("tr")
                
            else:
                rows = statTable_element[1].find_all("tr")
                
            i = 0
            for row in rows[1:]:
                
                td_elements = row.find_all("td", class_="nfl-t-stats__col-15")

                WeekList.append(int(td_elements[0].text.strip()))
                
                if td_elements[4].text.strip() == '':
                    RB_RushAttemptsList.append(0)
                else:
                    RB_RushAttemptsList.append(int(td_elements[4].text.strip()))
                    
                if td_elements[5].text.strip() == '':
                    RB_RushYardsList.append(0)
                else:
                    RB_RushYardsList.append(int(td_elements[5].text.strip()))
                    
                if td_elements[6].text.strip() == '':
                    RB_RushYards_PerAttemptList.append(0)
                else:
                    RB_RushYards_PerAttemptList.append(float(td_elements[6].text.strip()))
                    
                if td_elements[8].text.strip() == '':
                    RB_RushTouchdownsList.append(0)
                else:
                    RB_RushTouchdownsList.append(int(td_elements[8].text.strip()))
                    
                if td_elements[9].text.strip() == '':
                    RB_RecsList.append(0)
                else:
                    RB_RecsList.append(int(td_elements[9].text.strip()))
                    
                if td_elements[10].text.strip() == '':
                    RB_RecYardsList.append(0)
                else:
                    RB_RecYardsList.append(int(td_elements[10].text.strip()))
                    
                if td_elements[11].text.strip() == '':
                    RB_RecYards_PerRecList.append(0)
                else:
                    RB_RecYards_PerRecList.append(float(td_elements[11].text.strip()))
                    
                if td_elements[13].text.strip() == '':
                    RB_RecTouchdownsList.append(0)
                else:
                    RB_RecTouchdownsList.append(int(td_elements[13].text.strip()))
                
                
                # SQL query to check if the table exists
                check_table_query = f"SHOW TABLES LIKE '{SQLformatted_name}_GameLogs';"
                cursor.execute(check_table_query)

                # Fetch the result
                result = cursor.fetchone()
                
                if not result:
                    # SQL query to create the table
                    create_table_query = f"""
                    CREATE TABLE `{SQLformatted_name}_GameLogs` (
                        Week INT PRIMARY KEY,
                        Rush_Attempts INT,
                        Rush_Yards INT,
                        Rush_Yards_PA DECIMAL(3,1),
                        Rush_Touchdowns INT,
                        Receptions INT,
                        Rec_Yards INT,
                        Rec_Yards_PR DECIMAL(3,1),
                        Rec_Touchdowns INT
                    );
                    """
                    
                    
                    
                    # Execute the query to create the table
                    cursor.execute(create_table_query)

                    # Commit the changes
                    conn.commit()
                
                for i in range(len(WeekList)):
                    # Check if the row with the same Week already exists
                    check_duplicate_query = f"SELECT COUNT(*) FROM `{SQLformatted_name}_GameLogs` WHERE Week = %s;"
                    cursor.execute(check_duplicate_query, (WeekList[i],))
                    count = cursor.fetchone()[0]

                    if count == 0:
                        # The row doesn't exist, proceed with the insert
                        insert_query = f"""
                        INSERT INTO `{SQLformatted_name}_GameLogs` (
                            Week,
                            Rush_Attempts,
                            Rush_Yards,
                            Rush_Yards_PA,
                            Rush_Touchdowns,
                            Receptions,
                            Rec_Yards,
                            Rec_Yards_PR,
                            Rec_Touchdowns
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            Rush_Attempts = VALUES(Rush_Attempts),
                            Rush_Yards = VALUES(Rush_Yards),
                            Rush_Yards_PA = VALUES(Rush_Yards_PA),
                            Rush_Touchdowns = VALUES(Rush_Touchdowns),
                            Receptions = VALUES(Receptions),
                            Rec_Yards = VALUES(Rec_Yards),
                            Rec_Yards_PR = VALUES(Rec_Yards_PR),
                            Rec_Touchdowns = VALUES(Rec_Touchdowns);
                            
                        """
                        current_values = (
                            WeekList [i],
                            RB_RushAttemptsList [i],
                            RB_RushYardsList [i],
                            RB_RushYards_PerAttemptList [i],
                            RB_RushTouchdownsList [i],
                            RB_RecsList [i],
                            RB_RecYardsList [i],
                            RB_RecYards_PerRecList [i],
                            RB_RecTouchdownsList [i]
                            )
                        cursor.execute(insert_query, current_values)
                
            # Commit the changes
            conn.commit()

    # Close the cursor and connection
    cursor.close()
    
    cursor = conn.cursor() 
   
    for i in range(0, len(playerNames_WR1), index_size):
        chunk = playerNames_WR1[i:i + index_size]
        
        # Your code to process the current chunk goes here
        for j, WR in enumerate(chunk):
            # Your processing code for each QB in the current chunk
            formatted_name = WR.replace(" ", "-").replace("'", "-")
            SQLformatted_name = WR.replace(" ", "").replace("'", "-")
            
            if formatted_name == "drew-ogletree" or formatted_name == "Drew-Ogletree":
                
                formatted_name = "andrew-ogletree"
                SQLformatted_name = "andrewogletree"
                
            if formatted_name == "t.j.-hockenson" or formatted_name == "T.J.-Hockenson":
                
                formatted_name = "t-j-hockenson"
                SQLformatted_name = "tjhockenson"
            
            # Use the corresponding driver instance for each QB
            current_driver = drivers[j]
            
            url = "https://www.nfl.com/players/" + str(formatted_name) + "/stats/logs/"
            
            
            current_driver.get(url)
            
            WeekList = []
            WR_ReceptionsList = []
            WR_RecYardsList = []
            WR_RecYards_PRList = []
            WR_RecTouchdownsList = []
            WR_RushAttemptsList = []
            WR_RushYardsList = []
            WR_RushYards_PAList = []
            WR_RushTouchdowns = []
            
            html_content = current_driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the table element by class name
            statTable_element = soup.find_all("table", class_="d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]]}")
            
            if len(statTable_element) < 2:
                rows = statTable_element[0].find_all("tr")
                
            else:
                rows = statTable_element[1].find_all("tr")
                
            i = 0
            for row in rows[1:]:
                
                td_elements = row.find_all("td", class_="nfl-t-stats__col-15")

                WeekList.append(int(td_elements[0].text.strip()))
                
                if td_elements[4].text.strip() == '':
                    WR_ReceptionsList.append(0)
                else:
                    WR_ReceptionsList.append(int(td_elements[4].text.strip()))
                    
                if td_elements[5].text.strip() == '':
                    WR_RecYardsList.append(0)
                else:
                    WR_RecYardsList.append(int(td_elements[5].text.strip()))
                    
                if td_elements[6].text.strip() == '':
                    WR_RecYards_PRList.append(0)
                else:
                    WR_RecYards_PRList.append(float(td_elements[6].text.strip()))
                    
                if td_elements[8].text.strip() == '':
                    WR_RecTouchdownsList.append(0)
                else:
                    WR_RecTouchdownsList.append(int(td_elements[8].text.strip()))
                    
                if td_elements[9].text.strip() == '':
                    WR_RushAttemptsList.append(0)
                else:
                    WR_RushAttemptsList.append(int(td_elements[9].text.strip()))
                    
                if td_elements[10].text.strip() == '':
                    WR_RushYardsList.append(0)
                else:
                    WR_RushYardsList.append(int(td_elements[10].text.strip()))
                    
                if td_elements[11].text.strip() == '':
                    WR_RushYards_PAList.append(0)
                else:
                    WR_RushYards_PAList.append(float(td_elements[11].text.strip()))
                    
                if td_elements[13].text.strip() == '':
                    WR_RushTouchdowns.append(0)
                else:
                    WR_RushTouchdowns.append(int(td_elements[13].text.strip()))
                
                
                
                # SQL query to check if the table exists
                check_table_query = f"SHOW TABLES LIKE '{SQLformatted_name}_GameLogs';"
                cursor.execute(check_table_query)

                # Fetch the result
                result = cursor.fetchone()
                
                if not result:
                    # SQL query to create the table
                    create_table_query = f"""
                    CREATE TABLE `{SQLformatted_name}_GameLogs` (
                        Week INT PRIMARY KEY,
                        Receptions INT,
                        Rec_Yards INT,
                        Rec_Yards_PR DECIMAL(3,1),
                        Rec_Touchdowns INT,
                        Rush_Attempts INT,
                        Rush_Yards INT,
                        Rush_Yards_PA DECIMAL(3,1),
                        Rush_Touchdowns INT
                    );
                    """
                    
                    
                    
                    # Execute the query to create the table
                    cursor.execute(create_table_query)

                    # Commit the changes
                    conn.commit()
                for i in range(len(WeekList)):
                    # Check if the row with the same Week already exists
                    check_duplicate_query = f"SELECT COUNT(*) FROM `{SQLformatted_name}_GameLogs` WHERE Week = %s;"
                    cursor.execute(check_duplicate_query, (WeekList[i],))
                    count = cursor.fetchone()[0]

                    if count == 0:
                        # The row doesn't exist, proceed with the insert
                        insert_query = f"""
                        INSERT INTO `{SQLformatted_name}_GameLogs` (
                            Week,
                            Receptions,
                            Rec_Yards,
                            Rec_Yards_PR,
                            Rec_Touchdowns,
                            Rush_Attempts,
                            Rush_Yards,
                            Rush_Yards_PA,
                            Rush_Touchdowns
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            Receptions = VALUES(Receptions),
                            Rec_Yards = VALUES(Rec_Yards),
                            Rec_Yards_PR = VALUES(Rec_Yards_PR),
                            Rec_Touchdowns = VALUES(Rec_Touchdowns),
                            Rush_Attempts = VALUES(Rush_Attempts),
                            Rush_Yards = VALUES(Rush_Yards),
                            Rush_Yards_PA = VALUES(Rush_Yards_PA),
                            Rush_Touchdowns = VALUES(Rush_Touchdowns);
                            
                        """
                        current_values = (
                            WeekList [i],
                            WR_ReceptionsList [i],
                            WR_RecYardsList [i],
                            WR_RecYards_PRList [i],
                            WR_RecTouchdownsList [i],
                            WR_RushAttemptsList [i],
                            WR_RushYardsList [i],
                            WR_RushYards_PAList [i],
                            WR_RushTouchdowns [i]
                            )
                        cursor.execute(insert_query, current_values)
                
            # Commit the changes
            conn.commit()

    # Close the cursor and connection
    cursor.close()    
    
    cursor = conn.cursor() 
   
    for i in range(0, len(playerNames_WR2), index_size):
        chunk = playerNames_WR2[i:i + index_size]
        
        # Your code to process the current chunk goes here
        for j, WR in enumerate(chunk):
            # Your processing code for each WR in the current chunk
            formatted_name = WR.replace(" ", "-").replace("'", "-")
            SQLformatted_name = WR.replace(" ", "").replace("'", "-")
            
            if formatted_name == "drew-ogletree" or formatted_name == "Drew-Ogletree":
                
                formatted_name = "andrew-ogletree"
                SQLformatted_name = "andrewogletree"
                
            if formatted_name == "t.j.-hockenson" or formatted_name == "T.J.-Hockenson":
                
                formatted_name = "t-j-hockenson"
                SQLformatted_name = "tjhockenson"
                
            if formatted_name == "michael-pittman" or formatted_name == "Michael-Pittman":
                
                formatted_name = "michael-pittman-2"
                SQLformatted_name = "michaelpittman"
            
            if formatted_name == "a.j.-brown" or formatted_name == "A.J.-Brown":
                
                formatted_name = "a-j-brown"
                SQLformatted_name = "ajbrown"
                
            if formatted_name == "dj-moore" or formatted_name == "DJ-Moore":
                
                formatted_name = "d-j-moore"
                SQLformatted_name = "djmoore"
                
            if formatted_name == "amon-ra-st.-brown" or formatted_name == "Amon-Ra-St.-Brown":
                
                formatted_name = "amon-ra-st-brown"
                SQLformatted_name = "amonrastbrown"
                
            if formatted_name == "dk-metcalf" or formatted_name == "DK-Metcalf":
                
                formatted_name = "d-k-metcalf"
                SQLformatted_name = "dkmetcalf"
            
            # Use the corresponding driver instance for each QB
            current_driver = drivers[j]
            
            url = "https://www.nfl.com/players/" + str(formatted_name) + "/stats/logs/"
            
            
            current_driver.get(url)
    
            WeekList = []
            WR_ReceptionsList = []
            WR_RecYardsList = []
            WR_RecYards_PRList = []
            WR_RecTouchdownsList = []
            WR_RushAttemptsList = []
            WR_RushYardsList = []
            WR_RushYards_PAList = []
            WR_RushTouchdowns = []
            
            html_content = current_driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the table element by class name
            statTable_element = soup.find_all("table", class_="d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]]}")
            
            if len(statTable_element) < 2:
                rows = statTable_element[0].find_all("tr")
                
            else:
                rows = statTable_element[1].find_all("tr")
            
            i = 0
            for row in rows[1:]:
                
                td_elements = row.find_all("td", class_="nfl-t-stats__col-15")

                WeekList.append(int(td_elements[0].text.strip()))
                
                if td_elements[4].text.strip() == '':
                    WR_ReceptionsList.append(0)
                else:
                    WR_ReceptionsList.append(int(td_elements[4].text.strip()))
                    
                if td_elements[5].text.strip() == '':
                    WR_RecYardsList.append(0)
                else:
                    WR_RecYardsList.append(int(td_elements[5].text.strip()))
                    
                if td_elements[6].text.strip() == '':
                    WR_RecYards_PRList.append(0)
                else:
                    WR_RecYards_PRList.append(float(td_elements[6].text.strip()))
                    
                if td_elements[8].text.strip() == '':
                    WR_RecTouchdownsList.append(0)
                else:
                    WR_RecTouchdownsList.append(int(td_elements[8].text.strip()))
                    
                if td_elements[9].text.strip() == '':
                    WR_RushAttemptsList.append(0)
                else:
                    WR_RushAttemptsList.append(int(td_elements[9].text.strip()))
                    
                if td_elements[10].text.strip() == '':
                    WR_RushYardsList.append(0)
                else:
                    WR_RushYardsList.append(int(td_elements[10].text.strip()))
                    
                if td_elements[11].text.strip() == '':
                    WR_RushYards_PAList.append(0)
                else:
                    WR_RushYards_PAList.append(float(td_elements[11].text.strip()))
                    
                if td_elements[13].text.strip() == '':
                    WR_RushTouchdowns.append(0)
                else:
                    WR_RushTouchdowns.append(int(td_elements[13].text.strip()))
                
                
                
                # SQL query to check if the table exists
                check_table_query = f"SHOW TABLES LIKE '{SQLformatted_name}_GameLogs';"
                cursor.execute(check_table_query)

                # Fetch the result
                result = cursor.fetchone()
                
                if not result:
                    # SQL query to create the table
                    create_table_query = f"""
                    CREATE TABLE `{SQLformatted_name}_GameLogs` (
                        Week INT PRIMARY KEY,
                        Receptions INT,
                        Rec_Yards INT,
                        Rec_Yards_PR DECIMAL(3,1),
                        Rec_Touchdowns INT,
                        Rush_Attempts INT,
                        Rush_Yards INT,
                        Rush_Yards_PA DECIMAL(3,1),
                        Rush_Touchdowns INT
                    );
                    """
                    
                    
                    
                    # Execute the query to create the table
                    cursor.execute(create_table_query)

                    # Commit the changes
                    conn.commit()
                for i in range(len(WeekList)):
                    # Check if the row with the same Week already exists
                    check_duplicate_query = f"SELECT COUNT(*) FROM `{SQLformatted_name}_GameLogs` WHERE Week = %s;"
                    cursor.execute(check_duplicate_query, (WeekList[i],))
                    count = cursor.fetchone()[0]

                    if count == 0:
                        # The row doesn't exist, proceed with the insert
                        insert_query = f"""
                        INSERT INTO `{SQLformatted_name}_GameLogs` (
                            Week,
                            Receptions,
                            Rec_Yards,
                            Rec_Yards_PR,
                            Rec_Touchdowns,
                            Rush_Attempts,
                            Rush_Yards,
                            Rush_Yards_PA,
                            Rush_Touchdowns
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            Receptions = VALUES(Receptions),
                            Rec_Yards = VALUES(Rec_Yards),
                            Rec_Yards_PR = VALUES(Rec_Yards_PR),
                            Rec_Touchdowns = VALUES(Rec_Touchdowns),
                            Rush_Attempts = VALUES(Rush_Attempts),
                            Rush_Yards = VALUES(Rush_Yards),
                            Rush_Yards_PA = VALUES(Rush_Yards_PA),
                            Rush_Touchdowns = VALUES(Rush_Touchdowns);
                            
                        """
                        current_values = (
                            WeekList [i],
                            WR_ReceptionsList [i],
                            WR_RecYardsList [i],
                            WR_RecYards_PRList [i],
                            WR_RecTouchdownsList [i],
                            WR_RushAttemptsList [i],
                            WR_RushYardsList [i],
                            WR_RushYards_PAList [i],
                            WR_RushTouchdowns [i]
                            )
                        cursor.execute(insert_query, current_values)
                
            # Commit the changes
            conn.commit()

    # Close the cursor and connection
    cursor.close()    
                
    cursor = conn.cursor() 
   
    for i in range(0, len(playerNames_WR3), index_size):
        chunk = playerNames_WR3[i:i + index_size]
        
        # Your code to process the current chunk goes here
        for j, WR in enumerate(chunk):
            # Your processing code for each WR in the current chunk
            formatted_name = WR.replace(" ", "-").replace("'", "-")
            SQLformatted_name = WR.replace(" ", "").replace("'", "-")
            
            if formatted_name == "drew-ogletree" or formatted_name == "Drew-Ogletree":
                
                formatted_name = "andrew-ogletree"
                SQLformatted_name = "andrewogletree"
                
            if formatted_name == "t.j.-hockenson" or formatted_name == "T.J.-Hockenson":
                
                formatted_name = "t-j-hockenson"
                SQLformatted_name = "tjhockenson"
                
            if formatted_name == "michael-pittman" or formatted_name == "Michael-Pittman":
                
                formatted_name = "michael-pittman-2"
                SQLformatted_name = "michaelpittman"
            
            if formatted_name == "a.j.-brown" or formatted_name == "A.J.-Brown":
                
                formatted_name = "a-j-brown"
                SQLformatted_name = "ajbrown"
                
            if formatted_name == "dj-moore" or formatted_name == "DJ-Moore":
                
                formatted_name = "d-j-moore"
                SQLformatted_name = "djmoore"
                
            if formatted_name == "amon-ra-st.-brown" or formatted_name == "Amon-Ra-St.-Brown":
                
                formatted_name = "amon-ra-st-brown"
                SQLformatted_name = "amonrastbrown"
                
            if formatted_name == "dk-metcalf" or formatted_name == "DK-Metcalf":
                
                formatted_name = "d-k-metcalf"
                SQLformatted_name = "dkmetcalf"
                
            if formatted_name == "joshua-palmer" or formatted_name == "Joshua-Palmer":
                
                formatted_name = "josh-palmer"
                SQLformatted_name = "joshpalmer"
            
            # Use the corresponding driver instance for each QB
            current_driver = drivers[j]
            
            url = "https://www.nfl.com/players/" + str(formatted_name) + "/stats/logs/"
            
            
            current_driver.get(url)
    
            WeekList = []
            WR_ReceptionsList = []
            WR_RecYardsList = []
            WR_RecYards_PRList = []
            WR_RecTouchdownsList = []
            WR_RushAttemptsList = []
            WR_RushYardsList = []
            WR_RushYards_PAList = []
            WR_RushTouchdowns = []
            
            html_content = current_driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the table element by class name
            statTable_element = soup.find_all("table", class_="d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]]}")
            
            if len(statTable_element) < 2:
                rows = statTable_element[0].find_all("tr")
                
            else:
                rows = statTable_element[1].find_all("tr")
            
            i = 0
            for row in rows[1:]:
                
                td_elements = row.find_all("td", class_="nfl-t-stats__col-15")

                WeekList.append(int(td_elements[0].text.strip()))
                
                if td_elements[4].text.strip() == '':
                    WR_ReceptionsList.append(0)
                else:
                    WR_ReceptionsList.append(int(td_elements[4].text.strip()))
                    
                if td_elements[5].text.strip() == '':
                    WR_RecYardsList.append(0)
                else:
                    WR_RecYardsList.append(int(td_elements[5].text.strip()))
                    
                if td_elements[6].text.strip() == '':
                    WR_RecYards_PRList.append(0)
                else:
                    WR_RecYards_PRList.append(float(td_elements[6].text.strip()))
                    
                if td_elements[8].text.strip() == '':
                    WR_RecTouchdownsList.append(0)
                else:
                    WR_RecTouchdownsList.append(int(td_elements[8].text.strip()))
                    
                if td_elements[9].text.strip() == '':
                    WR_RushAttemptsList.append(0)
                else:
                    WR_RushAttemptsList.append(int(td_elements[9].text.strip()))
                    
                if td_elements[10].text.strip() == '':
                    WR_RushYardsList.append(0)
                else:
                    WR_RushYardsList.append(int(td_elements[10].text.strip()))
                    
                if td_elements[11].text.strip() == '':
                    WR_RushYards_PAList.append(0)
                else:
                    WR_RushYards_PAList.append(float(td_elements[11].text.strip()))
                    
                if td_elements[13].text.strip() == '':
                    WR_RushTouchdowns.append(0)
                else:
                    WR_RushTouchdowns.append(int(td_elements[13].text.strip()))
                
                
                
                # SQL query to check if the table exists
                check_table_query = f"SHOW TABLES LIKE '{SQLformatted_name}_GameLogs';"
                cursor.execute(check_table_query)

                # Fetch the result
                result = cursor.fetchone()
                
                if not result:
                    # SQL query to create the table
                    create_table_query = f"""
                    CREATE TABLE `{SQLformatted_name}_GameLogs` (
                        Week INT PRIMARY KEY,
                        Receptions INT,
                        Rec_Yards INT,
                        Rec_Yards_PR DECIMAL(3,1),
                        Rec_Touchdowns INT,
                        Rush_Attempts INT,
                        Rush_Yards INT,
                        Rush_Yards_PA DECIMAL(3,1),
                        Rush_Touchdowns INT
                    );
                    """
                    
                    
                    
                    # Execute the query to create the table
                    cursor.execute(create_table_query)

                    # Commit the changes
                    conn.commit()
                for i in range(len(WeekList)):
                    # Check if the row with the same Week already exists
                    check_duplicate_query = f"SELECT COUNT(*) FROM `{SQLformatted_name}_GameLogs` WHERE Week = %s;"
                    cursor.execute(check_duplicate_query, (WeekList[i],))
                    count = cursor.fetchone()[0]

                    if count == 0:
                        # The row doesn't exist, proceed with the insert
                        insert_query = f"""
                        INSERT INTO `{SQLformatted_name}_GameLogs` (
                            Week,
                            Receptions,
                            Rec_Yards,
                            Rec_Yards_PR,
                            Rec_Touchdowns,
                            Rush_Attempts,
                            Rush_Yards,
                            Rush_Yards_PA,
                            Rush_Touchdowns
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            Receptions = VALUES(Receptions),
                            Rec_Yards = VALUES(Rec_Yards),
                            Rec_Yards_PR = VALUES(Rec_Yards_PR),
                            Rec_Touchdowns = VALUES(Rec_Touchdowns),
                            Rush_Attempts = VALUES(Rush_Attempts),
                            Rush_Yards = VALUES(Rush_Yards),
                            Rush_Yards_PA = VALUES(Rush_Yards_PA),
                            Rush_Touchdowns = VALUES(Rush_Touchdowns);
                            
                        """
                        current_values = (
                            WeekList [i],
                            WR_ReceptionsList [i],
                            WR_RecYardsList [i],
                            WR_RecYards_PRList [i],
                            WR_RecTouchdownsList [i],
                            WR_RushAttemptsList [i],
                            WR_RushYardsList [i],
                            WR_RushYards_PAList [i],
                            WR_RushTouchdowns [i]
                            )
                        cursor.execute(insert_query, current_values)
                
            # Commit the changes
            conn.commit()

    # Close the cursor and connection
    cursor.close()
    
    cursor = conn.cursor() 
   
    for i in range(0, len(playerNames_TE), index_size):
        chunk = playerNames_TE[i:i + index_size]
        
        # Your code to process the current chunk goes here
        for j, TE in enumerate(chunk):
            # Your processing code for each WR in the current chunk
            formatted_name = TE.replace(" ", "-").replace("'", "-")
            SQLformatted_name = TE.replace(" ", "").replace("'", "-")
            
            if formatted_name == "drew-ogletree" or formatted_name == "Drew-Ogletree":
                
                formatted_name = "andrew-ogletree"
                SQLformatted_name = "andrewogletree"
                
            if formatted_name == "t.j.-hockenson" or formatted_name == "T.J.-Hockenson":
                
                formatted_name = "t-j-hockenson"
                SQLformatted_name = "tjhockenson"
                
            if formatted_name == "michael-pittman" or formatted_name == "Michael-Pittman":
                
                formatted_name = "michael-pittman-2"
                SQLformatted_name = "michaelpittman"
            
            if formatted_name == "a.j.-brown" or formatted_name == "A.J.-Brown":
                
                formatted_name = "a-j-brown"
                SQLformatted_name = "ajbrown"
                
            if formatted_name == "dj-moore" or formatted_name == "DJ-Moore":
                
                formatted_name = "d-j-moore"
                SQLformatted_name = "djmoore"
                
            if formatted_name == "amon-ra-st.-brown" or formatted_name == "Amon-Ra-St.-Brown":
                
                formatted_name = "amon-ra-st-brown"
                SQLformatted_name = "amonrastbrown"
                
            if formatted_name == "dk-metcalf" or formatted_name == "DK-Metcalf":
                
                formatted_name = "d-k-metcalf"
                SQLformatted_name = "dkmetcalf"
                
            if formatted_name == "joshua-palmer" or formatted_name == "Joshua-Palmer":
                
                formatted_name = "josh-palmer"
                SQLformatted_name = "joshpalmer"
                
            if formatted_name == "cedrick-wilson" or formatted_name == "Cedrick-Wilson":
                
                formatted_name = "ced-wilson"
                SQLformatted_name = "cedrickwilson"
                
            if formatted_name == "cedric-tillman" or formatted_name == "Cedric-Tillman":
                
                formatted_name = "cedric-tillman-2"
                SQLformatted_name = "cedrictillman"
            
            if formatted_name == "equanimeous-st.-brown" or formatted_name == "Equanimeous-St.-Brown":
                
                formatted_name = "equanimeous-st-brown"
                SQLformatted_name = "equanimeousstbrown"
                
            if formatted_name == "k.j.-osborn" or formatted_name == "K.J.-Osborn":
                
                formatted_name = "k-j-osborn"
                SQLformatted_name = "kjosborn"
                
            if formatted_name == "dj-chark" or formatted_name == "DJ-Chark":
                
                formatted_name = "d-j-chark"
                SQLformatted_name = "djchark"
            
            # Use the corresponding driver instance for each QB
            current_driver = drivers[j]
            
            url = "https://www.nfl.com/players/" + str(formatted_name) + "/stats/logs/"
            
            
            current_driver.get(url)
    
            WeekList = []
            TE_ReceptionsList = []
            TE_RecYardsList = []
            TE_RecYards_PRList = []
            TE_RecTouchdownsList = []
            TE_RushAttemptsList = []
            TE_RushYardsList = []
            TE_RushYards_PAList = []
            TE_RushTouchdowns = []
            
            html_content = current_driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the table element by class name
            statTable_element = soup.find_all("table", class_="d3-o-table d3-o-standings--detailed d3-o-table--sortable {sortlist: [[0,1]]}")
            
            if len(statTable_element) < 2:
                rows = statTable_element[0].find_all("tr")
                
            else:
                rows = statTable_element[1].find_all("tr")
            
            i = 0
            for row in rows[1:]:
                
                td_elements = row.find_all("td", class_="nfl-t-stats__col-15")

                WeekList.append(int(td_elements[0].text.strip()))
                
                if td_elements[4].text.strip() == '':
                    TE_ReceptionsList.append(0)
                else:
                    TE_ReceptionsList.append(int(td_elements[4].text.strip()))
                    
                if td_elements[5].text.strip() == '':
                    TE_RecYardsList.append(0)
                else:
                    TE_RecYardsList.append(int(td_elements[5].text.strip()))
                    
                if td_elements[6].text.strip() == '':
                    TE_RecYards_PRList.append(0)
                else:
                    TE_RecYards_PRList.append(float(td_elements[6].text.strip()))
                    
                if td_elements[8].text.strip() == '':
                    TE_RecTouchdownsList.append(0)
                else:
                    TE_RecTouchdownsList.append(int(td_elements[8].text.strip()))
                    
                if td_elements[9].text.strip() == '':
                    TE_RushAttemptsList.append(0)
                else:
                    TE_RushAttemptsList.append(int(td_elements[9].text.strip()))
                    
                if td_elements[10].text.strip() == '':
                    TE_RushYardsList.append(0)
                else:
                    TE_RushYardsList.append(int(td_elements[10].text.strip()))
                    
                if td_elements[11].text.strip() == '':
                    TE_RushYards_PAList.append(0)
                else:
                    TE_RushYards_PAList.append(float(td_elements[11].text.strip()))
                    
                if td_elements[13].text.strip() == '':
                    TE_RushTouchdowns.append(0)
                else:
                    TE_RushTouchdowns.append(int(td_elements[13].text.strip()))
                
                
                # SQL query to check if the table exists
                check_table_query = f"SHOW TABLES LIKE '{SQLformatted_name}_GameLogs';"
                cursor.execute(check_table_query)

                # Fetch the result
                result = cursor.fetchone()
                
                if not result:
                    # SQL query to create the table
                    create_table_query = f"""
                    CREATE TABLE `{SQLformatted_name}_GameLogs` (
                        Week INT PRIMARY KEY,
                        Receptions INT,
                        Rec_Yards INT,
                        Rec_Yards_PR DECIMAL(3,1),
                        Rec_Touchdowns INT,
                        Rush_Attempts INT,
                        Rush_Yards INT,
                        Rush_Yards_PA DECIMAL(3,1),
                        Rush_Touchdowns INT
                    );
                    """
                    
                    
                    
                    # Execute the query to create the table
                    cursor.execute(create_table_query)

                    # Commit the changes
                    conn.commit()
                for i in range(len(WeekList)):
                    # Check if the row with the same Week already exists
                    check_duplicate_query = f"SELECT COUNT(*) FROM `{SQLformatted_name}_GameLogs` WHERE Week = %s;"
                    cursor.execute(check_duplicate_query, (WeekList[i],))
                    count = cursor.fetchone()[0]

                    if count == 0:
                        # The row doesn't exist, proceed with the insert
                        insert_query = f"""
                        INSERT INTO `{SQLformatted_name}_GameLogs` (
                            Week,
                            Receptions,
                            Rec_Yards,
                            Rec_Yards_PR,
                            Rec_Touchdowns,
                            Rush_Attempts,
                            Rush_Yards,
                            Rush_Yards_PA,
                            Rush_Touchdowns
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            Receptions = VALUES(Receptions),
                            Rec_Yards = VALUES(Rec_Yards),
                            Rec_Yards_PR = VALUES(Rec_Yards_PR),
                            Rec_Touchdowns = VALUES(Rec_Touchdowns),
                            Rush_Attempts = VALUES(Rush_Attempts),
                            Rush_Yards = VALUES(Rush_Yards),
                            Rush_Yards_PA = VALUES(Rush_Yards_PA),
                            Rush_Touchdowns = VALUES(Rush_Touchdowns);
                            
                        """
                        current_values = (
                            WeekList [i],
                            TE_ReceptionsList [i],
                            TE_RecYardsList [i],
                            TE_RecYards_PRList [i],
                            TE_RecTouchdownsList [i],
                            TE_RushAttemptsList [i],
                            TE_RushYardsList [i],
                            TE_RushYards_PAList [i],
                            TE_RushTouchdowns [i]
                            )
                        cursor.execute(insert_query, current_values)
                
            # Commit the changes
            conn.commit()

    # Close the cursor and connection
    cursor.close()
    
    
    
    # Quit all driver instances after processing
    for current_driver in drivers:  
        current_driver.quit()       
        