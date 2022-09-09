from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import os


if os.path.exists("results.txt"):
    os.remove("results.txt")
else:
    print("The file does not exist")



driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME , 'q')
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
data_articles = driver.find_elements(By.XPATH, ".//*[@class='list-recent-events menu']//li")


with open("results.txt", "w") as f:
    for article in data_articles:
        f.write(article.text)
        f.write(3*"\n")


time.sleep(4)
driver.close()