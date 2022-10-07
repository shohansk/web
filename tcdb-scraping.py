from selenium import webdriver


import time
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
path='C:/Users/Mediusware/Documents/chromedrive/chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://www.tcdb.com/')

driver.maximize_window()