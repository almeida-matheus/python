import requests
import json
# b0ff56a9

req = None

try:
    req = requests.get('http://www.omdbapi.com/?apikey=b0ff56a9&t=titanic')
except:
    print('erro na conexao')
    exit()

#pega um texto em json e transforma em dicionario
dicionario = json.loads(req.text)

print('titulo:', dicionario['Title'])
print('ano:', dicionario['Year'])