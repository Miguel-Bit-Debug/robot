from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver.minimize_window()
driver.implicitly_wait(2)
driver.get('https://imdb.com/title/tt0120338/?ref_=fn_al_tt_1')
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://google.com')
driver.back()
driver.implicitly_wait(5)
driver.forward()
driver.refresh()
driver.implicitly_wait(5)
driver.close()