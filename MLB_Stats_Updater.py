from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

import mysql.connector

from main_Library import formatTeam_DatabaseName

from bs4 import BeautifulSoup
import time
from datetime import datetime
from datetime import date
import math
import re

chrome_driver_path = 'C:\\Users\\buddy\\.wdm\\drivers\\chromedriver.exe'

# Update All MLB Tables
#_________________________________________________

def updateAllMLBTables():
    
    supplyTable_Pitcher_Totals()
    supplyTable_Pitcher_Home()
    supplyTable_Pitcher_Away()
    supplyTable_Pitcher_Day()
    supplyTable_Pitcher_Night()
    supplyTable_Pitcher_VsLeft()
    supplyTable_Pitcher_VsRight()
    
    supplyTable_Batter_Total()
    supplyTable_Batter_Home()
    supplyTable_Batter_Away()
    supplyTable_Batter_Day()
    supplyTable_Batter_Night()
    supplyTable_Batter_vsLeft()
    supplyTable_Batter_vsRight()
    
    supplyTable_Team_Total()
    supplyTable_Team_Home()
    supplyTable_Team_Away()
    supplyTable_Team_Day()
    supplyTable_Team_Night()
    supplyTable_Team_1stInning()


# Supply Pitcher Tables
#_________________________________________________

def supplyTable_Pitcher_Totals():
    
    pitcherNames = []
    pitcherArms = []
    gamesPlayed = []
    InningsPitched = []
    Wins = []
    Losses = []
    ERA = []
    WHIP = []
    Strikeouts = []
    Walks = []
    Hits = []
    Runs = []
    HomeRuns = []
    
    pages = 31
    pageIndex = 1
    
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/pitching/games?page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                pitcherNames.append(aria_label)
         
         
        
                
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                gamesPlayed.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            except StaleElementReferenceException:
                
                continue
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                InningsPitched.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Wins.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Losses.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    ERA_Temp = "0.00"
                    ERA.append(ERA_Temp)
                else:
                    
                    ERA.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='19']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    WHIP_temp = "0.00"
                    
                    WHIP.append(WHIP_temp)
                    
                else:
                    
                    WHIP.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='18']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='17']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='13']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
        
        pageIndex +=1
        
        
    db_count = 0
    data_tuples = []
    for name in pitcherNames:
        data_tuple = (pitcherNames[db_count], gamesPlayed[db_count], InningsPitched[db_count], Wins[db_count], Losses[db_count], ERA[db_count], WHIP[db_count], Strikeouts[db_count], Walks[db_count], Hits[db_count], Runs[db_count] , HomeRuns[db_count])
        data_tuples.append(data_tuple)
        db_count += 1

    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO pitcher_total_stats (Name, Games_Played, Innings_Pitched, Wins, Losses, ERA, WHIP, Strikeouts, Walks, Hits, Runs, HomeRuns) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Innings_Pitched=VALUES(Innings_Pitched), Wins=VALUES(Wins), Losses=VALUES(Losses), ERA=VALUES(ERA), WHIP=VALUES(WHIP), Strikeouts=VALUES(Strikeouts), Walks=VALUES(Walks), Hits=VALUES(Hits), Runs=VALUES(Runs), HomeRuns=VALUES(HomeRuns)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    print("Updated Pitcher Total Stats")
    return pitcherNames, gamesPlayed, InningsPitched, Wins, Losses, ERA, WHIP, Strikeouts, Walks, Hits, Runs, HomeRuns  
        
def supplyTable_Pitcher_Home():
    
    pitcherNames = []
    pitcherArms = []
    gamesPlayed = []
    InningsPitched = []
    Wins = []
    Losses = []
    ERA = []
    WHIP = []
    Strikeouts = []
    Walks = []
    Hits = []
    Runs = []
    HomeRuns = []
    
    pages = 29
    pageIndex = 1
    
    data_rows = 24
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'mlb_stats'  # Replace with your database name

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
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/pitching/games?split=h&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                pitcherNames.append(aria_label)


        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                gamesPlayed.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            except StaleElementReferenceException:
                
                continue
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                InningsPitched.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            except StaleElementReferenceException:
                
                continue

        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Wins.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Losses.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                if element.text == "-.--":
                    
                    ERA.append(0.00)
                
                else:   
                    ERA.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='19']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                if element.text == "-.--":
                    
                    WHIP.append(0.00)
                    
                else:
                    
                    WHIP.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='18']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='17']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='13']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break

        pageIndex +=1
    
    db_count = 0
    data_tuples = []
    for name in pitcherNames:
        data_tuple = (pitcherNames[db_count], gamesPlayed[db_count], InningsPitched[db_count], Wins[db_count], Losses[db_count], ERA[db_count], WHIP[db_count], Strikeouts[db_count], Walks[db_count],  Hits[db_count], Runs[db_count] ,HomeRuns[db_count])
        data_tuples.append(data_tuple)
        db_count += 1

    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO pitcher_home_stats (Name, Games_Played, Innings_Pitched, Wins, Losses, ERA, WHIP, Strikeouts, Walks, Hits, Runs, HomeRuns) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Innings_Pitched=VALUES(Innings_Pitched), Wins=VALUES(Wins), Losses=VALUES(Losses), ERA=VALUES(ERA), WHIP=VALUES(WHIP), Strikeouts=VALUES(Strikeouts), Walks=VALUES(Walks), Hits=VALUES(Hits), Runs=VALUES(Runs), HomeRuns=VALUES(HomeRuns)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()  
    print("Updated Pitcher Home Stats") 
    
