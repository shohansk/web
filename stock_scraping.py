import os
import time
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from bs4 import BeautifulSoup
import pandas as pd

urls = [
    'https://www.tradingview.com/markets/stocks-usa/highs-and-lows-ath/',
    'https://www.tradingview.com/markets/stocks-usa/highs-and-lows-atl/',
    'https://www.tradingview.com/markets/stocks-usa/highs-and-lows-52wk-high/',
    'https://www.tradingview.com/markets/stocks-usa/highs-and-lows-52wk-low/',
    'https://www.tradingview.com/markets/stocks-usa/highs-and-lows-monthly-high/',
    'https://www.tradingview.com/markets/stocks-usa/highs-and-lows-monthly-low/',
    'https://www.tradingview.com/markets/stocks-usa/highs-and-lows-high-dividend/'
]

path='C:/Users/Mediusware/Documents/chromedrive/chromedriver.exe'
driver = webdriver.Chrome(path)

# driver.get(urls)
# driver.maximize_window()
driver.implicitly_wait(7)
driver.maximize_window()

for url in urls:
    driver.get(url)
    file_base_name = url.split('/')[-2]
    xlwriter = pd.ExcelWriter(file_base_name + '.xlsx')

    # iterate categories
    categories = driver.find_elements_by_xpath('//div[starts-with(@class, "item-EE_m_Lmj")]')

    for category in categories:
        print(f'Processing Report: {category.text}')
        try:
            # click on Overview tab
            try:
                driver.find_element_by_xpath(f'//div[text()="{category.text}"]').click()
            except ElementNotInteractableException:
                pass
                        
            # click on load more buttons until disappears
            load_more = True
            counter = 0
            max_counter = 3
            
            while load_more:
                try:
                    driver.find_element_by_class_name('tv-load-more__btn').click()
                    time.sleep(1)
                    if counter > max_counter:
                        load_more = False
                    counter += 1
                except ElementNotInteractableException:
                    load_more = False

            df = pd.read_html(driver.page_source)[1]
            df.replace('—', '', inplace=True)
            df.to_excel(xlwriter, sheet_name=category.text, index=False)

        except (NoSuchElementException, TimeoutException):
            print(f'Report {category.text} is not found.')
            continue
    print('Excel file saved at {0}'.format(file_base_name + '.xlsx'))
    xlwriter.save()
    
driver.quit()