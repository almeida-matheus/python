import re
#site: regex101
string_teste = 'o gato é bonito'

padrao = re.search(r'gat\w', string_teste) #r = RAW string, tira os caracteres especiasi e printa eles
#o . equivale a qualquer caractere // \w equivale a qualquer letra (espaço nao conta)
if padrao: #se existir alguma coisa em padrao
    print(padrao.group())
else:
    print('padrao nao encontrado')

string_teste = 'o gato, a gata e os gatinhos'

padrao = re.findall(r'gat\w+', string_teste) #r = RAW string, tira os caracteres especiasi e printa eles
#\w equivale a qualquer letra (espaço nao conta). +uma letra *uma ou mais
if padrao: #se existir alguma coisa em padrao
    print(padrao)
else:
    print('padrao nao encontrado')

#chave especifica 1 letra só/ + completa
padrao = re.findall(r'[gat]+\w+', string_teste)
print(padrao)

#achar de 4 a 6 letras
padrao = re.findall(r'\w{4,6}', string_teste)
#3 a seguidos
padrao = re.findall(r'a{3}', string_teste)
