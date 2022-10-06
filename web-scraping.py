

from itertools import count
from select import select
from selenium import webdriver
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
import pandas as pd
import os
from openpyxl import load_workbook

tt = '//*[@id="side-menu"]/li[7]/a'
tt1='//*[@id="side-menu"]/li[7]/ul/li[1]/a'
all_matches_button='//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]'
select_season = '//*[@id="season"]'
season = '//*[@id="season"]/option[6]'
t1 = '/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]/detailed-team/div/div/div[2]/div/div/div[2]'
website = 'https://www.adamchoi.co.uk/'
path='C:/Users/Mediusware/Documents/chromedrive/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)
driver.maximize_window()
driver.find_element("xpath", tt).click()
time.sleep(2)
driver.find_element("xpath", tt1).click()
time.sleep(2)
driver.find_element("xpath", all_matches_button).click()
time.sleep(2)
driver.find_element("xpath", select_season).click()
time.sleep(2)
driver.find_element("xpath", season).click()
time.sleep(2)
# all_matches_button = driver.find_element_by_xpath('//a[@ui-sref="site.fixtures"]')
# all_matches_button.click()
matches = driver.find_elements("xpath",t1)
d = './tr[1]'
h = './tr[2]'
s = './tr[3]'
a = './tr[4]'

date = []
home_team = []
score = []
away_team = []



for match in matches:
    de = driver.find_elements("xpath",d)
    print(de)
    date.append()
    hm = driver.find_elements("xpath",h)
    home_team.append(hm)
    sc = driver.find_elements("xpath",s)
    score.append(sc)
    aw = driver.find_elements("xpath",a)
    away_team.append(aw)
    # date.append(match.find_element("xpath",d).text)
    # home_team.append(match.find_element("xpath",h).text)
    # score.append(match.find_element("xpath",s).text)
    # away_team.append(match.find_element("xpath",a).text)
    # data.append.matches = driver.find_elements("xpath",d)
    # home_team.append.matches = driver.find_elements("xpath",h)
    # score.append.matches = driver.find_elements("xpath",s)
    # away_team.append.matches = driver.find_elements("xpath",a)
    print(match.text)

df = pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('team.csv',index=False)
print(df)
