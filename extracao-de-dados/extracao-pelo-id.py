from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://infomoney.com.br')

dados1 = driver.find_element(By.ID, 'high').text
dados2 = driver.find_elements(By.ID, 'high')[0].text

print(dados1)
print()
print(dados2)
