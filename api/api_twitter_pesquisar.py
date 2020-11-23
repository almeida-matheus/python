#twitter developer > create application
#pip3 install oauth2

#https://developer.twitter.com/en/docs/api-reference-index
#https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

import oauth2 #unir as keys
import json
import pprint #imprimir bonitinho
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

query = input('pesquisa: ')
query_codificada = urllib.parse.quote(query, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')
#requisicao[0] = response / requisicao[1] = bytes

decodificar = requisicao[1].decode()
#transformar para string

objeto = json.loads(decodificar)

#pprint.pprint(objeto)
#pprint.pprint(objeto['statuses'][0]['user']['screen_name'])
#pprint.pprint(objeto['statuses'][0]['text'])

twittes = objeto['statuses']
for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print('\n')