def supplyTable_Pitcher_Away():
    
    pitcherNames = []
    pitcherArms = []
    gamesPlayed = []
    InningsPitched = []
    Wins = []
    Losses = []
    ERA = []
    WHIP = []
    Strikeouts = []
    Walks = []
    Hits = []
    Runs = []
    HomeRuns = []
    
    pages = 29
    pageIndex = 1
    
    data_rows = 24
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'mlb_stats'  # Replace with your database name

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
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/pitching/games?split=a&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                pitcherNames.append(aria_label)


        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                gamesPlayed.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                InningsPitched.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break

            except StaleElementReferenceException:
                
                continue
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Wins.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Losses.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    ERA.append(0.00)
                    
                else:    
                    ERA.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='19']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    WHIP.append(0.00)
                    
                else:
                    
                    WHIP.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='18']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='17']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
                
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='13']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break

        pageIndex +=1
        
        
    db_count = 0
    data_tuples = []
    for name in pitcherNames:
        data_tuple = (pitcherNames[db_count], gamesPlayed[db_count], InningsPitched[db_count], Wins[db_count], Losses[db_count], ERA[db_count], WHIP[db_count], Strikeouts[db_count], Walks[db_count], Hits[db_count], Runs[db_count], HomeRuns[db_count])
        data_tuples.append(data_tuple)
        db_count += 1

    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO pitcher_away_stats (Name, Games_Played, Innings_Pitched, Wins, Losses, ERA, WHIP, Strikeouts, Walks, Hits, Runs, HomeRuns) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Innings_Pitched=VALUES(Innings_Pitched), Wins=VALUES(Wins), Losses=VALUES(Losses), ERA=VALUES(ERA), WHIP=VALUES(WHIP), Strikeouts=VALUES(Strikeouts), Walks=VALUES(Walks), Hits=VALUES(Hits), Runs=VALUES(Runs), HomeRuns=VALUES(HomeRuns)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit() 
    print("Updated Pitcher Away Stats")  
     
def supplyTable_Pitcher_Day():
    
    pitcherNames = []
    pitcherArms = []
    gamesPlayed = []
    InningsPitched = []
    Wins = []
    Losses = []
    ERA = []
    WHIP = []
    Strikeouts = []
    Walks = []
    Hits = []
    Runs = []
    HomeRuns = []
    
    pages = 29
    pageIndex = 1
    
    data_rows = 24
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'mlb_stats'  # Replace with your database name

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
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/pitching/games?split=d&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                pitcherNames.append(aria_label)


        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                gamesPlayed.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                InningsPitched.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break


        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Wins.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Losses.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    ERA.append(0.00)
                
                else:
                        
                    ERA.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='19']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    WHIP.append(0.00)
                    
                else:
                    
                    WHIP.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='18']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='17']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='13']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break

        pageIndex +=1
        
    db_count = 0
    data_tuples = []
    for name in pitcherNames:
        data_tuple = (pitcherNames[db_count], gamesPlayed[db_count], InningsPitched[db_count], Wins[db_count], Losses[db_count], ERA[db_count], WHIP[db_count], Strikeouts[db_count], Walks[db_count], Hits[db_count], Runs[db_count], HomeRuns[db_count])
        data_tuples.append(data_tuple)
        db_count += 1

    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO pitcher_day_stats (Name, Games_Played, Innings_Pitched, Wins, Losses, ERA, WHIP, Strikeouts, Walks, Hits, Runs, HomeRuns) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Innings_Pitched=VALUES(Innings_Pitched), Wins=VALUES(Wins), Losses=VALUES(Losses), ERA=VALUES(ERA), WHIP=VALUES(WHIP), Strikeouts=VALUES(Strikeouts), Walks=VALUES(Walks), Hits=VALUES(Hits), Runs=VALUES(Runs), HomeRuns=VALUES(HomeRuns)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    print("Updated Pitcher Day Stats")    

