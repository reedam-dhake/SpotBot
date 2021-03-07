def downloader(driver,songlist)
    cwdPath = os.getcwd()
    directory = "newSpotifyPlaylist"
    path1 = os.path.join(cwdPath, directory)
    if not os.path.exists(path1):
        os.mkdir(path1)
    #Below is the song list
    def latest_download_file():
        os.chdir(path1)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        newest = files[-1]
        return newest
    for i in range(len(songList)):
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