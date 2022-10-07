from lib2to3.pgen2 import driver
from selenium import webdriver
import pandas as pd
path='C:/Users/Mediusware/Documents/chromedrive/chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://www.worldometers.info/world-population/population-by-country/')
driver.maximize_window()
country_xpath ="//table[@id='example2']/tbody/tr/td[2]/a"
populantion_xpath='//table[@id="example2"]/tbody/tr/td[3]'
yearly_xpath = '//table[@id="example2"]/tbody/tr/td[4]'
wrold_share_xpath = '//table[@id="example2"]/tbody/tr/td[12]'


country = driver.find_elements("xpath",country_xpath)
populantion = driver.find_elements("xpath",populantion_xpath)
yearly = driver.find_elements("xpath",yearly_xpath)
wrold_share = driver.find_elements("xpath",wrold_share_xpath)

print(len(yearly))
world_populantion = []

for i in range (len(yearly)):
    temp_data = {'Country':country[i].text,
                'Population':populantion[i].text,
                'Yearly Change':yearly[i].text,
                'World Share':wrold_share[i].text
                }
    world_populantion.append(temp_data)

df_data = pd.DataFrame(world_populantion)
df_data.to_csv('world_populantion.csv',index=False)
print("#################    End    ###############")