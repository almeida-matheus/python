import requests
import json
# b0ff56a9

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=b0ff56a9&t=' + titulo)
        #req = requests.get('http://www.omdbapi.com/?apikey=b0ff56a9&t=' + titulo + '&type=movie')
        # pega um texto em json e transforma em dicionario
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('erro na conexao')
        return None

def printar_detalhes(filme):
    print('titulo:', filme['Title'])
    print('ano:', filme['Year'])
    print('nota:', filme['imdbRating'])
    print('diretor:', filme['Director'])
    print('atores:', filme['Actors'])
    print('premios:', filme['Awards'])
    print('poster:', filme['Poster'])
    print('')

#programa comeca aqui
sair = False
while not sair:
    op = input('digite o nome do filme ou digite sair para fechar:\n')
    if (op == 'sair') or (op == 'SAIR'):
        sair = True
        print('programa finalizado')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('filme nao encontrado')
        else:
            printar_detalhes(filme)


