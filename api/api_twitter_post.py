#https://developer.twitter.com/en/docs/api-reference-index
#POST statuses/update

import oauth2 #unir as keys
import json
import urllib.parse #para traduzir caracteres especiais ###

path1 = 'D:\\Arquivos\\matheus\\Documents\\Code\\python\\secret\\api_twitter.txt'

with open(path1, 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')

    token_key = tfile.readline().strip('\n')
    token_secret = tfile.readline().strip('\n')

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input('novo tweet: ')
query_codificada = urllib.parse.quote(query, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')
#requisicao[0] = response / requisicao[1] = bytes

decodificar = requisicao[1].decode()
#transformar para string

objeto = json.loads(decodificar)

print(objeto)


