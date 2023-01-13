from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://statusinvest.com.br/fundos-imobiliarios/krni11')

elemento_imagem = driver.find_elements(By.CLASS_NAME, 'navbar-brand')[0]
elemento_img = elemento_imagem.find_element(By.TAG_NAME, 'img')
atributoSrc = elemento_img.get_attribute('src')

print(atributoSrc)

driver.get('https://melhorcambio.com/dolar-hoje')

elementoCotacao = driver.find_element(By.ID, 'comercial')
valorCotacao = elementoCotacao.get_attribute('value')
classElement = elementoCotacao.get_attribute('class')
tipoElemento = elementoCotacao.get_attribute('type')

print(valorCotacao)
print(classElement)
print(tipoElemento)

driver.close()