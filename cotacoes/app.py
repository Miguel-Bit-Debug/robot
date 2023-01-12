from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.get('https://www.jornaldenegocios.pt/cotacoes')

cotacoes = navegador.find_element(By.XPATH, '//*[@id="bmsapp"]/div[1]/div[3]/section/div[1]/div[1]/table/tbody').text

file = open('cotacao.csv', 'w', newline='', encoding='utf-8')

file.write(cotacoes)
file.close()
