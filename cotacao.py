import requests
import pandas as pd



# link para obter as cotaçoes
# Aula dia 18/07/2022

url = 'https://economia.awesomeapi.com.br/all/EUR-BRL'

# Busca dos dados

response = requests.get(url)

if response.status_code==200: # esse codigo e o retorno quando deu tudo certo
    euro_value = response.json()['EUR']['low']
    print(f'O valor do Euro e R$ {euro_value}')
else:
    print('Erro ao buscar valor')


url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

response = requests.get(url)

if response.status_code==200:
    dolar_value = response.json()['USD']['low']
    print(f'O valor do Dolar e R$ {dolar_value}')
else:
    print('Errdo de requisição')

df = pd.DataFrame(response)
df.to_csv('cotação_dolar_euro.csv',index=False)    