def supplyTable_Pitcher_Night():
    
    pitcherNames = []
    pitcherArms = []
    gamesPlayed = []
    InningsPitched = []
    Wins = []
    Losses = []
    ERA = []
    WHIP = []
    Strikeouts = []
    Walks = []
    Hits = []
    Runs = []
    HomeRuns = []
    
    pages = 29
    pageIndex = 1
    
    data_rows = 24
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'mlb_stats'  # Replace with your database name

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
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/pitching/games?split=n&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                pitcherNames.append(aria_label)


        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                gamesPlayed.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                InningsPitched.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break


        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Wins.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Losses.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    ERA.append(0.00)
                    
                else:
                    ERA.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='19']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--":
                    
                    WHIP.append(0.00)
                    
                else:
                    WHIP.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='18']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='17']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='13']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break

        pageIndex +=1
    db_count = 0
    data_tuples = []
    for name in pitcherNames:
        data_tuple = (pitcherNames[db_count], gamesPlayed[db_count], InningsPitched[db_count], Wins[db_count], Losses[db_count], ERA[db_count], WHIP[db_count], Strikeouts[db_count], Walks[db_count], Hits[db_count], Runs[db_count], HomeRuns[db_count])
        data_tuples.append(data_tuple)
        db_count += 1

    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO pitcher_night_stats (Name, Games_Played, Innings_Pitched, Wins, Losses, ERA, WHIP, Strikeouts, Walks, Hits, Runs, HomeRuns ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Games_Played=VALUES(Games_Played), Innings_Pitched=VALUES(Innings_Pitched), Wins=VALUES(Wins), Losses=VALUES(Losses), ERA=VALUES(ERA),WHIP=VALUES(WHIP), Strikeouts=VALUES(Strikeouts), Walks=VALUES(Walks), Hits=VALUES(Hits), Runs=VALUES(Runs), HomeRuns=VALUES(HomeRuns)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    print("Updated Pitcher Night Stats")

def supplyTable_Pitcher_VsLeft():
    
    pitcherNames = []
    WHIP = []
    Strikeouts = []
    Walks = []
    Hits = []
    HomeRuns = []
    batting_AVGs = []
    
    pages = 31
    pageIndex = 1
    
    data_rows = 24
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'mlb_stats'  # Replace with your database name

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
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/pitching/games?split=vl&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                pitcherNames.append(aria_label)
                
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='19']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--" or element.text == "-":
                    
                    WHIP.append(0.00)
                    
                else:
                    
                    WHIP.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='18']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='17']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='20']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--" or element.text == "-":
                    
                    batting_AVGs.append(0.000)
                else:
                    
                    batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        pageIndex +=1
    
    db_count = 0
    data_tuples = []
    for name in pitcherNames:
        data_tuple = (pitcherNames[db_count], Hits[db_count], WHIP[db_count], Strikeouts[db_count], Walks[db_count], HomeRuns[db_count], batting_AVGs[db_count])
        data_tuples.append(data_tuple)
        db_count += 1

    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO pitcher_vsleft_stats (Name, Hits, WHIP, Strikeouts, Walks, HomeRuns, Batting_AVG ) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Hits =VALUES(Hits), WHIP=VALUES(WHIP), Strikeouts=VALUES(Strikeouts), Walks=VALUES(Walks), HomeRuns=VALUES(HomeRuns), Batting_AVG=VALUES(Batting_AVG)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    print("Updated Pitcher VsLeft Stats")
        
