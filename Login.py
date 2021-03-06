from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os
print("Enter the number corresponding to your preffered login method.")
print("1. Facebook")
print("2. Apple ID")
print("3. Google")
print("4. Phone number")
print("5. Username and Password\n")
loginMethod = int(input())
PATH = "C:\Program Files (x86)\chromedriver.exe"
#options = webdriver.ChromeOptions()
#options.headless = True
driver = webdriver.Chrome(PATH)#,options=options)
driver.get("https://open.spotify.com")
time.sleep(5)
loginbutton = driver.find_element_by_css_selector('[data-testid="login-button"]')
loginbutton.click()
time.sleep(5)
loginLinks = driver.find_elements_by_class_name('btn')
if loginMethod == 1:
    facebook = loginLinks[0]
    facebook.click()
    facebookUsername = input("Enter Facebook Username: ")
    facebookPassword = input("Enter Facebook Password: ")
    username = driver.find_element_by_id("email")
    username.send_keys(facebookUsername)
    passw = driver.find_element_by_id("pass")
    passw.send_keys(facebookPassword)
elif loginMethod == 2:
    appleID = loginLinks[1]
    appleID.click()
    appleUsername = input("Enter your Apple ID: ")
    username = driver.find_element_by_id("account_name_text_field")
    username.send_keys(appleUsername)
    enterButton = driver.find_element_by_css_selector("i")
    enterButton.click()
elif loginMethod == 3:
    google = loginLinks[2]
    google.click()
elif loginMethod == 4:
    phoneNumber = loginLinks[3]
    phoneNumber.click()