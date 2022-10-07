from lib2to3.pgen2 import driver
import time
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
with open('job_scraping.csv', 'w') as file:
    file.write("Job_title; Salary; Company \n")



path='C:/Users/Mediusware/Documents/chromedrive/chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://www.jobsite.co.uk/')

driver.maximize_window()
accept ='//*[@id="ccmgt_explicit_accept"]'
job_add = '//*[@id="keywords"]'
location_add = '//*[@id="location"]'
radius_add = '//*[@id="Radius"]'
radius = '//*[@id="Radius"]/option[5]'
search = '//*[@id="search-button"]'



job_t = '//div/a[@class="resultlist-1efz66h"]'
titles_xpath = '/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/article/div[1]/div[2]/div/a'
location_xpath = '//li[@class="location"]/span'

salary_xpath = '//li[@title="salary"]'
# salary_xpath = '//div/div[@class="resultlist-10769el"]'
contract_type_xpath = '//li[@class="job-type"]/span'
job_details_xpath = '//div[@title="job details"]/p'
time.sleep(1)

cookie = driver.find_element('xpath',accept)

try:
    cookie.click()
except:
    pass

# job_tittle = driver.find_element_by_id("keywords")
job_tittle = driver.find_element('xpath',job_add)
job_tittle.click()
job_tittle.send_keys("Software Enginner")

# job_location = driver.find_element_by_id("location")
job_location = driver.find_element('xpath',location_add)
job_location.click()
job_location.send_keys("Manchester")


job_radius = driver.find_element('xpath',radius_add)
job_radius.click()
driver.find_element('xpath',radius).click()
driver.find_element('xpath',search).click()
time.sleep(5)
# driver.get('https://www.jobsite.co.uk/jobs/software-enginner/in-manchester?radius=30')

# titles=driver.find_elements('xpath',titles_xpath)
# main_div=driver.find_element('xpath','//[@id="app-unifiedResultlist-f3a72f43-7251-4efd-9d5f-b1ac13c2f14f"]/div/div[2]/div/div[2]/div[2]/div')
# div = main_div.find_element(By.CLASS_NAME,"Wrapper-sc-11673k2-0")    
# # div1 = driver.find_elements('xpath',job_t)
# div1= main_div.find_elements(By.CLASS_NAME,"Wrapper-sc-11673k2-0")

# title1 = driver.find_elements(By.CLASS_NAME,"Wrapper-sc-11673k2-0") # all 
job_title1 = driver.find_elements(By.CLASS_NAME,"sc-fzqMAW") # s_job_title
job_salary = driver.find_elements(By.CLASS_NAME,"sc-fzoJMP") # s_salary
company_name = driver.find_elements(By.CLASS_NAME,"sc-fzoiQi") # company name

# titttt = driver.find_elements(By.CLASS_NAME,"resultlist-hbjkz4")
job_scraping = []
time.sleep(2)
last_page_number = driver.find_elements(By.CLASS_NAME,"resultlist-kyg8or")

print(len(last_page_number))
for i in range (10):
    job_title1 = driver.find_elements(By.CLASS_NAME,"sc-fzqMAW") # s_job_title
    job_salary = driver.find_elements(By.CLASS_NAME,"sc-fzoJMP") # s_salary
    company_name = driver.find_elements(By.CLASS_NAME,"sc-fzoiQi") # company name


    with open('job_scraping.csv', 'a') as file:
        for i in range(len(job_title1)):

            file.write(job_title1[i].text + ";" + job_salary[i].text + ";" + company_name[i].text +"\n")
            
        next=driver.find_element('xpath','//a[@aria-label="Next"]')
        next.click()
        time.sleep(2)
    # file.close()








print("End---------------------------------------------------------------")

# time.sleep(5)


