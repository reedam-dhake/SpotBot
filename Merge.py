def merger(driver,link1,link2):
    driver.get(link1)
    name = driver.find_element_by_css_selector('[data-testid="playlist-page"]').find_element_by_tag_name("h1").text
    driver.get(link2)
    actions = ActionChains(driver)
    songElements = driver.find_elements_by_css_selector('[data-testid="tracklist-row"]')
    for songElement in songElements:
        action.context_click(songElement).perform()
        contextMenu = driver.find_element_by_id("context-menu-root")
        addToPlaylist = contextMenu.find_element_by_xpath(".//li[contains(text(),'Add to playlist')]")
        addToPlaylist.click()
        addToPlaylist.find_element_by_xpath(".//li[contains(text(),name)]").click()
