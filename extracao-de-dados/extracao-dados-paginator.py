from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://catho.com.br')

linksVagas = []

driver.maximize_window()

sleep(2)

try:
    #cookies
    driver.find_element(By.XPATH, '//*[@id="lgpd-consent-widget"]/section/div/div[2]/button[1]').click()
    sleep(2)

except:
    print('erro')

search = driver.find_element(By.NAME, 'q')
search.send_keys('Engenharia de computação')

sleep(2)

driver.find_element(By.NAME, 'submit').click()

sleep(2)

driver.find_element(By.ID, 'salary').click()

sleep(2)

optSalario = driver.find_element(By.ID, 'downshift-3-item-4')
optSalario.click()

sleep(2)

elementosVagas = driver.find_elements(By.XPATH, '//*[@id="search-result"]/ul/li[1]/article')

for elementAtual in elementosVagas:
    elementoLink = elementAtual.find_element(By.TAG_NAME, 'a')
    textoLink = elementoLink.get_attribute('href')
    linksVagas.append(textoLink)
    print(textoLink)

for linkAtual in linksVagas:
    driver.get(linkAtual)
    print(driver.find_element(By.TAG_NAME, 'h2').text)
    sleep(2)