def supplyTable_Pitcher_VsRight():
    
    pitcherNames = []
    WHIP = []
    Strikeouts = []
    Walks = []
    Hits = []
    HomeRuns = []
    batting_AVGs = []
    
    pages = 31
    pageIndex = 1
    
    data_rows = 24
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'  # Replace with your database host
    db_user = 'root'  # Replace with your database username
    db_password = 'root'  # Replace with your database password
    db_name = 'mlb_stats'  # Replace with your database name

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
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/pitching/games?split=vr&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                pitcherNames.append(aria_label)    
        
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='19']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--" or element.text == "-":
                    
                    WHIP.append(0.00)
                    
                else:
                    WHIP.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='18']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='17']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                Hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='20']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                
                if element.text == "-.--" or element.text == "-":
                    
                    batting_AVGs.append(0.000)
                else:
                    
                    batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        pageIndex +=1
    
    
    db_count = 0
    data_tuples = []
    for name in pitcherNames:
        data_tuple = (pitcherNames[db_count], Hits[db_count], WHIP[db_count], Strikeouts[db_count], Walks[db_count], HomeRuns[db_count], batting_AVGs[db_count])
        data_tuples.append(data_tuple)
        db_count += 1

    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO pitcher_vsright_stats (Name, Hits, WHIP, Strikeouts, Walks, HomeRuns, Batting_AVG ) VALUES (%s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Hits =VALUES(Hits), WHIP=VALUES(WHIP), Strikeouts=VALUES(Strikeouts), Walks=VALUES(Walks), HomeRuns=VALUES(HomeRuns), Batting_AVG=VALUES(Batting_AVG)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    print("Updated Pitcher VsRight Stats")
    
def supplyTable_Arm_Pitcher():
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'
    db_user = 'root'
    db_password = 'root'
    db_name = 'mlb_stats'

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()

    names = []

    query = "SELECT Name FROM pitcher_total_stats"

    cursor.execute(query)

    names = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()

    arm_results = []

    iteration_count = 0
    for name in names:
        query = "SELECT Arm FROM pitcher_total_stats WHERE Name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        
        if result is not None and result[0] is not None and result[0] != "":
            continue
        else:
            
            time.sleep(5)
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--process-per-site")
            chrome_options.add_argument("--disable-background-networking")
            chrome_options.add_argument("--disable-background-timer-throttling")
            #chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            driver.set_window_size(1080, 1200)
            driver.get("https://www.rotowire.com/baseball")

            try:
                search_button = driver.find_element(By.ID, 'search-for-players')

                # Focus the search bar
                search_button.click()

                # Enter pitcher name in the search bar
                search_button.send_keys(name)
                
                search_button.send_keys(Keys.ENTER)

                # Use WebDriverWait to wait for the elements to be present
                wait = WebDriverWait(driver, 3)  # 10-second timeout (you can adjust as needed)
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'p-card__meta-data-item')))
                
                # Set up BeautifulSoup
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'html.parser')
                pitchingArm = ""
                
                metaData_div = soup.find_all('div', class_='p-card__meta-data-item')
                
                if len(metaData_div) >= 3:
                    third_div = metaData_div[2]
                    b_element = third_div.find('b')

                    if b_element:
                        pitchingArm = b_element.get_text(strip=True)
                        print(str(pitchingArm))
                update_query = "UPDATE pitcher_total_stats SET Arm = %s WHERE Name = %s"
                data = (pitchingArm, name)
                cursor.execute(update_query, data)
                
                conn.commit()
                
                
                
                driver.quit()
                
            except (NoSuchElementException, AttributeError,TimeoutException):
                driver.quit()
                arm_results.append("N/A")
            
        iteration_count += 1
        
        if iteration_count == 10:
            
            time.sleep(20)
        
            

    cursor.close()
    conn.close()

    print("Updated Pitcher Arm")
    
def supplyTable_Arm_Batter():
    
    # Connect to your MySQL database
    db_host = '127.0.0.1'
    db_user = 'root'
    db_password = 'root'
    db_name = 'mlb_stats'

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()

    names = []

    query = "SELECT Name FROM batter_total_stats"

    cursor.execute(query)

    names = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()

    arm_results = []

    iteration_count = 0
    for name in names:
        query = "SELECT Arm FROM batter_total_stats WHERE Name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        
        if result is not None and result[0] is not None and result[0] != "":
            continue
        else:
            
            time.sleep(5)
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--process-per-site")
            chrome_options.add_argument("--disable-background-networking")
            chrome_options.add_argument("--disable-background-timer-throttling")
            #chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            driver.set_window_size(1080, 1200)
            driver.get("https://www.rotowire.com/baseball")

            try:
                search_button = driver.find_element(By.ID, 'search-for-players')

                # Focus the search bar
                search_button.click()

                # Enter pitcher name in the search bar
                search_button.send_keys(name)
                
                search_button.send_keys(Keys.ENTER)

                # Use WebDriverWait to wait for the elements to be present
                wait = WebDriverWait(driver, 3)  # 10-second timeout (you can adjust as needed)
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'p-card__meta-data-item')))
                
                # Set up BeautifulSoup
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'html.parser')
                battingArm = ""
                
                metaData_div = soup.find_all('div', class_='p-card__meta-data-item')
                
                if len(metaData_div) >= 3:
                    third_div = metaData_div[2]
                    b_element = third_div.find('b')

                    if b_element:
                        battingArm = b_element.get_text(strip=True)
                        print(str(battingArm))
                update_query = "UPDATE batter_total_stats SET Arm = %s WHERE Name = %s"
                data = (battingArm, name)
                cursor.execute(update_query, data)
                
                conn.commit()
                
                
                
                driver.quit()
                
            except (NoSuchElementException, AttributeError,TimeoutException):
                driver.quit()
                arm_results.append("N/A")
            
        iteration_count += 1
        
        if iteration_count == 10:
            
            time.sleep(20)    
    
    
