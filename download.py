from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
PATH = "C:\Program Files (x86)\chromedriver.exe"
#options = webdriver.ChromeOptions()
#options.headless = True
driver = webdriver.Chrome(PATH)#,options=options)
cwdPath = os.getcwd()
directory = "newSpotifyPlaylist"
path = os.path.join(cwdPath, directory)
os.mkdir(path)
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
#Below is the song list
songList = ["roar katy perry", "firework katy perry"]
driver.get("https://www.google.com/")
for i in range(len(songList)):
    searchButton = driver.find_element_by_class_name("gLFyf")
    searchButton.send_keys(songList[i])
    searchButton.submit()
    time.sleep(1)
    #Below to check if song on Spotify
    #platformSpanList = driver.find_elements_by_class_name("hl")
    #for x in platformSpanList:
        #if x.text() == "Spotify":
            #Download from YouTube using below
    songYT = driver.find_element_by_class_name("FGpTBd")
    songYT.click()
    time.sleep(1)
    songURL = driver.current_url
    driver.get("https://ytmp3.cc/en13/")
    converterSearch = driver.find_element_by_id("input")
    converterSearch.send_keys(songURL)
    converterSearch.submit()
    time.sleep(1)
    buttons = driver.find_element_by_id("buttons")
    buttons.find_element_by_css_selector("a").click()
    time.sleep(1)
    driver.execute_script("window.history.go(-3)")