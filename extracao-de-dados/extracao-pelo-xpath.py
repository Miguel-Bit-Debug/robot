from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://statusinvest.com.br/fundos-imobiliarios/knri11')

driver.implicitly_wait(3)

dados = driver.find_elements(By.XPATH, '//*[@id="earning-section"]/div[7]/div/div[2]/table/tbody')[0].text

print(dados)
