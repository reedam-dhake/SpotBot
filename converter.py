def converter(driver):
    songElements = driver.find_elements_by_css_selector('[data-testid="tracklist-row"]')
    listOfSongs = []
    for songElement in songElements:
        listOfSongs.append(songElements.find_element_by_class_name("_5845794624a406a62eb5b71d3d1c4d63-scss").text)