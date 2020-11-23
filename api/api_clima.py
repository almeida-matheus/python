import requests
import json
# https://openweathermap.org/
# f4b1b1cb81a17f14da5076d4094545cd
cidade = input('digite a cidade:')
try:
    requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=f4b1b1cb81a17f14da5076d4094545cd')
except:
    print('erro na conexào')

dicionario = json.loads(requisicao.text)
calculo = float(dicionario['main']['temp'])-273.15

print(dicionario)
print('condição do tempo:',dicionario['weather'][0]['main'])
print('temperatura:','%.2f' % calculo,'graus celsius')

#formatar numeros https://github.com/maniero/SOpt/blob/master/Python/Round.py