import requests
import json
import datetime
#https://economia.awesomeapi.com.br/USD-BRL/
print('======================')
print('COTAÇÃO ATUAL DO DOLAR')
print('======================')

try:
    requisicao = requests.get('http://economia.awesomeapi.com.br/json/all/USD-BRL')
except:
    print('erro na conexão')
    exit()

dicionario = json.loads(requisicao.text)

dicionario1 = dicionario['USD']

dolar = float(dicionario1['bid'])

print('dolar atual:', '%.2f'%dolar, 'R$')
print('data e horário:', datetime.datetime.now())
