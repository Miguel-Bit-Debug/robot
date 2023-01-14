from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://imdb.com')

driver.implicitly_wait(3)
driver.execute_script('window.open()')
driver.switch_to.window(driver.window_handles[1])
driver.get('https://mercadolivre.com')
driver.implicitly_wait(3)

driver.switch_to.window(driver.window_handles[0])

driver.close()
