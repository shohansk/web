import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path='C:/Users/Mediusware/Documents/chromedrive/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.clear()
search_box.send_keys("dell laptops")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.XPATH,"//span[text()='Dell']").click()

laptops = driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')

laptop_name = []
laptop_price = []
no_reviews = []
image_list = []
print(len(laptops))
for laptop in laptops: 
  
    names =laptop.find_elements(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']")
    for name in names:
        laptop_name.append(name.text)
        
    try:
        if len(laptop.find_elements(By.XPATH,".//span[@class='a-price-whole']"))>0:
            prices= laptop.find_elements(By.XPATH,".//span[@class='a-price-whole']")
            for price in prices:
                
                laptop_price.append(price.text)
        else:
            laptop_price.append("NULL")
    except:
        pass
    
    
    try:
        if len(laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']"))>0:
            reviews = laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")
            for review in reviews:
            
                no_reviews.append(review.text)
        else:
            no_reviews.append("0")
    except:
        pass

    try:
        if len(laptops)>0:
            image = laptop.find_elements(By.CLASS_NAME,"s-image")
            for i in image:
                img = i.get_attribute("src")
                image_list.append(img)
                print(img)

        else:
            image_list.append("NULL")
    except:
        pass
        
print('no of laptops',len(laptop_name))
print('no of prices',len(laptop_price))
print('no of reviews',len(no_reviews))
print('no of image',len(image_list))


import pandas as pd
df = pd.DataFrame(zip(laptop_name,laptop_price,no_reviews,image_list),columns=['laptop_name','laptop_price','no_reviews','image_list'])

df.to_csv(r"C:\Users\Mediusware\Documents\New folder (3)\laptop.csv",index=False)

driver.quit()