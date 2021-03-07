from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
#options = webdriver.ChromeOptions()
#options.headless = True
driver = webdriver.Chrome(PATH)#,options=options)
driver.get("https://open.spotify.com")
time.sleep(5)
def search(driver):
    print("\nWhat do you want to search for?")
    print("(Please enter the corresponding number.)")
    print("1 - Playlist")
    print("2 - Album")
    print("3 - Song")
    print("4 - Artist\n")
    searchType=0
    while(True):
        searchType = input().strip()
        if searchType.isnumeric() and int(searchType) in (1, 2, 3, 4):
            searchType=int(searchType)
            break
        else:
            print("\nYour entry is invalid. Please try again.")
    driver.get("https://open.spotify.com/search")
    time.sleep(5)
    searchButton = driver.find_element_by_css_selector('[data-testid="search-input"]')
    #searchInput = input("\nPlease type the name of search item.\n")
    #searchButton.send_keys(searchInput)
    #searchButton.send_keys(Keys.RETURN)
    if searchType == 1: #playlist
        print("\nPlease choose the appropriate number.")
        print("1 - Search for own playlist.")
        print("2 - Search for other playlist.")
        playlistType=0
        while(True):
            playlistType = input().strip()
            if playlistType.isnumeric():
                playlistType=int(playlistType)
                break
            else:
                print("\nYour entry is invalid. Please try again.")
        if playlistType == 1:
            playlistname=input("Enter playlist name.").strip()
            menu = driver.find_elements_by_css_selector('[data-testid="rootlist"]')
            playlistlist=menu.find_elements_by_tag_name("li")
            for playlist in playlistlist:
                if playlist.text.lower()==playlistname.lower():
                    return(playlist.get_attribute("href"))
            return("No such playlist found in your library.")
        elif playlistType == 2:
            searchInput = input("\nPlease type the name of the playlist.\n")
            searchButton.send_keys(searchInput)
            searchButton.send_keys(Keys.RETURN)
            seeAllButtons = driver.find_elements_by_class_name("b490086127ec0ecdc7b170c03de9c5b1-scss")
            seeAllButtons[2].click()
            playlists = driver.find_elements_by_class_name("_8ffcbd2689adedee867afcf5090b6fd4-scss")[0:5]
            print("Please choose the number corresponding to your playlist.")
            for i in range(5):
                print(i+1, ' - ', playlists[i].get_attribute("title"))
            chosen=0
            while(True):
                chosen = input().strip()
                if chosen.isnumeric() and int(chosen) in (1, 2, 3, 4, 5):
                    chosen=int(chosen)
                    break
                else:
                    print("\nYour entry is invalid. Please try again.")
            return (playlists[chosen].get_attribute("href"))
    elif searchType == 2: #album
        searchInput = input("\nPlease type the name of the album.\n")
        searchButton.send_keys(searchInput)
        searchButton.send_keys(Keys.RETURN)
        seeAllButtons = driver.find_elements_by_class_name("b490086127ec0ecdc7b170c03de9c5b1-scss")
        seeAllButtons[1].click()
        albums = driver.find_element_by_class_name("_8ffcbd2689adedee867afcf5090b6fd4-scss")[0:5]
        albumNameList = [x.find_element_by_css_selector("a").get_attribute("text") for x in albums]
        albumArtistList = [x.find_element_by_class_name("_3cfbde1fd9fecaaa77935664eeb6e346-scss").find_element_by_css_selector("a").text for x in albums]
        print("Please choose the number corresponding to your album.")
        print("Number - Album Name - Artist")
        for i in range(5):
            print(i+1, ' - ', albumNameList[i], ' - ', albumArtistList[i])
        chosen=0
        while(True):
            chosen = input().strip()
            if chosen.isnumeric() and int(chosen) in (1, 2, 3, 4, 5):
                chosen=int(chosen)
                break
            else:
                print("\nYour entry is invalid. Please try again.")
        return (albums[chosen].get_attribute("href"))
    elif searchType == 3: #song
        songName = input("\nPlease type the song name.\n")
        print("Please type the artist(s) name.")
        print("Type NA if not applicable.")
        songArtist = input()
        if songArtist.lower() == "na":
            searchInput = songName
        else:
            searchInput = songName + ' ' + songArtist
        searchButton.send_keys(searchInput)
        searchButton.send_keys(Keys.RETURN)
        seeAllButtons = driver.find_elements_by_class_name("b490086127ec0ecdc7b170c03de9c5b1-scss")
        seeAllButtons[0].click()
        songs = driver.find_elements_by_css_selector('[data-testid="tracklist-row"]')[0:5]
        songNameList = [x.find_element_by_class_name("da0bc4060bb1bdb4abb8e402916af32e-scss").text for x in songs]
        songArtistList = [x.find_element_by_css_selector("a").text for x in songs]
        songAlbumList = [x.find_element_by_class_name("standalone-ellipsis-one-line") for x in songs]
        print("Please choose the number corresponding to your song.")
        print("Number - Song Name - Artist - Album")
        for i in range(5):
            print(i+1, ' - ',  songNameList[i], ' - ', songArtistList[i], ' - ', songAlbumList[i])
        chosen=0
        while(True):
            chosen = input().strip()
            if chosen.isnumeric() and int(chosen) in (1, 2, 3, 4, 5):
                chosen=int(chosen)
                break
            else:
                print("\nYour entry is invalid. Please try again.")
        return (songNameList[chosen] + ' ' + songArtistList[chosen] + ' ' + songAlbumList[chosen])
    elif searchType == 4: #artist
        searchInput = input("\nPlease type the name of the artist.\n")
        searchButton.send_keys(searchInput)
        searchButton.send_keys(Keys.RETURN)
        time.sleep(1)
        return driver.find_element_by_class_name("f7ebc3d96230ee12a84a9b0b4b81bb8f-scss").get_attribute("href")
search(driver)