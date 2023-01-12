from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://imdb.com')
driver.implicitly_wait(3)

search = driver.find_elements(By.NAME, 'q')[0]

search.send_keys('Titanic')

sleep(2)