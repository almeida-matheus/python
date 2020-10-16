import requests
import json
''''
def existe(titulo):
    #lista = []
    quant = 0
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=b0ff56a9&s=' + titulo)
        resposta = json.loads(req.text) #transforma json em dicionario
        #return resposta
    except:
        print('erro na conexao')
        return quant

    if resposta['Response'] == 'True':
        quant = resposta['totalResults']
        #return lista,quant #retorna uma tupla
    return quant #qualquer coisa q der errado retorn quant
#print(existefilmes('matrix'))
'''
def lista_filmes(titulo):
    catalago = []
    for i in range(1, 101): #ultimo nao é incluso
        try:
            print('pesquisando em pagina', i)
            req = requests.get('http://www.omdbapi.com/?apikey=b0ff56a9&page=' + str(i) +'&s=' + titulo)
            resposta = json.loads(req.text) #transforma json em dicionario
            if resposta['Response'] == 'True':
                # pra cada filme dessa lista vou querer o titulo e o ano
                for filme in resposta['Search']:  # resposta[search] retorna uma lista
                    nome = filme['Title']
                    ano = filme['Year']
                    # de uma lista de filmes quero so o title
                    string = nome + ' (' + ano + ')'
                    catalago.append(string)
                # return resposta
            else:
                print('fim das paginas')
                break #acabou programa, nao tem filme na pag
        except:
            print('erro na conexao')
    return catalago

#print(lista('matrix'))

sair = False
while not sair:
    op = input('digite o nome do filme ou digite sair para fechar:\n')
    if (op == 'sair') or (op == 'SAIR'):
        sair = True
        print('programa finalizado')
    else:
        lista = lista_filmes(op)
        print('filmes encontrados:', len(lista))
        for filme in lista:
            print(filme)


'''
req = requests.get('http://www.omdbapi.com/?apikey=b0ff56a9&page=1&s=star+wars')
resposta = json.loads(req.text)
#dentro do search eh uma lista{[{0},{1}, {2}]}
#print(resposta['Search'])
#print(resposta['totalResults'])
print(resposta['Search'][0]['Title'])
'''


