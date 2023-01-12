from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://statusinvest.com.br/fundos-imobiliarios/knri11')

driver.implicitly_wait(3)

nomeFii = driver.find_elements(By.TAG_NAME, 'h1')[0].text
valorAtual = driver.find_elements(By.TAG_NAME, 'strong')[0].text
tableRendimentos = driver.find_elements(By.TAG_NAME, 'table')[0].text
tableResult = driver.find_elements(By.TAG_NAME, 'table')[1].text

print(nomeFii)
print(valorAtual)
print(tableRendimentos)
print(tableResult)
