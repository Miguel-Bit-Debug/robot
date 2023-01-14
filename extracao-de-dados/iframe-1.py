from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

driver.get('http://b3.com.br/pt_br/market-data-e-indicas/servicos-de-dados/market-data/historico/derivativos/ajustes-de-pregao/')

driver.switch_to.frame('bvmf_iframe')

tabela = driver.find_element(By.ID, 'tblDadosAjustes')

m = []

for linha in tabela.find_elements(By.NAME, 'tr'):
    linhasDados = []
    for coluna in linha.find_elements(By.NAME, 'td'):
        linhasDados.append(coluna.text)
    m.append(linhasDados)

df = pd.DataFrame(m)
print(df)

