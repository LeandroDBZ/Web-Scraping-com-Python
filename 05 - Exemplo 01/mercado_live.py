# Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://lista.mercadolivre.com.br/'
produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)
lista_produtos = []
site = BeautifulSoup(response.text, 'html.parser')
produtos = site.findAll('div', attrs={'class': 'ui-search-result__wrapper'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})

    currency_symbol = produto.find('span', attrs={'class': 'andes-money-amount__currency-symbol'})
    real = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavo = produto.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

    # print(produto.prettify())
    '''print('Título do produto: ', titulo.text)
    print('Link do produto: ', link['href'])
    if(centavo):
        print('Valor do produto: ', currency_symbol.text, real.text + "," + centavo.text)
    else:
        print('Valor do produto: ', currency_symbol.text, real.text + ",00")

    print()'''

    if(centavo):
        valor_produto = currency_symbol.text + real.text + ',' + centavo.text
    else:
        valor_produto = currency_symbol.text + real.text + ',00'


    lista_produtos.append([titulo.text, link['href'], valor_produto])

itens = pd.DataFrame(lista_produtos, columns=['Título','Link', 'Valor'])
itens.to_csv('Mercado_Livre.csv', index=False)