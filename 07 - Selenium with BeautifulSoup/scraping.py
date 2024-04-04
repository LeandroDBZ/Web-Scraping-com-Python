import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

'''
response = requests.get('https://www.airbnb.com.br/')
site = BeautifulSoup(response.text, 'html.parser')
print(site.prettify())
'''
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://www.olx.com.br/")

input_place = navegador.find_element(By.ID,'oraculo-8-input')
input_place.send_keys('PS5')
sleep(2)
input_place.submit()
cidade = navegador.find_element(By.LINK_TEXT, "Campo Grande").click()
titulos = navegador.find_elements(By.CSS_SELECTOR, 'h2.olx-ad-card__title--horizontal')
precos = navegador.find_elements(By.XPATH, '//h3[@data-ds-component="DS-Text"]')

lista = []

for titulo, preco in zip(titulos, precos):
    #print('Titulo: '+titulo.text +'\nPreço: '+preco.text+'\n')
    lista.append([titulo.text, preco.text])

itens = pd.DataFrame(lista, columns=['Título','Preço'])
itens.to_csv('olx.csv', index=False)