# Supply Batter Tables
#_________________________________________________
def supplyTable_Batter_Total():
    
    batterNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []
    
    pages = 27
    pageIndex = 1
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/games?page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                batterNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in batterNames:
        data_tuple = (batterNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO batter_total_stats (Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return batterNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage  

def supplyTable_Batter_Home():   
    
    
    
    batterNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []
    
    pages = 26
    pageIndex = 1
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/games?split=h&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                batterNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in batterNames:
        data_tuple = (batterNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO batter_home_stats (Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return batterNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage
        
def supplyTable_Batter_Away():
    
    
    batterNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []
    
    pages = 26
    pageIndex = 1
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/games?split=a&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                batterNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in batterNames:
        data_tuple = (batterNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO batter_away_stats (Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return batterNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage
    
def supplyTable_Batter_Day():   
    
    batterNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []
    
    pages = 26
    pageIndex = 1
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/games?split=d&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                batterNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in batterNames:
        data_tuple = (batterNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO batter_day_stats (Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return batterNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage

def supplyTable_Batter_Night():
    
    batterNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []
    
    pages = 26
    pageIndex = 1
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/games?split=n&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                batterNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            except StaleElementReferenceException:
                
                continue
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in batterNames:
        data_tuple = (batterNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO batter_night_stats (Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return batterNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage

def supplyTable_Batter_vsLeft(): 
    
    batterNames = []
    games_Played = []
    atBats = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    batting_AVGs = []
    onBase_Percentage = []
    
    pages = 23
    pageIndex = 1
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/games?split=vl&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                batterNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in batterNames:
        data_tuple = (batterNames[db_count], games_Played[db_count], atBats[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO batter_vsleft_stats (Name, Games_Played, AtBats, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return batterNames, games_Played, atBats, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, batting_AVGs, onBase_Percentage 

def supplyTable_Batter_vsRight(): 
    
    batterNames = []
    games_Played = []
    atBats = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    batting_AVGs = []
    onBase_Percentage = []
    
    pages = 23
    pageIndex = 1
    data_rows = 24
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/games?split=vr&page=" + str(pageIndex))
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                batterNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in batterNames:
        data_tuple = (batterNames[db_count], games_Played[db_count], atBats[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO batter_vsright_stats (Name, Games_Played, AtBats, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return batterNames, games_Played, atBats, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, batting_AVGs, onBase_Percentage



# Supply Team Tables
#_________________________________________________

def supplyTable_Team_Total():
    
    teamNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []

    pages = 1
    pageIndex = 1
    data_rows = 30
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/team/games")
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                teamNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in teamNames:
        data_tuple = (teamNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO team_total_stats (Team_Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return teamNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage

def supplyTable_Team_Home():
    
    teamNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []

    pages = 1
    pageIndex = 1
    data_rows = 30
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/team/games?split=h")
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                teamNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in teamNames:
        data_tuple = (teamNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO team_home_stats (Team_Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return teamNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage
      
def supplyTable_Team_Away():
    
    teamNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []

    pages = 1
    pageIndex = 1
    data_rows = 30
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/team/games?split=a")
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                teamNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in teamNames:
        data_tuple = (teamNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO team_away_stats (Team_Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return teamNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage  

def supplyTable_Team_Day():
    
    teamNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []

    pages = 1
    pageIndex = 1
    data_rows = 30
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/team/games?split=d")
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                teamNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in teamNames:
        data_tuple = (teamNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO team_day_stats (Team_Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return teamNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage  

def supplyTable_Team_Night():
    
    teamNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []

    pages = 1
    pageIndex = 1
    data_rows = 30
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/team/games?split=n")
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                teamNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in teamNames:
        data_tuple = (teamNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO team_night_stats (Team_Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return teamNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage  
    
def supplyTable_Team_1stInning():

    teamNames = []
    games_Played = []
    atBats = []
    runs = []
    hits = []
    doubles = []
    triples = []
    HomeRuns = []
    RBIs = []
    walks = []
    strikeouts = []
    stolenBases = []
    batting_AVGs = []
    onBase_Percentage = []

    pages = 1
    pageIndex = 1
    data_rows = 30
    
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    while pageIndex <= pages:
        
        driver.get("https://www.mlb.com/stats/team/games?split=i01")
            
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bui-link')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
            
            
        names = soup.find_all('a', class_="bui-link")
            
        for name in names:
            aria_label = name.get('aria-label')
            if aria_label:
                teamNames.append(aria_label)
                
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='2']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                games_Played.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='3']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                atBats.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='4']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                runs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='5']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                hits.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='6']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                doubles.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='7']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                triples.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='8']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                HomeRuns.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='9']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                RBIs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
        
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='10']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                walks.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='11']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                strikeouts.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='12']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                stolenBases.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='14']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                batting_AVGs.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
            
            
        dataIndex = 0
        while dataIndex <= data_rows:
            
            try:
                
                # Construct the XPath based on the current dataIndex
                xpath_selector = f"//td[@data-row='{dataIndex}'][@data-col='15']"
                # Find the element using the constructed XPath
                element = driver.find_element(By.XPATH, xpath_selector)
                # Get the text value of the element and append it to the appropriate list (e.g., gamesPlayed)
                onBase_Percentage.append(element.text)
                
                
                dataIndex += 1   
        
            except NoSuchElementException:
                # Element not found, break out of the loop
                break
    
        pageIndex+=1
    
    db_count = 0
    data_tuples = []
    for name in teamNames:
        data_tuple = (teamNames[db_count], games_Played[db_count], atBats[db_count], runs[db_count], hits[db_count], doubles[db_count], triples[db_count], HomeRuns[db_count], RBIs[db_count], walks[db_count], strikeouts[db_count], stolenBases[db_count], batting_AVGs[db_count], onBase_Percentage[db_count])
        data_tuples.append(data_tuple)
        db_count += 1
    
    # Use INSERT ... ON DUPLICATE KEY UPDATE to handle duplicates
    insert_query = "INSERT INTO team_1stinning_stats (Team_Name, Games_Played, AtBats, Runs, Hits, Doubles, Triples, HomeRuns, RBIs, Walks, Strikeouts, StolenBases, Batting_AVG, OnBase_Percent ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE games_Played=VALUES(games_Played), AtBats=VALUES(AtBats), Runs=VALUES(Runs), Hits=VALUES(Hits), Doubles=VALUES(Doubles), Triples=VALUES(Triples), HomeRuns=VALUES(HomeRuns), RBIs=VALUES(RBIs), Walks=VALUES(Walks), Strikeouts=VALUES(Strikeouts), StolenBases=VALUES(StolenBases), Batting_AVG=VALUES(Batting_AVG), OnBase_Percent=VALUES(OnBase_Percent)"
    cursor.executemany(insert_query, data_tuples)
    conn.commit()   
    
    return teamNames, games_Played, atBats, runs, hits, doubles, triples, HomeRuns, RBIs, walks, strikeouts, stolenBases, batting_AVGs, onBase_Percentage

def supplyTable_TeamRoster():
    
    names = []
    
    
    team_shortNames = ["CHW","CLE","DET","KC","MIN","BAL","BOS","NYY","TB","TOR","HOU","LAA","OAK","SEA","TEX","CHC","CIN","MIL","PIT","STL","ATL","MIA","NYM","PHI","WAS","ARI","COL","LAD","SD","SF"]
    
    team_longNames = ["chicago-white-sox","cleveland-guardians","detroit-tigers","kansas-city-royals","minnesota-twins","baltimore-orioles","boston-red-sox",
                      "new-york-yankees","tampa-bay-rays","toronto-blue-jays","houston-astros","los-angeles-angels","oakland-athletics","seattle-mariners","texas-rangers",
                      "chicago-cubs","cincinnati-reds","milwaukee-brewers","pittsburgh-pirates","st-louis-cardinals","atlanta-braves","miami-marlins","new-york-mets","philadelphia-phillies",
                      "washington-nationals","arizona-diamondbacks","colorado-rockies","los-angeles-dodgers","san-diego-padres","san-francisco-giants"]
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    team_count = 0
    for team in team_shortNames:
        
        driver.get("https://www.cbssports.com/mlb/teams/"+str(team_shortNames[team_count])+"/"+str(team_longNames[team_count])+"/roster/")
        
        wait.until(EC.presence_of_element_located((By.ID, 'TableBase')))
            # Set up BeautifulSoup
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        sections = soup.find_all(id="TableBase")
        
        playerNames = []
        playerArms = []
        
        catcher_section = sections[1]
        infielder_section = sections[2]
        outfielder_section = sections[3]
        
        # Extract player names and batting arms from catcher_section
        catcher_players = catcher_section.find_all('tr', class_='TableBase-bodyTr')
        for player_row in catcher_players:
            columns = player_row.find_all('td', class_='TableBase-bodyTd')
            if len(columns) >= 4:
                player_name = columns[1].find('span', class_='CellPlayerName--long').find('a').get_text(strip=True)
                player_batting_arm = columns[3].get_text(strip=True)
        
                playerNames.append(player_name)
                playerArms.append(player_batting_arm)
                # Append the player name to the list
                
            
            
            
            
                
        # Extract player names and batting arms from infielder_section
        infielder_players = infielder_section.find_all('tr', class_='TableBase-bodyTr')
        for player_row in infielder_players:
            columns = player_row.find_all('td', class_='TableBase-bodyTd')
            if len(columns) >= 4:
                player_name = columns[1].find('span', class_='CellPlayerName--long').find('a').get_text(strip=True)
                player_batting_arm = columns[3].get_text(strip=True)

                playerNames.append(player_name)
                playerArms.append(player_batting_arm)
                # Append the player name to the list
                 
            
                
        # Extract player names and batting arms from outfielder_section
        outfielder_players = outfielder_section.find_all('tr', class_='TableBase-bodyTr')
        for player_row in outfielder_players:
            columns = player_row.find_all('td', class_='TableBase-bodyTd')
            if len(columns) >= 4:
                player_name = columns[1].find('span', class_='CellPlayerName--long').find('a').get_text(strip=True)
                player_batting_arm = columns[3].get_text(strip=True)

                playerNames.append(player_name)
                playerArms.append(player_batting_arm)
                # Append the player name to the list
                
            
            
        tableName = formatTeam_DatabaseName(team_shortNames[team_count])
        # Now, iterate through the player names and insert them into the database
        if playerNames:
            cursor = conn.cursor()
            insert_query = "INSERT INTO " + str(tableName) + " (Name, Arm) VALUES (%s, %s)"
            select_query = "SELECT Name FROM " + str(tableName) + " WHERE Name = %s"

            for player_name, player_batting_arm in zip(playerNames, playerArms):  # Assuming you have playerBattingArms list
                data = (player_name, player_batting_arm)

                # Check if player name already exists in the table
                cursor.execute(select_query, (player_name,))
                existing_player = cursor.fetchone()

                if not existing_player:  # Only insert if player doesn't already exist
                    cursor.execute(insert_query, data)
                    conn.commit()

            cursor.close()
            
        
        team_count +=1

def newSupplyTable_TeamRoster():
    
    
    
    team_shortNames = ["CHW","CLE","DET","KC","MIN","BAL","BOS","NYY","TB","TOR","HOU","LAA","OAK","SEA","TEX","CHC","CIN","MIL","PIT","STL","ATL","MIA","NYM","PHI","WSH","ARI","COL","LAD","SD","SF"]
    
    team_longNames = ["chicago-white-sox","cleveland-guardians","detroit-tigers","kansas-city-royals","minnesota-twins","baltimore-orioles","boston-red-sox",
                      "new-york-yankees","tampa-bay-rays","toronto-blue-jays","houston-astros","los-angeles-angels","oakland-athletics","seattle-mariners","texas-rangers",
                      "chicago-cubs","cincinnati-reds","milwaukee-brewers","pittsburgh-pirates","st-louis-cardinals","atlanta-braves","miami-marlins","new-york-mets","philadelphia-phillies",
                      "washington-nationals","arizona-diamondbacks","colorado-rockies","los-angeles-dodgers","san-diego-padres","san-francisco-giants"]
    
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
    db_name = 'mlb_stats'  # Replace with your database name

    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = conn.cursor()
    
    
    
    for short_name, long_name in zip(team_shortNames, team_longNames):

        names = []
        playerArms = []
        
        time.sleep(5)
        driver.get("https://www.espn.com/mlb/team/roster/_/name/"+str(short_name)+"/"+str(long_name))
        
        
        
        #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Wrapper Card__Content')))
            # Set up BeautifulSoup
        time.sleep(2)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        time.sleep(5)
        #Get Batter's Name
        catcher_Table = soup.find('div', class_="ResponsiveTable Catchers Roster__MixedTable")
        infielder_Table = soup.find('div', class_="ResponsiveTable Infielders Roster__MixedTable")
        outfielder_Table = soup.find('div', class_="ResponsiveTable Outfielders Roster__MixedTable")
        dh_Table = soup.find('div', class_="ResponsiveTable Designated Hitter Roster__MixedTable")
        
        catcher_NameColumn = catcher_Table.find_all('tbody', class_='Table__TBODY')
        infielder_NameColumn = infielder_Table.find_all('tbody', class_='Table__TBODY')
        outfielder_NameColumn = outfielder_Table.find_all('tbody', class_='Table__TBODY')
        if dh_Table != None:
            dh_NameColumn = dh_Table.find_all('tbody', class_='Table__TBODY')
            dh_aLinks = dh_NameColumn[0].find_all('a', class_='AnchorLink')
            
            dhDetail_Table = dh_Table.find('div', class_='Table__Scroller')
            dhDetail_TBODY = dhDetail_Table.find('tbody', class_='Table__TBODY')
            dhDetail_Columns = dhDetail_TBODY.find_all('td', class_='Table__TD')
            
            multiplier_count = 0
            if dh_aLinks:    
                for link in dh_aLinks:
                    
                    name = link.get_text()
                    if name != '':
                        names.append(name)
                        
                        dhArm_Element = dhDetail_Columns[3+(9*multiplier_count)]
                        multiplier_count +=1
                        armText = dhArm_Element.get_text()
                        
                        if armText == "B":
                            
                            armText = "S"
                        
                            playerArms.append(armText)
                    
                        else:
                            
                            playerArms.append(armText)
        
        catcher_aLinks = catcher_NameColumn[0].find_all('a', class_='AnchorLink')
        infielder_aLinks = infielder_NameColumn[0].find_all('a', class_='AnchorLink')
        outfielder_aLinks = outfielder_NameColumn[0].find_all('a', class_='AnchorLink')
        
            
        
              
        # Get Batter's Arm
        catcherDetail_Table = catcher_Table.find('div', class_='Table__Scroller')
        infielderDetail_Table = infielder_Table.find('div', class_='Table__Scroller')
        outfielderDetail_Table = outfielder_Table.find('div', class_='Table__Scroller')
        
            
            
        catcherDetail_TBODY = catcherDetail_Table.find('tbody', class_='Table__TBODY')
        infielderDetail_TBODY = infielderDetail_Table.find('tbody', class_='Table__TBODY')
        outfielderDetail_TBODY = outfielderDetail_Table.find('tbody', class_='Table__TBODY')
        
            
        
        catcherDetail_Columns = catcherDetail_TBODY.find_all('td', class_='Table__TD')   
        infielderDetail_Columns = infielderDetail_TBODY.find_all('td', class_='Table__TD') 
        outfielderDetail_Columns = outfielderDetail_TBODY.find_all('td', class_='Table__TD') 
        
             
            
        
        multiplier_count = 0
        for link in catcher_aLinks:

            
            name = link.get_text()
 
            if name != '':
                
                names.append(name)
                
                catcherArm_Element = catcherDetail_Columns[3+(9*multiplier_count)]
                multiplier_count +=1
                armText = catcherArm_Element.get_text()
                
                if armText == "B":
                    
                    armText = "S"
                
                    playerArms.append(armText)
                
                else:
                    
                    playerArms.append(armText)
                    
                
                
        multiplier_count = 0    
        for link in infielder_aLinks:
            
            name = link.get_text()
            
            if name != '':
                names.append(name)
                
                infielderArm_Element = infielderDetail_Columns[3+(9*multiplier_count)]
                multiplier_count +=1
                armText = infielderArm_Element.get_text()
                
                if armText == "B":
                    
                    armText = "S"
                
                    playerArms.append(armText)
            
                else:
                    
                    playerArms.append(armText)
                    
                
                    
        multiplier_count = 0             
        for link in outfielder_aLinks:
            
            name = link.get_text()
            if name != '':
                names.append(name)
                
                outfielderArm_Element = outfielderDetail_Columns[3+(9*multiplier_count)]
                multiplier_count +=1
                armText = outfielderArm_Element.get_text()
                
                if armText == "B":
                    
                    armText = "S"
                
                    playerArms.append(armText)
            
                else:
                    
                    playerArms.append(armText)
                    
                
                
        
                        
           
        tableName = formatTeam_DatabaseName(short_name)
        # Now, iterate through the player names and insert them into the database
        if names:
            cursor = conn.cursor()
            insert_query = "INSERT INTO " + str(tableName) + " (Name, Arm) VALUES (%s, %s)"
            select_query = "SELECT Name FROM " + str(tableName) + " WHERE Name = %s"

            for player_name, player_batting_arm in zip(names, playerArms):  # Assuming you have playerBattingArms list
                data = (player_name, player_batting_arm)

                # Check if player name already exists in the table
                cursor.execute(select_query, (player_name,))
                existing_player = cursor.fetchone()

                if not existing_player:  # Only insert if player doesn't already exist
                    cursor.execute(insert_query, data)
                    conn.commit()

            cursor.close()
        
        
    driver.quit()    
        