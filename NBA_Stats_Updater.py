from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from urllib.parse import urlparse
from urllib.parse import urljoin

from main_Library import *
import mysql.connector
from bs4 import BeautifulSoup
import time
from datetime import datetime
import math
import re
import copy





# Update Functions
def supplyTable_DefTeam_Scoring():
    
    try:
        team = []
        opp_Points_PerGame = []
        opp_Avg_ScoreMargin = []
        opp_1stQuarter_Points_PerGame = []
        opp_2ndQuarter_Points_PerGame = []
        opp_3rdQuarter_Points_PerGame = []
        opp_4thQuarter_Points_PerGame = []
        opp_Points_2Pointers = []
        opp_Points_3Pointers = []
        
        teamNames = ["New York", "Philadelphia", "Toronto", "Detroit", "Minnesota", "Orlando", "Denver", "LA Clippers", "Houston", "Golden State", "Boston",
                    "Cleveland", "New Orleans", "Chicago", "Portland", "Phoenix", "Memphis", "Sacramento", "Utah", "Miami", "Okla City",
                    "Brooklyn", "Atlanta", "Charlotte", "Milwaukee", "LA Lakers", "Dallas", "Indiana", "San Antonio", "Washington"]
        
        database_Name = "nba_stats"
        
        connection = create_connection("nba_stats")
        
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
        
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1080, 1200)
        wait = WebDriverWait(driver, 10)
        
        driver.get("https://www.teamrankings.com/nba/stat/opponent-points-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Points Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        pointsPerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(pointsPerGame_Elements) >= 3:
                            
                            pointsPerGame_element = pointsPerGame_Elements[0]
                            
                            pointsPerGame_Stat = pointsPerGame_element.text.strip()
                            
                            opp_Points_PerGame.append(pointsPerGame_Stat)
        
        driver.get("https://www.teamrankings.com/nba/stat/opponent-average-scoring-margin")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                            
        # Oppenents Average Score Margin
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        avg_ScoreMargin_Elements = row.find_all('td', class_='text-right')
                        
                        if len(avg_ScoreMargin_Elements) >= 3:
                            
                            avg_ScoreMargin_element = avg_ScoreMargin_Elements[0]
                            
                            avg_ScoreMargin_Stat = avg_ScoreMargin_element.text.strip()
                            
                            opp_Avg_ScoreMargin.append(avg_ScoreMargin_Stat)
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-1st-quarter-points-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                            
        # Oppenents 1st Quarter Points Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        points_1stQuarter_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(points_1stQuarter_PerGame_Elements) >= 3:
                            
                            points_1stQuarter_PerGame_element = points_1stQuarter_PerGame_Elements[0]
                            
                            points_1stQuarter_PerGame_Stat = points_1stQuarter_PerGame_element.text.strip()
                            
                            opp_1stQuarter_Points_PerGame.append(points_1stQuarter_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-2nd-quarter-points-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                            
        # Oppenents 2nd Quarter Points Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        points_2ndQuarter_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(points_2ndQuarter_PerGame_Elements) >= 3:
                            
                            points_2ndQuarter_PerGame_element = points_2ndQuarter_PerGame_Elements[0]
                            
                            points_2ndQuarter_PerGame_Stat = points_2ndQuarter_PerGame_element.text.strip()
                            
                            opp_2ndQuarter_Points_PerGame.append(points_2ndQuarter_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-3rd-quarter-points-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                            
        # Oppenents 3rd Quarter Points Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        points_3rdQuarter_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(points_3rdQuarter_PerGame_Elements) >= 3:
                            
                            points_3rdQuarter_PerGame_element = points_3rdQuarter_PerGame_Elements[0]
                            
                            points_3rdQuarter_PerGame_Stat = points_3rdQuarter_PerGame_element.text.strip()
                            
                            opp_3rdQuarter_Points_PerGame.append(points_3rdQuarter_PerGame_Stat)
                            
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-4th-quarter-points-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                            
        # Oppenents 4th Quarter Points Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        points_4thQuarter_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(points_4thQuarter_PerGame_Elements) >= 3:
                            
                            points_4thQuarter_PerGame_element = points_4thQuarter_PerGame_Elements[0]
                            
                            points_4thQuarter_PerGame_Stat = points_4thQuarter_PerGame_element.text.strip()
                            
                            opp_4thQuarter_Points_PerGame.append(points_4thQuarter_PerGame_Stat)
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-points-from-2-pointers")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                            
        # Oppenents Points from 2 pointers
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Points_2Pointers_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Points_2Pointers_Elements) >= 3:
                            
                            opp_Points_2Pointers_element = opp_Points_2Pointers_Elements[0]
                            
                            opp_Points_2Pointers_Stat = opp_Points_2Pointers_element.text.strip()
                            
                            opp_Points_2Pointers.append(opp_Points_2Pointers_Stat)
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-points-from-3-pointers")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
                            
        # Oppenents Points from 2 pointers
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Points_3Pointers_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Points_3Pointers_Elements) >= 3:
                            
                            opp_Points_3Pointers_element = opp_Points_3Pointers_Elements[0]
                            
                            opp_Points_3Pointers_Stat = opp_Points_3Pointers_element.text.strip()
                            
                            opp_Points_3Pointers.append(opp_Points_3Pointers_Stat)
                            
                            
        for i in range(len(teamNames)):
            insert_sql = "INSERT INTO team_defense_scoring (Team, opp_Points_PerGame, opp_Avg_ScoreMargin, opp_1stQuarter_Points_PerGame, opp_2ndQuarter_Points_PerGame, opp_3rdQuarter_Points_PerGame, opp_4thQuarter_Points_PerGame, opp_Points_2Pointers, opp_Points_3Pointers) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE opp_Points_PerGame = VALUES(opp_Points_PerGame), opp_Avg_ScoreMargin = VALUES(opp_Avg_ScoreMargin), opp_1stQuarter_Points_PerGame = VALUES(opp_1stQuarter_Points_PerGame), opp_2ndQuarter_Points_PerGame = VALUES(opp_2ndQuarter_Points_PerGame), opp_3rdQuarter_Points_PerGame = VALUES(opp_3rdQuarter_Points_PerGame), opp_4thQuarter_Points_PerGame = VALUES(opp_4thQuarter_Points_PerGame), opp_Points_2Pointers = VALUES(opp_Points_2Pointers), opp_Points_3Pointers = VALUES(opp_Points_3Pointers)"
        
            values = (teamNames[i], opp_Points_PerGame[i], opp_Avg_ScoreMargin[i], opp_1stQuarter_Points_PerGame[i], opp_2ndQuarter_Points_PerGame[i], opp_3rdQuarter_Points_PerGame[i], opp_4thQuarter_Points_PerGame[i], opp_Points_2Pointers[i], opp_Points_3Pointers[i])
        
            cursor.execute(insert_sql, values)
            
        conn.commit()
        cursor.close()
        conn.close()
    
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_DefTeam_Scoring()
                                              
def supplyTable_DefTeam_Shooting():
    
    try:
        team = []
        opp_Shooting_Perc = []
        opp_ThreePoint_Perc = []
        opp_FieldGoals_PerGame = []
        opp_FieldGoals_Attempts_PerGame = []
        opp_ThreePointers_PerGame = []
        opp_ThreePointers_Attempts_PerGame = []
        
        teamNames = ["New York", "Philadelphia", "Toronto", "Detroit", "Minnesota", "Orlando", "Denver", "LA Clippers", "Houston", "Golden State", "Boston",
                    "Cleveland", "New Orleans", "Chicago", "Portland", "Phoenix", "Memphis", "Sacramento", "Utah", "Miami", "Okla City",
                    "Brooklyn", "Atlanta", "Charlotte", "Milwaukee", "LA Lakers", "Dallas", "Indiana", "San Antonio", "Washington"]
        
        database_Name = "nba_stats"
        
        connection = create_connection("nba_stats")
        
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
        
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1080, 1200)
        wait = WebDriverWait(driver, 10)
        
        driver.get("https://www.teamrankings.com/nba/stat/opponent-shooting-pct")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Shooting Perc
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Shooting_Perc_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Shooting_Perc_Elements) >= 3:
                            
                            opp_Shooting_Perc_element = opp_Shooting_Perc_Elements[0]
                            
                            opp_Shooting_Perc_Stat = opp_Shooting_Perc_element.text.strip().replace('%', '')
                            
                            opp_Shooting_Perc.append(opp_Shooting_Perc_Stat)
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-three-point-pct")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')                    
                            
        # Oppenents Three Point Shooting Perc
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_ThreePoint_Perc_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_ThreePoint_Perc_Elements) >= 3:
                            
                            opp_ThreePoint_Perc_element = opp_ThreePoint_Perc_Elements[0]
                            
                            opp_ThreePoint_Perc_Stat = opp_ThreePoint_Perc_element.text.strip().replace('%', '')
                            
                            opp_ThreePoint_Perc.append(opp_ThreePoint_Perc_Stat)
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-field-goals-made-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')                     
                            
        # Oppenents Field Goals Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_FieldGoals_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_FieldGoals_PerGame_Elements) >= 3:
                            
                            opp_FieldGoals_PerGame_element = opp_FieldGoals_PerGame_Elements[0]
                            
                            opp_FieldGoals_PerGame_Stat = opp_FieldGoals_PerGame_element.text.strip().replace('%', '')
                            
                            opp_FieldGoals_PerGame.append(opp_FieldGoals_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-field-goals-attempted-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')                     
                            
        # Oppenents Field Goals Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_FieldGoals_Attempts_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_FieldGoals_Attempts_PerGame_Elements) >= 3:
                            
                            opp_FieldGoals_Attempts_PerGame_element = opp_FieldGoals_Attempts_PerGame_Elements[0]
                            
                            opp_FieldGoals_Attempts_PerGame_Stat = opp_FieldGoals_Attempts_PerGame_element.text.strip().replace('%', '')
                            
                            opp_FieldGoals_Attempts_PerGame.append(opp_FieldGoals_Attempts_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-three-pointers-made-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')                     
                            
        # Oppenents Field Goals Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_ThreePointers_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_ThreePointers_PerGame_Elements) >= 3:
                            
                            opp_ThreePointers_PerGame_element = opp_ThreePointers_PerGame_Elements[0]
                            
                            opp_ThreePointers_PerGame_Stat = opp_ThreePointers_PerGame_element.text.strip().replace('%', '')
                            
                            opp_ThreePointers_PerGame.append(opp_ThreePointers_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-three-pointers-attempted-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')                     
                            
        # Oppenents Field Goals Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_ThreePointers_Attempts_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_ThreePointers_Attempts_PerGame_Elements) >= 3:
                            
                            opp_ThreePointers_Attempts_PerGame_element = opp_ThreePointers_Attempts_PerGame_Elements[0]
                            
                            opp_ThreePointers_Attempts_PerGame_Stat = opp_ThreePointers_Attempts_PerGame_element.text.strip().replace('%', '')
                            
                            opp_ThreePointers_Attempts_PerGame.append(opp_ThreePointers_Attempts_PerGame_Stat)
                            
                            
                            
        
        for i in range(len(teamNames)):
            insert_sql = "INSERT INTO team_defense_shooting (Team, opp_Shooting_Perc, opp_ThreePoint_Perc, opp_FieldGoals_PerGame, opp_FieldGoals_Attempts_PerGame, opp_3Pointers_PerGame, opp_3Pointers_Attempts_PerGame) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE opp_Shooting_Perc = VALUES(opp_Shooting_Perc), opp_ThreePoint_Perc = VALUES(opp_ThreePoint_Perc), opp_FieldGoals_PerGame = VALUES(opp_FieldGoals_PerGame), opp_FieldGoals_Attempts_PerGame = VALUES(opp_FieldGoals_Attempts_PerGame), opp_3Pointers_PerGame = VALUES(opp_3Pointers_PerGame), opp_3Pointers_Attempts_PerGame = VALUES(opp_3Pointers_Attempts_PerGame)"
        
            values = (teamNames[i], opp_Shooting_Perc[i], opp_ThreePoint_Perc[i], opp_FieldGoals_PerGame[i], opp_FieldGoals_Attempts_PerGame[i], opp_ThreePointers_PerGame[i], opp_ThreePointers_Attempts_PerGame[i])
        
            cursor.execute(insert_sql, values)
            
        conn.commit()
        cursor.close()
        conn.close()
    
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_DefTeam_Shooting()
    
def supplyTable_Opp_Misc():
    
    try:
        team = []
        opp_OffRebounds_PerGame = []
        opp_DefRebounds_PerGame = []
        opp_Blocks_PerGame = []
        opp_Steals_PerGame = []
        opp_Steals_PerPossession = []
        opp_Steals_PerDefPlay = []
        opp_Assists_PerGame = []
        opp_Turnovers_PerGame = []
        opp_Turnovers_PerPossession = []
        opp_Turnovers_PerOffensivePlay = []
        opp_Fouls_PerGame = []
        
        teamNames = ["New York", "Philadelphia", "Toronto", "Detroit", "Minnesota", "Orlando", "Denver", "LA Clippers", "Houston", "Golden State", "Boston",
                    "Cleveland", "New Orleans", "Chicago", "Portland", "Phoenix", "Memphis", "Sacramento", "Utah", "Miami", "Okla City",
                    "Brooklyn", "Atlanta", "Charlotte", "Milwaukee", "LA Lakers", "Dallas", "Indiana", "San Antonio", "Washington"]
        
        database_Name = "nba_stats"
        
        connection = create_connection("nba_stats")
        
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
        
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1080, 1200)
        wait = WebDriverWait(driver, 10)
        
        driver.get("https://www.teamrankings.com/nba/stat/opponent-offensive-rebounds-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Offensive Rebounds Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_OffRebounds_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_OffRebounds_PerGame_Elements) >= 3:
                            
                            opp_OffRebounds_PerGame_element = opp_OffRebounds_PerGame_Elements[0]
                            
                            opp_OffRebounds_PerGame_Stat = opp_OffRebounds_PerGame_element.text.strip().replace('%', '')
                            
                            opp_OffRebounds_PerGame.append(opp_OffRebounds_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-defensive-rebounds-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Defensive Rebounds Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_DefRebounds_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_DefRebounds_PerGame_Elements) >= 3:
                            
                            opp_DefRebounds_PerGame_element = opp_DefRebounds_PerGame_Elements[0]
                            
                            opp_DefRebounds_PerGame_Stat = opp_DefRebounds_PerGame_element.text.strip().replace('%', '')
                            
                            opp_DefRebounds_PerGame.append(opp_DefRebounds_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-blocks-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Blocks_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Blocks_PerGame_Elements) >= 3:
                            
                            opp_Blocks_PerGame_element = opp_Blocks_PerGame_Elements[0]
                            
                            opp_Blocks_PerGame_Stat = opp_Blocks_PerGame_element.text.strip().replace('%', '')
                            
                            opp_Blocks_PerGame.append(opp_Blocks_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-steals-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Steals_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Steals_PerGame_Elements) >= 3:
                            
                            opp_Steals_PerGame_element = opp_Steals_PerGame_Elements[0]
                            
                            opp_Steals_PerGame_Stat = opp_Steals_PerGame_element.text.strip().replace('%', '')
                            
                            opp_Steals_PerGame.append(opp_Steals_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-steals-perpossession")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Steals_PerPossession_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Steals_PerPossession_Elements) >= 3:
                            
                            opp_Steals_PerPossession_element = opp_Steals_PerPossession_Elements[0]
                            
                            opp_Steals_PerPossession_Stat = opp_Steals_PerPossession_element.text.strip().replace('%', '')
                            
                            opp_Steals_PerPossession.append(opp_Steals_PerPossession_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-steal-pct")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Steals_PerDefPlay_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Steals_PerDefPlay_Elements) >= 3:
                            
                            opp_Steals_PerDefPlay_element = opp_Steals_PerDefPlay_Elements[0]
                            
                            opp_Steals_PerDefPlay_Stat = opp_Steals_PerDefPlay_element.text.strip().replace('%', '')
                            
                            opp_Steals_PerDefPlay.append(opp_Steals_PerDefPlay_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-assists-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Assists_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Assists_PerGame_Elements) >= 3:
                            
                            opp_Assists_PerGame_element = opp_Assists_PerGame_Elements[0]
                            
                            opp_Assists_PerGame_Stat = opp_Assists_PerGame_element.text.strip().replace('%', '')
                            
                            opp_Assists_PerGame.append(opp_Assists_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-turnovers-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Turnovers_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Turnovers_PerGame_Elements) >= 3:
                            
                            opp_Turnovers_PerGame_element = opp_Turnovers_PerGame_Elements[0]
                            
                            opp_Turnovers_PerGame_Stat = opp_Turnovers_PerGame_element.text.strip().replace('%', '')
                            
                            opp_Turnovers_PerGame.append(opp_Turnovers_PerGame_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-turnovers-per-possession")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Turnovers_PerPossession_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Turnovers_PerPossession_Elements) >= 3:
                            
                            opp_Turnovers_PerPossession_element = opp_Turnovers_PerPossession_Elements[0]
                            
                            opp_Turnovers_PerPossession_Stat = opp_Turnovers_PerPossession_element.text.strip().replace('%', '')
                            
                            opp_Turnovers_PerPossession.append(opp_Turnovers_PerPossession_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-turnover-pct")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Turnovers_PerOffensivePlay_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Turnovers_PerOffensivePlay_Elements) >= 3:
                            
                            opp_Turnovers_PerOffensivePlay_element = opp_Turnovers_PerOffensivePlay_Elements[0]
                            
                            opp_Turnovers_PerOffensivePlay_Stat = opp_Turnovers_PerOffensivePlay_element.text.strip().replace('%', '')
                            
                            opp_Turnovers_PerOffensivePlay.append(opp_Turnovers_PerOffensivePlay_Stat)
                            
                            
                            
        driver.get("https://www.teamrankings.com/nba/stat/opponent-personal-fouls-per-game")
        
        time.sleep(2)
                # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        scrollWrapper = soup.find('div', class_ = 'scroll-wrapper')
        
        # Oppenents Blocks Per Game
        for team in teamNames:
            
            rows = scrollWrapper.find_all('tr', role='row')
            
            for row in rows:
                team_name_element = row.find('td', class_='text-left nowrap')
                if team_name_element:
                    team_name = team_name_element.text.strip()

                    if team_name == team:
                        
                        opp_Fouls_PerGame_Elements = row.find_all('td', class_='text-right')
                        
                        if len(opp_Fouls_PerGame_Elements) >= 3:
                            
                            opp_Fouls_PerGame_element = opp_Fouls_PerGame_Elements[0]
                            
                            opp_Fouls_PerGame_Stat = opp_Fouls_PerGame_element.text.strip().replace('%', '')
                            
                            opp_Fouls_PerGame.append(opp_Fouls_PerGame_Stat)
        
        
                            
        for i in range(len(teamNames)):
            insert_sql = "INSERT INTO team_opp_misc (Team, opp_OffRebounds_PerGame, opp_DefRebounds_PerGame, opp_Blocks_PerGame, opp_Steals_PerGame, opp_Steals_PerPossession, opp_Steals_PerDefPlay, opp_Assists_PerGame, opp_Turnovers_PerGame, opp_Turnovers_PerPossession, opp_Turnovers_PerOffensivePlay, opp_Fouls_PerGame) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE opp_OffRebounds_PerGame = VALUES(opp_OffRebounds_PerGame), opp_DefRebounds_PerGame = VALUES(opp_DefRebounds_PerGame), opp_Blocks_PerGame = VALUES(opp_Blocks_PerGame), opp_Steals_PerGame = VALUES(opp_Steals_PerGame), opp_Steals_PerPossession = VALUES(opp_Steals_PerPossession), opp_Steals_PerDefPlay = VALUES(opp_Steals_PerDefPlay), opp_Assists_PerGame = VALUES(opp_Assists_PerGame), opp_Turnovers_PerGame = VALUES(opp_Turnovers_PerGame), opp_Turnovers_PerPossession = VALUES(opp_Turnovers_PerPossession), opp_Turnovers_PerOffensivePlay = VALUES(opp_Turnovers_PerOffensivePlay), opp_Fouls_PerGame = VALUES(opp_Fouls_PerGame)"
        
            values = (teamNames[i], opp_OffRebounds_PerGame[i], opp_DefRebounds_PerGame[i], opp_Blocks_PerGame[i], opp_Steals_PerGame[i], opp_Steals_PerPossession[i], opp_Steals_PerDefPlay[i], opp_Assists_PerGame[i], opp_Turnovers_PerGame[i], opp_Turnovers_PerPossession[i], opp_Turnovers_PerOffensivePlay[i], opp_Fouls_PerGame[i])
        
            cursor.execute(insert_sql, values)
            
        conn.commit()
        cursor.close()
        conn.close()
    
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_Opp_Misc()
                                                 
def supplyTable_Winning_Perc():
    
    try:
        teamNames_AllGames_List = []
        winPerc_AllGames = []
        teamNames_CloseGames_List = []
        winPerc_CloseGames = []
        teamNames_Opp_AllGames_List = []
        opp_winPerc_AllGames = []
        teamNames_Opp_CloseGames_List = []
        opp_winPerc_CloseGames = []
        
        master_dict = {}
        
        teamNames = ["New York", "Philadelphia", "Toronto", "Detroit", "Minnesota", "Orlando", "Denver", "LA Clippers", "Houston", "Golden State", "Boston",
                    "Cleveland", "New Orleans", "Chicago", "Portland", "Phoenix", "Memphis", "Sacramento", "Utah", "Miami", "Okla City",
                    "Brooklyn", "Atlanta", "Charlotte", "Milwaukee", "LA Lakers", "Dallas", "Indiana", "San Antonio", "Washington"]
        
        database_Name = "nba_stats"
        
        connection = create_connection("nba_stats")
        
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
        
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        
        
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        driver3 = webdriver.Chrome(options=chrome_options)
        driver4 = webdriver.Chrome(options=chrome_options)
        
        # List of drivers
        drivers = [driver, driver2, driver3, driver4] 
        
        url_1 = "https://www.teamrankings.com/nba/stat/win-pct-all-games"
        url_2 = "https://www.teamrankings.com/nba/stat/win-pct-close-games"
        url_3 = "https://www.teamrankings.com/nba/stat/opponent-win-pct-all-games"
        url_4 = "https://www.teamrankings.com/nba/stat/opponent-win-pct-close-games"
        
        driver.get(url_1)
        driver2.get(url_2)
        driver3.get(url_3)
        driver4.get(url_4)
        
        time.sleep(3)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        html_content_3 = driver3.page_source
        soup_3 = BeautifulSoup(html_content_3, 'html.parser')
        
        html_content_4 = driver4.page_source
        soup_4 = BeautifulSoup(html_content_4, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_3 = soup_3.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_4 = soup_4.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        tBody_3 = scroll_Wrapper_3.find("tbody")
        tBody_4 = scroll_Wrapper_4.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        table_Rows_Even3 = tBody_3.find_all("tr", class_="odd")
        table_Rows_Odd3 = tBody_3.find_all("tr", class_="even")
        table_Rows_Even4 = tBody_4.find_all("tr", class_="odd")
        table_Rows_Odd4 = tBody_4.find_all("tr", class_="even")
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_AllGames_List.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            winPerc_AllGames.append(float(Columns[0].text))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_AllGames_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            winPerc_AllGames.append(float(Columns[0].text))
            
        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_CloseGames_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            winPerc_CloseGames.append(float(Columns[0].text))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_CloseGames_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            winPerc_CloseGames.append(float(Columns[0].text))
            
        for row in table_Rows_Even3:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_Opp_AllGames_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            opp_winPerc_AllGames.append(float(Columns[0].text))
            
        for row in table_Rows_Odd3:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_Opp_AllGames_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            opp_winPerc_AllGames.append(float(Columns[0].text))
            
        for row in table_Rows_Even4:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_Opp_CloseGames_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            opp_winPerc_CloseGames.append(float(Columns[0].text))
            
        for row in table_Rows_Odd4:
            
            name_column = row.find("td", class_="text-left nowrap")

            teamNames_Opp_CloseGames_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            opp_winPerc_CloseGames.append(float(Columns[0].text))
        
        all_teams = set(teamNames_AllGames_List + teamNames_CloseGames_List +
                    teamNames_Opp_AllGames_List + teamNames_Opp_CloseGames_List)
        
        # Initialize master_dict with team names as keys
        for team in all_teams:
            master_dict[team] = {
                'winPerc_AllGames': 0.000,
                'winPerc_CloseGames': 0.000,
                'opp_winPerc_AllGames': 0.000,
                'opp_winPerc_CloseGames': 0.000
            }
            
        # Update master_dict with values from respective lists
        for team in teamNames_AllGames_List:
            index = teamNames_AllGames_List.index(team)
            master_dict[team]['winPerc_AllGames'] = winPerc_AllGames[index]

        for team in teamNames_CloseGames_List:
            index = teamNames_CloseGames_List.index(team)
            master_dict[team]['winPerc_CloseGames'] = winPerc_CloseGames[index]

        for team in teamNames_Opp_AllGames_List:
            index = teamNames_Opp_AllGames_List.index(team)
            master_dict[team]['opp_winPerc_AllGames'] = opp_winPerc_AllGames[index]

        for team in teamNames_Opp_CloseGames_List:
            index = teamNames_Opp_CloseGames_List.index(team)
            master_dict[team]['opp_winPerc_CloseGames'] = opp_winPerc_CloseGames[index]
                
        for team, values in master_dict.items():
            # SQL query to insert data into the team_winning_perc table
            sql = """
                INSERT INTO team_winning_perc
                (Team, winPerc_AllGames, winPerc_CloseGames, opp_winPerc_AllGames, opp_winPerc_CloseGames)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                winPerc_AllGames = VALUES(winPerc_AllGames),
                winPerc_CloseGames = VALUES(winPerc_CloseGames),
                opp_winPerc_AllGames = VALUES(opp_winPerc_AllGames),
                opp_winPerc_CloseGames = VALUES(opp_winPerc_CloseGames)
                """

            # Data for the current iteration
            data = (
                team,
                values['winPerc_AllGames'],
                values['winPerc_CloseGames'],
                values['opp_winPerc_AllGames'],
                values['opp_winPerc_CloseGames']
            )

            # Execute the SQL query
            cursor.execute(sql, data)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()     
        
        for driver in drivers:
            
            driver.close()
        
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_Winning_Perc()

def supplyTable_Team_Misc():
    
    try:
        team_Off_Rebounds_List = []
        off_Rebounds_PerGame_List = []
        
        team_Def_Rebounds_List = []
        def_Rebounds_PerGame_List = []
        
        team_Block_List = []
        blocks_PerGame_List = []
        
        team_Steals_List = []
        steals_PerGame_List = []
        
        team_Assists_List = []
        assists_PerGame_List = []
        
        team_Turnovers_List = []
        turnovers_PerGame_List = []
        
        team_PersonalFouls_List = []
        personalFouls_PerGame_List = []
        
        team_TechnicalFouls_List = []
        technicalFouls_PerGame_List = []
        
        master_dict = {}
        
        database_Name = "nba_stats"
        
        connection = create_connection("nba_stats")
        
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
        
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        
        
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        driver3 = webdriver.Chrome(options=chrome_options)
        driver4 = webdriver.Chrome(options=chrome_options)
        
        # List of drivers
        drivers = [driver, driver2, driver3, driver4] 
        
        url_1 = "https://www.teamrankings.com/nba/stat/opponent-offensive-rebounds-per-game"
        url_2 = "https://www.teamrankings.com/nba/stat/opponent-defensive-rebounds-per-game"
        url_3 = "https://www.teamrankings.com/nba/stat/blocks-per-game"
        url_4 = "https://www.teamrankings.com/nba/stat/steals-per-game"
        
        driver.get(url_1)
        driver2.get(url_2)
        driver3.get(url_3)
        driver4.get(url_4)
        
        time.sleep(3)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        html_content_3 = driver3.page_source
        soup_3 = BeautifulSoup(html_content_3, 'html.parser')
        
        html_content_4 = driver4.page_source
        soup_4 = BeautifulSoup(html_content_4, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_3 = soup_3.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_4 = soup_4.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        tBody_3 = scroll_Wrapper_3.find("tbody")
        tBody_4 = scroll_Wrapper_4.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        table_Rows_Even3 = tBody_3.find_all("tr", class_="odd")
        table_Rows_Odd3 = tBody_3.find_all("tr", class_="even")
        table_Rows_Even4 = tBody_4.find_all("tr", class_="odd")
        table_Rows_Odd4 = tBody_4.find_all("tr", class_="even")
        
        
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Off_Rebounds_List.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            off_Rebounds_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Off_Rebounds_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            off_Rebounds_PerGame_List.append(float(Columns[0].text))
        
        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Def_Rebounds_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            def_Rebounds_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Def_Rebounds_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            def_Rebounds_PerGame_List.append(float(Columns[0].text)) 
            
        for row in table_Rows_Even3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Block_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            blocks_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Block_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            blocks_PerGame_List.append(float(Columns[0].text))    
        
        for row in table_Rows_Even4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Steals_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            steals_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Steals_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            steals_PerGame_List.append(float(Columns[0].text))
        
        url_1 = "https://www.teamrankings.com/nba/stat/assists-per-game"
        url_2 = "https://www.teamrankings.com/nba/stat/turnovers-per-game"
        url_3 = "https://www.teamrankings.com/nba/stat/personal-fouls-per-game"
        url_4 = "https://www.teamrankings.com/nba/stat/technical-fouls-per-game"
        
        driver.get(url_1)
        driver2.get(url_2)
        driver3.get(url_3)
        driver4.get(url_4)
        
        time.sleep(3)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        html_content_3 = driver3.page_source
        soup_3 = BeautifulSoup(html_content_3, 'html.parser')
        
        html_content_4 = driver4.page_source
        soup_4 = BeautifulSoup(html_content_4, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_3 = soup_3.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_4 = soup_4.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        tBody_3 = scroll_Wrapper_3.find("tbody")
        tBody_4 = scroll_Wrapper_4.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        table_Rows_Even3 = tBody_3.find_all("tr", class_="odd")
        table_Rows_Odd3 = tBody_3.find_all("tr", class_="even")
        table_Rows_Even4 = tBody_4.find_all("tr", class_="odd")
        table_Rows_Odd4 = tBody_4.find_all("tr", class_="even")
        
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Assists_List.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            assists_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Assists_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            assists_PerGame_List.append(float(Columns[0].text))

        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Turnovers_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            turnovers_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Turnovers_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            turnovers_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Even3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_PersonalFouls_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            personalFouls_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_PersonalFouls_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            personalFouls_PerGame_List.append(float(Columns[0].text))

        for row in table_Rows_Even4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_TechnicalFouls_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            technicalFouls_PerGame_List.append(float(Columns[0].text))
            
        for row in table_Rows_Odd4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_TechnicalFouls_List.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            technicalFouls_PerGame_List.append(float(Columns[0].text))

        all_teams = set( team_Off_Rebounds_List + team_Def_Rebounds_List +
                    team_Block_List + team_Steals_List + team_Turnovers_List
                    + team_PersonalFouls_List + team_TechnicalFouls_List )
        
        # Initialize master_dict with team names as keys
        for team in all_teams:
            master_dict[team] = {
                'off_Rebounds_PerGame_List': 0.000,
                'def_Rebounds_PerGame_List': 0.000,
                'blocks_PerGame_List': 0.000,
                'steals_PerGame_List': 0.000,
                'assists_PerGame_List': 0.000,
                'turnovers_PerGame_List': 0.000,
                'personalFouls_PerGame_List': 0.000,
                'technicalFouls_PerGame_List': 0.000
            }
            
        # Update master_dict with values from respective lists
        for team in team_Off_Rebounds_List:
            index = team_Off_Rebounds_List.index(team)
            master_dict[team]['off_Rebounds_PerGame_List'] = off_Rebounds_PerGame_List[index]

        for team in team_Def_Rebounds_List:
            index = team_Def_Rebounds_List.index(team)
            master_dict[team]['def_Rebounds_PerGame_List'] = def_Rebounds_PerGame_List[index]

        for team in team_Block_List:
            index = team_Block_List.index(team)
            master_dict[team]['blocks_PerGame_List'] = blocks_PerGame_List[index]

        for team in team_Steals_List:
            index = team_Steals_List.index(team)
            master_dict[team]['steals_PerGame_List'] = steals_PerGame_List[index]
            
        for team in team_Assists_List:
            index = team_Assists_List.index(team)
            master_dict[team]['assists_PerGame_List'] = assists_PerGame_List[index]
            
        for team in team_Turnovers_List:
            index = team_Turnovers_List.index(team)
            master_dict[team]['turnovers_PerGame_List'] = turnovers_PerGame_List[index]
            
        for team in team_PersonalFouls_List:
            index = team_PersonalFouls_List.index(team)
            master_dict[team]['personalFouls_PerGame_List'] = personalFouls_PerGame_List[index]
            
        for team in team_TechnicalFouls_List:
            index = team_TechnicalFouls_List.index(team)
            master_dict[team]['technicalFouls_PerGame_List'] = technicalFouls_PerGame_List[index]
        
        for team, values in master_dict.items():
            # SQL query to insert data into the team_winning_perc table
            sql = """
                INSERT INTO team_misc
                (Team, off_Rebounds_PerGame, def_Rebounds_PerGame, blocks_PerGame, steals_PerGame, Assists_PerGame, turnovers_PerGame, personalFouls_PerGame, technicalFouls_PerGame)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                off_Rebounds_PerGame = VALUES(off_Rebounds_PerGame),
                def_Rebounds_PerGame = VALUES(def_Rebounds_PerGame),
                blocks_PerGame = VALUES(blocks_PerGame),
                steals_PerGame = VALUES(steals_PerGame),
                Assists_PerGame = VALUES(Assists_PerGame),
                turnovers_PerGame = VALUES(turnovers_PerGame),
                personalFouls_PerGame = VALUES(personalFouls_PerGame),
                technicalFouls_PerGame = VALUES(technicalFouls_PerGame)
                """

            # Data for the current iteration
            data = (
                team,
                values['off_Rebounds_PerGame_List'],
                values['def_Rebounds_PerGame_List'],
                values['blocks_PerGame_List'],
                values['steals_PerGame_List'],
                values['assists_PerGame_List'],
                values['turnovers_PerGame_List'],
                values['personalFouls_PerGame_List'],
                values['technicalFouls_PerGame_List']
            )

            # Execute the SQL query
            cursor.execute(sql, data)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()     
        
        for driver in drivers:
            
            driver.close()
        
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_Team_Misc()

def supplyTable_OffTeam_Shooting():
    
    try:
        team_Shooting_Perc = []
        shooting_Perc_List = []
        
        team_ThreePoint_Perc = []
        threePoint_Perc_List = []
        
        team_FieldGoals_PerGame = []
        fieldGoals_PerGame_List = []
        
        team_FieldGoals_attempts = []
        fieldGoals_Attempted_PerGame_List = []
        
        team_ThreePoint_PerGame = []
        threePointers_PerGame_List = []
        
        team_ThreePoint_Attempts = []
        threePointers_Attempted_PerGame_List = []
        
        master_dict = {}
        
        database_Name = "nba_stats"
        
        connection = create_connection("nba_stats")
        
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
        
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        
        
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        driver3 = webdriver.Chrome(options=chrome_options)
        driver4 = webdriver.Chrome(options=chrome_options)
        
        # List of drivers
        drivers = [driver, driver2, driver3, driver4] 
        
        url_1 = "https://www.teamrankings.com/nba/stat/shooting-pct"
        url_2 = "https://www.teamrankings.com/nba/stat/three-point-pct"
        url_3 = "https://www.teamrankings.com/nba/stat/field-goals-made-per-game"
        url_4 = "https://www.teamrankings.com/nba/stat/field-goals-attempted-per-game"
        
        driver.get(url_1)
        driver2.get(url_2)
        driver3.get(url_3)
        driver4.get(url_4)
        
        time.sleep(3)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        html_content_3 = driver3.page_source
        soup_3 = BeautifulSoup(html_content_3, 'html.parser')
        
        html_content_4 = driver4.page_source
        soup_4 = BeautifulSoup(html_content_4, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_3 = soup_3.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_4 = soup_4.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        tBody_3 = scroll_Wrapper_3.find("tbody")
        tBody_4 = scroll_Wrapper_4.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        table_Rows_Even3 = tBody_3.find_all("tr", class_="odd")
        table_Rows_Odd3 = tBody_3.find_all("tr", class_="even")
        table_Rows_Even4 = tBody_4.find_all("tr", class_="odd")
        table_Rows_Odd4 = tBody_4.find_all("tr", class_="even")
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Shooting_Perc.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            shooting_Perc_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Shooting_Perc.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            shooting_Perc_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_ThreePoint_Perc.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            threePoint_Perc_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_ThreePoint_Perc.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            threePoint_Perc_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Even3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_FieldGoals_PerGame.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            fieldGoals_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_FieldGoals_PerGame.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            fieldGoals_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Even4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_FieldGoals_attempts.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            fieldGoals_Attempted_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_FieldGoals_attempts.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            fieldGoals_Attempted_PerGame_List.append(float(Columns[0].text.replace("%", "")))

        url_1 = "https://www.teamrankings.com/nba/stat/three-pointers-made-per-game"
        url_2 = "https://www.teamrankings.com/nba/stat/three-pointers-attempted-per-game"
        
        driver.get(url_1)
        driver2.get(url_2)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_ThreePoint_PerGame.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            threePointers_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_ThreePoint_PerGame.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            threePointers_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_ThreePoint_Attempts.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            threePointers_Attempted_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_ThreePoint_Attempts.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            threePointers_Attempted_PerGame_List.append(float(Columns[0].text.replace("%", "")))
        
        all_teams = set(team_Shooting_Perc + team_ThreePoint_Perc + team_FieldGoals_PerGame + team_FieldGoals_attempts
                        + team_ThreePoint_PerGame + team_ThreePoint_Attempts)
        
        # Initialize master_dict with team names as keys
        for team in all_teams:
            master_dict[team] = {
                'shooting_Perc_List': 0.000,
                'threePoint_Perc_List': 0.000,
                'fieldGoals_PerGame_List': 0.000,
                'fieldGoals_Attempted_PerGame_List': 0.000,
                'threePointers_PerGame_List': 0.000,
                'threePointers_Attempted_PerGame_List': 0.000
            }
            
        # Update master_dict with values from respective lists
        for team in team_Shooting_Perc:
            index = team_Shooting_Perc.index(team)
            master_dict[team]['shooting_Perc_List'] = shooting_Perc_List[index]

        for team in team_ThreePoint_Perc:
            index = team_ThreePoint_Perc.index(team)
            master_dict[team]['threePoint_Perc_List'] = threePoint_Perc_List[index]

        for team in team_FieldGoals_PerGame:
            index = team_FieldGoals_PerGame.index(team)
            master_dict[team]['fieldGoals_PerGame_List'] = fieldGoals_PerGame_List[index]

        for team in team_FieldGoals_attempts:
            index = team_FieldGoals_attempts.index(team)
            master_dict[team]['fieldGoals_Attempted_PerGame_List'] = fieldGoals_Attempted_PerGame_List[index]
            
        for team in team_ThreePoint_PerGame:
            index = team_ThreePoint_PerGame.index(team)
            master_dict[team]['threePointers_PerGame_List'] = threePointers_PerGame_List[index]
            
        for team in team_ThreePoint_Attempts:
            index = team_ThreePoint_Attempts.index(team)
            master_dict[team]['threePointers_Attempted_PerGame_List'] = threePointers_Attempted_PerGame_List[index]
            
        
        
        for team, values in master_dict.items():
            # SQL query to insert data into the team_winning_perc table
            sql = """
                INSERT INTO team_offensive_shooting
                (Team, shooting_Perc, 3Point_Perc, fieldGoals_PerGame, fieldGoals_Attempted_PerGame, 3Pointers_PerGame, 3Pointers_Attempted_PerGame)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                shooting_Perc = VALUES(shooting_Perc),
                3Point_Perc = VALUES(3Point_Perc),
                fieldGoals_PerGame = VALUES(fieldGoals_PerGame),
                fieldGoals_Attempted_PerGame = VALUES(fieldGoals_Attempted_PerGame),
                3Pointers_PerGame = VALUES(3Pointers_PerGame),
                3Pointers_Attempted_PerGame = VALUES(3Pointers_Attempted_PerGame)
                """

            # Data for the current iteration
            data = (
                team,
                values['shooting_Perc_List'],
                values['threePoint_Perc_List'],
                values['fieldGoals_PerGame_List'],
                values['fieldGoals_Attempted_PerGame_List'],
                values['threePointers_PerGame_List'],
                values['threePointers_Attempted_PerGame_List']
            )

            # Execute the SQL query
            cursor.execute(sql, data)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()     
        
        for driver in drivers:
            
            driver.close()
    
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_OffTeam_Shooting()
           
def supplyTable_OffTeam_Scoring():
    
    try:
        team_Points_PerGame = []
        points_PerGame_List = []
        
        team_average_ScoreMargin = []
        average_ScoreMargin_List = []
        
        team_Points_1stQuarter_PerGame = []
        points_1stQuarter_PerGame_List = []
        
        team_Points_2ndQuarter_PerGame = []
        points_2ndQuarter_PerGame_List = []
        
        team_Points_3rdQuarter_PerGame = []
        points_3rdQuarter_PerGame_List = []
        
        team_Points_4thQuarter_PerGame = []
        points_4thQuarter_PerGame_List = []
        
        team_Avg_1stQuarter_Margin = []
        avg_1stQuarter_Margin_List = []
        
        team_Avg_2ndQuarter_Margin = []
        avg_2ndQuarter_Margin_List = []
        
        team_Avg_3rdQuarter_Margin = []
        avg_3rdQuarter_Margin_List = []
        
        team_Avg_4thQuarter_Margin = []
        avg_4thQuarter_Margin_List = []
        
        team_Points_2Pointers = []
        points_2Pointers_List = []
        
        team_Points_3Pointers = []
        points_3Pointers_List = []
        
        master_Dict = {}
        
        database_Name = "nba_stats"
        
        connection = create_connection("nba_stats")
        
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
        
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        
        
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        driver3 = webdriver.Chrome(options=chrome_options)
        driver4 = webdriver.Chrome(options=chrome_options)
        
        # List of drivers
        drivers = [driver, driver2, driver3, driver4] 
        
        # Points Per Game
        url_1 = "https://www.teamrankings.com/nba/stat/points-per-game"
        # Average Scoring Margin
        url_2 = "https://www.teamrankings.com/nba/stat/average-scoring-margin"
        # 1st Quarter Points Per Game
        url_3 = "https://www.teamrankings.com/nba/stat/1st-quarter-points-per-game"
        # 2nd Quarter Points Per Game
        url_4 = "https://www.teamrankings.com/nba/stat/2nd-quarter-points-per-game"
        
        driver.get(url_1)
        driver2.get(url_2)
        driver3.get(url_3)
        driver4.get(url_4)
        
        time.sleep(3)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        html_content_3 = driver3.page_source
        soup_3 = BeautifulSoup(html_content_3, 'html.parser')
        
        html_content_4 = driver4.page_source
        soup_4 = BeautifulSoup(html_content_4, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_3 = soup_3.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_4 = soup_4.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        tBody_3 = scroll_Wrapper_3.find("tbody")
        tBody_4 = scroll_Wrapper_4.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        table_Rows_Even3 = tBody_3.find_all("tr", class_="odd")
        table_Rows_Odd3 = tBody_3.find_all("tr", class_="even")
        table_Rows_Even4 = tBody_4.find_all("tr", class_="odd")
        table_Rows_Odd4 = tBody_4.find_all("tr", class_="even")
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_PerGame.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            points_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_PerGame.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            points_PerGame_List.append(float(Columns[0].text.replace("%", "")))
        
        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_average_ScoreMargin.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            average_ScoreMargin_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_average_ScoreMargin.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            average_ScoreMargin_List.append(float(Columns[0].text.replace("%", "")))
        
        for row in table_Rows_Even3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_1stQuarter_PerGame.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            points_1stQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_1stQuarter_PerGame.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            points_1stQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
        
        for row in table_Rows_Even4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_2ndQuarter_PerGame.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            points_2ndQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_2ndQuarter_PerGame.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            points_2ndQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
        
        # 3rd Quarter Points Per Game
        url_1 = "https://www.teamrankings.com/nba/stat/3rd-quarter-points-per-game"
        # 4th Quarter Points Per Game
        url_2 = "https://www.teamrankings.com/nba/stat/4th-quarter-points-per-game"
        # 1st Quarter Margin
        url_3 = "https://www.teamrankings.com/nba/stat/average-1st-quarter-margin"
        # 2nd Quarter Margin
        url_4 = "https://www.teamrankings.com/nba/stat/average-2nd-quarter-margin"
        
        driver.get(url_1)
        driver2.get(url_2)
        driver3.get(url_3)
        driver4.get(url_4)
        
        time.sleep(3)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        html_content_3 = driver3.page_source
        soup_3 = BeautifulSoup(html_content_3, 'html.parser')
        
        html_content_4 = driver4.page_source
        soup_4 = BeautifulSoup(html_content_4, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_3 = soup_3.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_4 = soup_4.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        tBody_3 = scroll_Wrapper_3.find("tbody")
        tBody_4 = scroll_Wrapper_4.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        table_Rows_Even3 = tBody_3.find_all("tr", class_="odd")
        table_Rows_Odd3 = tBody_3.find_all("tr", class_="even")
        table_Rows_Even4 = tBody_4.find_all("tr", class_="odd")
        table_Rows_Odd4 = tBody_4.find_all("tr", class_="even")
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_3rdQuarter_PerGame.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            points_3rdQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_3rdQuarter_PerGame.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            points_3rdQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
        
        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_4thQuarter_PerGame.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            points_4thQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_4thQuarter_PerGame.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            points_4thQuarter_PerGame_List.append(float(Columns[0].text.replace("%", "")))
        
        for row in table_Rows_Even3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_1stQuarter_Margin.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            avg_1stQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_1stQuarter_Margin.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            avg_1stQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
        
        for row in table_Rows_Even4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_2ndQuarter_Margin.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            avg_2ndQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_2ndQuarter_Margin.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            avg_2ndQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
        
        # 3rd Quarter Margin
        url_1 = "https://www.teamrankings.com/nba/stat/average-3rd-quarter-margin"
        # 4th Quarter Margin
        url_2 = "https://www.teamrankings.com/nba/stat/average-4th-quarter-margin"
        # Points from 2 pointers
        url_3 = "https://www.teamrankings.com/nba/stat/points-from-2-pointers"
        # Pointers from 3 pointers
        url_4 = "https://www.teamrankings.com/nba/stat/points-from-3-pointers"
        
        driver.get(url_1)
        driver2.get(url_2)
        driver3.get(url_3)
        driver4.get(url_4)
        
        time.sleep(3)
        
        html_content_1 = driver.page_source
        soup_1 = BeautifulSoup(html_content_1, 'html.parser')
        
        html_content_2 = driver2.page_source
        soup_2 = BeautifulSoup(html_content_2, 'html.parser')
        
        html_content_3 = driver3.page_source
        soup_3 = BeautifulSoup(html_content_3, 'html.parser')
        
        html_content_4 = driver4.page_source
        soup_4 = BeautifulSoup(html_content_4, 'html.parser')
        
        scroll_Wrapper_1 = soup_1.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_2 = soup_2.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_3 = soup_3.find("div", id="DataTables_Table_0_wrapper")
        scroll_Wrapper_4 = soup_4.find("div", id="DataTables_Table_0_wrapper")
        
        tBody_1 = scroll_Wrapper_1.find("tbody")
        tBody_2 = scroll_Wrapper_2.find("tbody")
        tBody_3 = scroll_Wrapper_3.find("tbody")
        tBody_4 = scroll_Wrapper_4.find("tbody")
        
        table_Rows_Even1 = tBody_1.find_all("tr", class_="odd")
        table_Rows_Odd1 = tBody_1.find_all("tr", class_="even")
        table_Rows_Even2 = tBody_2.find_all("tr", class_="odd")
        table_Rows_Odd2 = tBody_2.find_all("tr", class_="even")
        table_Rows_Even3 = tBody_3.find_all("tr", class_="odd")
        table_Rows_Odd3 = tBody_3.find_all("tr", class_="even")
        table_Rows_Even4 = tBody_4.find_all("tr", class_="odd")
        table_Rows_Odd4 = tBody_4.find_all("tr", class_="even")
        
        for row in table_Rows_Even1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_3rdQuarter_Margin.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            avg_3rdQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd1:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_3rdQuarter_Margin.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            avg_3rdQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Even2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_4thQuarter_Margin.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            avg_4thQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd2:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Avg_4thQuarter_Margin.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            avg_4thQuarter_Margin_List.append(float(Columns[0].text.replace("%", "")))
        
        for row in table_Rows_Even3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_2Pointers.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            points_2Pointers_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd3:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_2Pointers.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            points_2Pointers_List.append(float(Columns[0].text.replace("%", "")))   
        
        for row in table_Rows_Even4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_3Pointers.append(name_column.find("a").text)
            
            
            Columns = row.find_all("td", "text-right")
            
            points_3Pointers_List.append(float(Columns[0].text.replace("%", "")))
            
        for row in table_Rows_Odd4:
            
            name_column = row.find("td", class_="text-left nowrap")

            team_Points_3Pointers.append(name_column.find("a").text)
            
            Columns = row.find_all("td", "text-right")
            
            points_3Pointers_List.append(float(Columns[0].text.replace("%", "")))
        
        all_teams = set(team_Points_PerGame + team_average_ScoreMargin + team_Points_1stQuarter_PerGame + team_Points_2ndQuarter_PerGame
                        + team_Points_3rdQuarter_PerGame + team_Points_4thQuarter_PerGame + team_Avg_1stQuarter_Margin + team_Avg_2ndQuarter_Margin
                        + team_Avg_3rdQuarter_Margin + team_Avg_4thQuarter_Margin + team_Points_2Pointers + team_Points_3Pointers )
        
        # Initialize master_dict with team names as keys
        for team in all_teams:
            master_Dict[team] = {
                'points_PerGame_List': 0.0,
                'average_ScoreMargin_List': 0.000,
                'points_1stQuarter_PerGame_List': 0.000,
                'points_2ndQuarter_PerGame_List': 0.000,
                'points_3rdQuarter_PerGame_List': 0.000,
                'points_4thQuarter_PerGame_List': 0.000,
                'avg_1stQuarter_Margin_List': 0.000,
                'avg_2ndQuarter_Margin_List': 0.000,
                'avg_3rdQuarter_Margin_List': 0.000,
                'avg_4thQuarter_Margin_List': 0.000,
                'points_2Pointers_List': 0.000,
                'points_3Pointers_List': 0.000,
            }
        
        
        # Update master_dict with values from respective lists
        for team in team_Points_PerGame:
            index = team_Points_PerGame.index(team)
            master_Dict[team]['points_PerGame_List'] = points_PerGame_List[index]

        for team in team_average_ScoreMargin:
            index = team_average_ScoreMargin.index(team)
            master_Dict[team]['average_ScoreMargin_List'] = average_ScoreMargin_List[index]

        for team in team_Points_1stQuarter_PerGame:
            index = team_Points_1stQuarter_PerGame.index(team)
            master_Dict[team]['points_1stQuarter_PerGame_List'] = points_1stQuarter_PerGame_List[index]

        for team in team_Points_2ndQuarter_PerGame:
            index = team_Points_2ndQuarter_PerGame.index(team)
            master_Dict[team]['points_2ndQuarter_PerGame_List'] = points_2ndQuarter_PerGame_List[index]
            
        for team in team_Points_3rdQuarter_PerGame:
            index = team_Points_3rdQuarter_PerGame.index(team)
            master_Dict[team]['points_3rdQuarter_PerGame_List'] = points_3rdQuarter_PerGame_List[index]
            
        for team in team_Points_4thQuarter_PerGame:
            index = team_Points_4thQuarter_PerGame.index(team)
            master_Dict[team]['points_4thQuarter_PerGame_List'] = points_4thQuarter_PerGame_List[index]
            
        for team in team_Avg_1stQuarter_Margin:
            index = team_Avg_1stQuarter_Margin.index(team)
            master_Dict[team]['avg_1stQuarter_Margin_List'] = avg_1stQuarter_Margin_List[index]
            
        for team in team_Avg_2ndQuarter_Margin:
            index = team_Avg_2ndQuarter_Margin.index(team)
            master_Dict[team]['avg_2ndQuarter_Margin_List'] = avg_2ndQuarter_Margin_List[index]
            
        for team in team_Avg_3rdQuarter_Margin:
            index = team_Avg_3rdQuarter_Margin.index(team)
            master_Dict[team]['avg_3rdQuarter_Margin_List'] = avg_3rdQuarter_Margin_List[index]
            
        for team in team_Avg_4thQuarter_Margin:
            index = team_Avg_4thQuarter_Margin.index(team)
            master_Dict[team]['avg_4thQuarter_Margin_List'] = avg_4thQuarter_Margin_List[index]
            
        for team in team_Points_2Pointers:
            index = team_Points_2Pointers.index(team)
            master_Dict[team]['points_2Pointers_List'] = points_2Pointers_List[index]
            
        for team in team_Points_3Pointers:
            index = team_Points_3Pointers.index(team)
            master_Dict[team]['points_3Pointers_List'] = points_3Pointers_List[index]
        
        
        for team, values in master_Dict.items():
            # SQL query to insert data into the team_winning_perc table
            sql = """
                INSERT INTO team_offensive_scoring
                (Team, points_PerGame, average_ScoreMargin, 1stQuarter_Points_PerGame, 2ndQuarter_Points_PerGame, 3rdQuarter_Points_PerGame, 4thQuarter_Points_PerGame, avg_1stQuarter_Margin, avg_2ndQuarter_Margin, avg_3rdQuarter_Margin, avg_4thQuarter_Margin, points_2Pointers, points_3Pointers)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                points_PerGame = VALUES(points_PerGame),
                average_ScoreMargin = VALUES(average_ScoreMargin),
                1stQuarter_Points_PerGame = VALUES(1stQuarter_Points_PerGame),
                2ndQuarter_Points_PerGame = VALUES(2ndQuarter_Points_PerGame),
                3rdQuarter_Points_PerGame = VALUES(3rdQuarter_Points_PerGame),
                4thQuarter_Points_PerGame = VALUES(4thQuarter_Points_PerGame),
                avg_1stQuarter_Margin = VALUES(avg_1stQuarter_Margin),
                avg_2ndQuarter_Margin = VALUES(avg_2ndQuarter_Margin),
                avg_3rdQuarter_Margin = VALUES(avg_3rdQuarter_Margin),
                avg_4thQuarter_Margin = VALUES(avg_4thQuarter_Margin),
                points_2Pointers = VALUES(points_2Pointers),
                points_3Pointers = VALUES(points_3Pointers)
                """

            # Data for the current iteration
            data = (
                team,
                values['points_PerGame_List'],
                values['average_ScoreMargin_List'],
                values['points_1stQuarter_PerGame_List'],
                values['points_2ndQuarter_PerGame_List'],
                values['points_3rdQuarter_PerGame_List'],
                values['points_4thQuarter_PerGame_List'],
                values['avg_1stQuarter_Margin_List'],
                values['avg_2ndQuarter_Margin_List'],
                values['avg_3rdQuarter_Margin_List'],
                values['avg_4thQuarter_Margin_List'],
                values['points_2Pointers_List'],
                values['points_3Pointers_List']
            )

            # Execute the SQL query
            cursor.execute(sql, data)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()     
        
        for driver in drivers:
            
            driver.close()
    
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_OffTeam_Scoring()

def supplyTable_NBA_TeamRoster():
    
    try:
        teamNames = ["boston-celtics", "brooklyn-nets", "new-york-knicks", "philadelphia-76ers", "toronto-raptors", "golden-state-warriors",
                    "la-clippers", "los-angeles-lakers", "phoenix-suns", "sacramento-kings", "chicago-bulls", "cleveland-cavaliers",
                    "detroit-pistons", "indiana-pacers", "milwaukee-bucks", "dallas-mavericks", "houston-rockets", "memphis-grizzlies",
                    "new-orleans-pelicans", "san-antonio-spurs", "atlanta-hawks", "charlotte-hornets", "miami-heat", "orlando-magic",
                    "washington-wizards", "denver-nuggets", "minnesota-timberwolves", "oklahoma-city-thunder", "portland-trail-blazers", "utah-jazz"]
        
        teamNames_Short = ["bos", "bkn", "ny", "phi", "tor", "gs",
                        "lac", "lal", "phx", "sac", "chi", "cle",
                        "det", "ind", "mil", "dal", "hou", "mem",
                        "no", "sa", "atl", "cha", "mia", "orl",
                        "wsh", "den", "min", "okc", "por", "utah"]
        
        conn = create_connection("nba_stats")
        
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
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1080, 1200)
        wait = WebDriverWait(driver, 10)
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        driver3 = webdriver.Chrome(options=chrome_options)
        
        
        # List of drivers
        drivers = [driver, driver2, driver3]  
        
        index_size = 3
        
        count = 0
        
        for i in range(0, len(teamNames), index_size):
            
             chunk = teamNames[i:i + index_size]
            
            # code to process the current chunk goes here
             for j, team in enumerate(chunk):
                
                player_Info = []
                
                # Use the corresponding driver instance for each QB
                current_driver = drivers[j]
                
                url = f"https://www.espn.com/nba/team/depth/_/name/{teamNames_Short[count]}/{team}"
                
                current_driver.get(url)
                
                # Get the html content from the webpage
                html_content = current_driver.page_source
                soup = BeautifulSoup(html_content, 'html.parser')
                
                row_counter = 0
                
                # col 0 = PG
                # col 1 = SG
                # col 2 = SF
                # col 3 = PF
                # col 4 = C
                
                table_Scroller = soup.find("div", class_="Table__Scroller")
                
                table_Body = table_Scroller.find("tbody", class_="Table__TBODY")
                
                rows = table_Body.find_all("tr", class_="Table__TR Table__TR--sm Table__even")
                
                for row in rows:
                    
                    if row_counter == 0:
                        
                        player_Names_Elements = row.find_all("a", class_="AnchorLink")
                        
                        string_count = 1
                        for player in player_Names_Elements:
                            
                            player_Info.append(["PG", player.text, string_count])
                            
                            string_count +=1
                            
                    elif row_counter == 1:
                        
                        player_Names_Elements = row.find_all("a", class_="AnchorLink")
                        
                        string_count = 1
                        for player in player_Names_Elements:
                            
                            player_Info.append(["SG", player.text, string_count])
                            
                            string_count +=1
                    
                    elif row_counter == 2:
                        
                        player_Names_Elements = row.find_all("a", class_="AnchorLink")
                        
                        string_count = 1
                        for player in player_Names_Elements:
                            
                            player_Info.append(["SF", player.text, string_count])
                            
                            string_count +=1  
                            
                    elif row_counter == 3:
                        
                        player_Names_Elements = row.find_all("a", class_="AnchorLink")
                        
                        string_count = 1
                        for player in player_Names_Elements:
                            
                            player_Info.append(["PF", player.text, string_count])
                            
                            string_count +=1   
                            
                    elif row_counter == 4:
                        
                        player_Names_Elements = row.find_all("a", class_="AnchorLink")
                        
                        string_count = 1
                        for player in player_Names_Elements:
                            
                            player_Info.append(["C", player.text, string_count])
                            
                            string_count +=1
                        
                    row_counter += 1
                
                
                teamName_SQL = teamNames_Short[count]
                count +=1
                cursor = conn.cursor() 

                # SQL query to drop table
                drop_table_query = f"DROP Table {teamName_SQL}_roster;"
                cursor.execute(drop_table_query) 
                
                # SQL query to check if the table exists
                check_table_query = f"SHOW TABLES LIKE '{teamName_SQL}_Roster';"
                cursor.execute(check_table_query)   

                # Fetch the result
                result = cursor.fetchone()    

                if not result:
                    # SQL query to create the table
                    create_table_query = f"""
                    CREATE TABLE `{teamName_SQL}_Roster` (
                        Position varchar(45),
                        Name varchar(45),
                        String int,
                        PRIMARY KEY (Position, Name)
                    );
                    """
                    
                    # Execute the query to create the table
                    cursor.execute(create_table_query)

                    # Commit the changes
                    conn.commit() 
                    
                # Now the list player_Info is ready to be inserted into the database

                # SQL query to insert or update records
                insert_update_query = f"""
                INSERT INTO `{teamName_SQL}_Roster` (Position, Name, String)
                VALUES (%(Position)s, %(Name)s, %(String)s)
                ON DUPLICATE KEY UPDATE
                    String = VALUES(String);
                """  

                # Execute the query with the data
                cursor.executemany(insert_update_query, [{'Position': position, 'Name': name, 'String': string} for position, name, string in player_Info])

                # Commit the changes
                conn.commit()

                # Close the cursor
                cursor.close()
                print(player_Info)    
                
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_NBA_TeamRoster()
   
def supplyTable_Player_ReboundsTotals():
    
    try:
        conn = create_connection("nba_stats")
        
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
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 10)
        wait = WebDriverWait(driver2, 10)
        
        
        # List of drivers
        drivers = [driver, driver2]
        
        playerNames_List = []
        gamesPlayed_List = []
        gamesStarted_List = []
        minutesPerGame_List = []
        offRebounds_List = []
        defRebounds_List = []
        totalRebounds_List = []
        reboundsPerGame_List = []
        
        i = 1
        j = 2
        
        
        while i <= 11:
            
            url_1 = f"https://www.cbssports.com/nba/stats/player/rebounds/nba/regular/all-pos/all/?page={i}&sortcol=gp&sortdir=descending"
            if j < 11:
                url_2 = f"https://www.cbssports.com/nba/stats/player/rebounds/nba/regular/all-pos/all/?page={j}&sortcol=gp&sortdir=descending"
            
            
            i += 2
            j += 2
            
            
            driver.get(url_1)
            if j < 11:
                driver2.get(url_2)
            print(url_1)
            print(url_2)
            wait.until(EC.presence_of_element_located((By.ID, 'TableBase')))
            
            
            html_content_1 = driver.page_source
            soup_1 = BeautifulSoup(html_content_1, 'html.parser')
            
            if j < 11:
                html_content_2 = driver2.page_source
                soup_2 = BeautifulSoup(html_content_2, 'html.parser')
            
            
            
            TableBase_1 = soup_1.find("div", id="TableBase")
            
            if j < 11:
                TableBase_2 = soup_2.find("div", id="TableBase")
            
            
            
            Table_TBody_1 = TableBase_1.find("tbody")
            
            if j < 11:
                Table_TBody_2 = TableBase_2.find("tbody")
            
            Table_Rows_1 = Table_TBody_1.find_all("tr", class_="TableBase-bodyTr")
            
            if j < 11:
                Table_Rows_2 = Table_TBody_2.find_all("tr", class_="TableBase-bodyTr")
            
            
            for row in Table_Rows_1:
                
                rowColumns = row.find_all("td")
                
                name_Column = rowColumns[0]
                gamesPlayed_Column = rowColumns[1]
                gamesStarted_Column = rowColumns[2]
                minutesPerGame_Column = rowColumns[3]
                OffRebounds_Column = rowColumns[4]
                DefRebounds_Column = rowColumns[5]
                totalRebounds_Column = rowColumns[6]
                reboundsPerGame_Column = rowColumns[7]
                
                name_Element = name_Column.find('span', class_="CellPlayerName--long")
                playerName = name_Element.find('a').text.strip()
                playerNames_List.append(playerName)
                
                gamesPlayed = gamesPlayed_Column.text.strip()
                gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                gamesPlayed_List.append(gamesPlayed)  
                
                gamesStarted = gamesStarted_Column.text.strip()
                gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                gamesStarted_List.append(gamesStarted)
                
                minutesPerGame = minutesPerGame_Column.text.strip()
                minutesPerGame = float(minutesPerGame.replace(" ", "").replace("—","0"))
                minutesPerGame_List.append(minutesPerGame)
                
                OffRebounds = OffRebounds_Column.text.strip()
                OffRebounds = int(OffRebounds.replace(" ", "").replace("—","0"))
                offRebounds_List.append(OffRebounds)
                
                DefRebounds = DefRebounds_Column.text.strip()
                DefRebounds = int(DefRebounds.replace(" ", "").replace("—","0"))
                defRebounds_List.append(DefRebounds)
                
                totalRebounds = totalRebounds_Column.text.strip()
                totalRebounds = int(totalRebounds.replace(" ", "").replace("—","0"))
                totalRebounds_List.append(totalRebounds)
                
                reboundsPerGame = reboundsPerGame_Column.text.strip()
                reboundsPerGame = float(reboundsPerGame.replace(" ", "").replace("—","0"))
                reboundsPerGame_List.append(reboundsPerGame)
            
            if j < 11:   
                for row in Table_Rows_2:
                
                    rowColumns = row.find_all("td")
                    
                    name_Column = rowColumns[0]
                    gamesPlayed_Column = rowColumns[1]
                    gamesStarted_Column = rowColumns[2]
                    minutesPerGame_Column = rowColumns[3]
                    OffRebounds_Column = rowColumns[4]
                    DefRebounds_Column = rowColumns[5]
                    totalRebounds_Column = rowColumns[6]
                    reboundsPerGame_Column = rowColumns[7]
                    
                    name_Element = name_Column.find('span', class_="CellPlayerName--long")
                    playerName = name_Element.find('a').text.strip()
                    playerNames_List.append(playerName)
                    
                    gamesPlayed = gamesPlayed_Column.text.strip()
                    gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                    gamesPlayed_List.append(gamesPlayed)  
                    
                    gamesStarted = gamesStarted_Column.text.strip()
                    gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                    gamesStarted_List.append(gamesStarted)
                    
                    minutesPerGame = minutesPerGame_Column.text.strip()
                    minutesPerGame = float(minutesPerGame.replace(" ", "").replace("—","0"))
                    minutesPerGame_List.append(minutesPerGame)
                    
                    OffRebounds = OffRebounds_Column.text.strip()
                    OffRebounds = int(OffRebounds.replace(" ", "").replace("—","0"))
                    offRebounds_List.append(OffRebounds)
                    
                    DefRebounds = DefRebounds_Column.text.strip()
                    DefRebounds = int(DefRebounds.replace(" ", "").replace("—","0"))
                    defRebounds_List.append(DefRebounds)
                    
                    totalRebounds = totalRebounds_Column.text.strip()
                    totalRebounds = int(totalRebounds.replace(" ", "").replace("—","0"))
                    totalRebounds_List.append(totalRebounds)
                    
                    reboundsPerGame = reboundsPerGame_Column.text.strip()
                    reboundsPerGame = float(reboundsPerGame.replace(" ", "").replace("—","0"))
                    reboundsPerGame_List.append(reboundsPerGame)
            
            
            
        for i in range(len(playerNames_List)):
        # SQL query to insert data into the player_scoring_totals table
            sql = """
                INSERT INTO player_rebounds_totals 
                (Name, GamesPlayed, GamesStarted, MinutesPerGame, OffRebounds, DefRebounds,
                TotalRebounds,ReboundsPerGame)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                Name = VALUES(Name),
                GamesPlayed = VALUES(GamesPlayed),
                GamesStarted = VALUES(GamesStarted),
                MinutesPerGame = VALUES(MinutesPerGame),
                OffRebounds = VALUES(OffRebounds),
                DefRebounds = VALUES(DefRebounds),
                TotalRebounds = VALUES(TotalRebounds),
                ReboundsPerGame = VALUES(ReboundsPerGame)
                """
                    
            # Data for the current iteration
            data = (
                playerNames_List[i],
                gamesPlayed_List[i],
                gamesStarted_List[i],
                minutesPerGame_List[i],
                offRebounds_List[i],
                defRebounds_List[i],
                totalRebounds_List[i],
                reboundsPerGame_List[i]
            )

            # Execute the SQL query
            cursor.execute(sql, data) 
                
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
            
        for driver in drivers:
                
            driver.close()
        
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_Player_ReboundsTotals()  
 
def supplyTable_Player_AssistsAndTurnovers():
    
    try:
        conn = create_connection("nba_stats")
        
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
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        
        
        # List of drivers
        drivers = [driver, driver2]
        
        playerNames_List = []
        gamesPlayed_List = []
        gamesStarted_List = []
        totalAssists_List = []
        assistsPerGame_List = []
        turnovers_List = []
        turnoversPerGame_List = []
        assistsPerTurnovers_List = []
        
        i = 1
        j = 2
        
        
        while i <= 11:
            
            url_1 = f"https://www.cbssports.com/nba/stats/player/assists-turnovers/nba/regular/all-pos/all/?page={i}"
            if j < 11:
                url_2 = f"https://www.cbssports.com/nba/stats/player/assists-turnovers/nba/regular/all-pos/all/?page={j}"
            
            i += 2
            j += 2
            
            
            driver.get(url_1)
            
            if j < 11:
                driver2.get(url_2)
            
                
            time.sleep(10)
            
            html_content_1 = driver.page_source
            soup_1 = BeautifulSoup(html_content_1, 'html.parser')
            
            if j < 11:
                html_content_2 = driver2.page_source
                soup_2 = BeautifulSoup(html_content_2, 'html.parser')
            
            
            
            TableBase_1 = soup_1.find("div", id="TableBase")
            if j < 11:
                TableBase_2 = soup_2.find("div", id="TableBase")
            
            
            Table_TBody_1 = TableBase_1.find("tbody")
            if j < 11:
                Table_TBody_2 = TableBase_2.find("tbody")
            
            
            Table_Rows_1 = Table_TBody_1.find_all("tr", class_="TableBase-bodyTr")
            if j < 11:
                Table_Rows_2 = Table_TBody_2.find_all("tr", class_="TableBase-bodyTr")
            
            
            for row in Table_Rows_1:
                
                rowColumns = row.find_all("td")
                
                name_Column = rowColumns[0]
                gamesPlayed_Column = rowColumns[1]
                gamesStarted_Column = rowColumns[2]
                totalAssists_Column = rowColumns[3]
                assistsPerGame_Column = rowColumns[4]
                turnovers_Column = rowColumns[5]
                turnoversPerGame_Column = rowColumns[6]
                assistsPerTurnovers_Column = rowColumns[7]
                
                
                name_Element = name_Column.find('span', class_="CellPlayerName--long")
                playerName = name_Element.find('a').text.strip()
                playerNames_List.append(playerName)
                
                gamesPlayed = gamesPlayed_Column.text.strip()
                gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                gamesPlayed_List.append(gamesPlayed)  
                
                gamesStarted = gamesStarted_Column.text.strip()
                gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                gamesStarted_List.append(gamesStarted)
                
                totalAssists = totalAssists_Column.text.strip()
                totalAssists = int(totalAssists.replace(" ", "").replace("—","0"))
                totalAssists_List.append(totalAssists)
                
                assistsPerGame = assistsPerGame_Column.text.strip()
                assistsPerGame = float(assistsPerGame.replace(" ", "").replace("—","0"))
                assistsPerGame_List.append(assistsPerGame)
                
                turnovers = turnovers_Column.text.strip()
                turnovers = int(turnovers.replace(" ", "").replace("—","0"))
                turnovers_List.append(turnovers)
                
                turnoversPerGame = turnoversPerGame_Column.text.strip()
                turnoversPerGame = float(turnoversPerGame.replace(" ", "").replace("—","0"))
                turnoversPerGame_List.append(turnoversPerGame)
                
                assistsPerTurnovers = assistsPerTurnovers_Column.text.strip()
                assistsPerTurnovers = float(assistsPerTurnovers.replace(" ", "").replace("—","0"))
                assistsPerTurnovers_List.append(assistsPerTurnovers)
            
            if j < 11:
                
                for row in Table_Rows_2:
                    
                    rowColumns = row.find_all("td")
                    
                    name_Column = rowColumns[0]
                    gamesPlayed_Column = rowColumns[1]
                    gamesStarted_Column = rowColumns[2]
                    totalAssists_Column = rowColumns[3]
                    assistsPerGame_Column = rowColumns[4]
                    turnovers_Column = rowColumns[5]
                    turnoversPerGame_Column = rowColumns[6]
                    assistsPerTurnovers_Column = rowColumns[7]
                    
                    
                    name_Element = name_Column.find('span', class_="CellPlayerName--long")
                    playerName = name_Element.find('a').text.strip()
                    playerNames_List.append(playerName)
                    
                    gamesPlayed = gamesPlayed_Column.text.strip()
                    gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                    gamesPlayed_List.append(gamesPlayed)  
                    
                    gamesStarted = gamesStarted_Column.text.strip()
                    gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                    gamesStarted_List.append(gamesStarted)
                    
                    totalAssists = totalAssists_Column.text.strip()
                    totalAssists = int(totalAssists.replace(" ", "").replace("—","0"))
                    totalAssists_List.append(totalAssists)
                    
                    assistsPerGame = assistsPerGame_Column.text.strip()
                    assistsPerGame = float(assistsPerGame.replace(" ", "").replace("—","0"))
                    assistsPerGame_List.append(assistsPerGame)
                    
                    turnovers = turnovers_Column.text.strip()
                    turnovers = int(turnovers.replace(" ", "").replace("—","0"))
                    turnovers_List.append(turnovers)
                    
                    turnoversPerGame = turnoversPerGame_Column.text.strip()
                    turnoversPerGame = float(turnoversPerGame.replace(" ", "").replace("—","0"))
                    turnoversPerGame_List.append(turnoversPerGame)
                    
                    assistsPerTurnovers = assistsPerTurnovers_Column.text.strip()
                    assistsPerTurnovers = float(assistsPerTurnovers.replace(" ", "").replace("—","0"))
                    assistsPerTurnovers_List.append(assistsPerTurnovers)
            
                
        for i in range(len(playerNames_List)):
        # SQL query to insert data into the player_scoring_totals table
            sql = """
                INSERT INTO player_assists_turnovers_totals
                (Name, GamesPlayed, GamesStarted, TotalAssists, AssistsPerGame, Turnovers, TurnoversPerGame,
                AssistsPerTurnover)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                Name = VALUES(Name),
                GamesPlayed = VALUES(GamesPlayed),
                GamesStarted = VALUES(GamesStarted),
                TotalAssists = VALUES(TotalAssists),
                AssistsPerGame = VALUES(AssistsPerGame),
                Turnovers = VALUES(Turnovers),
                TurnoversPerGame = VALUES(TurnoversPerGame),
                AssistsPerTurnover = VALUES(AssistsPerTurnover)
                """
                    
            # Data for the current iteration
            data = (
                playerNames_List[i],
                gamesPlayed_List[i],
                gamesStarted_List[i],
                totalAssists_List[i],
                assistsPerGame_List[i],
                turnovers_List[i],
                turnoversPerGame_List[i],
                assistsPerTurnovers_List[i]
            )

            
            # Execute the SQL query
            cursor.execute(sql, data) 
                
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
            
        for driver in drivers:
                
            driver.close()
        
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        
        try:
            supplyTable_Player_AssistsAndTurnovers()
            
        except TimeoutException as e:
            
            print(f"Caught TimeoutException (2): {e}")
    
def supplyTable_Player_Blocks():
    
    try:
        conn = create_connection("nba_stats")
        
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
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        
        
        # List of drivers
        drivers = [driver, driver2] 
        
        playerNames_List = []
        gamesPlayed_List = []
        gamesStarted_List = []
        blocks_List = []
        blocksPerGame_List = []
        
        i = 1
        j = 2
        
        
        while i <= 11:
            
            url_1 = f"https://www.cbssports.com/nba/stats/player/blocks/nba/regular/all-pos/all/?page={i}"
            url_2 = f"https://www.cbssports.com/nba/stats/player/blocks/nba/regular/all-pos/all/?page={j}"
            
            
            i += 2
            j += 2
            
            
            driver.get(url_1)
            if j < 11:
                driver2.get(url_2)
            
                
            time.sleep(10)
            
            html_content_1 = driver.page_source
            soup_1 = BeautifulSoup(html_content_1, 'html.parser')
            
            if j < 11:
                html_content_2 = driver2.page_source
                soup_2 = BeautifulSoup(html_content_2, 'html.parser')
            
            
            
            TableBase_1 = soup_1.find("div", id="TableBase")
            
            if j < 11:
                TableBase_2 = soup_2.find("div", id="TableBase")
            
            
            
            Table_TBody_1 = TableBase_1.find("tbody")
            if j < 11:
                Table_TBody_2 = TableBase_2.find("tbody")
            
            Table_Rows_1 = Table_TBody_1.find_all("tr", class_="TableBase-bodyTr")
            
            if j < 11:
                Table_Rows_2 = Table_TBody_2.find_all("tr", class_="TableBase-bodyTr")
            
                
            for row in Table_Rows_1:
                
                rowColumns = row.find_all("td")
            
                name_Column = rowColumns[0]
                gamesPlayed_Column = rowColumns[1]
                gamesStarted_Column = rowColumns[2]
                blocks_Column = rowColumns[3]
                blocksPerGame_Column = rowColumns[4]
                
                name_Element = name_Column.find('span', class_="CellPlayerName--long")
                playerName = name_Element.find('a').text.strip()
                playerNames_List.append(playerName)
                
                gamesPlayed = gamesPlayed_Column.text.strip()
                gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                gamesPlayed_List.append(gamesPlayed)  
                
                gamesStarted = gamesStarted_Column.text.strip()
                gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                gamesStarted_List.append(gamesStarted)
                
                blocks = blocks_Column.text.strip()
                blocks = int(blocks.replace(" ", "").replace("—","0"))
                blocks_List.append(blocks)
                
                blocksPerGame = blocksPerGame_Column.text.strip()
                blocksPerGame = float(blocksPerGame.replace(" ", "").replace("—","0"))
                blocksPerGame_List.append(blocksPerGame)
            
            if j < 11:    
                for row in Table_Rows_2:
                    
                    rowColumns = row.find_all("td")
                
                    name_Column = rowColumns[0]
                    gamesPlayed_Column = rowColumns[1]
                    gamesStarted_Column = rowColumns[2]
                    blocks_Column = rowColumns[3]
                    blocksPerGame_Column = rowColumns[4]
                    
                    name_Element = name_Column.find('span', class_="CellPlayerName--long")
                    playerName = name_Element.find('a').text.strip()
                    playerNames_List.append(playerName)
                    
                    gamesPlayed = gamesPlayed_Column.text.strip()
                    gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                    gamesPlayed_List.append(gamesPlayed)  
                    
                    gamesStarted = gamesStarted_Column.text.strip()
                    gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                    gamesStarted_List.append(gamesStarted)
                    
                    blocks = blocks_Column.text.strip()
                    blocks = int(blocks.replace(" ", "").replace("—","0"))
                    blocks_List.append(blocks)
                    
                    blocksPerGame = blocksPerGame_Column.text.strip()
                    blocksPerGame = float(blocksPerGame.replace(" ", "").replace("—","0"))
                    blocksPerGame_List.append(blocksPerGame)
                

                    
        for i in range(len(playerNames_List)):
        # SQL query to insert data into the player_scoring_totals table
            sql = """
                INSERT INTO player_blocks_totals
                (Name, GamesPlayed, GamesStarted, Blocks, BlocksPerGame)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                Name = VALUES(Name),
                GamesPlayed = VALUES(GamesPlayed),
                GamesStarted = VALUES(GamesStarted),
                Blocks = VALUES(Blocks),
                BlocksPerGame = VALUES(BlocksPerGame)
                """
                    
            # Data for the current iteration
            data = (
                playerNames_List[i],
                gamesPlayed_List[i],
                gamesStarted_List[i],
                blocks_List[i],
                blocksPerGame_List[i]
            )

            
            # Execute the SQL query
            cursor.execute(sql, data) 
                
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
            
        for driver in drivers:
                
            driver.close()  
        
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_Player_Blocks()  
 
def supplyTable_Player_Fouls():
    
    try:
        conn = create_connection("nba_stats")
        
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
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        
        
        # List of drivers
        drivers = [driver, driver2] 
        
        playerNames_List = []
        gamesPlayed_List = []
        gamesStarted_List = []
        minutesPerGame_List = []
        totalPersonalFouls_List = []
        personalFoulsPerGame_List = []
        totalFlagrantFouls_List = []
        totalTechnicalFouls_List = []
        totalEjections_List = []
        disqualifications_List = []
    
        
        i = 1
        j = 2
        
        
        while i <= 11:
            
            url_1 = f"https://www.cbssports.com/nba/stats/player/fouls-minutes/nba/regular/all-pos/all/?page={i}"
            url_2 = f"https://www.cbssports.com/nba/stats/player/fouls-minutes/nba/regular/all-pos/all/?page={j}"
            
            i += 2
            j += 2
            
            
            driver.get(url_1)
            
            if j < 11:
                driver2.get(url_2)
            
            
            time.sleep(10)
            
            html_content_1 = driver.page_source
            soup_1 = BeautifulSoup(html_content_1, 'html.parser')
            
            if j < 11:
                html_content_2 = driver2.page_source
                soup_2 = BeautifulSoup(html_content_2, 'html.parser')
            
            
            TableBase_1 = soup_1.find("div", id="TableBase")
            
            if j < 11:
                TableBase_2 = soup_2.find("div", id="TableBase")
            
            Table_TBody_1 = TableBase_1.find("tbody")
            
            if j < 11:
                Table_TBody_2 = TableBase_2.find("tbody")
            
            Table_Rows_1 = Table_TBody_1.find_all("tr", class_="TableBase-bodyTr")
            
            if j < 11:
                Table_Rows_2 = Table_TBody_2.find_all("tr", class_="TableBase-bodyTr")

            for row in Table_Rows_1:
                
                rowColumns = row.find_all("td")
                
                name_Column = rowColumns[0]
                gamesPlayed_Column = rowColumns[1]
                gamesStarted_Column = rowColumns[2]
                minutesPerGame_Column = rowColumns[3]
                totalPersonalFouls_Column = rowColumns[4]
                personalFoulsPerGame_Column = rowColumns[5]
                totalFlagrantFouls_Column = rowColumns[6]
                totalTechnicalFouls_Column = rowColumns[7]
                totalEjections_Column = rowColumns[8]
                disqualifications_Column = rowColumns[9]
                
                name_Element = name_Column.find('span', class_="CellPlayerName--long")
                playerName = name_Element.find('a').text.strip()
                playerNames_List.append(playerName)
                
                gamesPlayed = gamesPlayed_Column.text.strip()
                gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                gamesPlayed_List.append(gamesPlayed)  
                
                gamesStarted = gamesStarted_Column.text.strip()
                gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                gamesStarted_List.append(gamesStarted)
                
                minutesPerGame = minutesPerGame_Column.text.strip()
                minutesPerGame = float(minutesPerGame.replace(" ", "").replace("—","0"))
                minutesPerGame_List.append(minutesPerGame)
                
                totalPersonalFouls = totalPersonalFouls_Column.text.strip()
                totalPersonalFouls = int(totalPersonalFouls.replace(" ", "").replace("—","0"))
                totalPersonalFouls_List.append(totalPersonalFouls)
                
                personalFoulsPerGame = personalFoulsPerGame_Column.text.strip()
                personalFoulsPerGame = float(personalFoulsPerGame.replace(" ", "").replace("—","0"))
                personalFoulsPerGame_List.append(personalFoulsPerGame)
                
                totalFlagrantFouls = totalFlagrantFouls_Column.text.strip()
                totalFlagrantFouls = int(totalFlagrantFouls.replace(" ", "").replace("—","0"))
                totalFlagrantFouls_List.append(totalFlagrantFouls)
                
                totalTechnicalFouls = totalTechnicalFouls_Column.text.strip()
                totalTechnicalFouls = int(totalTechnicalFouls.replace(" ", "").replace("—","0"))
                totalTechnicalFouls_List.append(totalTechnicalFouls)
                
                totalEjections = totalEjections_Column.text.strip()
                totalEjections = int(totalEjections.replace(" ", "").replace("—","0"))
                totalEjections_List.append(totalEjections)
                
                disqualifications = disqualifications_Column.text.strip()
                disqualifications = int(disqualifications.replace(" ", "").replace("—","0"))
                disqualifications_List.append(disqualifications)
            
            if j < 11:    
                for row in Table_Rows_2:
                    
                    rowColumns = row.find_all("td")
                    
                    name_Column = rowColumns[0]
                    gamesPlayed_Column = rowColumns[1]
                    gamesStarted_Column = rowColumns[2]
                    minutesPerGame_Column = rowColumns[3]
                    totalPersonalFouls_Column = rowColumns[4]
                    personalFoulsPerGame_Column = rowColumns[5]
                    totalFlagrantFouls_Column = rowColumns[6]
                    totalTechnicalFouls_Column = rowColumns[7]
                    totalEjections_Column = rowColumns[8]
                    disqualifications_Column = rowColumns[9]
                    
                    name_Element = name_Column.find('span', class_="CellPlayerName--long")
                    playerName = name_Element.find('a').text.strip()
                    playerNames_List.append(playerName)
                    
                    gamesPlayed = gamesPlayed_Column.text.strip()
                    gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                    gamesPlayed_List.append(gamesPlayed)  
                    
                    gamesStarted = gamesStarted_Column.text.strip()
                    gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                    gamesStarted_List.append(gamesStarted)
                    
                    minutesPerGame = minutesPerGame_Column.text.strip()
                    minutesPerGame = float(minutesPerGame.replace(" ", "").replace("—","0"))
                    minutesPerGame_List.append(minutesPerGame)
                    
                    totalPersonalFouls = totalPersonalFouls_Column.text.strip()
                    totalPersonalFouls = int(totalPersonalFouls.replace(" ", "").replace("—","0"))
                    totalPersonalFouls_List.append(totalPersonalFouls)
                    
                    personalFoulsPerGame = personalFoulsPerGame_Column.text.strip()
                    personalFoulsPerGame = float(personalFoulsPerGame.replace(" ", "").replace("—","0"))
                    personalFoulsPerGame_List.append(personalFoulsPerGame)
                    
                    totalFlagrantFouls = totalFlagrantFouls_Column.text.strip()
                    totalFlagrantFouls = int(totalFlagrantFouls.replace(" ", "").replace("—","0"))
                    totalFlagrantFouls_List.append(totalFlagrantFouls)
                    
                    totalTechnicalFouls = totalTechnicalFouls_Column.text.strip()
                    totalTechnicalFouls = int(totalTechnicalFouls.replace(" ", "").replace("—","0"))
                    totalTechnicalFouls_List.append(totalTechnicalFouls)
                    
                    totalEjections = totalEjections_Column.text.strip()
                    totalEjections = int(totalEjections.replace(" ", "").replace("—","0"))
                    totalEjections_List.append(totalEjections)
                    
                    disqualifications = disqualifications_Column.text.strip()
                    disqualifications = int(disqualifications.replace(" ", "").replace("—","0"))
                    disqualifications_List.append(disqualifications)
                
                    
        for i in range(len(playerNames_List)):
            # SQL query to insert data into the player_scoring_totals table
            sql = """
                INSERT INTO player_fouls_total
                (Name, GamesPlayed, GamesStarted, MinutesPerGame, PersonalFouls, 
                PersonalFoulsPerGame, FlagrantFouls, TechnicalFouls, Ejections, Disqualifications)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                Name = VALUES(Name),
                GamesPlayed = VALUES(GamesPlayed),
                GamesStarted = VALUES(GamesStarted),
                MinutesPerGame = VALUES(MinutesPerGame),
                PersonalFouls = VALUES(PersonalFouls),
                PersonalFoulsPerGame = VALUES(PersonalFoulsPerGame),
                FlagrantFouls = VALUES(FlagrantFouls),
                TechnicalFouls = VALUES(TechnicalFouls),
                Ejections = VALUES(Ejections),
                Disqualifications = VALUES(Disqualifications)
                """
                    
            # Data for the current iteration
            data = (
                playerNames_List[i],
                gamesPlayed_List[i],
                gamesStarted_List[i],
                minutesPerGame_List[i],
                totalPersonalFouls_List[i],
                personalFoulsPerGame_List[i],
                totalFlagrantFouls_List[i],
                totalTechnicalFouls_List[i],
                totalEjections_List[i],
                disqualifications_List[i]
                
            )

        
            # Execute the SQL query
            cursor.execute(sql, data)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
            
        for driver in drivers:
                
            driver.close() 
        
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_Player_Fouls()    
 
def supplyTable_Player_ScoringTotals():
    
    try:
        conn = create_connection("nba_stats")
        
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
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver2 = webdriver.Chrome(options=chrome_options)
        
        
        # List of drivers
        drivers = [driver, driver2] 
        
        playerNames_List = []
        gamesPlayed_List = []
        gamesStarted_List = []
        minutesPerGame_List = []
        pointsPerGame_List = []
        fieldGoalsMade_List = []
        fieldGoalsAttempted_List = []
        fieldGoalPerc_List = []
        threePointersMade_List = []
        threePointersAttempted_List = []
        threePointerPerc_List = []
        freeThrowsMade_List = []
        freeThrowsAttempted_List = []
        freeThrowPerc_List = []
        
        
        i = 1
        j = 2
        
        
        while i <= 11:
            
            url_1 = f"https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/all/?page={i}&sortcol=gp&sortdir=descending"
            if j < 11:
                url_2 = f"https://www.cbssports.com/nba/stats/player/scoring/nba/regular/all-pos/all/?page={j}&sortcol=gp&sortdir=descending"
            
            
            i += 2
            j += 2
            
            driver.get(url_1)
            
            if j < 11:
                driver2.get(url_2)
            
            time.sleep(10)
            
            html_content_1 = driver.page_source
            soup_1 = BeautifulSoup(html_content_1, 'html.parser')
            
            if j < 11:
                html_content_2 = driver2.page_source
                soup_2 = BeautifulSoup(html_content_2, 'html.parser')
            
            
            TableBase_1 = soup_1.find("div", id="TableBase")
            
            if j < 11:
                TableBase_2 = soup_2.find("div", id="TableBase")
            
            
            Table_TBody_1 = TableBase_1.find("tbody")
            
            if j < 11:
                Table_TBody_2 = TableBase_2.find("tbody")

            
            Table_Rows_1 = Table_TBody_1.find_all("tr", class_="TableBase-bodyTr")
            
            if j < 11:
                Table_Rows_2 = Table_TBody_2.find_all("tr", class_="TableBase-bodyTr")
            
            for row in Table_Rows_1:
                
                rowColumns = row.find_all("td")
            
                name_Column = rowColumns[0]
                gamesPlayed_Column = rowColumns[1]
                gamesStarted_Column = rowColumns[2]
                minutesPerGame_Column = rowColumns[3]
                pointsPerGame_Column = rowColumns[4]
                fieldGoalsMade_Column = rowColumns[5]
                fieldGoalsAttempted_Column = rowColumns[6]
                fieldGoalPerc_Column = rowColumns[7]
                threePointersMade_Column = rowColumns[8]
                threePointersAttempted_Column = rowColumns[9]
                threePointerPerc_Column = rowColumns[10]
                freeThrowMade_Column = rowColumns[11]
                freeThrowAttempted_Column = rowColumns[12]
                freeThrowPerc_Column = rowColumns[13]
                
                name_Element = name_Column.find('span', class_="CellPlayerName--long")
                playerName = name_Element.find('a').text.strip()
                playerNames_List.append(playerName)
                
                gamesPlayed = gamesPlayed_Column.text.strip()
                gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                gamesPlayed_List.append(gamesPlayed)  
                
                gamesStarted = gamesStarted_Column.text.strip()
                gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                gamesStarted_List.append(gamesStarted)
                
                minutesPerGame = minutesPerGame_Column.text.strip()
                minutesPerGame = float(minutesPerGame.replace(" ", "").replace("—","0"))
                minutesPerGame_List.append(minutesPerGame)
                
                pointsPerGame = pointsPerGame_Column.text.strip()
                pointsPerGame = float(pointsPerGame.replace(" ", "").replace("—","0"))
                pointsPerGame_List.append(pointsPerGame)
                
                fieldGoalsMade = fieldGoalsMade_Column.text.strip()
                fieldGoalsMade = int(fieldGoalsMade.replace(" ", "").replace("—","0"))
                fieldGoalsMade_List.append(fieldGoalsMade)
                
                fieldGoalsAttempted = fieldGoalsAttempted_Column.text.strip()
                fieldGoalsAttempted = int(fieldGoalsAttempted.replace(" ", "").replace("—","0"))
                fieldGoalsAttempted_List.append(fieldGoalsAttempted)
                
                fieldGoalPerc = fieldGoalPerc_Column.text.strip()
                fieldGoalPerc = float(fieldGoalPerc.replace(" ", "").replace("—","0"))
                fieldGoalPerc_List.append(fieldGoalPerc)
                
                threePointersMade = threePointersMade_Column.text.strip()
                threePointersMade = int(threePointersMade.replace(" ", "").replace("—","0"))
                threePointersMade_List.append(threePointersMade)
                
                threePointersAttempted = threePointersAttempted_Column.text.strip()
                threePointersAttempted = int(threePointersAttempted.replace(" ", "").replace("—","0"))
                threePointersAttempted_List.append(threePointersAttempted)
                
                threePointerPerc = threePointerPerc_Column.text.strip()
                threePointerPerc = float(threePointerPerc.replace(" ", "").replace("—","0"))
                threePointerPerc_List.append(threePointerPerc)
                
                freeThrowMade = freeThrowMade_Column.text.strip()
                freeThrowMade = int(freeThrowMade.replace(" ", "").replace("—","0"))
                freeThrowsMade_List.append(freeThrowMade)
                
                freeThrowAttempted = freeThrowAttempted_Column.text.strip()
                freeThrowAttempted = int(freeThrowAttempted.replace(" ", "").replace("—","0"))
                freeThrowsAttempted_List.append(freeThrowAttempted)
                
                freeThrowPerc = freeThrowPerc_Column.text.strip()
                freeThrowPerc = float(freeThrowPerc.replace(" ", "").replace("—","0"))
                freeThrowPerc_List.append(freeThrowPerc)
            
            if j < 11:    
                for row in Table_Rows_2:
                    
                    rowColumns = row.find_all("td")
                
                    name_Column = rowColumns[0]
                    gamesPlayed_Column = rowColumns[1]
                    gamesStarted_Column = rowColumns[2]
                    minutesPerGame_Column = rowColumns[3]
                    pointsPerGame_Column = rowColumns[4]
                    fieldGoalsMade_Column = rowColumns[5]
                    fieldGoalsAttempted_Column = rowColumns[6]
                    fieldGoalPerc_Column = rowColumns[7]
                    threePointersMade_Column = rowColumns[8]
                    threePointersAttempted_Column = rowColumns[9]
                    threePointerPerc_Column = rowColumns[10]
                    freeThrowMade_Column = rowColumns[11]
                    freeThrowAttempted_Column = rowColumns[12]
                    freeThrowPerc_Column = rowColumns[13]
                    
                    name_Element = name_Column.find('span', class_="CellPlayerName--long")
                    playerName = name_Element.find('a').text.strip()
                    playerNames_List.append(playerName)
                    
                    gamesPlayed = gamesPlayed_Column.text.strip()
                    gamesPlayed = int(gamesPlayed.replace(" ", "").replace("—","0"))       
                    gamesPlayed_List.append(gamesPlayed)  
                    
                    gamesStarted = gamesStarted_Column.text.strip()
                    gamesStarted = int(gamesStarted.replace(" ", "").replace("—","0"))
                    gamesStarted_List.append(gamesStarted)
                    
                    minutesPerGame = minutesPerGame_Column.text.strip()
                    minutesPerGame = float(minutesPerGame.replace(" ", "").replace("—","0"))
                    minutesPerGame_List.append(minutesPerGame)
                    
                    pointsPerGame = pointsPerGame_Column.text.strip()
                    pointsPerGame = float(pointsPerGame.replace(" ", "").replace("—","0"))
                    pointsPerGame_List.append(pointsPerGame)
                    
                    fieldGoalsMade = fieldGoalsMade_Column.text.strip()
                    fieldGoalsMade = int(fieldGoalsMade.replace(" ", "").replace("—","0"))
                    fieldGoalsMade_List.append(fieldGoalsMade)
                    
                    fieldGoalsAttempted = fieldGoalsAttempted_Column.text.strip()
                    fieldGoalsAttempted = int(fieldGoalsAttempted.replace(" ", "").replace("—","0"))
                    fieldGoalsAttempted_List.append(fieldGoalsAttempted)
                    
                    fieldGoalPerc = fieldGoalPerc_Column.text.strip()
                    fieldGoalPerc = float(fieldGoalPerc.replace(" ", "").replace("—","0"))
                    fieldGoalPerc_List.append(fieldGoalPerc)
                    
                    threePointersMade = threePointersMade_Column.text.strip()
                    threePointersMade = int(threePointersMade.replace(" ", "").replace("—","0"))
                    threePointersMade_List.append(threePointersMade)
                    
                    threePointersAttempted = threePointersAttempted_Column.text.strip()
                    threePointersAttempted = int(threePointersAttempted.replace(" ", "").replace("—","0"))
                    threePointersAttempted_List.append(threePointersAttempted)
                    
                    threePointerPerc = threePointerPerc_Column.text.strip()
                    threePointerPerc = float(threePointerPerc.replace(" ", "").replace("—","0"))
                    threePointerPerc_List.append(threePointerPerc)
                    
                    freeThrowMade = freeThrowMade_Column.text.strip()
                    freeThrowMade = int(freeThrowMade.replace(" ", "").replace("—","0"))
                    freeThrowsMade_List.append(freeThrowMade)
                    
                    freeThrowAttempted = freeThrowAttempted_Column.text.strip()
                    freeThrowAttempted = int(freeThrowAttempted.replace(" ", "").replace("—","0"))
                    freeThrowsAttempted_List.append(freeThrowAttempted)
                    
                    freeThrowPerc = freeThrowPerc_Column.text.strip()
                    freeThrowPerc = float(freeThrowPerc.replace(" ", "").replace("—","0"))
                    freeThrowPerc_List.append(freeThrowPerc)
                
                
        for i in range(len(playerNames_List)):
            # SQL query to insert data into the player_scoring_totals table
            sql = """
                INSERT INTO player_scoring_totals 
                (Name, GamesPlayed, GamesStarted, MinutesPerGame, PointsPerGame, 
                FieldGoalsMade, FieldGoalsAttempted, FieldGoalPerc, ThreePointersMade, 
                ThreePointersAttempted, ThreePointerPerc, FreeThrowsMade, 
                FreeThrowsAttempted, FreeThrowPerc)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                Name = VALUES(Name),
                GamesPlayed = VALUES(GamesPlayed),
                GamesStarted = VALUES(GamesStarted),
                MinutesPerGame = VALUES(MinutesPerGame),
                PointsPerGame = VALUES(PointsPerGame),
                FieldGoalsMade = VALUES(FieldGoalsMade),
                FieldGoalsAttempted = VALUES(FieldGoalsAttempted),
                FieldGoalPerc = VALUES(FieldGoalPerc),
                ThreePointersMade = VALUES(ThreePointersMade),
                ThreePointersAttempted = VALUES(ThreePointersAttempted),
                ThreePointerPerc = VALUES(ThreePointerPerc),
                FreeThrowsMade = VALUES(FreeThrowsMade),
                FreeThrowsAttempted = VALUES(FreeThrowsAttempted),
                FreeThrowPerc = VALUES(FreeThrowPerc)
                """
                    
            # Data for the current iteration
            data = (
                playerNames_List[i],
                gamesPlayed_List[i],
                gamesStarted_List[i],
                minutesPerGame_List[i],
                pointsPerGame_List[i],
                fieldGoalsMade_List[i],
                fieldGoalsAttempted_List[i],
                fieldGoalPerc_List[i],
                threePointersMade_List[i],
                threePointersAttempted_List[i],
                threePointerPerc_List[i],
                freeThrowsMade_List[i],
                freeThrowsAttempted_List[i],
                freeThrowPerc_List[i]
            )

            # Execute the SQL query
            cursor.execute(sql, data)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
            
        for driver in drivers:
                
            driver.close()
        
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_Player_ScoringTotals() 

def supplyTable_NBAPlayer_GameLogs(name):
    
    try:
        
        dates_List = []
        opp_List = []
        result_List = []
        WL_List = []
        min_List = []
        fieldGoals_Made_List = []
        fieldGoals_Attempted_List = []
        fieldGoal_Perc_List = []
        threePointers_Made_List = []
        threePointers_Attempted_List = []
        threePointer_Perc_List = []
        freeThrows_Made_List = []
        freeThrows_Attempted_List = []
        freeThrow_Perc_List = []
        rebounds_List = []
        assists_List = []
        blocks_List = []
        steals_List = []
        fouls_List = []
        turnovers_List = []
        points_List = []
        
        
    
        conn = create_connection("nba_stats")
        
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
        
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        timeout = 20
        driver = webdriver.Chrome(options=chrome_options)
        
        url = "https://www.espn.com/"
        
        driver.get(url)
        
        
        
        # Wait until the element with ID "global-search-trigger" is present
        search_button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, "global-search-trigger"))
        )
        
        # Click the button
        search_button.click()
        
        search_bar = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, "global-search-input"))
        )
        
        # Type into the search bar
        search_bar.send_keys(name)

        # Press Enter to submit the search
        search_bar.send_keys(Keys.RETURN)
        
        # Wait until the search results are loaded (replace "your_result_class" with the actual class of your result items)
        result_items = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "player__Results__Item"))
        )

        # Get the href link from the first result
        if result_items:
            first_result_link = result_items[0].find_element(By.TAG_NAME, "a").get_attribute("href")
            print("First Result Link:", first_result_link)
            url = first_result_link
            
            driver.get(first_result_link)
            
            # Split the URL into parts
            parts = first_result_link.split("/")

            # Insert "gamelog" at the desired position
            result_with_gamelog = "/".join(parts[:5] + ["gamelog"] + parts[5:])
            print("Result with Gamelog:", result_with_gamelog)
            
            driver.get(result_with_gamelog)
            
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            
            gameLog_Tables = soup.find_all("div", class_="mb5")
            
            
            numTables = len(gameLog_Tables)
            count = 1
            
            for i in range(1, len(gameLog_Tables)):
                table = gameLog_Tables[i]
                
                table_Scroller = table.find("div", class_="Table__Scroller")
                tBody = table_Scroller.find("tbody", class_="Table__TBODY")
                
                row_Type_1 = tBody.find_all("tr", class_="Table__TR Table__TR--sm Table__even")
                row_Type_2 = tBody.find_all("tr", class_="filled Table__TR Table__TR--sm Table__even")
                
                
                if len(row_Type_1) != 0:
                    
                    for row in row_Type_1:
                        columns = row.find_all("td", class_="Table__TD")
                        
                        date_Column = columns[0]
                        
                        date_unformatted = date_Column.text
                        
                        if count < numTables-3:
                            
                            # Set the year to the current year (or any other appropriate year)
                            date_unformatted = f"{datetime.now().year} {date_unformatted}"
                            
                            parsed_date = datetime.strptime(date_unformatted, '%Y %a %m/%d')
                            
                            # Format the date in 'YYYY-MM-DD' format
                            formatted_date_str = parsed_date.strftime('%Y-%m-%d')
                            
                            dates_List.append(formatted_date_str)
                    
                        elif count >= numTables-3:
                            
                            # Set the year to the current year (or any other appropriate year)
                            date_unformatted = f"{datetime.now().year} {date_unformatted}"
                            
                            # Parse the input date string
                            parsed_date = datetime.strptime(date_unformatted, '%Y %a %m/%d')

                            # Set the year to the previous year
                            previous_year_date = parsed_date.replace(year=parsed_date.year - 1)

                            # Format the date in 'YYYY-MM-DD' format
                            formatted_date_str = previous_year_date.strftime('%Y-%m-%d')
                            
                            dates_List.append(formatted_date_str)
                        
                        
                         
                        # Get Opponent Name
                        opp_Column = columns[1]
                        
                        opp_anchorLink = opp_Column.find_all("a", class_="AnchorLink v-mid")
                        opp_anchorLink = opp_anchorLink[1]
                        
                        opp_Name = opp_anchorLink.text
                        
                        opp_List.append(opp_Name)
                        
                        # Get Results of Game
                        result_Column = columns[2]
                        
                        # Check if either element exists
                        loss_element = result_Column.find('div', class_='ResultCell tl loss-stat')
                        win_element = result_Column.find('div', class_='ResultCell tl win-stat')
                        
                        if loss_element:
                            
                            WL_List.append(loss_element.text)
                            
                        elif win_element:
                            
                            WL_List.append(win_element.text)
                            
                        score_element = result_Column.find("span")
                        
                        result_List.append(score_element.text)
                        
                        # Get Minutes Played
                        minute_Column = columns[3]
                        
                        min_List.append(int(minute_Column.text))
                        
                        # Get Field Goal Stats
                        fieldGoal_Column = columns[4]
                        
                        fieldGoalStats_Text = fieldGoal_Column.text
                        
                        # Remove parentheses and split the string at "-"
                        field_goals_made, field_goal_attempted = fieldGoalStats_Text.split('-')
                        
                        fieldGoals_Made_List.append(int(field_goals_made))
                        fieldGoals_Attempted_List.append(int(field_goal_attempted))
                        
                        # Get Field Goal Percentage
                        fieldGoalPerc_Column = columns[5]
                        
                        fieldGoal_Perc_List.append(float(fieldGoalPerc_Column.text))
                        
                        # Get Three Pointer Stats
                        threePointer_Column = columns[6]
                        
                        threePointerStats_Text = threePointer_Column.text
                        
                        threePointers_Made, threePointers_Attempted = threePointerStats_Text.split('-')
                        
                        threePointers_Made_List.append(int(threePointers_Made))
                        threePointers_Attempted_List.append(int(threePointers_Attempted))
                        
                        # Get Three Pointers Percentage
                        threePointerPerc_Column = columns[7]
                        
                        threePointer_Perc_List.append(float(threePointerPerc_Column.text))
                        
                        # Get Free Throw Stats
                        freeThrow_Column = columns[8]
                        
                        freeThrowStats_Text = freeThrow_Column.text
                        
                        freeThrows_Made, freeThrows_Attempted = freeThrowStats_Text.split('-')
                        
                        freeThrows_Made_List.append(int(freeThrows_Made))
                        freeThrows_Attempted_List.append(int(freeThrows_Attempted))
                        
                        # Get Free Throw Percentage
                        freeThrowPerc_Column = columns[9]
                        
                        freeThrow_Perc_List.append(float(freeThrowPerc_Column.text))
                        
                        # Get Rebound Stats
                        rebound_Column = columns[10]
                        
                        rebounds_List.append(int(rebound_Column.text))
                        
                        # Get Assist Stats
                        assist_Column = columns[11]
                        
                        assists_List.append(int(assist_Column.text))
                        
                        # Get Block Stats
                        block_Column = columns[12]
                        
                        blocks_List.append(int(block_Column.text))
                        
                        # Get Steal Stats
                        steals_Column = columns[13]
                        
                        steals_List.append(int(steals_Column.text))
                        
                        # Get Foul Stats
                        fouls_Column = columns[14]
                        
                        fouls_List.append(int(fouls_Column.text))
                        
                        # Get Turnover Stats
                        turnovers_Column = columns[15]
                        
                        turnovers_List.append(int(turnovers_Column.text))
                        
                        # Get Points Stats
                        points_Column = columns[16]
                        
                        points_List.append(int(points_Column.text))
                        
                        print("Length of points List: " + str(len(points_List)) + "\n\n")
                    
                
                if len(row_Type_2) != 0:
    
                    for row in row_Type_2:
                        columns = row.find_all("td", class_="Table__TD")
                        
                        date_Column = columns[0]
                    
                        date_unformatted = date_Column.text
                        
                        if count < numTables-3:
                        
                            # Set the year to the current year (or any other appropriate year)
                            date_unformatted = f"{datetime.now().year} {date_unformatted}"

                            parsed_date = datetime.strptime(date_unformatted, '%Y %a %m/%d')
                            
                            # Format the date in 'YYYY-MM-DD' format
                            formatted_date_str = parsed_date.strftime('%Y-%m-%d')
                            
                            dates_List.append(formatted_date_str)
                    
                        elif count >= numTables-3:
                        
                            # Set the year to the current year (or any other appropriate year)
                            date_unformatted = f"{datetime.now().year} {date_unformatted}"
                            
                            # Parse the input date string
                            parsed_date = datetime.strptime(date_unformatted, '%Y %a %m/%d')

                            # Set the year to the previous year
                            previous_year_date = parsed_date.replace(year=parsed_date.year - 1)

                            # Format the date in 'YYYY-MM-DD' format
                            formatted_date_str = previous_year_date.strftime('%Y-%m-%d')
                            
                            dates_List.append(formatted_date_str)
                        
                        # Get Opponent Name
                        opp_Column = columns[1]
                        
                        opp_anchorLink = opp_Column.find_all("a", class_="AnchorLink v-mid")
                        opp_anchorLink = opp_anchorLink[1]
                        
                        opp_Name = opp_anchorLink.text
                        
                        opp_List.append(opp_Name)
                        
                        
                        # Get Results of Game
                        result_Column = columns[2]
                        
                        # Check if either element exists
                        loss_element = result_Column.find('div', class_='ResultCell tl loss-stat')
                        win_element = result_Column.find('div', class_='ResultCell tl win-stat')
                        
                        if loss_element:
                            
                            WL_List.append(loss_element.text)
                            
                        elif win_element:
                            
                            WL_List.append(win_element.text)
                            
                        score_element = result_Column.find("span")
                        
                        result_List.append(score_element.text)
                        
                        # Get Minutes Played
                        minute_Column = columns[3]
                        
                        min_List.append(int(minute_Column.text))
                        
                        # Get Field Goal Stats
                        fieldGoal_Column = columns[4]
                        
                        fieldGoalStats_Text = fieldGoal_Column.text
                        
                        # Remove parentheses and split the string at "-"
                        field_goals_made, field_goal_attempted = fieldGoalStats_Text.split('-')
                        
                        fieldGoals_Made_List.append(int(field_goals_made))
                        fieldGoals_Attempted_List.append(int(field_goal_attempted))
                        
                        
                        
                        # Get Field Goal Percentage
                        fieldGoalPerc_Column = columns[5]
                        
                        fieldGoal_Perc_List.append(float(fieldGoalPerc_Column.text))
                        
                        # Get Three Pointer Stats
                        threePointer_Column = columns[6]
                        
                        threePointerStats_Text = threePointer_Column.text
                        
                        threePointers_Made, threePointers_Attempted = threePointerStats_Text.split('-')
                        
                        threePointers_Made_List.append(int(threePointers_Made))
                        threePointers_Attempted_List.append(int(threePointers_Attempted))
                        
                        # Get Three Pointers Percentage
                        threePointerPerc_Column = columns[7]
                        
                        threePointer_Perc_List.append(float(threePointerPerc_Column.text))
                        
                        # Get Free Throw Stats
                        freeThrow_Column = columns[8]
                        
                        freeThrowStats_Text = freeThrow_Column.text
                        
                        freeThrows_Made, freeThrows_Attempted = freeThrowStats_Text.split('-')
                        
                        freeThrows_Made_List.append(int(freeThrows_Made))
                        freeThrows_Attempted_List.append(int(freeThrows_Attempted))
                        
                        # Get Free Throw Percentage
                        freeThrowPerc_Column = columns[9]
                        
                        freeThrow_Perc_List.append(float(freeThrowPerc_Column.text))
                        
                        # Get Rebound Stats
                        rebound_Column = columns[10]
                        
                        rebounds_List.append(int(rebound_Column.text))
                        
                        # Get Assist Stats
                        assist_Column = columns[11]
                        
                        assists_List.append(int(assist_Column.text))
                        
                        # Get Block Stats
                        block_Column = columns[12]
                        
                        blocks_List.append(int(block_Column.text))
                        
                        # Get Steal Stats
                        steals_Column = columns[13]
                        
                        steals_List.append(int(steals_Column.text))
                        
                        # Get Foul Stats
                        fouls_Column = columns[14]
                        
                        fouls_List.append(int(fouls_Column.text))
                        
                        # Get Turnover Stats
                        turnovers_Column = columns[15]
                        
                        turnovers_List.append(int(turnovers_Column.text))
                        
                        # Get Points Stats
                        points_Column = columns[16]
                        
                        points_List.append(int(points_Column.text))
                
                
                
                count +=1
            
        else:
            
            driver.close()
        
         
        for i in range(len(points_List)):
            
            print(str(dates_List[i]) + " | " + str(points_List[i]))
        
        time.sleep(30)
    
    except TimeoutException as e:
        
        print(f"Caught TimeoutException: {e}")
        print("Restarting the function...")
        time.sleep(5)
        supplyTable_NBAPlayer_GameLogs(name)
        
        
        
             
def supplyTable_AllNBAPlayer_GameLogs():
    
    teamNames_Short = ["bos", "bkn", "ny", "phi", "tor", "gs",
                       "lac", "lal", "phx", "sac", "chi", "cle",
                       "det", "ind", "mil", "dal", "hou", "mem",
                       "no", "sa", "atl", "cha", "mia", "orl",
                       "wsh", "den", "min", "okc", "por", "utah"]
    
    playerName = ""
    
    
    conn = create_connection("nba_stats")
    
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
    
    for team in teamNames_Short:
        
        select_query = f"SELECT Name FROM {team}_Roster"
        
        # Execute the query
        cursor.execute(select_query)
        
        # Fetch all the results
        result_set = cursor.fetchall()

        # Extract names from the result set
        names = [row[0] for row in result_set]
        
"""        
# Update Calls
supplyTable_Player_AssistsAndTurnovers()
time.sleep(10) 
supplyTable_Player_ReboundsTotals()
time.sleep(10) 
supplyTable_Player_ScoringTotals()
time.sleep(10) 
supplyTable_Player_Blocks()
time.sleep(10) 
supplyTable_Player_Fouls()
time.sleep(10) 
supplyTable_DefTeam_Scoring()
time.sleep(10) 
supplyTable_TeamRoster()
time.sleep(10)
supplyTable_DefTeam_Shooting()
time.sleep(10)
supplyTable_Opp_Misc()
"""