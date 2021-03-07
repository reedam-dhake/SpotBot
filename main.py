from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import time
import os
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.headless = True
prefs = {'download.default_directory' : path1}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(PATH,options=options)