from selenium import webdriver
from selenium.webdriver.common.by import By
import time


navegador = webdriver.Edge()
navegador.maximize_window()
navegador.get('https://g1.globo.com/')
elemento = navegador.find_element(By.ID, "busca-campo")
elemento.send_keys('fantastico')
elemento.submit()
time.sleep(5)
navegador.close()