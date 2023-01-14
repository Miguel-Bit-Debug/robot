from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': r'./',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://opera.com/pt-br/download')

spanBotao = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div[1]/div/span')
linkBotao = spanBotao.find_element(By.NAME, 'a')
linkBotao.click()
