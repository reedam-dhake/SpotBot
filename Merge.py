def merger(driver1,link1,link2):
    driver1.get(link1)
    name = driver1.find_element_by_css_selector('[data-testid="playlist-page"]').find_element_by_tag_name("h1").text
    driver1.get(link2)
    actions = ActionChains(driver1)
    songElements = driver1.find_elements_by_css_selector('[data-testid="tracklist-row"]')
    for songElement in songElements:
        actions.context_click(songElement).perform()
        contextMenu = driver1.find_element_by_id("context-menu-root")
        addToPlaylist = contextMenu.find_element_by_xpath(".//li[contains(text(),'Add to playlist')]")
        addToPlaylist.click()
        addToPlaylist.find_element_by_xpath(".//li[contains(text(),name)]").click()