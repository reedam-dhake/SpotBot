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
cwdPath = os.getcwd()
directory = "newSpotifyPlaylist"
path1 = os.path.join(cwdPath, directory)
if not os.path.exists(path1):
    os.mkdir(path1)
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path1}
chrome_options.add_experimental_option('prefs', prefs)
#Below is the song list
songList = ["roar katy perry", "firework katy perry"]
def latest_download_file():
    path = path1
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    return newest
for i in range(len(songList)):
    driver = webdriver.Chrome(PATH,chrome_options=chrome_options)
    #Below is the song list
    driver.get("https://www.google.com/")
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
    fileends = "crdownload"
    while "crdownload" == fileends:
        time.sleep(1)
        newest_file = latest_download_file()
        if "crdownload" in newest_file:
            fileends = "crdownload"
        else:
            fileends = "none"
    driver.close()