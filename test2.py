from selenium import webdriver
import pandas as pd
# driver=webdriver.Chrome('C:\webdrivers\chromedriver.exe')
path='C:/Users/chromedrive/chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://www.worldometers.info/world-population/population-by-country/')
driver.maximize_window()
countries=driver.find_elements_by_xpath('//tbody/tr/td[2]/a')
population=driver.find_elements_by_xpath('//tbody/tr/td[3]')
yearly_change=driver.find_elements_by_xpath('//tbody/tr/td[4]')
world_share=driver.find_elements_by_xpath('//tbody/tr/td[12]')


population_result=[]

for i in range(len(yearly_change)):
    temporary_data={'Country': countries[i].text,
                   'Population': population[i].text,
                   'Yearly Change': yearly_change[i].text,
                   'World Share': world_share[i].text}
    population_result.append(temporary_data)
df_data=pd.DataFrame(population_result)
df_data
df_data.to_excel('population_scraping_result.xlsx', index=False)