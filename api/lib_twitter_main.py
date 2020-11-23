from lib_twitter import Twitter

consumer_key = '2VE5seTLZwjSX22FomPLtxv66'
consumer_secret = 'izhdFg4MBWabkMYhYlKlpdZqVmMkiJ4iEC2Z0xEP6nTppVn5pN'

token_key = '1264671546926399492-K4fGXhPrpi2pMdWEZWWBS8hmgOo51z'
token_secret = 'XnWoXcf5CtncnPIGyx5dSEWaZuhoQaQzkAZuqPOvCYiWk'

twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)


#postar = twitter.tweet('testando a lib')

pesquisa = twitter.search('solyd', 'pt')

for resultado in pesquisa:
    print(resultado['user']['screen_name'])
    print(resultado['text'])