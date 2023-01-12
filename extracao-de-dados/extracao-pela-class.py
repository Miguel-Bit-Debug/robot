from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://statusinvest.com.br/fundos-imobiliarios/knri11')

driver.implicitly_wait(3) # seconds

dados0 = driver.find_element(By.CLASS_NAME, 'value').text
dados1 = driver.find_elements(By.CLASS_NAME, 'value')[0].text
dados2 = driver.find_elements(By.CLASS_NAME, 'value')[3].text
dados3 = driver.find_elements(By.CLASS_NAME, 'value')[4].text

print(dados0)
print(dados1)
print(dados2)
print(dados3)
