from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)
navegador.get('https://www.airbnb.com/')
sleep(10)

titulos = navegador.find_elements(By.XPATH, '//*[@data-testid="listing-card-title"]')
distancias = navegador.find_elements(By.XPATH, '//*[@data-testid="listing-card-subtitle"]/span')
valores = navegador.find_elements(By.CLASS_NAME, '_1y74zjx')

lista = []

for titulo, distancia, valor in zip(titulos, distancias, valores):
    if('km de distância' in distancia.text):
        #print('Titulo: '+titulo.text +'\nDistância: '+distancia.text+'\nValor: '+valor.text+'\n')
        lista.append([titulo.text, distancia.text, valor.text])

itens = pd.DataFrame(lista, columns=['Título','Distância', 'Valor'])
itens.to_csv('airbnb.csv', index=False)