from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://imdb.com')

driver.implicitly_wait(3)

driver.implicitly_wait(3)

driver.find_elements(By.NAME, 'q')[0].send_keys('Titanic', Keys.RETURN)

