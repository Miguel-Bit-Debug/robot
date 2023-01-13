from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

driver = webdriver.Chrome()
driver.get('https://imdb.com/title/tt0120338/mediaindex?ref_=tt_pv_mi_sm')
driver.implicitly_wait(3)

divImg = driver.find_element(By.ID, 'media_index_thumbnail_grid')
img = divImg.find_elements(By.TAG_NAME, 'img')[0]
attrHref = img.get_attribute('src')
print(attrHref)

try:
    urllib.request.urlretrieve(attrHref, r'./teste.jpg')
    print('deu certo')
except:
    print('erro')