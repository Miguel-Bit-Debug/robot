from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://statusinvest.com.br/fundos-imobiliarios/knri11')

sleep(2)

driver.get_screenshot_as_file('./screenshot.png')

driver.close()
