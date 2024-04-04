import requests

response = requests.get('https://www.udemy.com/')

print('Status code: ', response.status_code)
print('Header: ', response.headers)
print('\n Conteúdo')
print(response.content)